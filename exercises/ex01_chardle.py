"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730496915"

from winreg import HKEY_LOCAL_MACHINE


five_letter_word: str = input("Enter a 5-character word. ")
if len(five_letter_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character. ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character + " in " + five_letter_word)

matching_characters: str = 0

if five_letter_word[0] == single_character:
    print(single_character + " found at index 0")
    matching_characters = matching_characters + 1
if five_letter_word[1] == single_character:
    print(single_character + " found at index 1")
    matching_characters = matching_characters + 1
if five_letter_word[2] == single_character:
    print(single_character + " found at index 2")
    matching_characters = matching_characters + 1
if five_letter_word[3] == single_character:
    print(single_character + " found at index 3")
    matching_characters = matching_characters + 1
if five_letter_word[4] == single_character:
    print(single_character + " found at index 4")
    matching_characters = matching_characters + 1

if matching_characters == 0:
    print("No instances of " + single_character + " found in " + five_letter_word)
if matching_characters == 1:
    print("1 instance of " + single_character + " found in " + five_letter_word)
if matching_characters > 1:
    print(str(matching_characters) + " instances of " + single_character + " found in " + five_letter_word)