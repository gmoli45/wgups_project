# Gabriel Molina
# ID 011555816
# gmoli45@wgu.edu


# import necessary libraries and classes
import csv
from My_HashMap import HashMap
from Package import Package
from Truck import Truck
import datetime

# create hashmap instance to store packages
packageHashMap = HashMap()


# function to read package file
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


# call function to read package file
loadPackageData('WGUPS Package File.csv')


# function to read distance table
def loadDistanceData(filename):
    with open(filename) as distanceTable:
        distance_data = csv.reader(distanceTable, delimiter=',')
        data_read = [row for row in distance_data]

    return data_read


# call function to read distance table
distances = loadDistanceData('WGUPS Address-Distance Table.csv')


# function to find distance between two addresses
def find_distance_between(addr1, addr2):
    ind1 = None
    ind2 = None
    # find index of each address in distances data
    for i in range(len(distances)):
        if distances[i][0] == addr1:
            ind1 = i
        if distances[i][0] == addr2:
            ind2 = i
    # return distance between them
    if distances[ind1][ind2] == '':
        return distances[ind2][ind1]
    else:
        return distances[ind1][ind2]


# instantiate truck objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

# load truck 1
truck1.load([1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], datetime.timedelta(hours=8))
for i in truck1.packages_on_board:
    pkg = packageHashMap.get(int(i))
    pkg.assigned_truck = 'Truck 1'

# load truck 2
truck2.load([2, 3, 4, 5, 6, 7, 8, 18, 25, 28, 32, 36, 38], datetime.timedelta(hours=9, minutes=30))
for i in truck2.packages_on_board:
    pkg = packageHashMap.get(int(i))
    pkg.assigned_truck = 'Truck 2'

# update package 9 address at 10:20, before being loaded on truck 3
new_pkg_9 = Package(9, '410 S State St', 'Salt Lake City', 'UT', '84111', 'EOD', '2', 'Address corrected')
packageHashMap.add(9, new_pkg_9)

# load truck 3
truck3.load([9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39], datetime.timedelta(hours=10, minutes=30))
for i in truck3.packages_on_board:
    pkg = packageHashMap.get(int(i))
    pkg.assigned_truck = 'Truck 3'


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
        # update package
        truck.next_package.deliveredTime = truck.time
        truck.next_package.departure_time = truck.departure_time

        # update truck
        truck.mileage += next_stop_distance
        truck.time += datetime.timedelta(hours=next_stop_distance / truck.avg_speed)
        truck.location = next_package.address
        truck.packages_on_board.remove(next_package.id)

    # loop through deliveries until no packages on board
    while len(truck.packages_on_board) > 0:
        travel_and_deliver(find_next_stop(), truck.next_package)

    # return truck to hub
    dist_back_to_hub = float(find_distance_between(truck.location, "4001 S 700 E"))
    truck.mileage += dist_back_to_hub
    truck.time += datetime.timedelta(hours=dist_back_to_hub / truck.avg_speed)


# dispatch trucks at scheduled departure times
deliver_packages(truck1)
deliver_packages(truck2)
deliver_packages(truck3)


# user interface to check packages or view truck summary
class UserInterface:
    import re

    print("\nWelcome to the WGUPS package tracking service.\n\n-----------------------\n")

    # prompt user for options
    print("Please enter \"A\" if you would like to track one or more packages."
          "\nEnter \"B\" if you would like to view the Truck summary.")

    # while loop used with if-statements and try-except to catch invalid inputs
    while True:
        report_type = input()
        if report_type.upper() == "A":
            # prompt user to input time
            print("\nPlease enter the time at which you would like to check package status (format hh:mm:ss):\n")

            while True:
                input_time = input("")
                try:
                    # Validate the input using a regular expression
                    if re.match(r"^([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", input_time):
                        # Input is valid, break the loop
                        break
                    else:
                        print("\nInvalid input. Please enter a time in hh:mm:ss format.\n")
                except ValueError:
                    print("\nInvalid input. Please enter a time in hh:mm:ss format.\n")

            # split user input on colon and convert to datetime object
            hours, minutes, seconds = input_time.split(":")
            time_to_check = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

            # prompt user for package ID or "all" to view all packages
            print("\nEnter the package ID you would like to track. "
                  "If you would like to view all packages, enter \"all\".\n")
            while True:
                input_package = input("")
                try:
                    # validate input
                    if input_package.isnumeric():
                        if 1 <= int(input_package) <= 40:
                            pkg = packageHashMap.get(int(input_package))

                            # show old or corrected address for package 9
                            if int(input_package) == 9:
                                if time_to_check < datetime.timedelta(hours=10, minutes=20):
                                    pkg.address = '300 State St'
                                    pkg.zip = '84103'
                                    pkg.notes = 'Wrong address listed'

                            # compare report time to delivered time to determine status
                            if time_to_check >= pkg.deliveredTime:
                                pkg.status = f"Delivered at {pkg.deliveredTime}"
                            elif time_to_check >= pkg.departure_time:
                                pkg.status = "En route"
                            else:
                                pkg.status = "At hub"
                            print(pkg)
                            break
                        else:
                            print("\nInvalid input. Please enter a valid package ID "
                                  "or enter \"all\" to view all packages.\n")
                    elif input_package == "all":
                        for i in range(1, 41):
                            pkg = packageHashMap.get(i)

                            # show old or corrected address for package 9
                            if i == 9 and time_to_check < datetime.timedelta(hours=10, minutes=20):
                                pkg.address = '300 State St'
                                pkg.zip = '84103'
                                pkg.notes = 'Wrong address listed'

                            if time_to_check >= pkg.deliveredTime:
                                pkg.status = f"Delivered at {pkg.deliveredTime}"
                            elif time_to_check >= pkg.departure_time:
                                pkg.status = "En route"
                            else:
                                pkg.status = "At hub"
                            print(pkg)
                        break
                    else:
                        print("\nInvalid input. Please enter a valid package ID "
                              "or enter \"all\" to view all packages.\n")
                except ValueError:
                    print("\nInvalid input.\n")
            break
        # print truck summary report
        elif report_type.upper() == "B":
            print("\nTruck Summary:")
            print(f"\nTruck 1\n\tMileage: {truck1.mileage}\n\tDeparture time: {truck1.departure_time}\n\tReturn time: {truck1.time}")
            print(f"\nTruck 2\n\tMileage: {truck2.mileage}\n\tDeparture time: {truck2.departure_time}\n\tReturn time: {truck2.time}")
            print(f"\nTruck 3\n\tMileage: {truck3.mileage}\n\tDeparture time: {truck3.departure_time}\n\tReturn time: {truck3.time}")
            print(f"\nTotal mileage: {truck1.mileage + truck2.mileage + truck3.mileage}")
            break
        else:
            print("\nInvalid input. Please enter \"A\" if you would like to track one or more packages, or "
                  "\nenter \"B\" if you would like to view the Truck summary.")
