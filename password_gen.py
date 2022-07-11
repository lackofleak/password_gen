# password generator 

import os
import random

def clear():
    "clear terminal screen"
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    


banner = """
    ____                                          __
   / __ \____ ____________      ______  _________/ /
  / /_/ / __ `/ ___/ ___/ | /| / / __ \/ ___/ __  /
 / ____/ /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /
/_/    \__,_/____/____/ |__/|__/\____/_/   \__,_/
   ______                           __
  / ____/__  ____  ___  _________ _/ /_____  _____
 / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
/ /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /
\____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/
"""


def help(page_num):
    "fnc to show help"
    clear()
    if page_num == 0 :
        return """
Wellcome to the password Generator script with python !

you can use this script to generate passwords, you want !

1 -> this page 
2 -> generate passwords you wish
3 -> exit 
"""
    if page_num ==1 :
        return """
option 1 you can go by Defualt Values
optin 2 : you can Enter you favorit values :
e.g : 
abc = "amir"
num = "2000"
sym = "@#$"
option 3 this page
option 4 break process
"""



def page_0(status):
    "Wellcome page"
    if status == "main":
        clear()
        print(banner)
    else:
        print("--------------------------------")
    
    user_input1 = input("""
choose an option to continue :
[1].help
[2].generate password
[3].exit
    """)
    if user_input1 == "1":
        print(help(0))
        page_0("none")
    elif user_input1 == "2":
        page_1("main")
    else :
        exit()



def page_1(status1):
    "password generator page !"
    if status1 == "main":
        clear()
        print(banner)
    else :
        print("-----------------------------")
    user_input2 = input("""
choose option to continue :
[1].Generate password by defualt
[2].Enter custom settings
[3].help
[4].exit!
    """)
    if user_input2 == "1":
        page_1_1("main")
    elif user_input2 == "2":
        page_1_2("main")
    elif user_input2 =="3":
       print(help(1))
       page_1("none")
    else:
        exit()

class passwordgen:
    "heart of the script"
    def __init__(self , abc , sym ,num):
        self.abc = abc
        self.num = num
        self.sym = sym
        pass_count = int(input("[*].How many passwd U want to gen ?\n"))
        pass_length = int(input("[*].Enter length of passwd :\n"))
        pass_content = input("[*].your password will contain ...\n[1].abc..\n[2].character\n[3].numbers\n[4].all\n")
        pass_file_check = input("[*]. Do you want to Save Passwords y(es) , n(o): \n")
        if pass_file_check.lower() == "y":
            pass_file_name = input("Enter file name you want (*.txt):\n")
        for count in range(pass_count):
            password = ""
            for len in range(pass_length):
                if pass_content=="1":
                    password += random.choice(abc)
                elif pass_content =="2":
                    password += random.choice(sym)
                elif pass_content =="3":
                    password += random.choice(num)
                elif pass_content =="4":
                    allpass = num + abc + sym
                    password += random.choice(allpass)
                else :
                    break
            try :
                if pass_file_check.lower() == "y":
                    with open(f"{pass_file_name}" , "a" , encoding="UTF-8") as passfile:
                        passfile.write(f"{password}\n")
                else:
                    print(password)
            finally :
                pass



def page_1_1(status2):
    "defualt pass generator"
    if status2 == "main":
        clear()
        print(banner)
    else:
        print("--------------------------------")
    abc = "abcdefghijklmnopqrstuvwxyz"
    sym = r"~!@#$%^&*(){}|[]/\<>" 
    num = "0123456789"
    main1 = passwordgen(abc , sym , num )
    print("all done!")
    again()


def page_1_2(status3):
    "custome pass generator"
    if status3 == "main":
        clear()
        print(banner)
    else:
        print("--------------------------------")
    abc = input("Enter abc.. \n")
    sym = input(r"""Enter symbols.. 
""")
    num = input("Enter numbers...\n")
    main1 = passwordgen(abc , sym , num )
    print("all done!")
    again()


def again():
    "run script again"
    print("------------------------------------------")
    userstatus = input("choose an item to cuntinue:\n[1].main page\n[2].exit\n")
    if userstatus == "1":
        page_0("main")
    else:
        exit()

page_0("main")