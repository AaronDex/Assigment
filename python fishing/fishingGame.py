class fishableItem:
    def __init__(self,keeper,fish,pointsKept,pointsReleased):
        self.keeper = keeper
        self.fish = fish
        self.pointsKept= pointsKept
        self.pointsReleased =pointsReleased
kingGW=fishableItem(True,True,50,70)
bait=fishableItem(False,False,-10,0)
undersizedFish=fishableItem(False,True,-10,0)
print("kingGW")
