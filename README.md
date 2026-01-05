# 📜 Quotes Web Scraper (Python)

A simple Python web scraper that collects quotes, authors, and tags from
**quotes.toscrape.com** and saves the data into a CSV file. This project
demonstrates the basics of web scraping using Requests, BeautifulSoup,
and Pandas.

------------------------------------------------------------------------

## 🚀 Features

-   Scrapes quotes from multiple pages
-   Extracts quote text, author name, and tags
-   Handles request errors safely
-   Saves data into a CSV file
-   Adds delay between requests

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python 3
-   requests
-   beautifulsoup4
-   pandas
-   lxml

------------------------------------------------------------------------

## 📂 Project Structure

    .
    ├── web_scraper.py
    ├── quotes.csv
    └── README.md

------------------------------------------------------------------------

## 📦 Installation

``` bash
pip install requests beautifulsoup4 pandas lxml
```

------------------------------------------------------------------------

## ▶️ How to Run

``` bash
python web_scraper.py
```

After execution, `quotes.csv` will be generated.

------------------------------------------------------------------------

## 📊 Output Columns

-   quote
-   author
-   tags

------------------------------------------------------------------------

## 📌 Notes

-   Scrapes first 5 pages by default
-   Intended for educational purposes

------------------------------------------------------------------------

## 📜 License

Free to use for learning and educational projects.
