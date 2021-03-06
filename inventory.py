''' Inventory application for used car lot. Keeps track of inventory and allows the user to search for a certain car type.
    Authors: Dylan, Lukas, Tran, Jonathan
    Last edited: 7/9/22
'''
from tkinter import *
import random
import csv

# used car class
class UsedCar:
    def __init__(self, id=None, make=None, model=None, color=None, year=None):
        self.id = id
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    # print out a cars attributes
    def __str__(self):
        return f'Car Info: {self.make} {self.model} {self.color} {self.year}'

    # save to file
    def save_to_file(self):
        car_info = [self.id, self.make, self.model, self.color, self.year]
        used_car_file = open('UsedCar.txt', 'r+')
        if used_car_file.readline() is None:
            used_car_file.write("\n")
        for i in car_info:
            used_car_file.write("%s\t" % i)
        used_car_file.write("\n")
        used_car_file.close()
        print("Successfully add to the inventory.")
        
        ## Write to CSV File
        headers = ['id', 'make', 'model', 'color', 'year']
        car_info = {'id':self.id, 'make':self.make, 'model':self.model, 'color':self.color, 'year':self.year}
        with open('UsedCar.csv', 'a', newline = '') as file:
            csv_writer = csv.DictWriter(file, fieldnames = headers)
            csv_writer.writerow(car_info)

# inventory class  
class Inventory():
    def __init__(self, searchKey=None, searchValue=None):
        self.searchKey = searchKey
        self.searchValue = searchValue

    def search(self):
        carList = readIn()
        return list(filter(lambda item: item[self.searchKey] == self.searchValue, carList))

# customer class
class Customer():
    def __init__(self, downPayment, price, numMonths):
        self.downPayment = downPayment
        self.price = price
        self.numMonths = numMonths

    def showPayments(self):
        afterMoneyDown = self.price - self.downPayment
        monthlyTotal = afterMoneyDown / self.numMonths
        return monthlyTotal
       
# function to input car with user input
def inputCar():
    newId = random.randint(1, 50)
    newMake = input('Enter make: ')
    newModel = input('Enter model: ')
    newColor = input('Enter Color: ')
    newYear = input('Enter year: ')

    newCar = UsedCar(newId, newMake, newModel, newColor, newYear)
    newCar.save_to_file()

# function to read in from text file
def readIn(): 
    carList = []
    stuff = ''
    f = open('UsedCar.txt', 'rt')
    while True:
        line = f.readline()
        if not line:
            break
        stuff += line
    f.close()
    stuffList = list(stuff.split('\n'))
    stuffList.pop()
    for item in stuffList:
        keys = ['id', 'make', 'model', 'color', 'year']
        values = list(item.split('\t'))
        values.pop()
        carDict = {keys[i]: values[i] for i in range(len(keys))}
        carList.append(carDict)
    return carList