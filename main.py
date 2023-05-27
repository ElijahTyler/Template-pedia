from selenium import webdriver
from selenium.webdriver import FirefoxOptions

from TemplateListings import TemplateListings

from bs4 import BeautifulSoup
from sys import platform
import os, time
import time
import json

maindir = os.path.dirname(os.path.abspath(__file__))

def init_firefox(headless=False):
    opts = FirefoxOptions()

    if platform == "win32":
        opts.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver_executable = os.path.join(maindir, 'geckodriver.exe')
    elif platform in ["linux", "linux2"]:
        driver_executable = os.path.join(maindir, 'geckodriver')
    else:
        print("Unsupported OS. Exiting program...")
        exit(1)

    if headless:
        opts.add_argument("--headless")
    opts.add_argument("--ignore-certificate-errors")
    opts.add_argument("--start-maximized")

    driver = webdriver.Firefox(options = opts, executable_path = driver_executable)
    return driver

def main(url_list):
    start_time = time.time()

    template_list = []
    for USER_URL in url_list:
        print("Loading Selenium (firefox)...")
        driver = init_firefox(headless=False)

        print("Loading template.website URL...")
        driver.get(USER_URL)

        CURRENT_CLASS = "template-class-name"

        entries = []
        timeout = 0
        while not entries:
            time.sleep(1)
            html = driver.execute_script("return document.documentElement.outerHTML")
            soup = BeautifulSoup(html, 'html.parser')
            entries = soup.find_all(attrs={"class": CURRENT_CLASS})
            timeout += 1
            if timeout > 10:
                print(f"Timeout reached. Ending program...")
                driver.close()
                break
        
        for entry in entries:
            tl = TemplateListings(str(entry))
            template_list.append(tl)

        driver.close()

    print(f"Success! Results found: {len(template_list)}")
    
    with open("listings.json", "w") as f:
        listing = 1
        template_dict = {}
        for template in template_list:
            template_dict[listing] = template.to_dict()
            listing += 1
        json.dump(template_dict, f, indent=4)

    # time taken to 2 decimal points
    total_time = round(time.time() - start_time, 2)
    print(f"Time taken: {total_time} seconds")

if __name__ == "__main__":
    # step 1: Go to template.website
    # step 2: Set your search parameters
    # step 3: Copy the urls FOR EACH INDIVIDUAL PAGE and paste it here
    # aside: r"" (raw string) eliminates the need to escape the backslashes

    # example setup:
    # url1 = r"https://www.template.website/something"
    # url2 = r"https://www.template.website/something"
    # ...
    # urls = [url1, url2, ...]
    # main(urls)

    url1 = r"https://www.template.website/something"
    urls = [url1]
    main(urls)