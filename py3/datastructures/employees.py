employees = [
    {
        'name': 'John',
        'age': 46
    },
    {
        'name': 'Jay',
        'age': 39
    },
    {
        'name': 'Marcus',
        'age': 36
    },
    {
        'name': 'Adam',
        'age': 42
    }
]


for employee in employees:
    for key in employee:
        print(f'{key}={employee.get(key)}')
    print('', end='')


def get_older_than_40(employee_list):
    to_return_list = []
    for emp in employee_list:
        if emp['age'] >= 40:
            to_return_list.append(emp['name'])

    return to_return_list





over_40 = get_older_than_40(employees)
print(over_40)


get_older_than_40 = lambda emp: emp['name'] if emp['age'] >= 40 else None

employees_over_40 = map(get_older_than_40 , employees)
# filter None values
employees_over_40 = filter(None ,employees_over_40)
for i in employees_over_40:
    print(i + " " , end=',')