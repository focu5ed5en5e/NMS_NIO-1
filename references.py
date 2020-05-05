#-*-coding:utf-8*-
#!/usr/bin/env python
''''''
'''
Помните, что если вам нужно сделать копию списка или подобной последовательности, или другого сложного объекта
(не такого простого объекта, как целое число), вам следует воспользоваться операцией вырезки  .
Если вы просто присвоите имя переменной другому имени, оба они будут ссылаться на один и тот же объект,
а это может привести к проблемам, если вы не осторожны.
'''
print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist # mylist - лишь ещё одно имя, указывающее на тот же объект!
del shoplist[0] # Я сделал первую покупку, поэтому удаляю её из списка
print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что и shoplist, и mylist выводят один и тот же список
#  без пункта "яблоко", подтверждая тем самым, что они указывают на один объект.
print('Копирование при помощи полной вырезки')
########################################################################################################################
mylist = shoplist[:] # создаём КОПИЮ путём ПОЛНОЙ ВЫРЕЗКИ
del mylist[0] # удаляем первый элемент
print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что теперь списки разные
