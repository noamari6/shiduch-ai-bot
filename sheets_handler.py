import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import SHEET_ID

def save_user_data(user_id, data):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(SHEET_ID).sheet1
        sheet.append_row([str(user_id), data.get("age"), data.get("city")])
    except Exception as e:
        print(f"שגיאה בשמירת הנתונים: {e}")
