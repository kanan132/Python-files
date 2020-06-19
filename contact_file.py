import time
def add_contact(name, number):
    with open('contacts.txt', 'r+') as file:
        contents = file.read()
        file.seek(0)
        file.write(f'{name}\t\t{number}\n'+contents)    
        print(contents)

def add_certain_position(name, number, position):
    with open('contacts.txt', 'r+') as file:
        contents = file.readlines()
        pos=position-1
        contents.insert(pos, f'{name}\t\t{number}\n')
        file.seek(0)
        file.writelines(contents)
        print(contents)


def remove_contact(name, number):
    with open('contacts.txt', 'r+') as file:
        contents = file.readlines()
        contents.remove(f"{name}\t\t{number}\n")
        file.seek(0)
        file.writelines(contents)
        print(contents)

def sort_contacts():
    with open('contacts.txt', 'r+') as file:
        contents = file.readlines()
        contents.sort()
        file.seek(0)
        file.writelines(contents)
        print(contents)


while True:
    
    name=input("Enter a command(1-remove,2-sort,\n3-add contact,4-add contact with position) or exit:\t")
    if name.lower()=="exit":
        a=time.sleep(1)
        print(f"Exiting program...")
        break
    elif name.lower()=="1":
        nom=input("Enter name:\t")
        numb=input("Enter number:\t")
        remove_contact(nom,numb)
    elif name.lower()=="2":
        sort_contacts()
    elif name.lower()=="3":
        prenom=input("Enter name:\t")
        num=input("Enter number:\t")
        add_contact(prenom,num)
    elif name.lower()=="4":
        pre=input("Enter name:\t")
        numo=input("Enter number:\t")
        position=int(input("enter position:\t"))
        add_certain_position(pre,numo,position)