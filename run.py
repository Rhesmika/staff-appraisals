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
SALARY = SHEET.worksheet('salary')




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
            if i.isalpha() == False:
                raise ValueError(
                    f"Your name must alphabetical.\n'{i}' contains invalid symbols \n"
                )
        except ValueError as e:
            print(f"Invalid entry.{e}Please try again.")
            return False
    return True


def question_one():
    """
    Gets users rating to question one from spreadsheet
    """
    while True:
            topic = QUESTIONS.cell(1,3).value
            qi_rating = input(f"I {topic}: \n")
            if validate_rating(qi_rating):          
                break        
    return (qi_rating, )

def question_two():
    """
    Gets users rating to question two from spreadsheet
    """
    while True:
            topic = QUESTIONS.cell(1,4).value
            qii_rating = input(f"I {topic}: \n")
            if validate_rating(qii_rating):          
                break        
    return (qii_rating, )

def question_three():
    """
    Gets users rating to question three from spreadsheet
    """
    while True:
            topic = QUESTIONS.cell(1,5).value
            qiii_rating = input(f"I {topic}: \n")
            if validate_rating(qiii_rating):          
                break        
    return (qiii_rating, )

def question_four():
    """
    Gets users rating to question four from spreadsheet
    """
    while True:
            topic = QUESTIONS.cell(1,6).value
            qiv_rating = input(f"I {topic}: \n")
            if validate_rating(qiv_rating):          
                break        
    return (qiv_rating, )

def validate_rating(values):
    """
    Validates if question answer is a number between 1 and 5. Raises error if not. 
    """
    for rating in values:
        try:
            if rating.isnumeric() == False:
                raise ValueError(
                    "You must enter a whole number"
                )
            else:
                int_rating = int(rating)
                if int_rating > 5:
                    raise ValueError(
                        f"{int_rating} is more than 5."
                    )
                if int_rating < 1:
                    raise ValueError(
                        f"{int_rating} is less than 1."
                    )
        except ValueError as e:
            print(f"{e}\nPlease enter a number between 1-5...")
            return False
    return True


def question_five():
    """
    Gets users rating to question five from spreadsheet
    """
    while True:
            topic = QUESTIONS.cell(1,7).value
            qv_rating = input(f"I {topic}: \n")
            if validate_yn(qv_rating):          
                break        
    return (qv_rating, )

def validate_yn(qv_rating):
    """
    Validates if answer to question 5 is yes or no
    """
    try:
        if qv_rating == "yes" or qv_rating == "no":
            print(f"you entered {qv_rating}")
 
        else:
            raise ValueError(
                f"{qv_rating}is not valid"
            )
    except ValueError as e:
        print("Please enter exactly 'yes' or 'no'")
        return False
    return True


def update_answers(answers):
    """
    Updates worksheet with user answers
    """
    print(f"Updating...\n")
    QUESTIONS.append_row(answers)
    print(f"worksheet updated successfully\n")

def user_salary():
    """
    Gets users current salary from user
    """
    while True:
            salary = input(f"What is your current annual salary?\nenter amount with no punction or symbol\n")
            if validate_salary(salary):          
                break        
    return (salary, )

def validate_salary(salary):
    """
    Checks salary input contains numbers only and no punctuation or symbols
    """
    try:
        if salary.isnumeric() == False:
            raise ValueError(
                f"{salary} is not a valid number"
            )
        else:
            if len(salary) > 5:
                raise ValueError(
                    f"Your salary must be 5 digits. You entered {len(salary)}"
                )
            if len(salary) < 5:
                raise ValueError(
                    f"Your salary must be 5 digits. You entered {len(salary)}"
                )
    except ValueError as e:
        print(f"{e}\nPlease try again.")
        return False
    return True    


def update_salary(salary_data):
    """
    Updates salary worksheet with salary desire
    """
    print(f"Updating...\n")
    SALARY.append_row(salary_data)
    print(f"worksheet updated successfully\n")



def desired_increase():
    """
    Gets users desired increase of wage
    """
    while True:
            percentage_increase = input(f"What is your desired percentage increase?\n")
            if vaidate_percentage(percentage_increase):          
                break        
    return (percentage_increase, )

def vaidate_percentage(percentage_increase):
    try:
        if "%" in percentage_increase:
            raise ValueError(
                "Please do not enter the percentage symbol"
            )
        if percentage_increase.isnumeric() == False:
            raise ValueError(
                f"{percentage_increase} is not a valid number."
            )
        else:
            if int(percentage_increase) >= 100:
                raise ValueError(
                    f"Your request for an increase of 100% or over has been denied."
                )
    except ValueError as e:
        print(f"{e}\nPlease try again.")
        return False
    return True   





def main():
    """
    Runs all functionss
    """
    # names = get_employee_name()

    # qi_answer = question_one()
    # qii_answer = question_two()
    # qiii_answer = question_three()
    # qiv_answer = question_four()
    # qv_answer = question_five()
    # answers = (*names, *qi_answer, *qii_answer, *qiii_answer, *qiv_answer, *qv_answer)
    # update_answers(answers)

    current_salary = user_salary()
    percent = desired_increase()
    salary_data = (*names, *current_salary, *percent)
    update_salary(salary_data)


    




main()