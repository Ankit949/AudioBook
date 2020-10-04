import pyttsx3
import PyPDF2

pdf=open("ML.pdf", "rb")
Reader=PyPDF2.PdfFileReader(pdf)
No_of_pages=Reader.numPages
#initialising speaker
speaker=pyttsx3.init()
#reading from page no. 38
for read in range(50,No_of_pages):
    #getting a page to read
    page=Reader.getPage(read)
    #Extracting the text
    text=page.extractText()
    #changing speaking rate
    rate=speaker.getProperty('rate')
    speaker.setProperty('rate',150)
    #changing voice
    voices=speaker.getProperty('voices')
    #speaker.setProperty('voice',voices[0].id)  #for male voice
    speaker.setProperty('voice',voices[1].id)  #for female voice
    #changing volume
    volume=speaker.getProperty('volume')
    speaker.setProperty('volume',1.0)
    speaker.say(text)
    speaker.runAndWait()