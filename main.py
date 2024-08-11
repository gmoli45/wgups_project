import csv
import math
from My_HashMap import HashMap
from Package import Package
from Truck import Truck

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

def loadDistanceData(filename):
    with open(filename) as distanceTable:
        distance_data = csv.reader(distanceTable, delimiter=',')
        data_read = [row for row in distance_data]

    return data_read

distances = loadDistanceData('WGUPS Address-Distance Table.csv')