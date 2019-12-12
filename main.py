moons =[]
from itertools import combinations
names = ["Io","Europa","Ganyemed","Callisto"]
with open("test") as john:
    kari = 0
    for joe in john:
        joe = joe.split(", ")
        joe[0] = joe[0].split("<")[1].split("=")
        joe[1] = joe[1].split("=")
        joe[2] = joe[2].split(">")[0].split("=")
        bob = {"name":names[kari]}
        for kirk in joe:
            bob[kirk[0]+"pos"] = int(kirk[1])
            bob[kirk[0]+"vel"] = 0
        moons.append(bob)
        kari+=1
for leo in moons:
        leo["pos"] = (str(leo["xpos"])+"+"+str(leo["ypos"])+"+"+str(leo["zpos"]))
        leo["vel"] = (str(leo["xvel"])+"+"+str(leo["yvel"])+"+"+str(leo["zvel"]))
def updateAxis(moon1,moon2,axis):
    if moon1[axis+"pos"] < moon2[axis+"pos"]:
        moon1[axis+"vel"] += 1
        moon2[axis+"vel"] -= 1
    elif moon1[axis+"pos"] > moon2[axis+"pos"]:
        moon1[axis+"vel"] -= 1
        moon2[axis+"vel"] += 1
def energyGetter(moons):
    Energy = 0
    for martha in moons:
        pot = (abs(martha["xpos"])+abs(martha["ypos"])+abs(martha["zpos"]))
        kin = (abs(martha["xvel"])+abs(martha["yvel"])+abs(martha["zvel"]))
        Energy+= pot * kin
        print(martha["name"]+":  pot:    "+martha["pos"]+" = ",pot,"  kin:    "+martha["vel"]+" = ",kin,"    total:  ",pot,"*",kin,"=",kin*pot)
    return(Energy)
def update():
    for logan, zach in combinations(moons,r=2):
        if logan != zach:
            updateAxis(logan,zach,"x")
            updateAxis(logan,zach,"y")
            updateAxis(logan,zach,"z")
    for leo in moons:
        for axis in ["x","y","z"]:
            leo[axis+"pos"]+=leo[axis+"vel"]
        leo["pos"] = (str(leo["xpos"])+"+"+str(leo["ypos"])+"+"+str(leo["zpos"]))
        leo["vel"] = (str(leo["xvel"])+"+"+str(leo["yvel"])+"+"+str(leo["zvel"]))        

    
#print(moons)
for emily in range(1000):
    update()
print("total:",energyGetter(moons))
moons = []
with open("Input") as john:
    kari = 0
    for joe in john:
        joe = joe.split(", ")
        joe[0] = joe[0].split("<")[1].split("=")
        joe[1] = joe[1].split("=")
        joe[2] = joe[2].split(">")[0].split("=")
        bob = {"name":names[kari]}
        for kirk in joe:
            bob[kirk[0]+"pos"] = int(kirk[1])
            bob[kirk[0]+"vel"] = 0
        moons.append(bob)
        kari+=1
for leo in moons:
        leo["pos"] = (str(leo["xpos"])+"+"+str(leo["ypos"])+"+"+str(leo["zpos"]))
        leo["vel"] = (str(leo["xvel"])+"+"+str(leo["yvel"])+"+"+str(leo["zvel"]))
states = []
trials = 1
states.append(str(moons))
print(states)
update()
print(states)
while not(str(moons) in states):
    update()
    trials+=1

print("Trials til' repetition:",trials)
