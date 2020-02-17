from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from model import getData


class Parse:
    def __init__(self):
        self.driver = webdriver.Chrome('Путь до chromedriver.exe') # https://chromedriver.chromium.org/
        self.navigate()

    def navigate(self):
        self.driver.get('https://egrp365.ru/')
    
    def find_adress(self, adress: str) -> list: #поиск на главной
        wait = WebDriverWait(self.driver, 30)
        button = self.driver.find_element_by_xpath('//button[@id="search_by_kad_num"]')
        elem = self.driver.find_element_by_id('address').send_keys(adress)
        button.click()
        wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
        adresList = self.driver.find_elements_by_xpath('//div[@class="rs_element_item"]/div[@class="rs_address"]/a')
        

        LinkList = []
        for linkAdress in adresList:
            LinkList.append(linkAdress.get_attribute('href')) #ссылки на объект
        #print(LinkList)

        

        for Adress in LinkList:
            data = list()
            self.driver.get(Adress)
            d = self.driver.find_elements_by_xpath('//div[@id="information_about_object"]')
            for i in d:
                data.append(i.text)
            d = data[0].split('\n')
            h = list(filter(lambda x: x !='', d))
            print(h)


def main():
    p = Parse()
    p.find_adress('г Казань, ул Качалова, 76')

if __name__ == '__main__':
    main()
    
