from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def check_website_status():
    # Setup Chrome in headless mode
    service = Service(executable_path=r"C:\Users\Dhiman\Desktop\Projects\TestMorningDraft\chromedriver.exe")  # Update path if needed
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run without opening browser window

    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.themorningdraft.com")
        time.sleep(2)  # Wait for the page to load
        title = driver.title
        print(f"[main.py] Page loaded. Title: {title}")
        return title
    except Exception as e:
        print(f"[main.py] Error accessing the website: {e}")
        return None
    finally:
        driver.quit()

# Check if main.py is being run directly
if __name__ == "__main__":
    print("[main.py] Running main function...")
    check_website_status()
