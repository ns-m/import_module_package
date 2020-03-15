from application.salary import calculate_salary
import db.people
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now())
    calculate_salary()
    db.people.get_employees()