from flask import Flask, jsonify, request, render_template
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing
import requests
import json
import os

app = Flask(__name__)

# Function to scrape company data
def scrape_companies():
    url = "https://www.ijt.jp/tokyo/en-gb/search/2025/directory.html#/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    companies = {"hits": []}

    for company in soup.find_all('div', class_='company-info'):
        name = company.find('h3').text.strip()
        details_url = company.find('a')['href']  # Get the details URL
        details_response = requests.get(details_url)
        details_soup = BeautifulSoup(details_response.content, 'html.parser')

        # Extract details from the details page
        email = details_soup.find('a', class_='email').text.strip() if details_soup.find('a', class_='email') else 'N/A'
        phone = details_soup.find('span', class_='phone').text.strip() if details_soup.find('span', class_='phone') else 'N/A'
        website = details_soup.find('a', class_='website')['href'] if details_soup.find('a', class_='website') else 'N/A'
        logo = details_soup.find('img')['src'] if details_soup.find('img') else 'N/A'
        description = details_soup.find('p', class_='description').text.strip() if details_soup.find('p', class_='description') else 'N/A'
        stand_reference = details_soup.find('span', class_='stand-reference').text.strip() if details_soup.find('span', class_='stand-reference') else 'N/A'

        companies["hits"].append({
            "recordType": "exhibitor",
            "id": f"exh-{name.replace(' ', '-').lower()}",  # Create a unique ID
            "companyName": name,
            "website": website,
            "exhibitorDescription": description,
            "phone": phone,
            "email": email,
            "logo": logo,
            "standReference": stand_reference,
            "products": []  # Initialize with an empty list for products
        })

    # Save the scraped data to companies.json
    with open('companies.json', 'w', encoding='utf-8') as f:
        json.dump(companies, f, indent=4)

    print("Data scraped and saved to companies.json")

# Function to load data from companies.json
def load_data():
    if os.path.exists('companies.json'):
        try:
            with open('companies.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {"hits": []}
        except Exception as e:
            print(f"Error reading file: {e}")
            return {"hits": []}
    return {"hits": []}

# Route to trigger the scraping process
@app.route('/api/scrape', methods=['GET'])
def trigger_scrape():
    scrape_companies()
    return jsonify({'message': 'Scraping completed and data saved to companies.json'})

# Route to get company data
@app.route('/api/companies', methods=['GET'])
def get_companies():
    companies = load_data()
    return jsonify(companies)

# Route to edit company data
@app.route('/api/companies/<string:company_id>', methods=['PUT'])
def edit_company(company_id):
    updated_data = request.json
    companies = load_data()

    for company in companies['hits']:
        if company['id'] == company_id:
            company.update(updated_data)
            break

    with open('companies.json', 'w', encoding='utf-8') as f:
        json.dump(companies, f, indent=4)

    return jsonify({'message': 'Company updated successfully!'})

# Route to delete company data
@app.route('/api/companies/<string:company_id>', methods=['DELETE'])
def delete_company(company_id):
    companies = load_data()

    companies['hits'] = [company for company in companies['hits'] if company['id'] != company_id]

    with open('companies.json', 'w', encoding='utf-8') as f:
        json.dump(companies, f, indent=4)

    return jsonify({'message': 'Company deleted successfully!'})

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Ensure companies.json exists before running
    if not os.path.exists('companies.json'):
        with open('companies.json', 'w', encoding='utf-8') as f:
            json.dump({"hits": []}, f, indent=4)
    app.run(debug=True)
