Golf Odds Scraper

Overview:
This project is a web scraper designed to fetch golf betting odds from a specified URL. 
It utilizes Selenium with Chrome in headless mode to handle web scraping and BeautifulSoup for HTML parsing. 
The extracted data is saved to an Excel file for easy access and analysis.

Features:
- Headless browsing using undetected ChromeDriver.
- Extraction of golfer names and their odds (Winner, Top 10, Top 5).
- Data saved in Excel format for convenience.

Prerequisites:
Before running the scraper, ensure you have the following installed:

1. Python: Version 3.8 or higher. Download from https://www.python.org/downloads/.

2. Required Libraries: Install the necessary libraries using pip. Open a terminal and run:
   pip install -r requirements.txt

3. Chrome WebDriver: Download the Chrome WebDriver that matches your installed version of Google Chrome from https://chromedriver.chromium.org/downloads.

Configuration:
1. Create Configuration File: In the same directory as the scraper script, create a file named config.ini and add the following content:
   [settings]
   url = <your_target_url_here>
   chrome_path = <path_to_your_chromedriver>

   - Replace <your_target_url_here> with the URL you want to scrape.
   - Replace <path_to_your_chromedriver> with the full path to your ChromeDriver executable.

Usage:
1. Open Terminal or Command Prompt: Navigate to the directory where the scraper script is located.

2. Run the Script: Execute the following command:
   python <your_script_name.py>

   - Replace <your_script_name.py> with the actual name of your Python script file.

3. Wait for Completion: The scraper will run and display the extracted data in the console. 
   The data will be saved to an Excel file named golf_odds.xlsx in the same directory.

Functionality Breakdown:
- Loading Configuration: The scraper loads the target URL and Chrome driver path from the config.ini file.
- Selenium Setup: The script uses Selenium with undetected ChromeDriver to scrape the webpage in headless mode, avoiding detection by websites.
- Data Extraction: The scraper extracts golfer names and their betting odds for winning, top 10, and top 5 finishes.
- Saving Data: Extracted data is saved in an Excel file using pandas.

Troubleshooting:
- Chromedriver Issues: Ensure your ChromeDriver version matches your installed Chrome version. 
  You can check your Chrome version by navigating to chrome://settings/help in your browser.

- Configuration Errors: Double-check the path in your config.ini to ensure it’s correctly set up.

- Web Page Changes: If the web page structure changes, the scraper may not work correctly. 
  Inspect the webpage and adjust the extract_golf_odds function accordingly.

- Slow Loading: If the webpage takes longer to load, increase the time.sleep(4) duration in the script.

Contribution:
Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request.

License:
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments:
- Selenium: https://www.selenium.dev/
- BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/
- Pandas: https://pandas.pydata.org/
