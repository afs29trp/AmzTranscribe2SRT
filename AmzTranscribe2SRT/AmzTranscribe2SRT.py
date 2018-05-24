# A Simple Python Application to create timecoded SRT files from Amazon Transcribe JSON outputs.
# This will take a JSON file as input and output an SRT file
# Author: tgould
# Date 2018-05-23
import json
import datetime
from tkinter import filedialog
from tkinter import *



with open("JoCoomber.json", encoding="utf-8") as json_data:
    raw= json.load(json_data)
    transcription = raw['results']['items']
    print(len(transcription))
    #Loop through each transcription element. i value is global scope
    i=0
    for value in range(0,len(transcription)):
        if transcription[i]['type']=="pronunciation":
            start_time = float(transcription[i]['start_time'])
            start_time=str(datetime.timedelta(seconds= start_time))
            print(start_time)
        i=i+1


def construct_sub_line(pointer):
    "Creates each line of the subtitle file"
#You want to generate subtitles that are 64 charactes max, or 32 per line x2
#So we need to count the number of characters.
#We also need to know where in the output to start from, which would indicate a count being 
#passed in and out the function as it is called.

    charCount=0
    startTime=0
    endTime=0
    text=""
    while charCount<= 64:
        charCount=charCount+len(str(transcription[pointer]['content']))
        if charCount<64:
            text=text + str(transcription[pointer]['content'])
            pointer=pointer+1
        else:
            i=pointer
            endTime = toTimestamp(pointer,'end_time')



def getFile():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))
    print (root.filename)

def toTimestamp(pointer, key):
    if transcription[pointer]['type']=="pronunciation":
        tStamp=str(datetime.timedelta(seconds = float(transcription[i][key])))
        print (tStamp)
        return tStamp