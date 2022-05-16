
from random import randint
class fishableItem:
    def __init__(self,name,keeper,fish,pointsKept,pointsReleased):
        self.name= name
        self.keeper = keeper
        self.fish = fish
        self.pointsKept = pointsKept
        self.pointsReleased =pointsReleased
class user:
    def __init__(self,userName,password,score):
        self.userName=userName
        self.password=password
        self.score=score 
class fishTable:
    kingGW=fishableItem("King George Whiting",True,True,50,70)
    bait=fishableItem("Bait",False,False,-10,0)
    undersizedFish=fishableItem("Undersized Fish",False,True,-10,0)
    snapper=fishableItem("Snapper",True,True,30,40)
    largeMullet=fishableItem("Large Mullet",True,True,20,20)
    seaweed=fishableItem("Seaweed",True,False,5,-5)
def userInfoGet():
    accountStatus=input("Do You Have a Account? Y/N ")
    try:
        file = open("demofile.txt","x")
    except:
        if accountStatus=="N":
            userDetails=user(input("Please Enter a Username "),input(("Please Enter a Password ")),0)
            file = open("demofile.txt","a")
            file.write(userDetails.userName+" "+userDetails.password+" "+"0"+"\n")
            file.close()
        else:
            while True:
                userDetails=user(input("Please Enter Your Username "),input(("Please Enter Your Password ")),0)
                with open("demofile.txt", "r") as file:
                        lines=file.readlines()
                        
                        if userDetails.userName==lines[0] and userDetails.password==lines[1]:
                            return False
                            update=user(loginDetails[0],loginDetails[1],loginDetails[2])
                            #update=user(loginDetails[0],loginDetails[1],loginDetails[2])
                            #print("Welcome Back: "+userDetails.userName+" Your Score Is "+user.score)
                            return False
                
def goFishing():
    cast=randint(1,6)
    match cast:
        case 1:
            print(fishTable.kingGW.name)
        case 2:
            print(fishTable.kingGW.name)
        case 3:
            print(fishTable.kingGW.name)
        case 4:
            print(fishTable.kingGW.name)
        case 5:
            print(fishTable.kingGW.name)
        case 6:
            print(fishTable.kingGW.name)
userInfoGet()
goFishing()