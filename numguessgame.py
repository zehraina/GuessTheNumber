# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:09:49 2022

@author: Ina Zehra
"""
import random

import pandas as pd
n=random.randint(1,100)
list1=["Scoreboard","Player name"]

database=[]
name=input("Enter your name as player: ")

print("This goes as follows:")
print("You are supposed to guess the number that this computer generates. ")
ch=0
c=None
hint=input("Do you want hints? (recommended because nobody can beat the computer! [y/n]")
    

try:
    if hint=="y" or hint=="Y" or hint=="Yes" or hint=="YES":
        while(n!=c):
            try:
                c=int(input("your guess?"))
                ch=ch+1
                if c>n:
                    print("Lower guess please")
                elif c<n:
                    print("Higher guess please")
                else:
                    print("Guessed it right!\nnumber of tries:", ch)
            except ValueError:
                print("Enter a valid input!")
    if hint=="n" or hint=="N" or hint=="No" or hint=="NO":
        while(n!=c):
            try:
                c=int(input("your guess?"))
                ch=ch+1
                if c!=n:
                    print("Uh-oh! Try again.")
                
                else:
                    print("Guessed it right!\nnumber of tries:", ch)
            except ValueError:
                print("Enter a valid input!")
except ValueError:
    print("You have to enter either yes or no")
    
database.append(ch)
database.append(name)

table=pd.DataFrame([database], columns=list1)
table.to_csv("player_data.csv", mode='a')
t=input("Want to have a look at the scoreboard? [y/n]")
if t=="y" or t=="Y" or t=="Yes" or t=="YES":
    
    print(table)
else:
    print("Thanks for playing!")
    