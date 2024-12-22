# Company Directory Web Scraper

This project is a fully functional web application that scrapes and displays company information from an external directory. It offers an interactive interface with features for viewing, editing, and deleting company data. The application is built with Flask, BeautifulSoup, and JavaScript, ensuring a responsive and lightweight user experience.

## Features
- **Automated Web Scraping**: Scrapes company details from an external online directory and stores them in a structured JSON file.
- **Dynamic Company Directory**: Displays all scraped companies in a searchable, responsive format.
- **Edit and Delete Functionality**: Modify or remove company details directly from the web interface, with changes reflected in the JSON file.
- **Live Search**: Real-time search functionality for filtering companies by name.
- **Responsive Design**: Ensures seamless user experience across desktop and mobile devices.

## Technologies Used
- **Backend**: Flask (Python) for server-side functionality and API endpoints.
- **Frontend**: HTML5, CSS3, and JavaScript for the user interface.
- **Web Scraping**: BeautifulSoup and Requests (Python) for extracting and fetching data.
- **Data Storage**: JSON for storing scraped company details.

## Installation and Setup
1. **Clone the Repository**
    ```bash
    git clone https://github.com/SANKETKISHU/Web_Scraper.git
    cd Web_Scraper
    ```
2. **Create a Virtual Environment**
    ```bash
    python -m venv .venv
    ```
3. **Activate the Virtual Environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
4. **Install Dependencies**
    ```bash
    pip install flask beautifulsoup4 requests
    ```
5. **Ensure `companies.json` Exists**
    ```bash
    echo "{}" > companies.json
    ```

## Running the Application
1. **Start the Flask Server**
    ```bash
    python web_scrape.py
    ```
2. **Access the Application**
   - Open your browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage
- **Scraping New Data**: Visit `http://127.0.0.1:5000/api/scrape` to scrape and update company data.
- **Viewing Company Details**: View company information, including name, description, email, phone, website, and stand reference, on the main directory page.
- **Editing or Deleting Companies**: Edit company details or delete entries directly from the interface.
- **Searching for Companies**: Use the live search bar to filter companies by name in real time.

## Author
**Sanket Choudhary**  
- Email: [Sanketchoudhary2002@gmail.com](mailto:Sanketchoudhary2002@gmail.com)  
- MCA Student at Manipal University Jaipur  
- GitHub: [SANKETKISHU](https://github.com/SANKETKISHU)
