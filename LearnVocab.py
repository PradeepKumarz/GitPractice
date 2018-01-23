
# Github learn 1
# Connect to google docs spreadsheet via api
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from PyDictionary import PyDictionary 

from gtts import gTTS # Module for text to speech conversion

import os

# Establish connection 
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('cleint_secret.json',scope)
client = gspread.authorize(creds)

# Open spreedsheet and grab words
sheet = client.open('Vocab').sheet1
words = sheet.col_values(1)

# Get definitions for each word
defined = {}

dictionary = PyDictionary()

for word in words:
	if len(word) > 0:
		defined[word] = dictionary.meaning(word)

# Make one long string to be converted to audio
toAudio = ""
for word in defined:
	toAudio += word + " "
	for form in defined[word]:
		toAudio += form + " "
		for d in defined[word][form]:
			toAudio += d + " " 
	toAudio += "* " # Lets me put pauses between 2 words

# Github learn 2

toAudio = '                                                                    '.join(toAudio.split("*")) # Spacing is annoying

audio = gTTS(text=toAudio, lang='en', slow=False)

# Save audio to an mp3 file
audio.save("Vocab.mp3")

# Github learn 3
