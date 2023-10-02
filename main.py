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

#login function
def signUp(firstnamestr, secondnamestr, emailaddressstr, passwordstr, selectcountrystr):
    driver = webdriver.Chrome()

    driver.get('https://www.upwork.com/nx/signup/?dest=home')

    # time.sleep(5)
    # driver.find_element_by_link_text('Login').click()
    # radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and @value='hire']")
    # driver.find_element_by_xpath("//div[contains(@class, 'first_name')]")
    # driver.find_element_by_class_name("first_name")
    # selectItem='Agoda'
    #First click on the All reviews element to open up the dorpdown element
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[data-qa='hire']"))).click()
    # WebDriverWait(driver,10).until(EC.element_to_be_clickable()).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='btn-apply']"))).click()
    # test = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//text[@aria-label='First name']")))
    firstname = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "first-name-input")))
    firstname.send_keys(firstnamestr)
    firstname.send_keys(Keys.ENTER)

    secondname = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "last-name-input")))
    secondname.send_keys(secondnamestr)
    secondname.send_keys(Keys.ENTER)

    emailaddress = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "redesigned-input-email")))
    emailaddress.send_keys(emailaddressstr)
    emailaddress.send_keys(Keys.ENTER)

    password = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "password-input")))
    password.send_keys(passwordstr)
    password.send_keys(Keys.ENTER)
  
    # checkboxlabel = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "checkbox-terms")))
    # if not checkboxlabel.is_selected():
    # checkboxlabel.click()
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "checkbox-terms"))).click()

    # time.sleep(5)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,"country-dropdown"))).click()
    
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), '" + selectcountrystr + "')]"))).click()

    # div[@class='sort']/..
    checkboxlabel = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='checkbox-terms']/../..")))
    checkboxlabel.click()

    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,"button-submit-form"))).click()
    # button = driver.find_element(By.XPATH, "//input[@type='button' and @value=' Join as a Client ']")
    # button.click()
    # radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and @value='hire']")
    # driver.find_element_by_name('user').send_keys(user)
    # time.sleep(20)
    driver.quit()

def main():
    signUp(firstnamestr="firstname", secondnamestr="secondname", emailaddressstr="barrack_expose378@simplelogin.com", passwordstr="passwordstrR@123", selectcountrystr="Sweden")

#take input from user
print("======================================================================\n")
print("------Welcome to Online notes Sharing made in PHP by Nitin Kumar------\n")
print("======================================================================\n")

main()

#login()
#register()




