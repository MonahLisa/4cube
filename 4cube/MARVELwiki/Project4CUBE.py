import tkinter as tk
from MARVELwiki import *
import random
import os
flag = 0
zlo_info = 0
dobro_info = 0

#----------------------------------------------------------------УДАЛЕНИЕ ПЕРСОНАЖА-----------------------------------------------
def removeEntry():
    if flag == 1:
        n = ent_pers_name.get()
        remove.destroy()
        HERObase = dict()
        f = open('HERObase.txt','r')
        labels = f.readline().rstrip('\n').split('\t')
        for entry in f:
            tmp = entry.rstrip('\n').split('\t')
            # перезапись строки (если данных о герое нет в строке) или удаление строки (если данные о герое есть в строке)
            if n not in tmp:
                HERObase[int(tmp[0])] = dict(
                    name = tmp[1],
                    iq = tmp[2],
                    power = tmp[3],
                    speed = tmp[4],
                    skill = tmp[5],
                    fight = tmp[6]
                    )
        f.close()
        f = open('HERObase.txt','w')
        f.write('\t'.join(labels) + '\n')
        s = ''
        for key,value in HERObase.items():
            s += str(key) + '\t'
            s += value.get('name') + '\t'
            s += value.get('iq') + '\t'
            s += value.get('power') + '\t'
            s += value.get('speed') + '\t'
            s += value.get('skill') + '\t'
            s += value.get('fight') + '\n'
        f.write(s.rstrip('\n'))
        f.close()


        temp = dict()
        f = open('HERObase.txt','r')
        labels = f.readline().rstrip('\n').split('\t')
        print(labels)
        idd = 0
        mas_pers = []
        mas_pers.append(labels)
        for entry in f:
            idd += 1
            tmp = entry.rstrip('\n').split('\t')
            tmp[0]=str(idd)
            print(tmp)
            mas_pers.append(tmp)
            temp[int(tmp[0])] = dict(
                name = tmp[1],
                iq = tmp[2],
                power = tmp[3],
                speed = tmp[4],
                skill = tmp[5],
                fight = tmp[6]
                )
        f.close()
        print(mas_pers)
        print()
        os.system(r'nul>HERObase.txt')


        f = open('HERObase.txt','w')
        s = mas_pers[0][0] +'\t'
        s += mas_pers[0][1] + '\t'
        s += mas_pers[0][2] + '\t'
        s += mas_pers[0][3] + '\t'
        s += mas_pers[0][4] + '\t'
        s += mas_pers[0][5] + '\t'
        s += mas_pers[0][6]
        f.write(s)
        f.close()
        f = open('HERObase.txt','a', 1, 'ANSI')
        for i in range(1, len(mas_pers)):
            s = '\n' + mas_pers[i][0] +'\t'
            s += mas_pers[i][1] + '\t'
            s += mas_pers[i][2] + '\t'
            s += mas_pers[i][3] + '\t'
            s += mas_pers[i][4] + '\t'
            s += mas_pers[i][5] + '\t'
            s += mas_pers[i][6]
            f.write(s)
        f.close()

        
    if flag == 2:
        n = ent_pers_name.get()
        remove.destroy()
        APIhero = dict()
        f = open('APIzlo.txt','r')
        labels = f.readline().rstrip('\n').split('\t')
        for entry in f:
            tmp = entry.rstrip('\n').split('\t')
            # перезапись строки (если данных о злодее нет в строке) или удаление строки (если данные о герое есть в строке)
            if n not in tmp:
                APIhero[int(tmp[0])] = dict(
                    name = tmp[1],
                    iq = tmp[2],
                    power = tmp[3],
                    speed = tmp[4],
                    skill = tmp[5],
                    fight = tmp[6]
                    )
        f.close()
        f = open('APIzlo.txt','w')
        f.write('\t'.join(labels) + '\n')
        s = ''
        for key,value in APIhero.items():
            s += str(key) + '\t'
            s += value.get('name') + '\t'
            s += value.get('iq') + '\t'
            s += value.get('power') + '\t'
            s += value.get('speed') + '\t'
            s += value.get('skill') + '\t'
            s += value.get('fight') + '\n'
        f.write(s.rstrip('\n'))
        f.close()



