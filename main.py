import csv
import math
from My_HashMap import HashMap
from Package import Package
from Truck import Truck
from datetime import datetime

# create hashmap instance
myHashMap = HashMap()


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

            # load into hashmap
            myHashMap.add(pID, p)


loadPackageData('WGUPS Package File.csv')


# read distance table
def loadDistanceData(filename):
    with open(filename) as distanceTable:
        distance_data = csv.reader(distanceTable, delimiter=',')
        data_read = [row for row in distance_data]

    return data_read


distances = loadDistanceData('WGUPS Address-Distance Table.csv')

# instantiate truck objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

truck1.load([1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 'Driver A', '8:00', 'idk yet')
truck2.load([2, 3, 4, 5, 6, 7, 8, 18, 25, 28, 32, 36, 38], 'Driver B', '9:05', 'idk yet')
truck3.load([9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39], '', '', '')

