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

QUESTIONS = SHEET.worksheet('questions')
data = QUESTIONS.get_all_values()


def get_employee_name():
    """
    Gets users name
    """
    first_name = input("what is your first name? \n")
    last_name = input("what is your last name? \n")
    full_name = first_name,last_name
    validate_name(full_name)
    return first_name, last_name

def validate_name(full_name):
    """
    Checks users entry contains letters only
    """
    for i in full_name:
        try:
            if i.isalpha()==False:
                raise ValueError(
                    f"Your name must alphabetical.\n'{i}' contains invalid symbols \n"
                )
        except ValueError as e:
            print(f"Invalid entry.{e}Please try again.")



def update_name(names):
    """
    Add name values to questions spreadsheet
    """
    print(f"Updating...\n")
    QUESTIONS.append_row(names)
    print(f"worksheet updated successfully\n")


def question_one():
    topic = QUESTIONS.cell(1,3).value
    qi_rating = input(f"I {topic}: \n")
    return qi_rating
    

def validate_rating(q_one_answer):
    try:
        if q_one_answer.isdigit()==False:
            raise ValueError(
                f"Your rating must be a whole number.\n'{q_one_answer}' contains something other than numbers.\n"
            )
    except ValueError as e:
        print(f"Invalid entry. {e} Please try again.")






def main():
    """
    Runs all functions
    """
    names = get_employee_name()
    update_name(names)
    q_one_answer = question_one()
    validate_rating(q_one_answer)
    




main()