def removeTK():
    global ent_pers_name, remove
    remove = tk.Tk()

    pers_name = tk.Label(remove, text = "Введите имя персонажа", width=60)
    pers_name.pack()

    ent_pers_name = tk.Entry(remove, width = 60)
    ent_pers_name.pack()

    remove_pers = tk.Button(
    master=remove,
    text="Удалить",
    width=60,
    height=2,
    bg="blue",
    fg="yellow",
    font = 10,
    command = removeEntry)

    remove_pers.pack()
    remove.mainloop()
#----------------------------------------------------------------УДАЛЕНИЕ ПЕРСОНАЖА-----------------------------------------------
#
#
#
#
#
#----------------------------------------------------------------ИНФОРМАЦИЯ О ГЕРОЕ--------------------------------------------------------
def hero_inf(event):
    global info_hero, dobro_info, zlo_info
    dobro_info+=1
    if (dobro_info == 2):
        info_hero.destroy()
        dobro_info-=1
    if (zlo_info == 1):
        info_zlo.destroy()
        zlo_info-=1
    
    info_hero = tk.Tk()
    name_pers = event.widget.cget('text')


    HERObase = dict()
    f = open('HERObase.txt','r')
    labels = f.readline().rstrip('\n').split('\t')
    for entry in f:
        tmp = entry.rstrip('\n').split('\t')
        HERObase[int(tmp[0])] = dict(
            name = tmp[1],
            iq = tmp[2],
            power = tmp[3],
            speed = tmp[4],
            skill = tmp[5],
            fight = tmp[6]
            )
    f.close()


    
    for i in range(1, len(HERObase)+1):
        if name_pers == HERObase[i]["name"]:
            pers_index = i
            
    lbl_name_pers = tk.Label(info_hero, text = name_pers, font = 11)
    lbl_name_pers.pack()

    mas_pers = ["name", "iq", "power", "speed", "skill", "fight"]
    labels = ['Имя', 'Интеллект', 'Сила', 'Скорость и ловкость', 'Особые умения', 'Бойцовские навыки']

    for i in range(1, len(mas_pers)):
        lbl_pers = tk.Label(info_hero, text = labels[i]+" "+HERObase[pers_index][mas_pers[i]])
        lbl_pers.pack()


    #lbl_info_pers = tk.Label(info_hero, text = mas_pers[len(mas_pers)-1])
    #lbl_info_pers.pack()
                

    info_hero.mainloop()
#----------------------------------------------------------------ИНФОРМАЦИЯ О ГЕРОЕ-END----------------------------------------------------
#
#
#
#----------------------------------------------------------------ИНФОРМАЦИЯ О ЗЛОДЕЕ-------------------------------------------------------
def zlo_inf(event):
    global info_zlo, dobro_info, zlo_info
    zlo_info+=1
    if (zlo_info == 2):
        info_zlo.destroy()
        zlo_info-=1
    if (dobro_info == 1):
        info_hero.destroy()
        dobro_info-=1
    
    info_zlo = tk.Tk()
    name_pers = event.widget.cget('text')



    APIzlo = dict()
    f = open('APIzlo.txt','r')
    labels = f.readline().rstrip('\n').split('\t')
    for entry in f:
        tmp = entry.rstrip('\n').split('\t')
        APIzlo[int(tmp[0])] = dict(
            name = tmp[1],
            iq = tmp[2],
            power = tmp[3],
            speed = tmp[4],
            skill = tmp[5],
            fight = tmp[6]
            )
    f.close()


    
    for i in range(1, len(APIzlo)+1):
        if name_pers == APIzlo[i]["name"]:
            pers_index = i
            
    lbl_name_pers = tk.Label(info_zlo, text = name_pers, font = 11)
    lbl_name_pers.pack()

    mas_pers = ["name", "iq", "power", "speed", "skill", "fight"]
    labels = ['Имя', 'Интеллект', 'Сила', 'Скорость и ловкость', 'Особые умения', 'Бойцовские навыки']

    

    for i in range(1, len(mas_pers)):
        lbl_pers = tk.Label(info_zlo, text = labels[i]+" "+APIzlo[pers_index][mas_pers[i]])
        lbl_pers.pack()

    #lbl_info_pers = tk.Label(info_zlo, text = mas_pers[len(mas_pers)-1])
    #lbl_info_pers.pack()
                

    info_zlo.mainloop()
