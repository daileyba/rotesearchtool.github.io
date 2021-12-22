# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 08:50:25 2021

@author: Brady Dailey
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
  
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
  
  
  
# Assign credentials ann path of style sheet
creds = ServiceAccountCredentials.from_json_keyfile_name("RoTEcreds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Record of Tape Extractions.xlsx").sheet1
RoTEsheetlst = sheet.get_all_values()
#print(RoTEsheetlst[0])






entlst = []

#make a list of all Northern Pomo words, eliminating entries in the speadsheet that have an empty cell in the N. Pomo column
for l in RoTEsheetlst:
    if l[3] != '':
        entlst.append([l[3], l[2], l[4], l[8], l[1], l[9]])

digrams = ['Th', 'th', 'ph', 'kh' 'ch', 'ts', "T'", "t'", "p'", "k'", "ch'", "ts'", "s'", 'sh', 'a:', 'i:', 'e:', 'o:', 'u:']

#for i in entlst[1:10]:
#    NPwrd = i[0].split()
#    for n in NPwrd:
#        for s in digrams:
#            if s in n:
#                dn = n.split(s)
#                wrd = list(dn)
#                print(dn)
#            else:
#                wrd = list(n)
#        print(wrd)
    #if len(NPwrd) == 1 and 'Th' == NPwrd[0]:
    #    print(NPwrd)

def segsearch(seg):
    
    NPomodct = {}
    for i in entlst:
        NPwrd = i[0].split()
        for w in NPwrd:
            if seg in w:
                #take each individual word containing 'Th' and make it the key for a dictionary entry
                if w in NPomodct.keys():
                    NPomodct[w].append((" ".join(NPwrd), i[1]))
                if w not in NPomodct.keys():
                    NPomodct.update({w : [(" ".join(NPwrd), i[1])]})
    if len(NPomodct) == 0:
        print('No Entries Found')
    else:
        for k in NPomodct.keys():
            print(k, '[', len(NPomodct[k]), ']', ':  ', NPomodct[k], '\n')
 