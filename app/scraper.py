from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


def scrape_data(username, password, url):
    # Set up headless Chrome options
    chrome_options = Options()
    # chrome_options.add_argument('--headless=new')
 
    # Initialize Chrome driver with headless options
    service = Service('C:\\Users\\viju\\Desktop\\plugins\\New folder\\linkedin-bot-master\\chromedriver_win32\\new driver\\chromedriver-win64\\chromedriver.exe')  # Replace with path to your ChromeDriver executable
    service.start()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)

        # Wait until the email input field is present on the page
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'email')))

        # Locate the username and password fields and input credentials
        username_input = driver.find_element(By.NAME, 'email')  # Update to the correct name for the email input
        password_input = driver.find_element(By.NAME, 'password')  # Update to the correct name for the password input
        username_input.send_keys(username)
        password_input.send_keys(password)

        # Submit the form
        # password_input.submit()
        password_input.send_keys(Keys.ENTER)

        # Wait for the page to load after login
        time.sleep(5)
        driver.get(url)

        time.sleep(5)

        # Wait for the page to load after login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'BrowseInternship_container__33LSA')))

        # # Now, the browser should be logged in. Proceed to fetch job details
        # soup = BeautifulSoup(driver.page_source, 'html.parser')
        # main_container = soup.find(class_='BrowseInternship_container__33LSA')

        # # Extract job details
        # job_listings = []

        # job_elements = main_container.find_all(class_='StudentInternshipCard_innerContainer__3shqY')
        
        # for job_element in job_elements:
        #     job_title = job_element.find("h3").text.strip()
        #     company_info = job_element.find("p").text.strip()
        #     company_name, location = company_info.split(" | ")
        #     skills_container = job_element.find("div", class_="StudentInternshipCard_skills__36uA_")
        #     skills = [skill.text.strip() for skill in skills_container.find_all("div", class_="StudentInternshipCard_skill__3OESd")]
        #     job_link = "exaple.com"
        #     # share_button = job_element.find('div', class_='StudentInternshipCard_internshipHeader__eCWX').find('div', class_='StudentInternshipCard_right__3w8L3').find('StudentInternshipCard_shareBtn__fR5A0')
        #     # job_element.find("a")["href"]


        # Now, the browser should be logged in. Proceed to fetch job details
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        main_container = soup.find(class_='BrowseInternship_container__33LSA')   #find_all(class_="BrowseInternship_container__33LSA")
        #print(main_container);
        
        # Extract job details
        job_elements = main_container.find_all(class_='StudentInternshipCard_innerContainer__3shqY'); #soup.find_all(class_="StudentJobCard_innerContainer__1HYXP")
        #button_container = soup.find(class_='StudentInternshipCard_internshipHeader__eCWX-')
        #share_buttons = button_container.find_all(class_='StudentInternshipCard_shareBtn__fR5A0');
        share_buttons = driver.find_elements(By.CSS_SELECTOR, '.StudentInternshipCard_shareBtn__fR5A0 img')
        # print(share_buttons)
        #print(job_elements)
        time.sleep(3)
        job_listings = []
        for i in range(len(job_elements)):
            job_element = job_elements[i]
            share_button = share_buttons[i]
            job_title = job_element.find("h3").text.strip()
            company_info = job_element.find("p").text.strip()
            company_name, location = company_info.split(" | ")
            skills_container = job_element.find("div", class_="StudentInternshipCard_skills__36uA_")
            skills = [skill.text.strip() for skill in skills_container.find_all("div", class_="StudentInternshipCard_skill__3OESd")] 
            job_link = ""
            time.sleep(3)
            # Click the share button and get the textarea value
            time.sleep(3)
            if share_button:
            
                driver.execute_script("arguments[0].click();", share_button)
                time.sleep(2)  
                # Wait for the dialog to appear (you may need to adjust the wait time)
                textarea_element = driver.find_element(By.CSS_SELECTOR, '.Share_linkText__LBY0t textarea')
                textarea_value = textarea_element.get_attribute('value').split("Link:")
                job_link = textarea_value[1]
                print("Textarea value:", textarea_value)
                time.sleep(2)
                parent_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "Share_header__urDAp")))

                # Find the SVG element within the parent div
                svg_element = parent_div.find_element(By.TAG_NAME, "svg")

                # Click on the SVG element
                svg_element.click()
                time.sleep(1)
            

            # Store job details in a dictionary
            job_data = {
                'title': job_title,
                'company': company_name,
                'location': location,
                'skills': skills,
                'link': job_link
            }

            # Append job data to the list of job listings
            job_listings.append(job_data)

    finally:
        driver.quit()
        service.stop()
    
    print(job_listings)

    return job_listings
