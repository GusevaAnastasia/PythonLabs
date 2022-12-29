import csv
from functools import reduce

with open("iris.data",'r') as file:
        reader = csv.reader(file,delimiter=",")
        filtered_iterable = filter(lambda row: len(row) != 0 and row[4] == 'Iris-setosa', reader)
        mapped_iterable = map(lambda row : float(row[2]),filtered_iterable)
        enumerated_iterable = enumerate(mapped_iterable,1)
        result = reduce(lambda accumulator, element: (
        element[0], accumulator[1]+element[1]), enumerated_iterable, (0, 0))
        average = result[1]/result[0]
with open("result.txt",'w',encoding="UTF-8") as result_file:
    result_file.write(str(average))

#Файл iris.data содержит информацию о цветках ириса
#Информация о атрибутах цветка:
#№1. длина чашелистика в см
#№2. ширина чашелистика в см
#№3. длина лепестка в см
#№4. ширина лепестка в см
#5. class:
#-- Iris Setosa
#-- Iris Versicolour
#-- Iris Virginica

#Нужно посчитать среднюю длину лепестка, где class='Iris Setosa'
#Длина лепестка - Индекс 2