#----------------------------------------------------------------ИНФОРМАЦИЯ О ЗЛОДЕЕ-END--------------------------------------------------
#
#
#
#----------------------------------------------------------------КНОПКА ДОБАВЛЕНИЯ--------------------------------------------------------
def addInList():
    name, brain, power, speed, exp, fight, info = ent_name.get(), ent_brain.get(), ent_power.get(), ent_speed.get(), ent_exp.get(), ent_fight.get(), txt_info.get("1.0", tk.END)
    addEntry(flag, name, brain, power, speed, exp, fight)
    master.destroy()
#----------------------------------------------------------------КНОПКА ДОБАВЛЕНИЯ-END----------------------------------------------------
#
#
#
#----------------------------------------------------------------ДОБАВЛЕНИЕ ПЕРСОНАЖА-----------------------------------------------------
def add():
    global master, ent_name, ent_brain, ent_power, ent_speed, ent_exp, ent_fight, txt_info, dobro_info, zlo_info, info_zlo, info_hero
    if (zlo_info == 1):
        info_zlo.destroy()
        zlo_info-=1
    if (dobro_info == 1):
        info_hero.destroy()
        dobro_info-=1
    master = tk.Tk()
    
    lbl_name = tk.Label(master, text = "Введите имя", width = 37)
    lbl_name.pack()
    ent_name = tk.Entry(master, width = 37)
    ent_name.pack()

    lbl_brain = tk.Label(master, text = "\nВведите интеллект (0-500)", width = 37)
    lbl_brain.pack()
    ent_brain = tk.Entry(master, width = 37)
    ent_brain.pack()

    lbl_power = tk.Label(master, text = "\nВведите силу (0-500)", width = 37)
    lbl_power.pack()
    ent_power = tk.Entry(master, width = 37)
    ent_power.pack()

    lbl_speed = tk.Label(master, text = "\nВведите скорость и ловкость (0-500)", width = 37)
    lbl_speed.pack()
    ent_speed = tk.Entry(master, width = 37)
    ent_speed.pack()

    lbl_exp = tk.Label(master, text = "\nВведите особые умения (0-500)", width = 37)
    lbl_exp.pack()
    ent_exp = tk.Entry(master, width = 37)
    ent_exp.pack()

    lbl_fight = tk.Label(master, text = "\nВведите бойцовские навыки (0-500)", width = 37)
    lbl_fight.pack()
    ent_fight = tk.Entry(master, width = 37)
    ent_fight.pack()

    lbl_info = tk.Label(master, text = "\nВведите информацию о персонаже", width = 37)
    lbl_info.pack()
    txt_info = tk.Text(master, height = 15, width = 40)
    txt_info.pack()

    btn_add2 = tk.Button(
    master,
    text="Добавить",
    width=60,
    height=2,
    bg="blue",
    fg="yellow",
    font = 10,
    command = addInList)

    btn_add2.pack()

    
    master.mainloop()

#--------------------------------------------------------------------ДОБАВЛЕНИЕ ПЕРСОНАЖА-END------------------------------------------------
#
#
#
#
#-------------------------------------------------------------------------ФРЕЙМ ГЕРОЕВ-------------------------------------------------------
def frame_hero():
    global flag, frm_hero

    if flag == 2:
        frm_zlo.destroy()
    
    flag = 1

    
    frm_hero = tk.Frame()
    frm_hero.pack()

    HERObase = dict()
    f = open('HERObase.txt','r')
    labels = f.readline().rstrip('\n').split('\t')
    idd = 0
    for entry in f:
        idd += 1
        tmp = entry.rstrip('\n').split('\t')
        tmp[0]=str(idd)
        HERObase[int(tmp[0])] = dict(
            name = tmp[1],
            iq = tmp[2],
            power = tmp[3],
            speed = tmp[4],
            skill = tmp[5],
            fight = tmp[6]
            )
    f.close()       


        
    for i in range(1, len(HERObase)+1):
        btn_ger = tk.Button(
            master=frm_hero,
            text=HERObase[i]["name"],
            width=60,
            height=2,
            bg="blue",
            fg="yellow",
            font = 10,
            command = hero_inf)
        btn_ger.pack()
        btn_ger.bind('<Button-1>', hero_inf)


    probel = tk.Label(master=frm_hero, text = " ")
    probel.pack()
   


    btn_add = tk.Button(
    master=frm_hero,
    text="Добавить своего героя",
    width=60,
    height=2,
    bg="blue",
    fg="yellow",
    font = 10,
    command = add)

    btn_add.pack()


    btn_remove = tk.Button(
    master=frm_hero,
    text="Удалить героя",
    width=60,
    height=2,
    bg="blue",
    fg="yellow",
    font = 10,
    command = removeTK)

    btn_remove.pack()

    btn_hero.config(
        width=25,
        height=5,
        bg="orange",
        fg="blue",
        command=""
        )

    btn_zlo.config(
        text="ЗЛОДЕИ",
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
        command=frame_zlo
        )

    btn_ludi.config(
        text="ДРУГИЕ",
        width=25,
        height=5,
        bg="blue",
        fg="yellow"
        )

