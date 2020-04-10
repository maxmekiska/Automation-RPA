# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:20:06 2020

@author: Max
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def load_data():
    global df
    form_data = 'Data.xlsx'
    df = pd.read_excel(form_data)
    




def open_browser():
    global driver
    driver = webdriver.Firefox()
    driver.get('http://www.rpachallenge.com/')



# start the challenge baby!!!
def start_challenge():
    initiate = driver.find_element_by_xpath("//button[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']")
    initiate.click()



# finding fields to fill out
def getfields():
    global address_field, companyName_field, email_field, firstName_field, lastName_field, phoneNumber_field, role_field, submit 
    address_field = driver.find_element_by_xpath("//input[@ng-reflect-name='labelAddress']")
    companyName_field = driver.find_element_by_xpath("//input[@ng-reflect-name='labelCompanyName']")
    email_field= driver.find_element_by_xpath("//input[@ng-reflect-name='labelEmail']")
    firstName_field = driver.find_element_by_xpath("//input[@ng-reflect-name='labelFirstName']")
    lastName_field = driver.find_element_by_xpath("//input[@ng-reflect-name='labelLastName']")
    phoneNumber_field = driver.find_element_by_xpath("//input[@ng-reflect-name='labelPhone']")
    role_field = driver.find_element_by_xpath("//input[@ng-reflect-name='labelRole']")
    submit = driver.find_element_by_xpath("//input[@value='Submit']")
    


def fillfields():
    for i in range(len(df)):
        getfields()
        address_field.send_keys(df['Address'][i])
        companyName_field.send_keys(df['Company Name'][i])
        email_field.send_keys(df['Email'][i])
        firstName_field.send_keys(df['First Name'][i])
        lastName_field.send_keys(df['Last Name '][i])
        role_field.send_keys(df['Role in Company'][i])
        phoneNumber_field.send_keys(str(df['Phone Number'][i]))
        submit.click()
    

def main():
    load_data()
    open_browser()
    start_challenge()
    getfields()
    fillfields()
    

main()




