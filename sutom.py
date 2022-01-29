from selenium import webdriver
from selenium.webdriver.chrome.service import Service





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

class webScraping() :

    def __init__(self) :
        self.wordLength = 0
        self.hiddenWord = ""
        self.firstLetter = ""
        self.wordListLength = []
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
    
        self.driver.get("https://sutom.nocle.fr/")
    
    def getHiddenWord(self):

        rows = self.driver.find_elements_by_xpath(f"""//table/tr[{self.loop}]/td""")
        print("== JAMBON")
        print([elm for elm in rows])
        print("=== BEURE")



        text = self.driver.find_element_by_xpath(f"//table/tr[{self.loop}]").text
        for i in text :
            if(i != "." and i != " ") :
                self.wordNoComplete = i 
    
    def getFirstLetter(self):
        text = self.driver.find_element_by_xpath(f"//table/tr[{self.loop}]").text
        print(text)
        self.firstLetter = text[0]
        for i in text :
            if(i != "." and i != " ") :
                self.wordNoComplete.append(i)
            elif(i == ".") :
                self.wordNoComplete.append("")
        self.wordNoComplete[0] = text[0]
        print(self.wordNoComplete)
        

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

    def createWordListLength(self,lines) :
        i = myDictionary[self.firstLetter]
        while i < 297250 :
            if(len(lines[i]) == self.wordLength) :
                self.wordListLength.append(lines[i])
            i+=1
    def test(self, lines):
        final_arr = []
        start = "."
        for index,item in enumerate(lines) :
            if(item[0] != start) :
                final_arr.append(index)
                start = item[0]
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];

        for i,item in enumerate(alphabet) :
            print("\""+ item.capitalize() + "\" : " + str(final_arr[i]))

    def writeWord(self,word):
        for i in word :
            self.inputText(i.capitalize())
        
    def start(self):
        self.driver.get("https://sutom.nocle.fr/")
        self.getLength()
        self.getFirstLetter()
        # self.getHiddenWord()
        
        
        self.createWordListLength(self.openFiles())
        self.writeWord(self.wordListLength[0])
        self.inputText("_entree")

        # self.getFirstLetter()
        self.getHiddenWord()


new = webScraping()
new.start()

