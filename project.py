
def shutdown():
    print("Would you like to shut down the computer? ")
    choice= input("Yes or No   ")
    if choice == 'yes' or 'Yes':
        print("Are all tabs closed? ")
        choice2 = input ("Yes or No:   ")
        if choice2 == 'no':
            print ("Close all Tabs to continue ")
        else:
            print ("Shutting down")
        
shutdown()






