from application.salary import *
from db.people import *
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now())
    calculate_salary()
    get_employees()