from random import *
import os

u_pwd = input("Enter a password:")
pwd=['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
     'B', 'C', 'D', 'E', 'H', 'I', 'G', 'K', 'L', 'M',
     'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'Q', 'Y',
     'Z', '0', '!', '@', '#', '$', '%', '&']

pw=""
while(pw!=u_pwd):
    pw=""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0,35)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("Cheyenne is Cracking Password....Please Wait!")
        os.system("cls")
print("Your Password is :", pw)