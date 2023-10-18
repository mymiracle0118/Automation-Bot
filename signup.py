import selenium
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

#login function
def signUp(firstnamestr, secondnamestr, emailaddressstr, passwordstr, selectcountrystr):
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--start-maximized")  # Maximize the browser window
    chrome_options.add_experimental_option("detach", True)
    # chrome_options.add_argument("--user-data-dir=" + r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')  # Replace with the path to your profile directory
    # chrome_options.add_argument("--profile-directory=\\Profile 61")
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()

    driver.get('https://www.upwork.com/nx/signup/?dest=home')

    # time.sleep(5)
    # driver.find_element_by_link_text('Login').click()
    # radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and @value='hire']")
    # driver.find_element_by_xpath("//div[contains(@class, 'first_name')]")
    # driver.find_element_by_class_name("first_name")
    # selectItem='Agoda'
    #First click on the All reviews element to open up the dorpdown element
    time.sleep(2)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[data-qa='work']"))).click()
    # WebDriverWait(driver,10).until(EC.element_to_be_clickable()).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='btn-apply']"))).click()
    # test = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//text[@aria-label='First name']")))
    time.sleep(2)
    firstname = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "first-name-input")))
    firstname.send_keys(firstnamestr)
    firstname.send_keys(Keys.ENTER)

    time.sleep(2)
    secondname = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "last-name-input")))
    secondname.send_keys(secondnamestr)
    secondname.send_keys(Keys.ENTER)

    time.sleep(2)
    emailaddress = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "redesigned-input-email")))
    emailaddress.send_keys(emailaddressstr)
    emailaddress.send_keys(Keys.ENTER)
    # print(passwordstr)
    # return

    time.sleep(2)
    password = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "password-input")))
    password.send_keys(passwordstr)
    password.send_keys(Keys.ENTER)
  
    # checkboxlabel = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "checkbox-terms")))
    # if not checkboxlabel.is_selected():
    # checkboxlabel.click()
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "checkbox-terms"))).click()

    # time.sleep(5)
    # time.sleep(20)
    time.sleep(2)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,"country-dropdown"))).click()

    time.sleep(2)
    countrysearch = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class, 'up-dropdown-menu')]/div/div/div/child::input")))
    # testdiv.click()

    countrysearch.click()
    time.sleep(1)
    countrysearch.send_keys(selectcountrystr)
    countrysearch.send_keys(Keys.ENTER)
    # //div[@class='sort']/child::select
    # time.sleep(500)
    time.sleep(2)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//li[contains(@class, 'up-menu-item')]"))).click()

    # WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), '" + selectcountrystr + "')]"))).click()

    # time.sleep(10)

    # div[@class='sort']/..
    time.sleep(2)
    checkboxlabel = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='checkbox-terms']/../../..")))
    checkboxlabel.click()

    time.sleep(2)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,"button-submit-form"))).click()
    # button = driver.find_element(By.XPATH, "//input[@type='button' and @value=' Join as a Client ']")
    # button.click()
    # radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and @value='hire']")
    # driver.find_element_by_name('user').send_keys(user)
    # time.sleep(20)
    time.sleep(3)
    # driver.quit()

def importCSVFile():
    with open('signupinfo.csv', newline='') as csvfile:
        dataArray = list(csv.reader(csvfile))
        # print(len(dataArray))
        # print(dataArray)
    return dataArray

def exportCSVFile(data):
    header = ['email', 'password', 'verify_url']
    with open('signupverify.csv', 'w', encoding='UTF8', newline='') as f:
        csvfile = csv.writer(f)

        # write the header
        csvfile.writerow(header)

        # write multiple rows
        csvfile.writerows(data)

def main():
    print("\n=========Import CSV=========\n")
    accountinfos = importCSVFile()
    data = []
    index = 1
    print("\n=========Start=========\n")
    for account in accountinfos:
        if(account[0] != 'No' and account[0] != ''):
            # print(account[0], account[1], account[2], account[3], account[4], account[5])
            print("Account\n", index)
            signUp(firstnamestr=account[1], secondnamestr=account[2], emailaddressstr=account[3], passwordstr=account[4], selectcountrystr=account[5])
            verifyaccount = []
            verifyaccount.append(account[3])
            verifyaccount.append(account[4])
            verifyaccount.append('')
            data.append(verifyaccount)
            index = index + 1
    print("=========Export CSV========\n")
    exportCSVFile(data)
    print("=========End=========\n")

#take input from user
print("======================================================================\n")
print("------Welcome to My Sign Up Bot------\n")
print("======================================================================\n")

main()

#login()
#register()




