# Data comes from Johns Hopkins University
# https://github.com/CSSEGISandData/COVID-19
# Thanks to them for making this data set public.
# You can find data beyond cumulative cases there!

'''
Test your code by analysing total confirmed cases over time.
Each line in the file represents one day. The first value is
confirmed cases on January 22nd. The number of confirmed cases
is "cumulative" meaning that it is the total number of cases up
until the current day. It will never go down! 
'''

import datetime
from typing import Tuple

COUNTRY_PATH = 'week4/covid/Italy.txt'
START_DATE = datetime.date(2020,1,22)
DATE_FORMAT = "%b %d,%Y"

def main():
    # TODO: your code here
    case_list = get_case_list()
    new_cases = count_new_cases(case_list)
    first_infected_day = get_first_infected_day(new_cases)
    print('The first day of infection was %s with %d cases' % 
        (first_infected_day[0].strftime(DATE_FORMAT), first_infected_day[1]))
    print_most_infected_day(new_cases)

def get_case_list():
    case_list = []
    with open(COUNTRY_PATH) as f:
        for cases in f:
            case_list.append(int(cases.strip()))
    return case_list

def get_infected_days(case_list: list)->int:
    infected_days = 0
    for cases in case_list:
        if cases != 0:
            infected_days += 1
    return infected_days

def count_new_cases(case_list: list)->list:
    cases_per_day = case_list.copy()
    cases_per_day[0] = 0
    for day in range(1, len(case_list)):
        new_cases = int(case_list[day] - case_list[day - 1])
        cases_per_day[day] = new_cases
    return cases_per_day

def get_first_infected_day(new_cases: list)->Tuple[datetime.date, int]:
    case_count = 0
    for day in range(0, len(new_cases) - 1):
        case_count = new_cases[day]
        if case_count != 0:
            break
    first_infected_day = START_DATE + datetime.timedelta(day)
    return first_infected_day, case_count

def print_new_cases(new_cases: list)->None:
    for cases in new_cases:
        print(cases)

def print_most_infected_day(new_cases: list)->None:
    max_day = new_cases.index(max(new_cases))
    max_day_str = (START_DATE + datetime.timedelta(max_day)).strftime(DATE_FORMAT)
    max_cases = new_cases[max_day]
    statement = 'The most cases were seen on %s with %d cases.'
    print(statement % (max_day_str, max_cases))

if __name__ == '__main__':
    main()