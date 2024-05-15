import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Path to your Microsoft Edge WebDriver executable
webdriver_path = r'C:\Users\Administrator\Downloads\Compressed\edgedriver_win64.exe'

# Path to the directory where you want to store user data
# Replace 'your_user_data_directory' with the actual path
user_data_directory = r'C:\Users\YourUserName\AppData\Local\Microsoft\Edge\User Data\Profile 2'


def generate_random_number():
    return random.randint(1, 10000)


def search_random_number(driver):
    random_number = generate_random_number()
    search_query = f"Random number: {random_number}"
    driver.get("https://www.bing.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)


def main():
    driver = None
    try:
        edge_options = webdriver.EdgeOptions()
        #edge_options.add_argument("user-data-dir=" + user_data_directory)

        driver = webdriver.Edge()

        search_random_number(driver)

        # Loop to open additional tabs and perform searches
        # 14 tabs as my laptop has only 8gb RAM you can change the range to 30-40 tabs too
        for _ in range(14):
            # Opens a new tab
            driver.execute_script("window.open('');")

            # Switch to the newly opened tab
            driver.switch_to.window(driver.window_handles[-1])

            # Search for a random number
            search_random_number(driver)
            
            # Wait for 10 seconds for Edge to update the reward points
            # You can reduce to sleep time if it takes less time to update!
            time.sleep(10)
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

