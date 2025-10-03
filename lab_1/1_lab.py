import pandas as pd
import numpy as np
import re

# Чтение данных

data = pd.read_csv('titanic_train.csv', index_col='PassengerId')

# --- 1. Количество мужчин и женщин ---
sex_counts = data['Sex'].value_counts()

# --- 2. Распределение классов ---
pclass_counts = data['Pclass'].value_counts()
pclass_by_sex = data.groupby('Sex')['Pclass'].value_counts()

# --- 3. Медиана и стандартное отклонение тарифа ---
fare_median = round(data['Fare'].median(), 2)
fare_std = round(data['Fare'].std(), 2)

# --- 4. Средний возраст выживших и погибших ---
age_by_survival = data.groupby('Survived')['Age'].mean()

# --- 5. Доли выживших среди <30 и >60 ---
young = data[data['Age'] < 30]
old = data[data['Age'] > 60]
young_survival = round(young['Survived'].mean()*100, 1)
old_survival = round(old['Survived'].mean()*100, 1)

# --- 6. Доли выживших среди мужчин и женщин ---
sex_survival = round(data.groupby('Sex')['Survived'].mean()*100, 1)

# --- 7. Наиболее популярное мужское имя ---
def extract_first_name(fullname):
    name = re.search(r", (.+)", fullname).group(1)
    name = re.sub(r"(Mr\.|Mrs\.|Miss\.|Master\.|Dr\.|Rev\.|Col\.|Major\.|Capt\.|Mme\.|Mlle\.|Lady\.|Sir\.|Don\.|Countess|Jonkheer)\s*", "", name)
    first = name.split()[0].replace('"','').replace('(','').replace(')','')
    return first

male_names = data[data['Sex']=='male']['Name'].apply(extract_first_name)
top_male_name = male_names.value_counts().idxmax()

# --- 8. Средний возраст по полу и классам ---
age_by_class_sex = data.groupby(['Pclass','Sex'])['Age'].mean()

# --- Запись результатов в файл ---
with open("results.txt", "w", encoding="utf-8") as f:
    f.write("1. Количество мужчин и женщин:\n")
    f.write(str(sex_counts) + "\n\n")

    f.write("2. Распределение классов:\n")
    f.write(str(pclass_counts) + "\n\n")
    f.write("Распределение по полу и классу:\n")
    f.write(str(pclass_by_sex) + "\n\n")

    f.write("3. Медиана и стандартное отклонение тарифа:\n")
    f.write(f"Медиана = {fare_median}, std = {fare_std}\n\n")

    f.write("4. Средний возраст по выжившим и погибшим:\n")
    f.write(str(age_by_survival) + "\n\n")

    f.write("5. Доли выживших среди молодых (<30) и пожилых (>60):\n")
    f.write(f"Молодые: {young_survival}%, Пожилые: {old_survival}%\n\n")

    f.write("6. Доли выживших среди мужчин и женщин:\n")
    f.write(str(sex_survival) + "\n\n")

    f.write("7. Самое популярное мужское имя:\n")
    f.write(top_male_name + "\n\n")

    f.write("8. Средний возраст мужчин и женщин по классам:\n")
    f.write(str(age_by_class_sex) + "\n")