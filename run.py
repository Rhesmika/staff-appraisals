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
    while True: 
        first_name = input("what is your first name? \n")
        last_name = input("what is your last name? \n")
        full_name = first_name,last_name

        if validate_name(full_name):
            break
    return first_name, last_name



def validate_name(full_name):
    """
    Checks users entry contains letters only. Raises error if not.
    """
    for i in full_name:
        try:
            if i.isalpha()==False:
                raise ValueError(
                    f"Your name must alphabetical.\n'{i}' contains invalid symbols \n"
                )
        except ValueError as e:
            print(f"Invalid entry.{e}Please try again.")
            return False

    return True



def update_name(names):
    """
    Add name values to questions spreadsheet
    """
    print(f"Updating...\n")
    QUESTIONS.append_row(names)
    print(f"worksheet updated successfully\n")


def question_one():
    """
    Gets users rating to question one from spreadsheet
    """
    while True:
        topic = QUESTIONS.cell(1,3).value
        qi_rating = input(f"I {topic}: \n")
        if validate_rating(qi_rating):
            break
    return qi_rating


    

def validate_rating(qi_rating):
    """
    Validates if question one answer is a number. Raises error if not. 
    """
    try:
        if qi_rating.isnumeric()==False:
            raise ValueError(
                f"{qi_rating} is not a valid entry."
            )
        if int(qi_rating) > 5:
            raise ValueError(
                f"{qi_rating} is more than 5."
            )
        if int(qi_rating) < 1:
            raise ValueError(
                f"{qi_rating} is less than 1."
            )
    except ValueError as e:
        print(f"{e}\nPlease enter a number between 1-5...")
        question_one()
    return True

# def update_qi_answer(qi_answer):
#     print(qi_answer



def main():
    """
    Runs all functions
    """
    names = get_employee_name()
    update_name(names)
    qi_answer = question_one()
    # update_qi_answer(qi_answer)
    




main()