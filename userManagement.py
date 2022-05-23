import csv

from  user import *
filename = "users.csv"
def makeNewCSV():
    fields = ["Username", "Password", "Score"]
    try:
        with open(filename, "x", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fields)
    except:
        pass
def userInfoGet():
    while True:
        accountStatus = input("Do You Have a Account? Y/N ")
        if accountStatus == "N" or accountStatus == "n":
            userDetails = user(
                input("Please Enter a Username "),
                input(("Please Enter a Password ")),
                0,
            )
            with open(filename, "a", newline="") as csvfile:

                rows = [userDetails.userName, userDetails.password, userDetails.score]
                writer = csv.writer(csvfile)
                writer.writerow(rows)
                return False
        elif accountStatus == "Y" or accountStatus == "y":
            while True:
                user.userName = input("Please Enter Your Username ")
                user.password = input(("Please Enter Your Password "))
                usernames=[]
                passwords=[]
                
                with open(filename, "r") as csvfile:
                    csvreader = csv.reader(csvfile)
                    for row in csvreader:
                        usernames.append(row[0])
                        passwords.append(row[1])
                    if user.userName==usernames and user.password == passwords:
                            user.userName=row[0]
                            user.password=row[1]
                            user.score=int(row[2])
                            print("Welcome Back "+user.userName+"!"" You Currently Have: "+str(user.score)+" Points")
                            return False
                       
        else:
            print("Please Select a Valid Option")
