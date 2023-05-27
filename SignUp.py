from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import threading
from faker import Faker
import faker
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from random import uniform
import string

class SignUp:

    
    GENDER_FIELD = (By.ID, "gender-male")
    FIRST_NAME_FIELD = (By.ID, "FirstName")
    LAST_NAME_FIELD = (By.ID, "LastName")
    DATE_OF_BIRTH_DAY_FIELD = (By.NAME, "DateOfBirthDay")
    DATE_OF_BIRTH_MONTH_FIELD = (By.NAME, "DateOfBirthMonth")
    DATE_OF_BIRTH_YEAR_FIELD = (By.NAME, "DateOfBirthYear")
    EMAIL_FIELD = (By.ID, "Email")
    COMPANY_NAME_FIELD = (By.ID, "Company")
    PASSWORD_FIELD = (By.ID, "Password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
    CONTINUE_BUTTON = (By.CSS_SELECTOR,"body > div.master-wrapper-page > div.master-wrapper-content > div > div > div > div.page-body > div.buttons > a")
    
    def __init__(self,signup_url):
        # options= webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_argument("--lang=en-US")
        # options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--incognito")
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-setuid-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--disable-accelerated-2d-canvas')
        # options.add_argument('--disable-gpu')
        # self.driver = webdriver.Chrome('chromedriver.exe', options=options)
        self.driver = webdriver.Chrome()
        self.driver.get(signup_url)

    def chose_gender(self ):
        self.driver.find_element(*self.GENDER_FIELD).click()

    def enter_first_name(self,first_name):
        
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)

    def enter_last_name(self,last_name):
        
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)

    def select_date_of_birth_day(self, day):
        Select(self.driver.find_element(*self.DATE_OF_BIRTH_DAY_FIELD)).select_by_visible_text(day)

    def select_date_of_birth_month(self, month):
        Select(self.driver.find_element(*self.DATE_OF_BIRTH_MONTH_FIELD)).select_by_visible_text(month)

    def select_date_of_birth_year(self, year):
        Select(self.driver.find_element(*self.DATE_OF_BIRTH_YEAR_FIELD)).select_by_visible_text(year)    

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email) 

    def enter_company_name(self,company_name):
        self.driver.find_element(*self.COMPANY_NAME_FIELD).send_keys(company_name) 

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password) 

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.CONFIRM_PASSWORD_FIELD).send_keys(confirm_password) 
        
    def click_register_button(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()
         

    def click_continue_button(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def store_data(self,email,company_name,password):
        with open(r'data_list.txt','a') as abood :
               new_record='Email:'+email+', Company Name: '+company_name+', Password:'+password
               abood.write(f"[{new_record}]\n")