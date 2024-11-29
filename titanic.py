import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_parquet('titanic.parquet') #читаем parquet
df.to_csv('titanic.csv', index=False) #переделываем его в csv

df = pd.read_csv('titanic.csv') #читаем csv файл
#переделываем наши данные в таблицу
survival_counts = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)

#строим гистограмму с объединыннеми столбцами
survival_counts.plot(kind='bar', stacked=True)

plt.title('Выживаемость пассажиров Титаника') 
plt.xlabel('Класс билета') 
plt.ylabel('Количество пассажиров') 
plt.xticks(rotation=0)# повернем значения классов билетов
plt.legend(['Не выжил', 'Выжил']) #легенда карты
plt.tight_layout()
plt.show()