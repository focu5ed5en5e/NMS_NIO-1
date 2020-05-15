# -*- coding: utf-8 -*-
import os
import time
import datetime


import sys
import subprocess

time_tuple = (
                2019, # Year
                  9, # Month
                  6, # Day
                  0, # Hour
                 38, # Minute
                  0, # Second
                  0, # Millisecond
              )
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def win_set_time(time):
    os.system("time " + time)

def win_set_date(date):
    os.system("date " + date)

# выполнение требует прав суперпользователя
def linux_set_time_date(timedate):
    # sudo timedatectl set-time YYYY-MM-DD №
    # sudo timedatectl set-time HH:MM:SS
    # sudo timedatectl set-time '10:42:43'
    # sudo timedatectl set-time '2015-11-23 08:10:40'
    # date - s "2 NOV 2019 18:00:00"
    # date +%Y%m%d -s "20191107"
    # date
    subprocess.call(["timedatectl", "set-time", timedate])
    print 'date were set:' + str(subprocess.call(["date"]))

#if __name__ == 'main':

sp = sys.platform
print sys.platform
#win_set_time("15:20") # tested
#win_set_date("08-11-2019") # tested
linux_set_time_date("2019-11-07") # tested
linux_set_time_date("16:31:35")# tested

