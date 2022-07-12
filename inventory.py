''' Inventory application for used car lot. Keeps track of inventory and allows the user to search for a certain car type.
    Authors: Dylan, Lukas, Tran, Jonathan
    Last edited: 7/9/22
'''
import random

carList = []

def dictFunction(key, value, items):
    # dictFunction('make', 'mazda', [{'make': 'ford', 'model': 'focus'}, {'make': 'mazda', 'model': 'cx7'}])
    for item in items:
        if item[key] == value:
            print(item)

'''||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'''
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

    # add to the car list inventory as a dictionary structure
    def addCar(self):
        carList.append({'id': self.id, 'make': self.make, 'model': self.model, 'color': self.color, 'year': self.year})

    # save to file
    def save_to_file(self):
        car_info = [self.id, self.make, self.model, self.color, self.year]
        used_car_file = open('UsedCar.txt', 'a')
        for i in car_info:
            used_car_file.write("%s\t" % i)
        used_car_file.write("\n")
        used_car_file.close()
        print("Successfully add to the inventory.")

'''|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'''
# Inventory/computer class  
class Inventory():
    def __init__(self, searchKey=None, searchValue=None):
        self.searchKey = searchKey
        self.searchValue = searchValue

    def deepSearch(self):
        readIn()
        searchValue = input("Make: ")
        if searchValue is None or len(searchValue) == 0:
            make_list = carList
        else:
            make_list = list(filter(lambda item: item["make"] == searchValue, carList))
        print(make_list)

        searchValue = input("Model: ")
        if searchValue is None or len(searchValue) == 0:
            model_list = make_list
        else:
            model_list = list(filter(lambda item: item["model"] == searchValue, make_list))
        print(model_list)

        searchValue = input("Color: ")
        if searchValue is None or len(searchValue) == 0:
            color_list = model_list
        else:
            color_list = list(filter(lambda item: item["color"] == searchValue, model_list))
        print(color_list)

        searchValue = input("Year: ")
        if searchValue is None or len(searchValue) == 0:
            year_list = color_list
        else:
            year_list = list(filter(lambda item: item["year"] == int(searchValue), color_list))
        print(year_list)
    
    # search for one attribute and one value
    def singleSearch(self):
        readIn()
        skey = input('Attribute: ')
        sValue = input('Attribute value: ')
        print(list(filter(lambda item: item[skey] == sValue, carList)))

    # search for one attribute and one value with class attributes -- not sure which is better
    def search(self):
        readIn()
        print(list(filter(lambda item: item[self.searchKey] == self.searchValue, carList)))

'''|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'''
#customer class
class Customer():
    def __init__(self, name, downPayment, price, numMonths):
        self.name = name
        self.downPayment = downPayment
        self.price = price
        self.numMonths = numMonths

    def showPayments(self):
        afterMoneyDown = self.price - self.downPayment
        monthlyTotal = afterMoneyDown / self.numMonths
        print('$' + '%.2f'% float(monthlyTotal), 'per month for ' + str(self.numMonths), 'months')

#function to input car with user input
def inputCar():
    newId = random.randint(1, 50)
    newMake = input('Enter make: ')
    newModel = input('Enter model: ')
    newColor = input('Enter Color: ')
    newYear = input('Enter year: ')

    newCar = UsedCar(newId, newMake, newModel, newColor, newYear)
    newCar.save_to_file()

'''||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'''

#function to read in from text file
def readIn():
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

# inputCar()
s = Inventory()
s.singleSearch()

# inputCar()

'''Commented out calls'''
# Used car objects
# myCar1 = UsedCar('1', 'mazda', 'cx-7', 'purple', 2012)
# myCar2 = UsedCar('2', 'ford', 'focus', 'white', 2015)
# myCar3 = UsedCar('3', 'subaru', 'forester', 'black', 2018)

# methods on usedCars
# myCar1.addCar()
# myCar2.addCar()
# myCar3.addCar()

#Save car objects to file
'''
myCar1.save_to_file()
myCar2.save_to_file()
myCar3.save_to_file()
'''
# Inventory objects
#s1 = Inventory('year', 2012)
#s1.search()

# cus1 = Customer('dylan', 500, 12500, 36)
# cus1.showPayments()