import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from datetime import datetime
import os

def write_to_sheet(username, bet, odds, units, sport, league, record, roi, net_units, message):
	credentials = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
	creds = ServiceAccountCredentials.from_json_keyfile_name(credentials)
	client = gspread.authorize(creds)
	sheet = client.open("POTDTracker").worksheet('Week1')
	row = [username, bet, odds, units, sport, league, record, roi, net_units, message, str(datetime.today())]
	sheet.append_row(row)
	formatted = format_correctly(bet, odds, units, sport, league, record, roi, net_units, message)
	return formatted

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)-2)