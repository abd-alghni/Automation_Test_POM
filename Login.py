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

class Login:

    EMAIL_FIELD = (By.ID, "Email")
    PASSWORD_FIELD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "body > div.master-wrapper-page > div.master-wrapper-content > div > div > div > div.page-body > div.customer-blocks > div.returning-wrapper.fieldset > form > div.buttons > button")
    
    def __init__(self,login_url):
        self.driver = webdriver.Chrome()
        self.driver.get(login_url)

    def read_data(self):
        #with open(r'data_list.txt','r') as abood :
               #abood.read()
               file = open('emails.txt', 'r')
               # Read the email and password from the file
               lines = file.readlines()
               email = lines[1].strip()
               return email
               # password = lines[1].strip()


    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email) 

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password) 

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
