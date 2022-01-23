from selenium import webdriver
from selenium.webdriver.chrome.service import Service



class webScraping() :

    def __init__(self) :
        self.wordLength = 0
        self.hiddenWord = ""
        self.win = False 
        self.loop = 1
        ser = Service(".\chromedriver.exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)
    
        self.driver.get("https://sutom.nocle.fr/")
    
    def getHiddenWord(self):
        text = self.driver.find_element_by_xpath(f"//table/tr[{self.loop}]").text
        

    def getLength(self):
        self.wordLength =(len(self.driver.find_element_by_xpath("//table/tr").text) + 1)/2

    def inputText(self,letter):
        bouton = self.driver.find_element_by_xpath(f"//div[@data-lettre ='{letter}']")  
        print(bouton)
        bouton.click()

    def start(self):
        self.driver.get("https://sutom.nocle.fr/")
        self.getLength()

        self.getHiddenWord()
        self.inputText("B")



new = webScraping()
new.start()