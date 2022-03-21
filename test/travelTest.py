import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

from UserCredential import UserData


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('C:\\Users\\user\\PycharmProjects\\TestTask\\chromedriver.exe')
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        cls.action = ActionChains(cls.driver)



    def testRun(self):
        self.signup()
        self.login()
        self.hotel()
        self.search()
        self.book()
        self.buy()
        self.tearDown()

    def signup(self):
        self.driver.get('https://www.phptravels.net/signup')
        self.driver.find_element(By.NAME, 'first_name').send_keys(UserData.Name)
        self.driver.find_element(By.NAME, 'last_name').send_keys(UserData.Surname)
        self.driver.find_element(By.NAME, 'phone').send_keys(UserData.Phone)
        self.driver.find_element(By.NAME, 'email').send_keys(UserData.Email)
        self.driver.find_element(By.NAME, 'password').send_keys(UserData.Password)
        self.action.move_to_element(self.driver.find_element(By.XPATH, '//*[@id="cookie_stop"]')).click().perform()
        self.driver.execute_script("window.scrollTo(0, 300);")
        sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[7]/button').click()

    def login(self):
        # print('starting login test')
        self.driver.find_element(By.NAME, 'email').send_keys(UserData.Email)
        self.driver.find_element(By.NAME, 'password').send_keys(UserData.Password)
        self.driver.implicitly_wait(5)
        url1 = self.driver.current_url
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[3]/button').click()
        sleep(2)
        url2 = self.driver.current_url
        self.assertNotEqual(url1, url2)

    def hotel(self):
        self.driver.implicitly_wait(3)
        url3 = self.driver.current_url
        self.driver.find_element(By.XPATH, '//*[@id="fadein"]/header/div[2]/div/div/div/div/div[2]/nav/ul/li[2]/a').click()
        sleep(2)
        url4 = self.driver.current_url
        self.assertNotEqual(url3, url4)

    def search(self):
        self.driver.find_element(By.XPATH, '// *[ @ id = "select2-hotels_city-container"]').click()
        self.driver.find_element(By.XPATH, '// *[ @ id = "fadein"] / span / span / span[1] / input').send_keys('Yerevan')
        sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="select2-hotels_city-results"]/li').click()
        self.driver.find_element(By.ID, 'submit').click()
        sleep(2)
        self.driver.find_element(By.XPATH,'//i[contains(@class, "la la-angle-right")]').click() #details button
        sleep(6)
        self.driver.switch_to.window(self.driver.window_handles[1])
        element = self.driver.find_element(By.XPATH, '//li[contains(@class, "PropertyCard PropertyCardItem")]')
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(element))
        sleep(6)
        self.action.move_to_element(self.driver.find_element(By.XPATH, '//*[@id="contentContainer"]/div[3]/ol/li[2]/div/a/div/div[3]/div/div[3]/button/div/div/div/span')).click().perform()




    def book(self):
        sleep(5)
        print('starting book testing')
        self.driver.switch_to.window(self.driver.window_handles[2])
        sleep(6)
        self.driver.execute_script("window.scrollTo(0, 3000);")
        self.action.move_to_element(self.driver.find_element(By.XPATH, '//*[@id="ChildRoom-CqcBCP6Ul6wDEAIgAjAGSg0zNjVEMTAwUF8xMDBQUIq2A3qFAVNvbWUoNzE0NDk4OTkpfDQ0ODk4MDI4N3wxfDIwMTgxNDQ0Ml8yMDkyNTMzNDZAbnwzfFJPfExpc3QoKXwzNjVEMTAwUF8xMDBQfFNvbWUoMXxST3w3MTQ0OTg5OXx4aXdhbnwyMDE4MTQ0NDJfMjA5MjUzMzQ2QG58MjAxODE0NDQyfCkSAggBGgQoBjAB"]/div/div[5]/div[1]/div/div[1]/button')).click().perform() #book button





    def buy(self):
        self.driver.implicitly_wait(3)
        print('starting buy test')
        self.driver.find_element(By.ID, 'firstName_lastName').send_keys(UserData.Name+' '+UserData.Surname)
        self.driver.find_element(By.ID, 'email').send_keys(UserData.Email)
        self.driver.find_element(By.ID, 'retypeEmail').send_keys(UserData.Email)
        self.driver.execute_script("window.scrollTo(0, 3000);")
        self.action.move_to_element(self.driver.find_element(By.XPATH, '//*[@id="SiteContent"]/div/div[1]/div[5]/div/button/div/div')).click().perform()





    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

