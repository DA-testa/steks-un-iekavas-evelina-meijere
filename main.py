# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text): # enumarete funkcija dod atpakaļ pašreizējo iterāciju skaitu un vērtību
        if next in "([{": 
            opening_brackets_stack.append(Bracket(next, i )) # append funkcija pievieno elementu saraksta beigās
            # Process opening bracket, write your code here
           

        if next in ")]}":
            if not opening_brackets_stack: return i+1 
            m = opening_brackets_stack.pop() 
            if not are_matching: 
                return i+1 # pop funkcijas izņemt specifiskā pozīcījā esošu elementu
           

            if opening_brackets_stack:
                m = opening_brackets_stack.pop() 
                return m.position + 1 
            return ("Success")
            # Process closing bracket, write your code here


def main():
    print("1. Nolasa no faila, 2. Ievada pats: Izvēlies 1 vai 2")
    atbilde = input()
    if "1" in atbilde:
     failanos = input ("Faila nosaukums: ")
     with open(failanos, "r") as file:
        iekavas = file.read()
        mekle = find_mismatch(iekavas)
        if mekle == "Success":
            print("Success")
        else:
            print(mekle)
    elif "2" in atbilde:
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

