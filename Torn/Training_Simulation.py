import pandas as pd
from math import log as ln
from my_classes import Player,Gym

Gym_Data = [
["Premier Fitness",10,5,2.0,2.0,2.0,2.0,200,2.67],
["Average Joes",100,5,2.4,2.7,2.4,2.4,500,2.67],
["Woody's Workout",250,5,2.7,3.0,3.2,2.7,1000,2.67],
["Beach Bods",500,5,3.2,3.2,3.2,0,2000,2.67],
["Silver Gym",1000,5,3.4,3.4,3.6,3.2,2750,2.67],
["Pour Femme",2500,5,3.4,3.6,3.6,3.8,3000,2.67],
["Davies Den",5000,5,3.7,3.7,0,3.7,3500,2.67],
["Global Gym",10000,5,4.0,4.0,4.0,4.0,4000,2.67],
["Knuckle Heads",50000,10,4.8,4.0,4.4,4.2,6000,5.],
["Pioneer Fitness",100000,10,4.4,4.8,4.6,4.4,7000,5.],
["Anabolic Anomalies",250000,10,5.0,5.2,4.6,4.6,8000,5.],
["Core",500000,10,5.0,5.0,5.2,5.0,11000,5.],
["Racing Fitness",1000000,10,5.4,5.0,4.8,5.2,12420,5.],
["Complete Cardio",2000000,10,5.5,5.5,5.7,5.2,18000,5.],
["Legs Bums and Tums",3000000,10,5.5,0,5.5,5.7,18100,5.],
["Deep Burn",5000000,10,6.0,6.0,6.0,6.0,24140,5.],
["Apollo Gym",7500000,10,6.0,6.4,6.2,6.2,31260,5.],
["Gun Shop",10000000,10,6.5,6.2,6.4,6.2,36610,5.],
["Force Training",15000000,10,6.5,6.4,6.4,6.8,46640,5.],
["Cha Cha's",20000000,10,6.4,6.6,6.4,7.0,56520,5.],
["Atlas",30000000,10,7.0,6.4,6.4,6.5,67775,5.],
["Last Round",50000000,10,6.8,7.0,6.5,6.5,84535,5.],
["The Edge",75000000,10,6.8,7.0,7.0,6.8,106305,5.],
["George's",100000000,10,7.3,7.3,7.3,7.3,-1,5.],
]

GYM = []
for data in Gym_Data:
    new_gym = Gym(data)
    GYM.append(new_gym)

XAN_CD = 48
ECS_CD = 22
CHOCO_CD = 3
EDVD_CD = 36
JUMP_STOP = 400000.
JUMP_STOP_1 = 200000.
JUMP_STOP_2 = 600000.
JUMP_STOP_3 = 800000.



def Get_Time():
    return '[Day '+str(Day)+' '+str(Hour)+':'+str(Tick)+'0] '

def Update(event):
    global log
    n = 0
    if type(event) is list:
        for item in event:
            log.append(Get_Time() + item)
            n+=1
    else:
        log.append(Get_Time() + event)
        n+=1
    return n

def Train(player):
    n = 0
    use_gym = GYM[player.Get_GymID()]
    n += Update(use_gym.Train_Max(player))
    to_next_gym = use_gym.Get_Next_Gym_E()
    while to_next_gym >= 0 and player.Get_Current_Gym_E() >= to_next_gym:
        n += Update(Change_Gym(player,to_next_gym))
    return n
    

def Change_Gym(Player,next_gym_e):
    Player.Set_Current_Gym_E(Player.Get_Current_Gym_E()-next_gym_e)
    Player.Set_GymID(Player.Get_GymID()+1)
    new_gym = GYM[Player.Get_GymID()]
    s = [Player.Get_Name() + " purchased a gym membership to " + new_gym.Get_Name() + f" for ${new_gym.Get_Cost():,}\n"]
    s += [Player.Get_Name() + " switched your active gym to " + new_gym.Get_Name() + "\n"]
    return s

    


def Jack_Turn():
    log_change = 0
    if Jack.Get_DrugCD() <= 0:
        log_change += Update(Jack.Take_Xanax())
    if Jack.Get_Energy() >= Jack.Get_MaxEnergy():
        log_change += Train(Jack)
    return log_change


def Barrel_Turn():
    log_change = 0
    if Barrel.Get_DrugCD() <= 0:
        log_change += Update(Barrel.Take_Xanax())
    if Barrel.Get_Energy() >= Barrel.Get_MaxEnergy():
        while Barrel.Get_BoosterCD() <= Barrel.Get_MaxBooster():
            log_change += Update(Barrel.Take_Edvd())
        log_change += Train(Barrel)
    return log_change


