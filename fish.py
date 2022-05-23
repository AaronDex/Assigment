class fishableItem:
    def __init__(self,name,keeper,fish,pointsKept,pointsReleased):
        self.name= name
        self.keeper = keeper
        self.fish = fish
        self.pointsKept = pointsKept
        self.pointsReleased =pointsReleased
class fishTable:
    kingGW=fishableItem("King George Whiting",True,True,50,70)
    bait=fishableItem("Bait",False,False,-10,0)
    undersizedFish=fishableItem("Undersized Fish",False,True,-10,0)
    snapper=fishableItem("Snapper",True,True,30,40)
    largeMullet=fishableItem("Large Mullet",True,True,20,20)
    seaweed=fishableItem("Seaweed",True,False,5,-5)