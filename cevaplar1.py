#Contact List

def print_menu(): #with def print_menu we can add menu options
    print("______PHONE BOOK_________")                                                     
    print('1. Show Phone Numbers')
    print('2. Add a Phone Number')                                                                           
    print('3. Edit a Phone Number')
    print('4. Delete a Phone Number')
    print('5. Show Important numbers ')
    print()

numbers = {} # need a dict voor names and numbers which the contact list has 
numbers2=()
l=list(numbers2)
menu_choice = 0
print_menu()
while True:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        print("Telephone Numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()
    elif menu_choice == 2:
        print("Add Name and Number")     
        name = input("Name: ")
        phone = int(input("Number: "))                                                             #Program accept just digits 
        if len(str(phone))==10 and name.isalpha():                                                 #Phone number must max 10 digits and it must upper or lowercase
            numbers[name] = phone
            answer=input("If number is important push Y")                                           #If the person and number is important then program keep the datas safer pleace with in another the tuple file to not to these datas change.
            if answer=='Y':
                l.append(numbers)
            else:
                continue
        else:
            print("Phone number must 10 digit and names must just letter be created ")

    elif menu_choice == 3:
        name = input("Please add a name which you edit: ")
        newphone=input("Please add a newphone:")
        print("Edit Number")
        newname=input("Please add a new name:")
        if name in numbers:
            numbers[newname]=newphone
            del(numbers[name])

        else:
            print(name, "was not found")

    elif menu_choice == 4:
        print("Remove Name and Number")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")

    elif menu_choice == 5:
        print("Important Numbers")
        print(l) 