def Sally_Turn():
    log_change = 0
    if Sally.Get_Energy() >= Sally.Get_MaxEnergy():
        if Sally.Get_DrugCD() <= 0:
            cgd = GYM[Sally.Get_GymID()].Get_Gym_Dots()
            if Sally.Get_BoosterCD() <= 0 and Sally.Get_Stats()[cgd.index(max(cgd))] < JUMP_STOP:
                while Sally.Get_BoosterCD() <= Sally.Get_MaxBooster():
                    log_change += Update(Sally.Take_Lollipop())
                log_change += Update(Sally.Take_Ecstasy())
                log_change += Train(Sally)
            else:
                log_change += Update(Sally.Take_Xanax())
                log_change += Train(Sally)
        else:
            log_change += Train(Sally)
            
    return log_change

def Sally_C1_Turn():
    log_change = 0
    if Sally_C1.Get_Energy() >= Sally_C1.Get_MaxEnergy():
        if Sally_C1.Get_DrugCD() <= 0:
            cgd = GYM[Sally_C1.Get_GymID()].Get_Gym_Dots()
            if Sally_C1.Get_BoosterCD() <= 0 and Sally_C1.Get_Stats()[cgd.index(max(cgd))] < JUMP_STOP_1:
                while Sally_C1.Get_BoosterCD() <= Sally_C1.Get_MaxBooster():
                    log_change += Update(Sally_C1.Take_Lollipop())
                log_change += Update(Sally_C1.Take_Ecstasy())
                log_change += Train(Sally_C1)
            else:
                log_change += Update(Sally_C1.Take_Xanax())
                log_change += Train(Sally_C1)
        else:
            log_change += Train(Sally_C1)
            
    return log_change


def Sally_C2_Turn():
    log_change = 0
    if Sally_C2.Get_Energy() >= Sally_C2.Get_MaxEnergy():
        if Sally_C2.Get_DrugCD() <= 0:
            cgd = GYM[Sally_C2.Get_GymID()].Get_Gym_Dots()
            if Sally_C2.Get_BoosterCD() <= 0 and Sally_C2.Get_Stats()[cgd.index(max(cgd))] < JUMP_STOP_2:
                while Sally_C2.Get_BoosterCD() <= Sally_C2.Get_MaxBooster():
                    log_change += Update(Sally_C2.Take_Lollipop())
                log_change += Update(Sally_C2.Take_Ecstasy())
                log_change += Train(Sally_C2)
            else:
                log_change += Update(Sally_C2.Take_Xanax())
                log_change += Train(Sally_C2)
        else:
            log_change += Train(Sally_C2)
            
    return log_change


def Sally_C3_Turn():
    log_change = 0
    if Sally_C3.Get_Energy() >= Sally_C3.Get_MaxEnergy():
        if Sally_C3.Get_DrugCD() <= 0:
            cgd = GYM[Sally_C3.Get_GymID()].Get_Gym_Dots()
            if Sally_C3.Get_BoosterCD() <= 0 and Sally_C3.Get_Stats()[cgd.index(max(cgd))] < JUMP_STOP_3:
                while Sally_C3.Get_BoosterCD() <= Sally_C3.Get_MaxBooster():
                    log_change += Update(Sally_C3.Take_Lollipop())
                log_change += Update(Sally_C3.Take_Ecstasy())
                log_change += Train(Sally_C3)
            else:
                log_change += Update(Sally_C3.Take_Xanax())
                log_change += Train(Sally_C3)
        else:
            log_change += Train(Sally_C3)
            
    return log_change



def Oogie_Turn():
    log_change = 0
    if Oogie.isStacking():
        if Oogie.Get_DrugCD() <= 0:
            if Oogie.Get_Energy() >= 1000.:
                if Oogie.Get_BoosterCD() <= 0:
                    while Oogie.Get_BoosterCD() <= Oogie.Get_MaxBooster():
                        log_change += Update(Oogie.Take_Choco())
                    log_change += Update(Oogie.Take_Ecstasy())
                    log_change += Train(Oogie)
                    Oogie.Set_Stacking(False)
            else:
                log_change += Update(Oogie.Take_Xanax())
    elif Oogie.Get_DrugCD() <= 0:
        log_change += Train(Oogie)
        cgd = GYM[Oogie.Get_GymID()].Get_Gym_Dots()
        if Oogie.Get_BoosterCD() <= 4*XAN_CD and Oogie.Get_Stats()[cgd.index(max(cgd))] < JUMP_STOP:
            log_change += Update(Oogie.Take_Xanax())
            Oogie.Set_Stacking(True)
        else:
            log_change += Update(Oogie.Take_Xanax())
            log_change += Train(Oogie)
    elif Oogie.Get_Energy() >= Oogie.Get_MaxEnergy():
            log_change += Train(Oogie)
    return log_change


