import csv
from random import randint
from userManagement import *
from user import *
from fish import *
from GUI import *
def goFishing():
    cast=randint(1,6)
    add=user.score
    match cast:
        case 1:
            print(fishTable.bait.name)
            
            user.score+fishTable.bait.pointsKept
            print(user.score)
        case 2:
            print(fishTable.seaweed.name)
            add+fishTable.largeMullet.pointsKept
            print(user.score)
        case 3:
            print(fishTable.undersizedFish.name)
            add+fishTable.largeMullet.pointsKept
            print(user.score)
        case 4:
            print(fishTable.largeMullet.name)
            add+fishTable.largeMullet.pointsKept
            print(user.score)
        case 5:
            print(fishTable.snapper.name)
            add+fishTable.largeMullet.pointsKept
            print(user.score)
        case 6:
            print(fishTable.kingGW.name)
            add+fishTable.largeMullet.pointsKept
            print(user.score)
           
    
if __name__ == "__main__":
    #GUI()
    
    #makeNewCSV()
    userInfoGet()
    
    
    #goFishing()
   