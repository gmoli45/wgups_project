# Gabriel Molina
# ID 011555816
# gmoli45@wgu.edu

import csv
from My_HashMap import HashMap
from Package import Package
from Truck import Truck
import datetime

# create hashmap instance to store packages
packageHashMap = HashMap()


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
            packageHashMap.add(pID, p)


loadPackageData('WGUPS Package File.csv')


# read distance table
def loadDistanceData(filename):
    with open(filename) as distanceTable:
        distance_data = csv.reader(distanceTable, delimiter=',')
        data_read = [row for row in distance_data]

    return data_read


distances = loadDistanceData('WGUPS Address-Distance Table.csv')


def find_distance_between(addr1, addr2):
    ind1 = None
    ind2 = None
    # find index of each address in distances data
    for i in range(len(distances)):
        if distances[i][0] == addr1:
            ind1 = i
        if distances[i][0] == addr2:
            ind2 = i
    # return distance between
    if distances[ind1][ind2] == '':
        return distances[ind2][ind1]
    else:
        return distances[ind1][ind2]


# instantiate truck objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

# load trucks
truck1.load([1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], datetime.timedelta(hours=8))
truck2.load([2, 3, 4, 5, 6, 7, 8, 18, 25, 28, 32, 36, 38], datetime.timedelta(hours=10, minutes=20))
truck3.load([9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39],
            None)  # departure time to be updated when truck1 or truck2 returns


def deliver_packages(truck):
    # find closest next address from packages on truck
    def find_next_stop():
        next_stop_distance = 100000
        for packageId in truck.packages_on_board:
            distance = find_distance_between(truck.location, packageHashMap.get(packageId).address)
            if float(distance) < float(next_stop_distance):
                next_stop_distance = float(distance)
                truck.next_package = packageHashMap.get(packageId)
        return next_stop_distance

    def travel_and_deliver(next_stop_distance, next_package):
        # update truck
        truck.mileage += next_stop_distance
        truck.time += datetime.timedelta(hours=next_stop_distance / truck.avg_speed)
        truck.location = next_package.address
        truck.packages_on_board.remove(next_package.id)

        # !!! update package

    # loop through deliveries until no packages on board
    while len(truck.packages_on_board) > 0:
        travel_and_deliver(find_next_stop(), truck.next_package)

    # return truck to hub
    dist_back_to_hub = float(find_distance_between(truck.location, "4001 S 700 E"))
    truck.mileage += dist_back_to_hub
    truck.time += datetime.timedelta(hours=dist_back_to_hub / truck.avg_speed)


deliver_packages(truck1)
deliver_packages(truck2)

print(truck1.time)
print(truck2.time)

print(truck3.time)
truck3.departure_time = min(truck1.time, truck2.time)
truck3.time = truck3.departure_time
print(truck3.time)
deliver_packages(truck3)

print(truck3.time)
