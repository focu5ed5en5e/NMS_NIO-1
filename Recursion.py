# -*- coding: UTF-8 -*-
# !/usr/bin/env python2
# Имя модуля:        
# Назначение:
# Версия интерпретатора: 2.7.15
# Автор: Дмитрий Ильюшкò ilyushko@itain.ru dm.ilyushko@gmail.com
# Создан: 
# Изменен: 
# Правообладатель: Н.А. Прохоренок ISBN-978-5-9775-0614-4 2011
# Лицензия: MIT www.opensource.org/licenses/mit-license.php
# Рекурсию удобно использовать для перебора объекта, имеющего заранее неизвестную структуру,
# или выполнения неопределенного количества операций.
# В качестве примера рассмотрим вычисление факториала (листинг 11.22).
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


while True:
    x = raw_input("Bвведите число: ")

    if x.isdigit():  # Если строка содержит только цифры
        x = int(x)  # Преобразуем строку в число
        break  # Выходим из цикла
    else:
        print "Вы ввели не число!"
print "Факториал числа %s = %s" % (x, factorial(x))