def Oogie_C1_Turn():
    log_change = 0
    if Oogie_C1.isStacking():
        if Oogie_C1.Get_DrugCD() <= 0:
            if Oogie_C1.Get_Energy() >= 1000.:
                if Oogie_C1.Get_BoosterCD() <= 0:
                    while Oogie_C1.Get_BoosterCD() <= Oogie_C1.Get_MaxBooster():
                        log_change += Update(Oogie_C1.Take_Choco())
                    log_change += Update(Oogie_C1.Take_Ecstasy())
                    log_change += Train(Oogie_C1)
                    Oogie_C1.Set_Stacking(False)
            else:
                log_change += Update(Oogie_C1.Take_Xanax())
    elif Oogie_C1.Get_DrugCD() <= 0:
        log_change += Train(Oogie_C1)
        cgd = GYM[Oogie_C1.Get_GymID()].Get_Gym_Dots()
        if Oogie_C1.Get_BoosterCD() <= 4*XAN_CD and Oogie_C1.Get_Stats()[cgd.index(max(cgd))] < JUMP_STOP_1:
            log_change += Update(Oogie_C1.Take_Xanax())
            Oogie_C1.Set_Stacking(True)
        else:
            log_change += Update(Oogie_C1.Take_Xanax())
            log_change += Train(Oogie_C1)
    elif Oogie_C1.Get_Energy() >= Oogie_C1.Get_MaxEnergy():
            log_change += Train(Oogie_C1)
    return log_change


def Oogie_C2_Turn():
    log_change = 0
    if Oogie_C2.isStacking():
        if Oogie_C2.Get_DrugCD() <= 0:
            if Oogie_C2.Get_Energy() >= 1000.:
                if Oogie_C2.Get_BoosterCD() <= 0:
                    while Oogie_C2.Get_BoosterCD() <= Oogie_C2.Get_MaxBooster():
                        log_change += Update(Oogie_C2.Take_Choco())
                    log_change += Update(Oogie_C2.Take_Ecstasy())
                    log_change += Train(Oogie_C2)
                    Oogie_C2.Set_Stacking(False)
            else:
                log_change += Update(Oogie_C2.Take_Xanax())
    elif Oogie_C2.Get_DrugCD() <= 0:
        log_change += Train(Oogie_C2)
        cgd = GYM[Oogie_C2.Get_GymID()].Get_Gym_Dots()
        if Oogie_C2.Get_BoosterCD() <= 4*XAN_CD and Oogie_C2.Get_Stats()[cgd.index(max(cgd))] < JUMP_STOP_2:
            log_change += Update(Oogie_C2.Take_Xanax())
            Oogie_C2.Set_Stacking(True)
        else:
            log_change += Update(Oogie_C2.Take_Xanax())
            log_change += Train(Oogie_C2)
    elif Oogie_C2.Get_Energy() >= Oogie_C2.Get_MaxEnergy():
            log_change += Train(Oogie_C2)
    return log_change


def Oogie_C3_Turn():
    log_change = 0
    if Oogie_C3.isStacking():
        if Oogie_C3.Get_DrugCD() <= 0:
            if Oogie_C3.Get_Energy() >= 1000.:
                if Oogie_C3.Get_BoosterCD() <= 0:
                    while Oogie_C3.Get_BoosterCD() <= Oogie_C3.Get_MaxBooster():
                        log_change += Update(Oogie_C3.Take_Choco())
                    log_change += Update(Oogie_C3.Take_Ecstasy())
                    log_change += Train(Oogie_C3)
                    Oogie_C3.Set_Stacking(False)
            else:
                log_change += Update(Oogie_C3.Take_Xanax())
    elif Oogie_C3.Get_DrugCD() <= 0:
        log_change += Train(Oogie_C3)
        cgd = GYM[Oogie_C3.Get_GymID()].Get_Gym_Dots()
        if Oogie_C3.Get_BoosterCD() <= 4*XAN_CD and Oogie_C3.Get_Stats()[cgd.index(max(cgd))] < JUMP_STOP_3:
            log_change += Update(Oogie_C3.Take_Xanax())
            Oogie_C3.Set_Stacking(True)
        else:
            log_change += Update(Oogie_C3.Take_Xanax())
            log_change += Train(Oogie_C3)
    elif Oogie_C3.Get_Energy() >= Oogie_C3.Get_MaxEnergy():
            log_change += Train(Oogie_C3)
    return log_change


