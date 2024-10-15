import undetected_chromedriver as uc
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import pandas as pd
import configparser

def load_config(config_file="config.ini"):
    """
    Load configuration settings from the config file.
    """
    config = configparser.ConfigParser(interpolation=None)  # Disable interpolation
    config.read(config_file)
    url = config.get("settings", "url")
    chrome_path = config.get("settings", "chrome_path")
    return url, chrome_path

def selenium_headless_request(url, chrome_path):
    """
    Fetches the webpage content using Selenium in headless mode when other methods fail.
    Returns the BeautifulSoup object of the page.
    """
    caps = DesiredCapabilities.CHROME
    caps["pageLoadStrategy"] = "eager"

    # Setup Chrome options for headless mode
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-xss-auditor")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--log-level=3")
    chrome_options.headless = True  # Set to True for headless operation

    # Preferences to avoid pop-ups
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 1
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = None
    try:
        # Initialize the Chrome driver
        driver = uc.Chrome(options=chrome_options, desired_capabilities=caps, executable_path=chrome_path)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # Load the page using Selenium
        driver.get(url)

        # Return the page source as a BeautifulSoup object
        return BeautifulSoup(driver.page_source, "lxml")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if driver:
            try:
                # Ensure that the browser is closed after scraping
                print("Closing browser")
                driver.quit()
            except Exception as quit_exception:
                print(f"Error occurred while quitting the browser: {quit_exception}")

def extract_golf_odds(soup):
    """
    Extracts golfer names and their odds (Winner, Top 10, Top 5) from the provided HTML content.
    """
    data = []

    # Extract golfer names
    golfers = [li.get_text(strip=True) for li in soup.find_all("li", class_="side-rail-name")]

    # Extract odds for Winner, Top 10, and Top 5
    winner_odds = [li.get_text(strip=True) for li in soup.select("div:has(> p.participants:contains('Winner')) ul.outcomes li")]
    top_10_odds = [li.get_text(strip=True) for li in soup.select("div:has(> p.participants:contains('Top 10')) ul.outcomes li")]
    top_5_odds = [li.get_text(strip=True) for li in soup.select("div:has(> p.participants:contains('Top 5')) ul.outcomes li")]

    # Combine data into a structured format
    for i, golfer in enumerate(golfers):
        data.append({
            "Golfer": golfer,
            "Winner Odds": winner_odds[i] if i < len(winner_odds) else "N/A",
            "Top 10 Odds": top_10_odds[i] if i < len(top_10_odds) else "N/A",
            "Top 5 Odds": top_5_odds[i] if i < len(top_5_odds) else "N/A"
        })

    return data

def save_to_excel(data, filename="golf_odds.xlsx"):
    """
    Saves the extracted data to an Excel file using pandas.
    """
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Data successfully saved to {filename}")

if __name__ == "__main__":
    # Load URL and Chrome driver path from config file
    url, chrome_path = load_config()

    # Fetch the webpage content
    soup = selenium_headless_request(url, chrome_path)
    time.sleep(4)  # Allow time for the page to load completely

    # Extract odds data
    odds_data = extract_golf_odds(soup)
    print('odds_data:', odds_data)

    # Save the data to an Excel file
    save_to_excel(odds_data)
