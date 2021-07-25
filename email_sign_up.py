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

def format_correctly(bet, odds, units, sport, league, record, roi, net_units, message):
    string = '<b>Record</b>: ' + record + ' <br><br>' + '<b>ROI</b>: ' + roi + '<br><br>' + '<b>Net_units</b>: ' + net_units + '<br><br>'
    string2 = '| ' + sport + ' | ' + league + ' |<br><br>'
    string3 = '<b>Pick</b>: ' + bet + ' - ' + '<b>Odds</b>: ' + odds + ' - ' + '<b>Units</b>: ' + units + '<br><br>'
    string4 = '<b>Write Up</b>: ' + message
    return string + string2 + string3 + string4