def Flink_Turn():
    log_change = 0
    if Flink.isStacking():
        if Flink.Get_DrugCD() <= 0:
            if Flink.Get_Energy() >= 1000.:
                if Flink.Get_BoosterCD() <= 0:
                    while Flink.Get_BoosterCD() <= Flink.Get_MaxBooster():
                        log_change += Update(Flink.Take_Edvd())
                    log_change += Update(Flink.Take_Ecstasy())
                    log_change += Train(Flink)
                    Flink.Set_Stacking(False)
            else:
                log_change += Update(Flink.Take_Xanax())
    elif Flink.Get_DrugCD() <= 0:
        log_change += Train(Flink)
        cgd = GYM[Flink.Get_GymID()].Get_Gym_Dots()
        if Flink.Get_BoosterCD() <= 4*XAN_CD and Flink.Get_Stats()[cgd.index(max(cgd))] < JUMP_STOP:
            log_change += Update(Flink.Take_Xanax())
            Flink.Set_Stacking(True)
        else:
            log_change += Update(Flink.Take_Xanax())
            log_change += Train(Flink)
    elif Flink.Get_Energy() >= Flink.Get_MaxEnergy():
            log_change += Train(Flink)
    return log_change


def Flink_C1_Turn():
    log_change = 0
    if Flink_C1.isStacking():
        if Flink_C1.Get_DrugCD() <= 0:
            if Flink_C1.Get_Energy() >= 1000.:
                if Flink_C1.Get_BoosterCD() <= 0:
                    while Flink_C1.Get_BoosterCD() <= Flink_C1.Get_MaxBooster():
                        log_change += Update(Flink_C1.Take_Edvd())
                    log_change += Update(Flink_C1.Take_Ecstasy())
                    log_change += Train(Flink_C1)
                    Flink_C1.Set_Stacking(False)
            else:
                log_change += Update(Flink_C1.Take_Xanax())
    elif Flink_C1.Get_DrugCD() <= 0:
        log_change += Train(Flink_C1)
        cgd = GYM[Flink_C1.Get_GymID()].Get_Gym_Dots()
        if Flink_C1.Get_BoosterCD() <= 4*XAN_CD and Flink_C1.Get_Stats()[cgd.index(max(cgd))] < JUMP_STOP_1:
            log_change += Update(Flink_C1.Take_Xanax())
            Flink_C1.Set_Stacking(True)
        else:
            log_change += Update(Flink_C1.Take_Xanax())
            log_change += Train(Flink_C1)
    elif Flink_C1.Get_Energy() >= Flink_C1.Get_MaxEnergy():
            log_change += Train(Flink_C1)
    return log_change


def Flink_C2_Turn():
    log_change = 0
    if Flink_C2.isStacking():
        if Flink_C2.Get_DrugCD() <= 0:
            if Flink_C2.Get_Energy() >= 1000.:
                if Flink_C2.Get_BoosterCD() <= 0:
                    while Flink_C2.Get_BoosterCD() <= Flink_C2.Get_MaxBooster():
                        log_change += Update(Flink_C2.Take_Edvd())
                    log_change += Update(Flink_C2.Take_Ecstasy())
                    log_change += Train(Flink_C2)
                    Flink_C2.Set_Stacking(False)
            else:
                log_change += Update(Flink_C2.Take_Xanax())
    elif Flink_C2.Get_DrugCD() <= 0:
        log_change += Train(Flink_C2)
        cgd = GYM[Flink_C2.Get_GymID()].Get_Gym_Dots()
        if Flink_C2.Get_BoosterCD() <= 4*XAN_CD and Flink_C2.Get_Stats()[cgd.index(max(cgd))] < JUMP_STOP_2:
            log_change += Update(Flink_C2.Take_Xanax())
            Flink_C2.Set_Stacking(True)
        else:
            log_change += Update(Flink_C2.Take_Xanax())
            log_change += Train(Flink_C2)
    elif Flink_C2.Get_Energy() >= Flink_C2.Get_MaxEnergy():
            log_change += Train(Flink_C2)
    return log_change


