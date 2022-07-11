import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('staff_appraisals')

questions = SHEET.worksheet('questions')
data = questions.get_all_values()


def get_employee_name():
    """
    Gets users name
    """
    first_name = input("what is your first name? \n")
    last_name = input("what is your last name? \n")
    print(first_name, last_name)
    return first_name, last_name


def main():
    get_employee_name()

main()