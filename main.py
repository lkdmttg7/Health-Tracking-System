# Python Script for Tracking Health by logging their Diet and Exercise
def getdate():
    #Get the time stamp for the log entry
    import datetime
    return datetime.datetime.now()
while True:
    #Run Loop until user exits
    client = int(input("Enter the Number corresponding to the Client Name:\n1. John\n2. Smith\n3. Amy\n"))
    log_or_retrieve = int(input("Do you want to log or retrieve the Data:\n1. Log\n2. Retrieve\n"))
    f_or_e = int(input("Select Food or Exercise:\n1. Food\n2. Exercise\n"))
    if client == 1:                      # Client: John
        if log_or_retrieve == 1:         # Log the Data
            if f_or_e == 1:              # Food
                log = input("What did you eat?\n")
                final_log = "["+str(getdate())+"] "+log
                print(final_log)
                with open("john_food.txt","a") as f:
                    f.write(final_log)
            elif f_or_e == 2:              # Exercise
                log = input("What exercise did you do?\n")
                final_log = "["+str(getdate())+"] "+log
                print(final_log)
                with open("john_exercise.txt","a") as f:
                    f.write(final_log)
            else:
                print("Invalid Choice")
        elif log_or_retrieve == 2:         # Retrieve the Data
            if f_or_e == 1:                # Food
                with open("john_food.txt","r") as f:
                    a = f.read()
                    print(a)
            elif f_or_e == 2:              # Exercise
                log = input("What exercise did you do?\n")
                final_log = "["+str(getdate())+"] "+log
                print("Logged:",final_log)
                with open("john_exercise.txt","a") as f:
                    f.write(final_log)
            else:
                print("Invalid Choice")
        else:
            print("Invalid Choice")
    ans = int(input("Do you want to Continue?\n1. Yes\n2. No"))
    if ans == 0:
        break
    else:
        continue
