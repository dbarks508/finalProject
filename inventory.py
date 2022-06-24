# list for holding inventory
carList = []

# used car class
class UsedCar:
    def __init__(self, id=None, make=None, model=None, color=None, year=None):
        self.id = id
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    # print out a cars attributes
    def show_stats(self):
        print('Car Info: ', self.make, self.model, self.color, self.year)

    # add to the car list inventory as a dictionary structure
    def addCar(self):
        carList.append({'id': self.id, 'make': self.make, 'model': self.model, 'color': self.color, 'year': self.year})

# Inventory/computer class  
class Inventory():
    def __init__(self, searchKey, searchValue):
        self.searchKey = searchKey
        self.searchValue = searchValue

    def search(self):
        print(list(filter(lambda item: item[self.searchKey] == self.searchValue, carList)))

# Used car objects
myCar1 = UsedCar('1', 'mazda', 'cx-7', 'purple', 2012)
myCar2 = UsedCar('2', 'ford', 'focus', 'white', 2015)
myCar3 = UsedCar('3', 'subaru', 'forester', 'black', 2018)

# methods on usedCars
myCar1.addCar()
myCar2.addCar()
myCar3.addCar()

# Inventory objects
search1 = Inventory('make', 'ford')

# methods on Inventory
search1.search() 




