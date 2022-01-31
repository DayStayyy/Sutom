from re import T
import re
from tkinter import E, PIESLICE
from turtle import pen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time




myDictionary = {
    "A" : 0,
    "B" : 24369,
    "C" : 39475,
    "D" : 73683,
    "E" : 114177,
    "F" : 149048,
    "G" : 161532,
    "H" : 171721,
    "I" : 177562,
    "J" : 189271,
    "K" : 191669,
    "L" : 192160,
    "M" : 199237,
    "N" : 215529,
    "O" : 219417,
    "P" : 224789,
    "Q" : 251864,
    "R" : 252995,
    "S" : 288826,
    "T" : 311190,
    "U" : 327162,
    "V" : 328153,
    "W" : 335370,
    "X" : 335562,
    "Y" : 335625,
    "Z" : 335717,
}
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

class webScraping() :

    def __init__(self) :
        self.wordLength = 0
        self.hiddenWord = ""
        self.firstLetter = ""
        self.wordListCheck = []
        self.wordListLetter = []
        self.badLetter = []
        self.goodLetter = []
        self.wordNoComplete = []
        self.keys_list = list(myDictionary)
        self.win = False 
        self.loop = 1
        ser = Service(".\chromedriver.exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)
    
    def getHiddenWord(self):

        rows = self.driver.find_elements_by_xpath(f"//table/tr[{self.loop}]/td")
        for elm in rows :
            if(elm.get_attribute("class") == "bien-place resultat" or elm.get_attribute("class") == "mal-place resultat") :
                self.goodLetter.append(elm.text)
            else :
                if(self.goodLetter.count(elm.text) == 0 ) :
                    self.badLetter.append(elm.text)



        text = self.driver.find_element_by_xpath(f"//table/tr[{self.loop + 1}]")
        text = text.text
        i = 0
        for letter in text :
            if(letter == " ") :
                continue
            if(letter != ".") :
                self.wordNoComplete[i] = letter
            i += 1 

    def newWord(self) :
        newWordListLetter = []
        for word in self.wordListCheck :
            if(self.wordIsOk(word)) :
                newWordListLetter.append(word)
        self.wordListCheck = newWordListLetter

    def wordIsOk(self,word) :
        for letter in self.goodLetter :
            if word.find(letter.lower()) == -1 :
                return False

        for i,letter in enumerate(word) :
            if(self.badLetter.count(letter.upper()) != 0) :
                return False
            if(self.wordNoComplete[i] != "" ) :
                if(self.wordNoComplete[i].lower() != letter) :
                    return False

        return True
                
    def getFirstLetter(self):
        text = self.driver.find_element_by_xpath(f"//table/tr[{self.loop}]").text
        self.firstLetter = text[0]
        for i in text :
            if(i != "." and i != " ") :
                self.wordNoComplete.append(i)
            elif(i == ".") :
                self.wordNoComplete.append("")
        self.wordNoComplete[0] = text[0]
        

    def getLength(self):
        self.wordLength =(len(self.driver.find_element_by_xpath("//table/tr").text) + 1)/2

    def inputText(self,letter):
        bouton = self.driver.find_element_by_xpath(f"//div[@data-lettre ='{letter}']")  
        bouton.click()


    def openFiles(self) :
        file = open("WordList.txt", "r")
        list_of_lists = []
        for line in file:
            stripped_line = line.strip()
            list_of_lists.append(stripped_line)
        return list_of_lists

    def createWordListCheck(self,lines) :
        i = myDictionary[self.firstLetter]
        if(self.firstLetter == "Z") :
            limite = 336513
        else :
            limite = myDictionary[alphabet[alphabet.index(self.firstLetter.lower())+1].upper()]
        while i < limite :
            if(len(lines[i]) == self.wordLength) :
                self.wordListCheck.append(lines[i])
            i+=1


    def writeWord(self,word):
        for i in word :
            self.inputText(i.capitalize())
        
    def start(self):
        self.driver.get("https://sutom.nocle.fr/")
        self.getLength()
        self.getFirstLetter()
        
        self.createWordListCheck(self.openFiles())
        self.writeWord(self.wordListCheck[0])
        self.inputText("_entree")
        self.wordListCheck.remove(self.wordListCheck[0])

        while self.loop < 6 :
            self.driver.refresh()
            time.sleep(1)  
            self.getHiddenWord()
            self.loop += 1
            self.newWord()
            self.writeWord(self.wordListCheck[0])
            self.inputText("_entree")
            self.wordListCheck.remove(self.wordListCheck[0])

        # self.driver.close()


new = webScraping()
new.start()

