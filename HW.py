# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна
# определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

from collections import namedtuple as ntuple

company_info = ntuple('company_info', ['name', 'income'])

numbers_of_company = int(input('Введите количество предприятий: '))
sheet = []

for _ in range(numbers_of_company):
    company_data = input('Введите название предприятия и доход за 4 квартала через пробел: ').split()
    company_name = ' '.join(company_data[:-4])
    company_income = list(map(float, company_data[-4:]))
    sheet.append(company_info(company_name, company_income))

medial = sum([sum(x.income) for x in sheet])/len(sheet)

print('Средняя прибыль за год для всех предприятий:', medial)
print('Выше/равна среднего прибыль у компаний:')
for x in filter(lambda x: sum(x.income) >= medial, sheet):
    print('\t', x.name)
print('Ниже среднего прибыль у компаний:')
for x in filter(lambda x: sum(x.income) < medial, sheet):
    print('\t', x.name)
