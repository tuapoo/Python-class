# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:02:15 2022

@author: tuapoo
"""

A=int(input('How many stick in the pile :\n'))
print("There are ",A,"stick in the pile" )
B=input("whats your name :\n" )
print("My name is : " , B)
i=1

while A<=3 :
  print(B,", how many stick you will take : ")
  C=int(input())
  A=A-C
  if A==1 and i==1 :
    print("there are  1 stick in the pile")
    i=i+1
  elif A==2 and i ==1:
     print("there are  2 stick in the pile")
     i=i+1
  elif A==1 and i ==2:
     print("there are  1 stick in the pile")
     i=i+1
  elif i==3 :
    print("Ok there is no stick in the pile . You spend 2 times")
    break
  elif A ==4 and i==1 :
     print("No you cant take more less than 1 stick")
     A=3
  elif A==-1 and i==2 :
    print("There are no enough sticks to take")
    break
  elif A==0 and i==2 :
     print("there are no stick left in the pile")
     break
  elif A==0 and i==1 :
    print("you can not take more than 2 sticks!")
    A=A+C

