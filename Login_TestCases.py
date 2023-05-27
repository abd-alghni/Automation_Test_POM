import unittest
from selenium import webdriver
# import SignUp
from Login import Login
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

class Login_TestCases():
    def run(self):
        login_url="https://demo.nopcommerce.com/login?returnUrl=%2F"
        self.login = Login(login_url)

        #Happy Path Registration
        
        email=self.login.read_data()
        self.login.enter_email(email)
        password='Test1234$$'
        self.login.enter_password(password)
        sleep(1)
        self.login.click_login_button()  
        sleep(10)

        #I Can Add More Test Cases As I Need..
        

Login_TestCases().run()
