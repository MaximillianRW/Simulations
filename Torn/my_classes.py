from math import log as ln

XAN_CD = 48
ECS_CD = 22
CHOCO_CD = 3
EDVD_CD = 36


#Start Player
class Player:
    def __init__(self,name):
        self.name = name
        self.maxenergy = 150.
        self.energy = self.maxenergy
        self.maxhappy = 5025.
        self.happy = self.maxhappy
        self.maxbooster = 24*6
        self.boostercd = 0
        self.drugcd = 0
        self.strength = 10.
        self.defense = 10.
        self.speed = 10.
        self.dexterity = 10.
        self.totalstats = 40.
        self.gymid = 0
        self.total_gym_e = 0
        self.current_gym_e = 0
        self.stacking = False

    def __str__(self):

        booster_str = ""
        drug_str = ""
        s = ""
        hline = ""
        for i in range(30):
            hline += "-"

        if (self.boostercd != 0):
            bhour = self.boostercd // 6
            bmin = self.boostercd % 6
            bhour_max = self.maxbooster // 6
            bmin_max = self.maxbooster % 6

            booster_str = "Booster CD:  " + str(bhour) + ":" + str(bmin) + "0/" + str(bhour_max) + ":" + str(bmin_max*10) + "0\n"
            
        if (self.drugcd != 0):
            dhour = self.drugcd // 6
            dmin = self.drugcd % 6

            drug_str = "Drug CD:    " + str(dhour) + ":" + str(dmin) + "0\n\n"
        s += "\n" + hline + "\n"
        s += "Player: " + self.name + " [XXXXXXXX] \n\n"
        s += "Energy:      " + str(round(self.energy)) + "/" + str(round(self.maxenergy)) + "\n"
        s += "Happiness:   " + str(round(self.happy)) + "/" + str(round(self.maxhappy)) + "\n\n"
        s += booster_str + drug_str +"\n"
        s += "Strength:    " + f"{round(self.strength,2):,}" + "\n"
        s += "Defense:     " + f"{round(self.defense,2):,}" + "\n"
        s += "Speed:       " + f"{round(self.speed,2):,}" + "\n"
        s += "Dexterity:   " + f"{round(self.dexterity,2):,}" + "\n\n"
        s += "Total Stats: " + f"{round(self.totalstats,2):,}" + "\n"
        s += hline + "\n"
        return s

    def Tick(self):
        if self.energy < self.maxenergy:
            self.energy += 5.
        if self.energy > 1000.:
            self.energy = 1000.
        if self.happy < self.maxhappy:
            self.happy += 10.
        if self.happy > self.maxhappy:
            self.happy = self.maxhappy
        if self.boostercd > 0:
            self.boostercd -= 1
        if self.boostercd < 0:
            self.boostercd = 0
        if self.drugcd > 0:
            self.drugcd -= 1
        if self.drugcd < 0:
            self.drugcd = 0

    def Take_Xanax(self):
        if self.drugcd <= 0:
            self.energy += 250.
            self.happy += 75.
            self.drugcd = XAN_CD

            log_entry = self.name + " used some Xanax gaining 250 energy and 75 happiness.\n"
            
        else:
            log_entry = self.name + " tried to use some Xanax, but needs to wait more " + str(self.drugcd) + "0 minutes.\n"

        return log_entry
        

    def Take_Ecstasy(self):
        if self.drugcd <= 0:
            gained_happy = self.happy
            self.happy += gained_happy
            self.drugcd = ECS_CD

            log_entry = self.name + " used some Ecstasy gaining " + str(gained_happy) + " happiness.\n"
            
        else:
            log_entry = self.name + " tried to use some Ecstasy, but needs to wait more " + str(self.drugcd) + "0 minutes.\n"

        return log_entry

    def Take_Edvd(self):
        if self.boostercd <= self.maxbooster:
            self.happy += 2500.
            self.boostercd += EDVD_CD

            log_entry = self.name + " used some Erotic DVD gaining 2500 happiness.\n"
            
        else:
            log_entry = self.name + " tried to use some Erotic DVD, but needs to wait more " + self.boostercd + "0 minutes.\n"

        return log_entry

    def Take_Lollipop(self):
        if self.boostercd <= self.maxbooster:
            self.happy += 25.
            self.boostercd += CHOCO_CD

            log_entry = self.name + " used some Lollipops gaining 25 happiness.\n"
            
        else:
            log_entry = self.name + " tried to use some Big Chocolate Box, but needs to wait more " + self.boostercd + "0 minutes.\n"

        return log_entry

    def Take_Choco(self):
        if self.boostercd <= self.maxbooster:
            self.happy += 35.
            self.boostercd += CHOCO_CD

            log_entry = self.name + " used some Big Chocolate Box gaining 35 happiness.\n"
            
        else:
            log_entry = self.name + " tried to use some Big Chocolate Box, but needs to wait more " + self.boostercd + "0 minutes.\n"

        return log_entry
        
    

    def Get_Sim_Data(self):
        return [self.name,self.energy,self.happy,self.boostercd,self.drugcd,
                self.gymid,self.current_gym_e,self.total_gym_e] + self.Get_Stats()
    
    def Get_Name(self):
        return self.name

    def Get_MaxEnergy(self):
        return self.maxenergy

    def Get_Energy(self):
        return self.energy

    def Get_MaxHappy(self):
        return self.maxhappy

    def Get_Happy(self):
        return self.happy
    
    def Get_MaxBooster(self):
        return self.maxbooster

    def Get_BoosterCD(self):
        return self.boostercd

    def Get_DrugCD(self):
        return self.drugcd

    def Get_Strength(self):
        return self.strength

    def Get_Defense(self):
        return self.defense

    def Get_Speed(self):
        return self.speed

    def Get_Dexterity(self):
        return self.dexterity

    def Get_TotalStats(self):
        return self.totalstats

    def Get_Stats(self):
        return [self.strength, self.defense, self.speed, self.dexterity, self.totalstats]

    def Get_GymID(self):
        return self.gymid

    def Get_Total_Gym_E(self):
        return self.total_gym_e

    def Get_Current_Gym_E(self):
        return self.current_gym_e

    def isStacking(self):
        return self.stacking
    

    def Set_Name(self,value):
        self.name = value

    def Set_MaxEnergy(self,value):
        self.maxenergy = value

    def Set_Energy(self,value):
        self.energy = value

    def Set_MaxHappy(self,value):
        self.maxhappy = value

    def Set_Happy(self,value):
        self.happy = value

    def Set_MaxBooster(self,value):
        self.maxbooster = value

    def Set_BoosterCD(self,value):
        self.boostercd = value

    def Set_DrugCD(self,value):
        self.drugcd = value

    def Set_Strength(self,value):
        self.strength = value
        self.Set_TotalStats()

    def Set_Defense(self,value):
        self.defense = value
        self.Set_TotalStats()

    def Set_Speed(self,value):
        self.speed = value
        self.Set_TotalStats()

    def Set_Dexterity(self,value):
        self.dexterity = value
        self.Set_TotalStats()

    def Set_TotalStats(self):
        self.totalstats = round(self.strength + self.defense + self.speed + self.dexterity,2)

    def Set_Stats(self,stats=[]):
        if len(stats) >= 4:
            self.Set_Strength(stats[0])
            self.Set_Defense(stats[1])
            self.Set_Speed(stats[2])
            self.Set_Dexterity(stats[3])
            self.Set_TotalStats()
            
    def Set_GymID(self,value):
        self.gymid = value

    def Set_Total_Gym_E(self,value):
        self.total_gym_e = value

    def Set_Current_Gym_E(self,value):
        self.current_gym_e = value

    def Set_Stacking(self,value):
        self.stacking = value
    
    
