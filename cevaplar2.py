#Name Dongusu 
#Be sure that names have only letters(Uppercase or lowcase). No numbers
# No characters or any other thing.. Justletters.. Program should ask for new input if the input is not valid
#There must not be a name twice in the list. Then the program should start them for the same name


while True:
    name=input("Name *(Just letters) (quit 1):" )
    if name in contacts_list.keys():
        ask=input("Do you want to add number to this name y(yes) or n(no)")
        print(ask)
        if ask!='y':
            break
    
    if name=='1':
        break
    elif name.isalpha()== False:
        print("Just Letters...")
        continue
    else:
        break
    
    #Phone numbers must have 10 digits.
    #Otherwise the program shouldn't accept the input and should ask the user to enter the number again
    
    while True:
        number=input("Number")
        if (len(number)) != 10:
            print("Please 10 digits..")
            continue
        elif (number.isdigit()==False):
            print("Please only digits")
        else:
            break           
        """elif menu=="3": #Add
        while True:
            name=input("Name *(Just letters) (quit 1): ")
            print(name)
            if name=="1":
                break
            elif name.isalpha==(False):
                print("Just letters..")
                continue
            else:
                break"""
        while True:
            if name in contacts_list.keys():
                print("This name added already...")
                ask=input("Do you want to add number to this name? y(yes) or n(no)")
                print(ask)
                if ask != y :
                    break
            number=input("Number*(Just digits)(quit 1):")
            print(number)
            if number=='1':
                break
            elif (len(number)!=10)or(number.isdigit()==False):
                print("Numbers must have 10 digits or Just Digit...")
                continue
            else:
                if name in contacts_list.keys():
                    contacts_list(name).append(number)
                    ask_imp=input("If the user is important click 1 or click any other key:")
                    print(ask_imp)
                    contacts_list[name]=[number]
                    if ask_imp!='1':
                        break
                    else:
                        important_contact_list[name]=[number]
                        break
                                                                  