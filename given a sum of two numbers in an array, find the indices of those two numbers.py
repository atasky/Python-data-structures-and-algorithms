# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:10:25 2017

@author: Vaidehee
"""

#given an array of integers, return indices of those two numbers such that they add up to a specific target

#input -
#array = [5,9,12,6,8]
#target - 20
#output -
#array = [2,4]

#input -
#array = [1,9,6,7,2,5]
#target - 7
#output -
#array = 
#[0,2]
#[4,5]

def sums(arr,target,l):
    a=list()
    for i in range(0,l):
        for j in range(i+1,l):
            if(target==(arr[i]+arr[j])):
                a.append(i)
                a.append(j)
                print(a)
                a=list()
    
arr=list()
l=int(input("Enter how many elements"))
print("Enter elements")
for i in range(l):
    element=int(input("element: "))
    arr.append(element)
print("The array is", arr)
target=int(input("Enter the target"))
sums(arr,target,l)
