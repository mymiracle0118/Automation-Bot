import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def leave():
    driver = webdriver.Chrome()
    driver.quit()

#login function
def login():
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
    firstname.send_keys(user)
    firstname.send_keys(Keys.ENTER)

    secondname = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "last-name-input")))
    secondname.send_keys(pswd)
    secondname.send_keys(Keys.ENTER)

    emailaddress = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "redesigned-input-email")))
    emailaddress.send_keys('bagel_blaspheme726@simplelogin.com')
    emailaddress.send_keys(Keys.ENTER)

    password = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "password-input")))
    password.send_keys('testtesttesttest!23Q')
    password.send_keys(Keys.ENTER)

    # time.sleep(5)
    selectcountry = 'Sweden'
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,"country-dropdown"))).click()
    
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Sweden')]"))).click()
    # button = driver.find_element(By.XPATH, "//input[@type='button' and @value=' Join as a Client ']")
    # button.click()
    # radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and @value='hire']")
    # driver.find_element_by_name('user').send_keys(user)

    #put username
    time.sleep(20)
    driver.find_element_by_name('user').send_keys(user)

    #put password
    time.sleep(3)
    driver.find_element_by_name('pass').send_keys(pswd)

    #click on submit link
    time.sleep(3)
    driver.find_element_by_name('login').click()

def register():
    driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

    driver.get('http://onlinenotessharing.epizy.com/index.php')
    time.sleep(5)
    driver.find_element_by_link_text('Sign Up').click()

    #put name
    time.sleep(3)
    driver.find_element_by_name('name').send_keys(name)

    #put email
    time.sleep(3)
    driver.find_element_by_name('email').send_keys(mail)

    #put username
    time.sleep(3)
    driver.find_element_by_name('username').send_keys(usrnm)

    #put password
    time.sleep(3)
    driver.find_element_by_name('password').send_keys(pswd1)

    #put repassword
    time.sleep(3)
    driver.find_element_by_name('repassword').send_keys(pswd1)

    #select gender from dropdown
    time.sleep(3)
    select_gender = Select(driver.find_element_by_name('gender'))
    if gndr == 1:
        select_gender.select_by_visible_text('Male')
    else:
        select_gender.select_by_visible_text('Female')

    #select profession
    time.sleep(3)
    select_profession = Select(driver.find_element_by_name('role'))
    if role == 1:
        select_profession.select_by_visible_text('Teacher')
    else:
        select_profession.select_by_visible_text('Student')

    #select branch
    time.sleep(3)
    select_branch = Select(driver.find_element_by_name('course'))
    if branch == 1:
        select_branch.select_by_visible_text('Computer Sc Engineering')
    elif branch == 2:
        select_branch.select_by_visible_text('Electrical Engineering')
    else:
        select_branch.select_by_visible_text('Mechanical Engineering')

    #click submit
    time.sleep(3)
    driver.find_element_by_name('signup').click()

    #registerred successfully alert
    time.sleep(1)
    alert = driver.switch_to_alert()
    alert.accept()

    time.sleep(3)

    #put username
    time.sleep(3)
    driver.find_element_by_name('user').send_keys(usrnm)

    #put password
    time.sleep(3)
    driver.find_element_by_name('pass').send_keys(pswd1)

    #click on submit link
    time.sleep(3)
    driver.find_element_by_name('login').click()

    time.sleep(5)
    driver.quit()

#--------------------------------------------

#take input from user
print("======================================================================\n")
print("------Welcome to Online notes Sharing made in PHP by Nitin Kumar------\n")
print("======================================================================\n")
ask = int(input("What do you want to do ?\n 1. Login\n 2. Make Account"))

if ask == 1:
    user = input("Enter your username:")
    pswd = input("Enter your password:")
    login()
elif ask == 2:
    name = input("Enter your fullname:")
    mail = input("Enter your email:")
    usrnm = input("Enter your username:")
    pswd1 = input("Enter your password:")
    gndr = int(input("Chose your gender: \n 1. Male\n 2. Female\n1 or 2:"))
    role = int(input("Chose your role:\n 1. Teacher\n 2. Student\n1 or 2:"))
    branch = int(input("Choose branch:\n 1. Computer Science\n 2. Electrical Engineering\n 3. Mechanical Engineering\n1 or 2 or 3:"))

    register()
else:
    print("Please chose valid answer ...")


#login()
#register()