#--------------------------------------------------------------------------ФРЕЙМ ГЕРОЕВ-END---------------------------------------------
#
#
#
#
#
#---------------------------------------------------------------------------ФРЕЙМ ЗЛОДЕЕВ-----------------------------------------------

def frame_zlo():
    global flag, frm_zlo
    if flag == 1:
        frm_hero.destroy()

    flag = 2
    
    frm_zlo = tk.Frame()
    frm_zlo.pack()


    APIzlo = dict()
    f = open('APIzlo.txt','r')
    labels = f.readline().rstrip('\n').split('\t')
    idd = 0;
    for entry in f:
        idd += 1
        tmp = entry.rstrip('\n').split('\t')
        APIzlo[idd] = dict(
            name = tmp[1],
            iq = tmp[2],
            power = tmp[3],
            speed = tmp[4],
            skill = tmp[5],
            fight = tmp[6]
            )
    f.close()
    
    for i in range(1, len(APIzlo)+1):
        btn_zloi = tk.Button(
            master=frm_zlo,
            text=APIzlo[i]["name"],
            width=60,
            height=2,
            bg="blue",
            fg="yellow",
            font = 10,
            command = zlo_inf)
        btn_zloi.pack()
        btn_zloi.bind('<Button-1>', zlo_inf)


    probel = tk.Label(master=frm_zlo, text = " ")
    probel.pack()
   


    btn_add = tk.Button(
    master=frm_zlo,
    text="Добавить своего злодея",
    width=60,
    height=2,
    bg="blue",
    fg="yellow",
    font = 10,
    command = add)

    btn_add.pack()



    btn_remove = tk.Button(
    master=frm_zlo,
    text="Удалить злодея",
    width=60,
    height=2,
    bg="blue",
    fg="yellow",
    font = 10,
    command = removeTK)

    btn_remove.pack()

    

    btn_hero.config(
        bg = "blue",
        fg = "yellow",
        command=frame_hero
        )

    btn_zlo.config(
        bg="orange",
        fg="blue",
        command = ""
        )

    btn_ludi.config(
        bg="blue",
        fg="yellow"
        )

#------------------------------------------------------------------------ФРЕЙМ ЗЛОДЕЕВ-END-----------------------------------------------------
#
#
#
#
#
#
#-------------------------------------------------------------------------ТРИ КНОПКИ ПАНЕЛИ----------------------------------------------------
window = tk.Tk()
frm_btns = tk.Frame()
frm_btns.pack()


btn_hero = tk.Button(
    master=frm_btns,
    text="СУПЕРЫ",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=frame_hero
)
btn_hero.pack(side=tk.LEFT)


btn_zlo = tk.Button(
    master=frm_btns,
    text="ЗЛОДЕИ",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=frame_zlo
)
btn_zlo.pack(side=tk.LEFT)

btn_ludi = tk.Button(
    master=frm_btns,
    text="ДРУГИЕ",
    width=25,
    height=5,
    bg="blue",
    fg="yellow"
)
 
btn_ludi.pack(side=tk.LEFT)
window.mainloop()
#-------------------------------------------------------------------------------ТРИ КНОПКИ ПАНЕЛИ-END----------------------------------------
