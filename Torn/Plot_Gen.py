import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

Players = ["Jack","Sally_Clone1","The_Barrel","Oogie_Clone1","Oogie_Clone2","Dr_Flinkestein_Clone1"]

#Players = ["Sally","Sally_Clone1","Sally_Clone2","Sally_Clone3"]

#Players = ["Oogie","Oogie_Clone1","Oogie_Clone2","Oogie_Clone3"]

#Players = ["Dr_Flinkestein","Dr_Flinkestein_Clone1","Dr_Flinkestein_Clone2","Dr_Flinkestein_Clone3"]

Simulation_Data = pd.read_csv('Out\Simulation_Data.txt')

def plot_months(column,name,save):
    for i in range(12):
        fig, ax = plt.subplots()
        d0 = i*30
        df = (i+1)*30

        for player in Players:
            Player_Data = Simulation_Data.query("Player == @player and Hour == 0 and Tick == 0 and Day >= @d0 and Day <= @df")
            ax.plot(Player_Data.Day,Player_Data[column], label=player)

        ax.set_xlabel("Days")
        ax.set_ylabel(name)
        ax.set_title(name + " - Month " + str(i+1))
        ax.legend()
        ax.grid(True)
        fig.savefig("Plots\Plot_"+save+"_Month_"+str(i+1))
        plt.close()

def plot_year(column,name,save):
    fig, ax = plt.subplots()

    for player in Players:
        Player_Data = Simulation_Data.query("Player == @player and Hour == 0 and Tick == 0")
        ax.plot(Player_Data.Day,Player_Data[column], label=player)

    ax.set_xlabel("Days")
    ax.set_ylabel(name)
    ax.set_title(name + " - All Time")
    ax.legend()
    ax.grid(True)
    fig.savefig("Plots\Plot_"+save)
    plt.close()

Column = ["Total_Stats","Total_Gym_E","Gym_ID"]
Name = ["Total Stats","Total Gym Energy","Gym Level"]
Save = ["TotalStats","GymEnergy","GymLevel"]

for i in range(len(Column)):
    plot_months(Column[i],Name[i],Save[i])
    plot_year(Column[i],Name[i],Save[i])

