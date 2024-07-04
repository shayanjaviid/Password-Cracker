# Password Cracker

This Python script attempts to crack a user-provided password by generating random guesses. It demonstrates a basic brute force approach to password cracking.

## How it Works

1. The user is prompted to enter a password.
2. The script randomly generates characters from a predefined set of possible characters.
3. The script continues to generate random guesses until it matches the user-provided password.
4. The progress of each guess is printed to the console.
5. Once the password is guessed correctly, the script prints the guessed password.

## Character Set

The script uses the following set of characters for generating guesses:
- Digits: `1` to `9`, `0`
- Uppercase Letters: `A` to `Z` (excluding `O`)
- Special Characters: `!`, `@`, `#`, `$`, `%`, `&`

## Running the Script

1. Make sure you have Python installed on your system.
2. Save the script to a file, for example, `password_cracker.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory where you saved the script.
5. Run the script using the command:

from random import randint
import os

u_pwd = input("Enter a password:")
pwd = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A",
       "B", "C", "D", "E", "H", "I", "G", "K", "L", "M",
       "M", "N", "P", "Q", "R", "S", "T", "W", "Q", "Y",
       "Z", "0", "!", "@", "#", "$", "%", "&"]

pw = ""
while pw != u_pwd:
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, len(pwd) - 1)]
        pw = str(guess_pwd) + str(pw)
        print(pw)
        print("Cheyenne is Cracking Password....Please Wait!")
        os.system("cls" if os.name == "nt" else "clear")
print("Your Password is:", pw)



from random import randint
import os

u_pwd = input("Enter a password:")
pwd = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
       'B', 'C', 'D', 'E', 'H', 'I', 'G', 'K', 'L', 'M',
       'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'Q', 'Y',
       'Z', '0', '!', '@', '#', '$', '%', '&']

pw = ""
while pw != u_pwd:
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, len(pwd) - 1)]
        pw = str(guess_pwd) + str(pw)
        print(pw)
        print("Cheyenne is Cracking Password....Please Wait!")
        os.system("cls" if os.name == 'nt' else "clear")
print("Your Password is:", pw)


