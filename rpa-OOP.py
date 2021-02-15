import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class AutoFill:
    browser = webdriver.Firefox()
    browser.get('http://www.rpachallenge.com/')

    def __init__(self, filename):
        self.df =pd.read_excel(filename)

    def fill_form(self):
        objecto = AutoFill.browser
        print(objecto)
        AutoFill.browser.find_element_by_xpath("//button[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']").click()
        for i in range(len(self.df)):

            AutoFill.browser.find_element_by_xpath("//input[@ng-reflect-name='labelAddress']").send_keys(self.df['Address'][i])
            AutoFill.browser.find_element_by_xpath("//input[@ng-reflect-name='labelCompanyName']").send_keys(self.df['Company Name'][i])
            AutoFill.browser.find_element_by_xpath("//input[@ng-reflect-name='labelEmail']").send_keys(self.df['Email'][i])
            AutoFill.browser.find_element_by_xpath("//input[@ng-reflect-name='labelFirstName']").send_keys(self.df['First Name'][i])
            AutoFill.browser.find_element_by_xpath("//input[@ng-reflect-name='labelLastName']").send_keys(self.df['Last Name '][i])
            AutoFill.browser.find_element_by_xpath("//input[@ng-reflect-name='labelPhone']").send_keys(str(self.df['Phone Number'][i]))
            AutoFill.browser.find_element_by_xpath("//input[@ng-reflect-name='labelRole']").send_keys(self.df['Role in Company'][i])
            AutoFill.browser.find_element_by_xpath("//input[@value='Submit']").click()
        


def main():
    Test = AutoFill('data/Data.xlsx')
    Test.fill_form()


if __name__ == "__main__":
    main()






