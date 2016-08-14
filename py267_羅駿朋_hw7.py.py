import urllib.request
from html.parser import HTMLParser
data = urllib.request.urlopen('https://tw.movies.yahoo.com/movieinfo_main.html/id=6255') 
content = data.read().decode('utf_8')
data.close()

file = open('6255.txt', 'w', encoding = 'UTF-8')

class myparser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.isNumber = 0
        self.isNumber0 = 0
        self.isNumber1 = 0
        self.isNumber2 = 0
        self.isNumber3 = 0
        self.isNumber4 = 0
        self.numbers = []

    def handle_data(self, data):
        if self.isNumber == 1:
            if self.numbers == []:
                self.numbers.append(data)
                self.isNumber = 0
        if self.isNumber0 == 1:
            if len(self.numbers)==1:
                self.numbers.append(data)
                self.isNumber0 = 0
        if self.isNumber1 == 1:
            self.numbers.append(data)
            self.isNumber1 = 0
        if self.isNumber2 == 1:
            self.numbers.append(data)
            self.isNumber2 = 0
        if self.isNumber3 == 1:
            self.numbers.append(data)
            self.isNumber3 = 0
        if self.isNumber4 == 1:
            self.numbers.append(data)
            self.isNumber4 = 0
            
    def handle_starttag(self, tag, attrs):
        if tag == 'span' and attrs == [('class','tit')]:
            self.isNumber1 = 1
        if tag == 'span' and attrs == [('class','dta')]:
            self.isNumber2 = 1
        if tag == 'div' and attrs == [('class','text full')]:
            self.isNumber3 = 1
        if tag == 'h4':
            self.isNumber = 1
        if tag == 'h5':
            self.isNumber0 = 1
        if tag == 'br':
            self.isNumber4 = 1           

    def handle_endtag(self,tag):
        pass
    
Parser = myparser() 
Parser.feed(content)
print(Parser.numbers)
a=Parser.numbers

for i in a:
    file.write( i +'\n' )
    
file.close()