def Flink_C3_Turn():
    log_change = 0
    if Flink_C3.isStacking():
        if Flink_C3.Get_DrugCD() <= 0:
            if Flink_C3.Get_Energy() >= 1000.:
                if Flink_C3.Get_BoosterCD() <= 0:
                    while Flink_C3.Get_BoosterCD() <= Flink_C3.Get_MaxBooster():
                        log_change += Update(Flink_C3.Take_Edvd())
                    log_change += Update(Flink_C3.Take_Ecstasy())
                    log_change += Train(Flink_C3)
                    Flink_C3.Set_Stacking(False)
            else:
                log_change += Update(Flink_C3.Take_Xanax())
    elif Flink_C3.Get_DrugCD() <= 0:
        log_change += Train(Flink_C3)
        cgd = GYM[Flink_C3.Get_GymID()].Get_Gym_Dots()
        if Flink_C3.Get_BoosterCD() <= 4*XAN_CD and Flink_C3.Get_Stats()[cgd.index(max(cgd))] < JUMP_STOP_3:
            log_change += Update(Flink_C3.Take_Xanax())
            Flink_C3.Set_Stacking(True)
        else:
            log_change += Update(Flink_C3.Take_Xanax())
            log_change += Train(Flink_C3)
    elif Flink_C3.Get_Energy() >= Flink_C3.Get_MaxEnergy():
            log_change += Train(Flink_C3)
    return log_change
             
                

    

log = []


sim_data = {
            "Day":[],
            "Hour":[],
            "Tick":[],
            "Player":[],
            "Energy":[],
            "Happiness":[],
            "Booster_CD":[],
            "Drug_CD":[],
            "Gym_ID":[],
            "Current_Gym_E":[],
            "Total_Gym_E":[],
            "Strength":[],
            "Speed":[],
            "Defense":[],
            "Dexterity":[],
            "Total_Stats":[]
        }

def Collect_Data(players):
    global sim_data
    keys = list(sim_data.keys())
    
    if type(players) is list:
        for player in players:
            data = [Day,Hour,Tick] + player.Get_Sim_Data()
            for i in range(len(keys)):
                sim_data[keys[i]].append(data[i])     
    else:
        data = [Day,Hour,Tick] + player.Get_Sim_Data()
        for i in range(len(keys)):
            sim_data[keys[i]].append(data[i])


Jack = Player("Jack")
Sally = Player("Sally")
Sally_C1 = Player("Sally_Clone1")
Sally_C2 = Player("Sally_Clone2")
Sally_C3 = Player("Sally_Clone3")
Barrel = Player("The_Barrel")
Oogie = Player("Oogie")
Oogie_C1 = Player("Oogie_Clone1")
Oogie_C2 = Player("Oogie_Clone2")
Oogie_C3 = Player("Oogie_Clone3")
Flink = Player("Dr_Flinkestein")
Flink_C1 = Player("Dr_Flinkestein_Clone1")
Flink_C2 = Player("Dr_Flinkestein_Clone2")
Flink_C3 = Player("Dr_Flinkestein_Clone3")


Players = [Jack,Barrel,Sally,Sally_C1,Sally_C2,Sally_C3,Oogie,Oogie_C1,Oogie_C2,Oogie_C3,Flink,Flink_C1,Flink_C2,Flink_C3]

for Day in range(361):
    for Hour in range(24):
        for Tick in range(6):
            if Day == 360 and (Hour > 0 or Tick > 0):
                break
            
            Collect_Data(Players)

            if Day == 360:
                break

            if Jack_Turn() > 0:
                log.append('\n')

            if Barrel_Turn() > 0:
                log.append('\n')

            if Sally_Turn() > 0:
                log.append('\n')

            if Sally_C1_Turn() > 0:
                log.append('\n')

            if Sally_C2_Turn() > 0:
                log.append('\n')

            if Sally_C3_Turn() > 0:
                log.append('\n')

            if Oogie_Turn() > 0:
                log.append('\n')

            if Oogie_C1_Turn() > 0:
                log.append('\n')

            if Oogie_C2_Turn() > 0:
                log.append('\n')

            if Oogie_C3_Turn() > 0:
                log.append('\n')

            if Flink_Turn() > 0:
                log.append('\n')

            if Flink_C1_Turn() > 0:
                log.append('\n')

            if Flink_C2_Turn() > 0:
                log.append('\n')

            if Flink_C3_Turn() > 0:
                log.append('\n')
            
            for player in Players:
                player.Tick()

    log.append('\n')

for player in Players:
    print(player)


Simulation_Data = pd.DataFrame(sim_data).set_index(["Day","Hour","Tick","Player"])

Simulation_Data.to_csv('Out\Simulation_Data.txt')

Log_File = open('Out\Simulation_Log.txt','w')
Log_File.writelines(log)
Log_File.close()

    
