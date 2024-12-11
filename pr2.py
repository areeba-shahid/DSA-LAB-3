from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
login_url = 'http://eduko.spikotech.com/Account/Login'
courses_url = 'http://eduko.spikotech.com/Course'
path = r'c:\Users\Rashid ch\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)


driver.get(login_url)


input("Press Enter after logging in...")


driver.get(courses_url)


WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"card-body text-center")]')))

titles = []
instructors = []
semesters = []
descriptions = []
course_codes = []
textbook1s = []
textbook2s = []


def scrape_page():
    courses = driver.find_elements(By.XPATH, '//div[contains(@class,"card-body text-center")]')
    for course in courses:
        try:
            title = course.find_element(By.XPATH, './/h4[contains(@class,"card-title")]').text
            titles.append(title)
        except:
            titles.append('N/A')
        
        try:
            instructors.append(course.find_element(By.XPATH, './/h7[1]').text)  # Assuming first h7 is the instructor
        except:
            instructors.append('N/A')
        
        try:
            semesters.append(course.find_element(By.XPATH, './/h7[2]').text)  # Assuming second h7 is the semester
        except:
            semesters.append('N/A')
        
        try:
            descriptions.append(course.find_element(By.XPATH, './/p[contains(@class,"card-text")]').text)
        except:
            descriptions.append('N/A')
        
        try:
            details_link = course.find_element(By.XPATH, './/a[contains(@class,"btn  btn-md waves-effect")]')
            details_link.click()

            
            WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '//div[contains(@id,"CourseCode")]'))
            )
            time.sleep(3) 
            
            course_code = driver.find_element(By.XPATH, '//div[contains(@id,"CourseCode")]').text
            course_codes.append(course_code)

            try:
                book_list = driver.find_element(By.XPATH, '//ul[contains(@id,"CourseBooks")]')
                textbooks = book_list.find_elements(By.TAG_NAME, 'li')

              
                if len(textbooks) >= 1:
                    textbook1s.append(textbooks[0].text)
                else:
                    textbook1s.append('N/A')

                if len(textbooks) >= 2:
                    textbook2s.append(textbooks[1].text)
                else:
                    textbook2s.append('N/A')

            except:
             
                textbook1s.append('N/A')
                textbook2s.append('N/A')

          
            driver.back()

           
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"card-body text-center")]')))
        
        except Exception as e:
            print(f"An error occurred while scraping details for {title}: {e}")
            course_codes.append('N/A')
            textbook1s.append('N/A')
            textbook2s.append('N/A')

# Scrape the page
scrape_page()


driver.quit()


df_courses = pd.DataFrame({
    'Course Code': course_codes,
    'Title': titles, 
    'Semester': semesters, 
    'Instructor': instructors, 
    'Description': descriptions, 
    'TextBook1': textbook1s,
    'TextBook2': textbook2s
})

df_courses.to_csv('courses.csv', index=False)
print(f'Successfully scraped {len(titles)} entries!')
