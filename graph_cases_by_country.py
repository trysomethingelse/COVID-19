import csv
import os
from os.path import expanduser
import matplotlib.pyplot as plt

threshold_cases = 100
max_days = 10

path = expanduser(os.path.dirname(os.path.abspath(__file__)))
path += '\\csse_covid_19_data\\csse_covid_19_daily_reports'

files_full_path = []
files_names = []
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files_names.append(file)
            files_full_path.append(os.path.join(r, file))

dates = []
confirmed_poland = []
confirmed_germany = []
confirmed_italy = []
confirmed_czechia = []
confirmed_usa = []
confirmed_uk = []

for file in files_full_path:
    with open(file, newline='') as csvfile:
        a = csv.reader(csvfile)
        confirmed_usa_day = 0
        confirmed_uk_day = 0
        for row in a:
            if row[1] == 'US':
                confirmed_usa_day += int(row[3])
            if row[1] == 'UK':
                confirmed_uk_day += int(row[3])
            if row[1] == 'Poland' and int(row[3]) >= threshold_cases:
                confirmed_poland.append(int(row[3]))
            if row[1] == 'Germany' and int(row[3]) >= threshold_cases:
                confirmed_germany.append(int(row[3]))
            if row[1] == 'Italy' and int(row[3]) >= threshold_cases:
                confirmed_italy.append(int(row[3]))
            if row[1] == 'Czechia' and int(row[3]) >= threshold_cases:
                confirmed_czechia.append(int(row[3]))
        if confirmed_usa_day > threshold_cases:
            confirmed_usa.append(confirmed_usa_day)
        if confirmed_uk_day > threshold_cases:
            confirmed_uk.append(confirmed_uk_day)

plt.plot(confirmed_poland, "*-")
plt.plot(confirmed_germany[0:max_days])
plt.plot(confirmed_italy[0:max_days])
plt.plot(confirmed_czechia[0:max_days])
plt.plot(confirmed_usa[0:max_days])
# plt.plot(confirmed_uk[0:max_days])

plt.title("Convirmed COVID-19 in country from " + str(threshold_cases) + " case above")
plt.xlabel("day")
plt.ylabel("cases")
plt.legend(['Poland', 'Germany', 'Italy', 'Czechia', 'USA'])
plt.show()