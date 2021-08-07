# purpose of this program is to 
from PIL import Image
import os
import nltk

blank_sheet = Image.open('blank_page.jpg')
new_blank_sheet = ''

sheetwidth,sheetheight = blank_sheet.size

MARGIN = 300
FIXED_HEIGHT = 70                  # set height of img here
sheet = 1
Chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?.!,()[]:-=\'" ;'


#print(blank_sheet.size)
# it is 3300,2550
bspace,nwline = 0,0
def set_FIXED_HEIGHT(x):
    global FIXED_HEIGHT
    # try at ~70 pixels then check what suits 
    FIXED_HEIGHT = x

def resetpage():
    global bspace,nwline
    bspace,nwline = MARGIN,FIXED_HEIGHT*4
    
def width_size( width, height_per):
    return int((float(width) * float(height_per)))

def writetopage(letter):
    global bspace,nwline,new_blank_sheet
    try:
        img = Image.open('fonts/'+letter+'.jpg')
        height_percent = (FIXED_HEIGHT / float(img.size[1]))
        img = img.resize((width_size(img.size[0],height_per=height_percent), FIXED_HEIGHT), Image.NEAREST)
        
        new_blank_sheet.paste(img,(bspace,nwline))
        bspace += img.width
    except:
        print('newline 2 incoming via letter '+str(letter))
        letter = ''
        nwline +=FIXED_HEIGHT
        bspace = MARGIN
    
    

def opensheet():
    global new_blank_sheet
    new_blank_sheet = Image.open("blank_page.jpg")
    return 

def writeword(word):
    global bspace,nwline
    
    if bspace > (sheetwidth - 75*len(word)):#- MARGIN):   # margin here
        #print('newline incoming')
        bspace = MARGIN
        nwline += FIXED_HEIGHT

    if nwline > sheetheight - FIXED_HEIGHT*4:
        print('newpage init')
        global sheet,new_blank_sheet
        resetpage()
        new_blank_sheet.save("out{}.jpg".format(sheet))
        #savesheet(sheet)
        new_blank_sheet.close()
        new_sheet = Image.open("blank_page.jpg")
        new_blank_sheet = new_sheet
        sheet+=1

    specialCharacters = {'!':'exclamation','?':'question',',':'comma','.':'fullstop',':':'colon','(':'braketopen', ')':'braketclose','-':'hiphen','[':'squareopen',']':'squareclose','=':'equal','\'':'apostrophe','"':'qoute',';':'semicolon'}
    for letter in word:
        if letter in Chars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter +='_u'
            elif letter >='0' and letter <= '9':
                pass
            elif specialCharacters[letter] != None:
                letter = specialCharacters[letter]
            
            #print(letter)
            writetopage(letter)
            
     
if __name__ == "__main__":
    with open('content.txt','r',encoding='utf-8') as file:
        data = file.read()
    
       
    sentences = data.split('\n')
    # print(sentences)
    
    resetpage()
    opensheet()
    
    for sentence in sentences:
        words = sentence.split(' ')
        #print(words)
        for word in words:
            #print(word)
            writeword(word)
            writetopage('space')
    
        writetopage('newline')

    new_blank_sheet.save("out{}.jpg".format(sheet))
    new_blank_sheet.close()