user_data = []
import random
def bank():
    while True :
        question = input("""how can we help you today
        Enter from the available options: 
        open acount
        close acount
        balance inquiry
        withdraw amount
        deposite amount
        transfer amount
        if you want to quit then Enter Quit """)
        if question == "Quit":
            print ("thank you for using our service")
            break
        else:
            if question == "open acount":
                name = input("Enter your name")
                CNIC  = int(input("enter CNIC number"))
                Contact = int(input("enter your Conatact Number"))
                initial_amount = int(input("enter your Initial Deposite"))
                acount_number = random.randint(10000,10000000)
                Acount={"Name":name,
                        "CNIC":CNIC,
                        "Contact":Contact,
                        "Acount Number":acount_number,
                        "balance":initial_amount}
                user_data.append(Acount)
                print(f"""thank you for opening acount with us your
                        Acount Number and Name is:
                        {Acount['Acount Number']} 
                        {Acount['Name']}""")
            elif question == "deposite amount":
                acount_num = int(input("enter your acount number"))
                for ac_num in user_data:
                    if ac_num['Acount Number'] == acount_num:
                        amount = int(input("enter deposite amount"))
                        if amount > 0:
                            ac_num['balance'] += amount
                            print(f" {ac_num['Name']} your current balance now is {ac_num['balance']}")
                            break
                        else:
                            print("invalid amount")
                    else:
                        print("ivalid acount number")
            elif question == "withdraw amount":
                acount_num = int(input("enter your acount number"))
                for ac_num in user_data:
                    if ac_num['Acount Number'] == acount_num:
                        amount = int(input("enter withdraw amount"))
                        if amount > ac_num['balance']:
                            print("not sufficient balance")
                        else:
                            ac_num['balance'] -= amount
                            print(f" {ac_num['Name']} your current balance now is {ac_num['balance']}")
                            break
                    else:
                        print("ivalid acount number")
            elif question == "balance inquiry":
                acount_num = int(input("enter your acount number"))
                for ac_num in user_data:
                    if ac_num['Acount Number'] == acount_num:
                        print(f" {ac_num['Name']} your current balance now is {ac_num['balance']}")
                        break
                    else:
                        print("ivalid acount number")
            elif question == "close acount":
                acount_num = int(input("enter your acount number"))
                for i,ac_num in enumerate(user_data):
                    if ac_num['Acount Number'] == acount_num:
                        print(f"here is your acount balance {ac_num['balance']}")
                        ac_num['balance'] = 0
                        del user_data[i]
                        print("acount closed successfully")
                        break
                    else:
                        print("ivalid acount number")
            elif question == "transfer amount":
                acount_num = int(input("enter your acount number"))
                for ac_num in user_data:
                    if ac_num['Acount Number'] == acount_num:
                        amount = int(input("enter amount "))
                        if amount > ac_num['balance']:
                            print("not sufficient balance")
                        else:
                            ac_num['balance'] -= amount
                            print(f" {ac_num['Name']} your current balance now is {ac_num['balance']}")
                            acount_num2 = int(input("enter your receiver acount number"))
                            for ac_num in user_data:            
                                if ac_num['Acount Number'] == acount_num2:
                                    ac_num['balance'] += amount
                                    print(f" {ac_num['Name']} your current balance now is {ac_num['balance']}")
                                    print("your fund has been transfered")
                                    break
                                else:
                                    print("invalid reciever acount number")
                    else:
                        print("ivalid acount number")