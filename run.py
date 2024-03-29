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
        print("Welcome to your staff appraisal form.\n")
        first_name = input("what is your first name? \n")
        last_name = input("\nwhat is your last name? \n")
        full_name = first_name, last_name

        if validate_name(full_name):
            break
    return first_name, last_name


def validate_name(full_name):
    """
    Checks users entry contains letters only. Raises error if not.
    """
    for i in full_name:
        try:
            if i.isalpha() is False:
                raise ValueError(
                    f"{i}' contains invalid symbols.\n"
                )
        except ValueError as e:
            print(f"{e}Please enter your name again.")
            return False
    return True


def question_one():
    """
    Gets users rating to question one from spreadsheet
    """
    print("\nPlease answer the following questions rating your answer 1-5.")
    print("1 being strongly disagree. 5 being strongly agree.\n")
    while True:
            topic = QUESTIONS.cell(1, 3).value
            print("On a scale of 1-5:")
            qi_rating = input(f"I {topic}. \n")
            if validate_rating(qi_rating):
                break
    return (qi_rating, )


def question_two():
    """
    Gets users rating to question two from spreadsheet
    """
    while True:
            topic = QUESTIONS.cell(1, 4).value
            print("\nOn a scale of 1-5:")
            qii_rating = input(f"I {topic}. \n")
            if validate_rating(qii_rating):
                break
    return (qii_rating, )


def question_three():
    """
    Gets users rating to question three from spreadsheet
    """
    while True:
            topic = QUESTIONS.cell(1, 5).value
            print("\nOn a scale of 1-5:")
            qiii_rating = input(f"I {topic}. \n")
            if validate_rating(qiii_rating):
                break
    return (qiii_rating, )


def question_four():
    """
    Gets users rating to question four from spreadsheet
    """
    while True:
            topic = QUESTIONS.cell(1, 6).value
            print("\nOn a scale of 1-5:")
            qiv_rating = input(f"I {topic}. \n")
            if validate_rating(qiv_rating):
                break
    return (qiv_rating, )


def validate_rating(values):
    """
    Validates if question answer is a number between 1 and 5.
    """
    for rating in values:
        try:
            if len(values) > 1:
                raise ValueError(
                    "You must enter a single number"
                )
            if rating.isnumeric() is False:
                raise ValueError(
                    "You must enter a whole number"
                )
            else:
                if int(rating) > 5:
                    raise ValueError(
                        f"{rating} is more than 5."
                    )
                if int(rating) < 1:
                    raise ValueError(
                        f"{rating} is less than 1."
                    )
        except ValueError as e:
            print(f"{e}\nPlease enter a whole number between 1-5...")
            return False
    return True


def question_five():
    """
    Gets users rating to question five from spreadsheet
    """
    while True:
            topic = QUESTIONS.cell(1, 7).value
            print("\nPlease answer this question as 'yes' or 'no'.")
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
            print("Thank you for your honesty")
        else:
            raise ValueError(
                f"{qv_rating} is not valid."
            )
    except ValueError as e:
        print(f"{e} Please enter exactly 'yes' or 'no'")
        return False
    return True


def user_salary():
    """
    Gets users current salary from user
    """
    while True:
        print("\nPlease answer this question without symbols or commas.")
        salary = input("What is your current annual salary?\n")
        if validate_salary(salary):
            break
    return (salary, )


def validate_salary(salary):
    """
    Checks salary input contains numbers only and no punctuation or symbols
    """
    try:
        if salary.isnumeric() is False:
            raise ValueError(
                f"{salary} is not a valid answer"
            )
        else:
            if len(salary) > 5:
                raise ValueError(
                    f"Your salary must be 5 digits. You entered {len(salary)}."
                )
            if len(salary) < 5:
                raise ValueError(
                    f"Your salary must be 5 digits. You entered {len(salary)}."
                )
    except ValueError as e:
        print(f"{e}\nPlease try again and answer your annual salary.")
        return False
    return True


def desired_increase():
    """
    Gets users desired increase of wage
    """
    while True:
        print("\nPlease answer this question as a whole number.")
        print("No % symbol is required.")
        percentage_inc = input("What percentage increase would you like?\n")
        if vaidate_percentage(percentage_inc):
            break
    return (percentage_inc, )


def vaidate_percentage(percentage_inc):
    """
    Validates the percentage increase requested
    """
    try:
        if "%" in percentage_inc:
            raise ValueError(
                "Please do not enter the percentage symbol."
            )
        if percentage_inc.isnumeric() is False:
            raise ValueError(
                f"{percentage_inc} is not a valid number."
            )
        else:
            if int(percentage_inc) >= 100:
                raise ValueError(
                    f"Your request to increase {percentage_inc}% is too high."
                )
    except ValueError as e:
        print(f"{e}\nPlease try again.")
        return False
    return True


def calculate_salary_increase(current_salary, percent):
    """
    Calculates the increase of salary with perentage increase
    """
    one_percent_salary = int(current_salary[0]) / 100
    int_percent = int(percent[0])
    increase = one_percent_salary * int_percent
    new_salary = increase + int(current_salary[0])
    return new_salary


def update_answers(ans):
    """
    Updates worksheet with user answers
    """
    QUESTIONS.append_row(ans)
    print("\nYour answers have been submitted,")


def update_salary(salary_data, names):
    """
    Updates salary worksheet with desired salary
    """
    SALARY.append_row(salary_data)
    print("and your salary request has been submitted.\n")

    print(f"Thank you for your time today {names[0]}!")
    print("Your manager will arrange a meeting with you shortly.")


def main():
    """
    Runs all functionss
    """
    names = get_employee_name()

    qi_ans = question_one()
    qii_ans = question_two()
    qiii_ans = question_three()
    qiv_ans = question_four()
    qv_ans = question_five()

    ans = (*names, *qi_ans, *qii_ans, *qiii_ans, *qiv_ans, *qv_ans)

    current_salary = user_salary()
    percent = desired_increase()
    new_salary = calculate_salary_increase(current_salary, percent)

    salary_data = (*names, *current_salary, *percent, new_salary)

    update_answers(ans)
    update_salary(salary_data, names)


main()
