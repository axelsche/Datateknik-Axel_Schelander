#Definiera en klass “Student” som har minst tre attribut: förnamn, efternamn och personnummer. Klassen ska ha minst två
#metoder, __init__ och __str__.

#Skapa minst tre objekt av typen “Student” genom att be användaren skriva in information om studenter. Fundera på bästa
#sättet att spara ner de skapade objekten.

#När alla objekt är skapade ska programmet skriva ut alla skapade objekt.

names = []#index börjar på 0 i python
pers_num = []#lista med personnummer


n0 = input("Vad heter Studenten")
names.append(n0)
p0 = input("Vad är studentens personnummer")
pers_num.append(p0)

print("Objekt skapat")

n1 = input("Vad heter Studenten")
names.append(n1)
p1 = input("Vad är studentens personnummer")
pers_num.append(p1)

print("Objekt skapat")


n2 = input("Vad heter Studenten")
names.append(n2)
p2 = input("Vad är studentens personnummer")
pers_num.append(p2)

print("Objekt skapat")

print (names[0], pers_num[0])
print (names[1], pers_num[1])
print (names[2], pers_num[2])
