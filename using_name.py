#-*-coding:utf-8*-
#!/usr/bin/env python
''''''
'''
В каждом модуле Python определено его имя – __name__ Если оно равно
'__main__', это означает, что модуль запущен самостоятельно пользователем, и мы можем выполнить соответствующие действия.
'''
import using_name
if __name__ == '__main__':
    print('Эта программа запущена сама по себе.')
else:
    print('Меня импортировали в другой модуль.')
