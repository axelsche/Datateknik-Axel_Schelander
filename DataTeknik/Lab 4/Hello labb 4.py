#Definiera en klass “Student” som har minst tre attribut: förnamn, efternamn och personnummer. Klassen ska ha minst två
#metoder, __init__ och __str__.

#Skapa minst tre objekt av typen “Student” genom att be användaren skriva in information om studenter. Fundera på bästa
#sättet att spara ner de skapade objekten.

#När alla objekt är skapade ska programmet skriva ut alla skapade objekt.

import integer_input
import string_input
def student (first_name, last_name, personnummer):

    names = [first_name, last_name]#index börjar på 0 i python
    pers_num = [personnummer]#lista med personnummer

full_name = input("Vad heter Studenten: ")

name_parts = full_name.split()

if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = ' '.join(name_parts[1:])  # Join remaining parts as the last name
else:
    first_name = full_name
    last_name = ""

print("First Name:", first_name)
print("Last Name:", last_name)

n0 = input("Vad heter Studenten")
names.append(n0)
p0 = integer_input.get_integer_input("Vad är studentens personnummer")
pers_num.append(p0)

print("")
print("Objekt skapat")
print("")
n1 = input("Vad heter Studenten")
names.append(n1)
p1 = integer_input.get_integer_input("Vad är studentens personnummer")
pers_num.append(p1)
print("")
print("Objekt skapat")
print("")

n2 = input("Vad heter Studenten")
names.append(n2)
p2 = integer_input.get_integer_input("Vad är studentens personnummer")
pers_num.append(p2)
print("")
print("Objekt skapat")
print("")
print (names[0], pers_num[0])
print (names[1], pers_num[1])
print (names[2], pers_num[2])
