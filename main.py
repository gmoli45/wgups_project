import csv
from My_HashMap import HashMap
from Package import Package

# create hashmap instance
myHashMap = HashMap(size=30)


# read package file
def loadPackageData(fileName):
    with open(fileName) as packages:
        package_data = csv.reader(packages, delimiter=',')
        next(package_data)
        for package in package_data:
            # read data into variables
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pWeight = int(package[6])
            pNotes = package[7]

            # create package object
            p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pNotes)
            print(p)

            # load into hashmap
            myHashMap.add(pID, p)
