# import pprint to print "pretty"

import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('cleint_secret.json',scope)
client = gspread.authorize(creds)

sheet = client.open('Vocab').sheet1

#words = sheet.get_all_records()
words = sheet.col_values(1)
#sheet.update_cell()
#sheet.cell(1,1).value

print(words)
