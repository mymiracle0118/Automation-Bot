import selenium
import time
import os
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def verify():
    driver = webdriver.Chrome()
    driver.get(verify_url)
    
    time.sleep(3)
    emailInput = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login_username")))
    emailInput.send_keys(email)
    emailInput.send_keys(Keys.ENTER)

    time.sleep(3)
    pwdInput = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login_password")))
    pwdInput.send_keys(pwd)
    pwdInput.send_keys(Keys.ENTER)

    try:
        time.sleep(3)
        getStartedBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='d-md-flex d-none mr-md-7 align-items-center']/button[1]")))
        getStartedBtn.click()

        time.sleep(3)    
        experBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='span-md-4'][3]")))
        experBtn.click()
        
        time.sleep(3)
        nextBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='next-button']")))
        nextBtn.click()
        
        time.sleep(3)
        moneySideBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='span-md-3'][2]")))
        moneySideBtn.click()

        time.sleep(3)
        nextBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='next-button']")))
        nextBtn.click()
        
        time.sleep(3)
        referenceOptionBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'span-md-4') and contains(@class, 'd-flex')][1]")))
        referenceOptionBtn.click()

        time.sleep(3)
        nextBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='next-button']")))
        nextBtn.click()
    except TimeoutException:
        print("Go to uploading resume beyond this steps!~~~")

    try:
        # uploading resume file
        time.sleep(3)
        base_resume_dir = os.getcwd() + "\\source\\resumes\\"
        openUploadResumeBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='resume-upload-btn-mobile']")))
        openUploadResumeBtn.click()

        time.sleep(3)
        driver.execute_script("document.querySelector('span.fe-upload-btn input').style.left='0px'")
        uploadResumeInput = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'fe-upload-btn') and contains(@class, 'upload-btn')]/input")))
        uploadResumeInput.send_keys(os.path.join(base_resume_dir, resume_url))

        time.sleep(3)
        uploadResumeBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='resume-upload-continue-btn']")))
        uploadResumeBtn.click()
    
        # professional roles
        time.sleep(3)
        roleInput = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-qa='title-text']/input")))
        roleInput.clear()
        roleInput.send_keys(role)

        time.sleep(3)
        nextBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='next-button']")))
        nextBtn.click()
        
        time.sleep(3)
        nextBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='next-button']")))
        nextBtn.click()
        
        time.sleep(3)
        nextBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='next-button']")))
        nextBtn.click()
        
        time.sleep(3)
        nextBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='next-button']")))
        nextBtn.click()
    except TimeoutException:
        print("Go to skill setting beyond this steps!~~~")
    
    try:
        time.sleep(3)
        skillTokens = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class, 'air3-token-multi-select') and contains(@class, 'air3-token')]")))
        selected_skill_cnt = 0
        for skillToken in skillTokens:
            time.sleep(1)
            if selected_skill_cnt < 15:
                skillToken.click()
                selected_skill_cnt += 1
            else:
                break
        time.sleep(3)
        nextBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='next-button']")))
        nextBtn.click()
    except TimeoutException:
        print("Go to profile setting beyond this steps!~~~")

    try:
        time.sleep(3)
        profileTextarea = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-qa='overview-text']/div/textarea")))
        profileTextarea.clear()
        profileTextarea.send_keys(profile)

        time.sleep(3)
        nextBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='next-button']")))
        nextBtn.click()
    except TimeoutException:
        print("Go to service setting beyond this steps!~~~")
    
    try:
        time.sleep(3)
        serviceTokens = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//button[@data-qa='category-add-btn']")))
        for serviceToken in serviceTokens:
            time.sleep(1)
            serviceToken.click()
        
        time.sleep(3)
        nextBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='next-button']")))
        nextBtn.click()
    except TimeoutException:
        print("Go to hourly rate setting beyond this steps!~~~")
    
    try:
        time.sleep(3)
        rateInput = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@data-ev-label='currency_input']")))
        rateInput.send_keys(rate)
        
        time.sleep(3)
        nextBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='next-button']")))
        nextBtn.click()
    except TimeoutException:
        print("Go to photo and location setting beyond this steps!~~~")
        
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "onetrust-accept-btn-handler"))).click()
        
        time.sleep(3)    
        openUploadPhotoBtn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-qa='open-loader']")))
        openUploadPhotoBtn.click()
        
        time.sleep(3)
        base_photo_dir = os.getcwd() + "\\source\\avatars\\"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='air3-image-crop-area']/div/label")))
        driver.execute_script("""document.querySelector("[name='imageUpload']").style.opacity=100""")

        time.sleep(3)
        uploadPhotoInput = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='air3-image-crop-area']/div/input")))
        uploadPhotoInput.send_keys(os.path.join(base_photo_dir, photo))
        
        time.sleep(3)
        uploadPhotoBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='btn-save']")))
        uploadPhotoBtn.click()
        
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//button[@data-qa='btn-save']")))
        countryInputDiv = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-qa='dropdown-country']/div")))
        countryInputDiv.click()
        
        time.sleep(3)
        countrySearchInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'air3-dropdown-menu-container')]//input")))
        countrySearchInput.click()
        countrySearchInput.send_keys(country)

        time.sleep(1)
        countryToken = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='air3-dropdown-menu-container']//ul[@data-test='menu']/li[1]")))
        countryToken.click()
        # WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(By.ID, "onetrust-accept-btn-handler"))
        
        time.sleep(3)
        cityInputdiv = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-qa='input-city']//div[contains(@class, 'air3-input-group') and contains(@class, 'air3-input-group-clear')]")))
        actions = ActionChains(driver)
        actions.click(cityInputdiv).perform()
        
        time.sleep(3)
        cityInput = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-qa='input-city']//input[@type='search']")))
        cityInput.send_keys(city)
        
        time.sleep(2)
        li_elements = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@data-test='menu-container']/ul/li[1]")))
        # elementcount = len(li_elements)

        # if elementcount == 1:
        #     li_elements.send_keys(Keys.ENTER)
        # else:
        #     li_elements[1].send_keys(Keys.ENTER)
        # li_elements.send_keys(Keys.ENTER)
        li_elements.click()
        
        time.sleep(3)
        birthInput = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-labelledby='date-of-birth-label']")))
        birthInput.send_keys(transform_date_format(birth))

        time.sleep(3)
        streetInput = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-labelledby='street-label']")))
        streetInput.send_keys(street)

        time.sleep(3)
        postCodeInput = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-labelledby='postal-code-label']")))
        postCodeInput.send_keys(str(post_code))

        time.sleep(3)
        phoneInput = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='tel']")))
        phoneInput.send_keys(phone)

        time.sleep(3)
        nextBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='next-button']")))
        nextBtn.click()
    except TimeoutException:
        print("Go to submit step!~~~")
    
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='submit-profile-top-btn']"))).click()

    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Browse jobs')]"))).click()

    time.sleep(3)
    driver.quit()
    
def transform_date_format(date_string):
    # Parse the input date string
    date_obj = datetime.strptime(date_string, '%m/%d/%Y')
    
    # Format the date object to the desired format
    transformed_date = date_obj.strftime('%Y-%m-%d')
    
    return transformed_date

#--------------------------------------------

#take input from user
print("======================================================================\n")
print("------Welcome to Costless Project------\n")
print("======================================================================\n")

datas = pd.read_csv('source/signupverify.csv')

summary = pd.read_csv('source/summary.csv')
summary_len = len(summary)

print("================Start================")

for index, row in datas.iterrows():
    print("Account - %d\n", index)
    verify_url = row['verify_url']
    email = row['email']
    pwd = row['password']
    
    summary_row = summary.iloc[index % summary_len]
    resume_url = summary_row['resume_url']
    role = summary_row['role']
    rate = summary_row['rate']
    photo = summary_row['self_img']
    street = summary_row['street']
    city = summary_row['city']
    post_code = summary_row['post_code']
    phone = summary_row['phone']
    profile = summary_row['profile']
    birth = summary_row['birth']
    country = summary_row['country']
    
    verify()

print("================End================\n")

