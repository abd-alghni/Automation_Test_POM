import unittest
from selenium import webdriver
# import SignUp
from SignUp import SignUp
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

class SignUp_TestCases():
    def run(self):
        signup_url="https://demo.nopcommerce.com/register?returnUrl=%2F"
        self.signup = SignUp(signup_url)

        #Happy Path Registration
        self.signup.chose_gender()
        self.signup.enter_first_name('Abdalghani')
        self.signup.enter_last_name("Owda")
        self.signup.select_date_of_birth_day('24')
        self.signup.select_date_of_birth_month('June')
        self.signup.select_date_of_birth_year('2000')
        f=Faker()
        email=(f.email())
        self.signup.enter_email(email)
        f=Faker()
        company_name=(f.company())
        self.signup.enter_company_name(company_name)
        password='Test1234$$'
        self.signup.enter_password(password)
        self.signup.enter_confirm_password(password)
        sleep(1)
        self.signup.click_register_button()  
        sleep(1)
        self.signup.store_email(email)
        sleep(1)
        self.signup.click_continue_button()
        sleep(10)

        #I Can Add More Test Cases As I Need..
        

SignUp_TestCases().run()
