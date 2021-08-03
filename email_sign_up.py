import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from datetime import datetime
import os

def write_to_sheet(name): #, email, telephone, quantity, arrival, departure, message):
	credentials = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
	creds = ServiceAccountCredentials.from_json_keyfile_name(credentials)
	client = gspread.authorize(creds)
	sheet = client.open("Prenotare").sheet1
	row = [name] #, email, telephone, quantity, arrival, departure, message, str(datetime.today())] help
	sheet.append_row(row)
	return 'Thank you, we have received your request!'

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)-2)