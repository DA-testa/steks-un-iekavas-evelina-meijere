# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text): # enumarete funkcija dod atpakaļ pašreizējo iterāciju skaitu un vērtību
        if next in "([{": 
            opening_brackets_stack.append(Bracket(next, i + 1 )) # append funkcija pievieno elementu saraksta beigās
            # Process opening bracket, write your code here
        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            if not are_matching(opening_brackets_stack[-1].char,next):
             return i + 1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return
        opening_brackets_stack[-1].position
    else : return "Success"
            # Process closing bracket, write your code here


def main():
    print("F vai I?")
    atbilde = input()
    if "F" in atbilde:
     failanos = input ("Faila nosaukums: ")
     with open(failanos, "r") as file:
        iekavas = file.read()
        mekle = find_mismatch(iekavas)
        if mekle == "Success":
            print("Success")
        else:
            print(mekle)
    elif "I" in atbilde:
        iekavas = input()
        mekle = find_mismatch(iekavas)
        if mekle == "Success":
            print("Success")
        else:
            print(mekle)
    else:
        print("Ievadīts nepareizs cipars!")

    # Printing answer, write your code here
 

if __name__ == "__main__":
    main()

