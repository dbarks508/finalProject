def convertTextFile(file):
    carList = []
    stuff = ''
    f = open(file, 'rt')
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
    # print(carList)

convertTextFile('UsedCar.txt')