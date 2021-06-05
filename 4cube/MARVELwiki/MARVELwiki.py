'''
Модуль работы с базой данных героев
----------------------------------------------------------------------------------------------------------------------------------------
Структура модуля:

Реализованные ф-ии:
removeLastEnter()           Удаление переноса строки в конце файла
printDataBase()             Печать базы данных из файла HERObase.txt    
addEntry()                  Добавление одной записи в базу в конец файла HERObase.txt
removeEntry()               Удаление записи(-ей) по заданному значению одного из полей


В процессе:
sortEntries()               Сортировка записей базы данных по одному из полей
addEntriesToTempFile()      Добавление определенного списка записей в доп текстовый файл
selectEntries()             Выборка записей из базы по заданному значению одного из полей


Нереализованные:
comparingCharacters()       Сравнение двух выбранных персонажей
versusBattle()              Сражение выбранных героев с выбранными злодеями
----------------------------------------------------------------------------------------------------------------------------------------
'''
import tkinter as tk


def removeLastEnter():
    f = open('HERObase.txt','r')
    s = f.read().rstrip('\n')
    f = open('HERObase.txt','w')
    f.write(s)
    f.close()



def printDataBase():
    f = open('HERObase.txt','r')
    print(f.read())
    f.close()



def addEntry(flag, name, brain, power, speed, exp, fight):
    if flag == 1:
        # определение id новой записи 
        f = open('HERObase.txt','r')
        last_entry = f.readlines()[-1] # считываение последней строки из файла базы данных
        next_id = int(last_entry.split()[0]) + 1 # определение id новой записи
        f.close()
        # формирование новой записи базы данных
        f = open('HERObase.txt','a', 1, 'ANSI')
        s = '\n' + str(next_id) +'\t'
        s += name + '\t'
        s += brain + '\t'
        s += power + '\t'
        s += speed + '\t'
        s += exp + '\t'
        s += fight
        f.write(s)
        f.close()
    if flag == 2:
        # определение id новой записи 
        f = open('APIzlo.txt','r')
        last_entry = f.readlines()[-1] # считываение последней строки из файла базы данных
        next_id = int(last_entry.split()[0]) + 1 # определение id новой записи
        f.close()
        # формирование новой записи базы данных
        f = open('APIzlo.txt','a', 1, 'ANSI')
        s = '\n' + str(next_id) +'\t'
        s += name + '\t'
        s += brain + '\t'
        s += power + '\t'
        s += speed + '\t'
        s += exp + '\t'
        s += fight
        f.write(s)
        f.close()

