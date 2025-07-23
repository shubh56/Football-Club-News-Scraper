Football Club News Scraper

This Python script allows you to scrape the latest news articles for a specific football club from EyeFootball.com and save the extracted information (URL, Title, and Content) into a CSV file.

Features
Club-Specific News: Fetches news articles relevant to a user-specified football club.

RSS Feed Integration: Starts by parsing the main RSS feed to find the club's news page URL.

Dynamic Content Extraction: Navigates to the club's news page and extracts individual article links.

Article Detail Scraping: For each article, it visits the page to extract the main title and paragraph content.

CSV Export: Saves all scraped data into a structured CSV file (clubname_news.csv) for easy analysis.

User-Agent Spoofing: Includes a User-Agent header in requests to mimic a web browser, reducing the chance of being blocked.

Prerequisites
Before running this script, ensure you have the following installed:

Python 3.x

requests library: For making HTTP requests.

BeautifulSoup4 library: For parsing HTML and XML content.

Installation
Clone this repository (or copy the script content into a .py file).

git clone <repository_url>
cd <repository_directory>

(Note: Replace <repository_url> and <repository_directory> if you host this on GitHub)

Install the required Python libraries:

pip install requests beautifulsoup4

Usage
Run the script from your terminal:

python your_script_name.py

(Replace your_script_name.py with the actual name of your Python file, e.g., news_scraper.py)

The script will prompt you to enter the name of the football club:

Enter the club name: Arsenal

(Enter the full club name as it appears on the website, e.g., "Arsenal", "Liverpool", "Chelsea").

The script will then:

Print the prettified XML content of the RSS feed.

Print the detected <a> tag for the club's news.

List the extracted news article URLs.

Display the titles and content of each article as it's scraped.

Finally, confirm that the data has been saved to a CSV file.

Output
A CSV file named [club_name]_news.csv (e.g., Arsenal_news.csv) will be created in the same directory where you run the script. This file will have three columns:

URL: The full URL of the news article.

Title: The main title of the news article (extracted from the <h1> tag with itemprop="name").

Content: The full text content of the news article (concatenated from <p> tags with style="font-size:16px; padding-top:10px").

Error Handling
The script includes basic error handling for:

Network issues: If it fails to fetch the RSS feed or the club's news page.

File I/O errors: If there's an issue saving the CSV file.

Club Not Found: If the entered club name does not have a corresponding news link in the RSS feed.

License
This project is open-source and available under the MIT LicenseFootball Club News Scraper
This Python script allows you to scrape the latest news articles for a specific football club from EyeFootball.com and save the extracted information (URL, Title, and Content) into a CSV file.

Features
Club-Specific News: Fetches news articles relevant to a user-specified football club.

RSS Feed Integration: Starts by parsing the main RSS feed to find the club's news page URL.

Dynamic Content Extraction: Navigates to the club's news page and extracts individual article links.

Article Detail Scraping: For each article, it visits the page to extract the main title and paragraph content.

CSV Export: Saves all scraped data into a structured CSV file (clubname_news.csv) for easy analysis.

User-Agent Spoofing: Includes a User-Agent header in requests to mimic a web browser, reducing the chance of being blocked.

Prerequisites
Before running this script, ensure you have the following installed:

Python 3.x

requests library: For making HTTP requests.

BeautifulSoup4 library: For parsing HTML and XML content.

Installation
Clone this repository (or copy the script content into a .py file).

git clone <repository_url>
cd <repository_directory>

(Note: Replace <repository_url> and <repository_directory> if you host this on GitHub)

Install the required Python libraries:

pip install requests beautifulsoup4

Usage
Run the script from your terminal:

python your_script_name.py

(Replace your_script_name.py with the actual name of your Python file, e.g., news_scraper.py)

The script will prompt you to enter the name of the football club:

Enter the club name: Arsenal

(Enter the full club name as it appears on the website, e.g., "Arsenal", "Liverpool", "Chelsea").

The script will then:

Print the prettified XML content of the RSS feed.

Print the detected <a> tag for the club's news.

List the extracted news article URLs.

Display the titles and content of each article as it's scraped.

Finally, confirm that the data has been saved to a CSV file.

Output
A CSV file named [club_name]_news.csv (e.g., Arsenal_news.csv) will be created in the same directory where you run the script. This file will have three columns:

URL: The full URL of the news article.

Title: The main title of the news article (extracted from the <h1> tag with itemprop="name").

Content: The full text content of the news article (concatenated from <p> tags with style="font-size:16px; padding-top:10px").

Error Handling
The script includes basic error handling for:

Network issues: If it fails to fetch the RSS feed or the club's news page.

File I/O errors: If there's an issue saving the CSV file.

Club Not Found: If the entered club name does not have a corresponding news link in the RSS feed.

License
This project is open-source and available under the MIT License.
