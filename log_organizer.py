## SOME PART OF THE CODE WERE SNIPPED DUE TO SECURITY PURPOSES
## If you need more detail, please send me an email via barisozensel@gmail.com

from ttp import ttp
import json
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from datetime import datetime
import threading

root= Tk()
root.geometry('1000x800')
root.configure(bg='#262626')
#root.resizable(0,0)
root.title('LOG Organizor By Ozensel')

def click_my_parsed_file():
    msg_box = tk.messagebox.askquestion('OPEN Parsed File.','Click to open parsed file.')
    #print(msg_box)
    if msg_box == "yes":
        os.system(f"notepad.exe {path_log_organizerX}{zaman}.txt")

def click_my_parsed_file_extractor():
    msg_box = tk.messagebox.askquestion('OPEN Parsed File.','Click to open parsed file.')
    #print(msg_box)
    if msg_box == "yes":
        os.system(f"notepad.exe {path_log_organizerX}{zaman}_extracted_file.txt")

data_to_have_it_extractor = ""
def wr_to_a_file_extractor(parsed_file):

    global data_to_have_it_extractor
    log_data_to_parse_extractorX111 = log_data_to_parse_extractor.split()

    main_templatedict = {}
    main_template = []
    for w in range(0, len(log_data_to_parse_extractorX111)):
        w1 = "data_" + str(w)
        main_template.append(w1)
        main_templatedict[w1] = log_data_to_parse_extractorX111[w]

    main_lst_dta_have = []
    for dataXX in parsed_file[0]:
        main_dict_data_have = {**main_templatedict,**dataXX}
        main_lst_dta_have.append(main_dict_data_have)

    with open(f"{path_log_organizerX}{zaman}.txt", "w") as a:
        a.write(f"ANOHER BUTTON IS CLIKCED.\n\n\n")

    for i in main_lst_dta_have:
        for k,v in i.items():
            if k == "MY_REST_DATA":
                with open(f"{path_log_organizerX}{zaman}.txt", "a") as a:
                    a.write(f"\n{v} ")
            else:
                with open(f"{path_log_organizerX}{zaman}.txt", "a") as a:
                    a.write(f"{v} ")
        with open(f"{path_log_organizerX}{zaman}.txt", "a") as a:
            a.write(f"\n\n")

    with open(f"{path_log_organizerX}{zaman}.txt", "a") as a:
        a.write(f"\n")

    with open(data_to_parse) as f:
        main_lines_inserted_file = f.read().splitlines()
    main_lines_inserted_file.append("\n")
    with open(f"{path_log_organizerX}{zaman}.txt") as f:
        parsed_lines_sub_file = f.read().splitlines()

    for id_main, line_main in enumerate(main_lines_inserted_file):
        line_main = line_main.replace("  ", " ")
        for id_sub, line_sub in enumerate(parsed_lines_sub_file):
            if line_sub == "" or line_sub == "\n":
                continue

            if line_sub.strip() in line_main:
                if main_lines_inserted_file[id_main+2].strip() == "":
                    main_lines_inserted_file.pop(id_main+2)
                main_lines_inserted_file.pop(id_main+1)
                main_lines_inserted_file.pop(id_main)
                if parsed_lines_sub_file[id_sub+2].strip() == "":
                    parsed_lines_sub_file.pop(id_sub+2)
                parsed_lines_sub_file.pop(id_sub+1)
                parsed_lines_sub_file.pop(id_sub)

    with open(f"{path_log_organizerX}{zaman}_extracted_file.txt", "w") as a:
        a.write(f"\n")

    for line in main_lines_inserted_file:
        with open(f"{path_log_organizerX}{zaman}_extracted_file.txt", "a") as a:
            a.write(f"{line}\n")

def hide():
    capture_frame.place_forget()
    extract_frame.place_forget()
    about_frame.place_forget()
my_template = ""
def button_action(i):
    global my_template
    my_template = ""
    global log_captured_data_to_parseX_chosen_button

    for index, k in enumerate(log_data_to_parseX):
        if k == i:
            log_data_to_parseX[index] = "{{data_%s}}" % index

    for template in log_data_to_parseX:
        my_template += template + " "
    
    my_syslog_captured_parser(data_to_parse)
 
log_extractor=Label(about_frame,text='Thanks for using LOG Organizer. \nYou can reach me out via https://github.com/bozensel \n',border=0,bg='#ffffff',fg='#262626',activeforeground='#12c4c0',activebackground='#262626')
log_extractor['font']= helv37
log_extractor.place(x=20,y=5)

log_organizor=Button(root,text='Run LOG Organizer',command=main_menu,border=0,bg='#a6a6a6',fg='#262626',activeforeground='#12c4c0',activebackground='#262626')
log_organizor['font']= helv37
log_organizor.place(x=20,y=8)