#End of Player

#Start of Gym
class Gym:

    def __init__(self,Data):
        self.data = Data.copy()
        self.name = Data[0]
        self.cost = Data[1]
        self.ept = Data[2]
        self.gp = Data[3:7]
        self.next = Data[7]
        self.hl = Data[8]


    def _gain_per_train(self,Gym_Stat_Dots,Energy_Per_Train,Happy,Stat_Total,A,B,Perks):
        S = min(Stat_Total,50E6)
        H = Happy
        G = Gym_Stat_Dots
        E = Energy_Per_Train

        Perks_Mod = 1

        for item in Perks:
            Perks_Mod *= (1+item)
        
        return  (S * round(1 + 0.07 * round(ln(1+H/250),4),4) + 8 * H**1.05 +
                 (1-(H/99999)**2) * A + B) * (1/200000) * G * E * Perks_Mod


    def _iterate_trains(self,N,Gym_Stat_Dots,Energy_Per_Train,Happy_Loss,Energy,Happy,Stat_Total,A,B,Perks=[]):
        Total = 0
        for i in range(N):
            if Energy < Energy_Per_Train:
                return Total, Stat_Total, Energy, Happy
            else:
                dS = round(self._gain_per_train(Gym_Stat_Dots,Energy_Per_Train,Happy,Stat_Total,A,B,Perks),4)
                Total += dS
                Stat_Total += dS
                Energy -= Energy_Per_Train
                Happy -= Happy_Loss

        return Total, Stat_Total, Energy, Happy

    def Train_Stat(self,StatID,Player,N=1):
        Stats = ["strength","defense","speed","dexterity"]
        A = [1600,2100,1600,1800]
        B = [1700,-600,2000,1500]

        Energy = Player.Get_Energy()
        Happy = Player.Get_Happy()
        Stats_Total = Player.Get_Stats()

        result = ""

        if Energy >= N*self.ept:
            Total, New_Stat, New_Energy, New_Happy = self._iterate_trains(N,self.gp[StatID],self.ept,self.hl,
                                                                          Energy,Happy,Stats_Total[StatID],A[StatID],B[StatID])
            dE = Energy - New_Energy
            
            Stats_Total[StatID] = round(New_Stat,2)

            Player.Set_Stats(Stats_Total)
            Player.Set_Energy(round(New_Energy))
            Player.Set_Happy(round(New_Happy))
            Player.Set_Current_Gym_E(round(Player.Get_Current_Gym_E() + dE))
            Player.Set_Total_Gym_E(round(Player.Get_Total_Gym_E() + dE))

            result += Player.Get_Name() + " used " + str(round(dE)) + " energy and " + str(round(Happy-New_Happy)) + " happiness "
            result += "training their " + Stats[StatID] + " " + str(N) + " times in " + self.name
            result += " increasing it by " + f"{round(Total,2):,}" + " to " + f"{round(New_Stat,2):,}" + "\n"

            #You used 150 energy and 77 happiness training your dexterity 15 times in Cha Chas increasing it by 135,383.29 to 18,642,119.09

        return result

    def Train_Max(self,Player):
        if Player.Get_Energy() >= self.ept:
            N = int(Player.Get_Energy() // self.ept)
            StatID = self.gp.index(max(self.gp))
            
            return self.Train_Stat(StatID,Player,N)

    def Get_Data(self):
        return self.data.copy()

    def Get_Name(self):
        return self.name

    def Get_Cost(self):
        return self.cost

    def Get_Next_Gym_E(self):
        return self.next

    def Get_Gym_Dots(self):
        return self.gp.copy()
#End of Gym
