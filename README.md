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

![Screenshot 2024-07-04 120308](https://github.com/shayanjaviid/Password-Cracker/assets/104303445/732f27c4-ccb7-41e7-b3d4-a342d954d414)

## Example
Enter a password: P@ssw0rd
Cheyenne is Cracking Password....Please Wait!
...
Your Password is: P@ssw0rd
