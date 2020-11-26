"""
Author: Ajay Bhagchandani
"""

def createParkingLot(n):
    """Creates a parking lot of size n"""

    if n <= 0:
        return -1

    parking_lot = {}
    vrn_array = []
    for i in range(1, n+1):
        parking_lot[i] = {}
    return parking_lot, vrn_array


def parkThatCar(parking_lot, vrn, driver_age=0):
    """Assigns the nearest parking lot to the car"""

    if len(vrn) != 13:
        print("Invalid Vehicle Registration Number!")
        return -1 

    if not (vrn[:2].isalpha() and vrn[6:8].isalpha() and vrn[3:5].isdigit() and vrn[10:].isdigit() \
    and vrn[2] == '-' and vrn[5] == '-' and vrn[8] == '-'):
        print("Invalid Vehicle Registration Number!")
        return -2 

    if driver_age < 18 or not isinstance(driver_age, int):
        print("Driver Age Should be atleast 18")
        return -3

    for i in parking_lot.keys():
        flag = -4
        if parking_lot[i] == {}:
            parking_lot[i]['VRN'] = vrn
            parking_lot[i]['driverAge'] = driver_age
            flag = i
            break

    if flag == -4:
        print("All Parking Slots full. Please Come Back Later")

    return flag


def returnSlotNumbers(parking_lot, driver_age=0):
    """Returns all the slot numbers for all drivers of a particular age"""

    if not isinstance(driver_age, int) or driver_age < 18:
        print("Driver Age Should be atleast 18")
        return -1 

    slot_numbers = []

    for i in range(1, len(parking_lot) + 1):

        if 'driverAge' in parking_lot[i]:
            if parking_lot[i]['driverAge'] == driver_age:
                slot_numbers.append(i)

    return slot_numbers if slot_numbers else 0


def returnSlotNumberForACar(parking_lot, vrn):
    """Returns the slot number for the vehicle"""

    if len(vrn) != 13:
        print("Invalid Vehicle Registration Number!")
        return -1 

    if not (vrn[:2].isalpha() and vrn[6:8].isalpha() and vrn[3:5].isdigit() and vrn[10:].isdigit() \
    and vrn[2] == '-' and vrn[5] == '-' and vrn[8] == '-'):
        print("Invalid Vehicle Registration Number!")
        return -2

    else:
        final_val = -3
        for i in range(1, len(parking_lot)+1):
            if 'VRN' in parking_lot[i]:
                if parking_lot[i]['VRN'] == vrn:
                    final_val = i
                    break

        return final_val


def returnVRNsForDriver(parking_lot, driver_age):
    """Returns all Vehicle Registration numbers for all drivers of a particular age"""

    if not isinstance(driver_age, int) or driver_age < 18:
        print("Driver Age Should be atleast 18")
        return -1

    vrn_list = []

    for i in range(1, len(parking_lot) + 1):
        if 'VRN' in parking_lot[i]:
            if parking_lot[i]['driverAge'] == driver_age:
                vrn_list.append(parking_lot[i]['VRN'])

    return vrn_list if vrn_list else -2


def vacantTheSpot(parking_lot, posn):
    """Vacant that parking spot"""

    if posn in parking_lot.keys():
        driver_age = parking_lot[posn]['driverAge']
        vrn = parking_lot[posn]['VRN']
        parking_lot[posn] = {}
        print(f"Slot number {posn} vacated, the car with vehicle registration number '{vrn}' left the space, the driver of the car was of age {driver_age}")
        return parking_lot, vrn
    else:
        print("Invalid Slot Number")
        return parking_lot, -1

def validateForInteger(val):
    """Check if the parameter can be converted to type int"""

    try:
        val = int(val)
        return val
    except:
        return -1


if __name__ == '__main__':
    """Program execution starts from here"""

    with open('./input_files/input.txt') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        count += 1
        if line.strip().lower().startswith('create_parking_lot'):
            # Code section to create a parking lot

            lot_size = line.split()[-1]
            lot_size = validateForInteger(lot_size)

            if lot_size == -1:
                print("Invalid Value of Parking Lot Size")
                break

            parking_lot, vrn_array = createParkingLot(lot_size)
            print(f"Created Parking of {lot_size} slots")
            

        elif line.strip().lower().startswith('park '):
            # Code section to Park the car

            params = line.split()
            driver_age = params[-1]
            car_number = params[1]
            driver_age = validateForInteger(driver_age)

            if driver_age == -1:
                print("Driver Age must be a Number!")
                continue           

            if car_number in vrn_array:
                print(f"Car with same vehical registration number '{car_number}' exists already.")
                continue

            car_slot = parkThatCar(parking_lot, car_number, driver_age)
            if car_slot < 0:
                continue
            vrn_array.append(car_number)
            print(f"Car with vehicle registration number '{car_number}' has been parked at slot number {car_slot}")


        elif line.strip().lower().startswith('leave'):
            # Code section to Vacate a particular slot

            car_slot = line.split()[-1]
            car_slot = validateForInteger(car_slot)

            if car_slot == -1:
                print("Invalid Car Slot!")
                continue             

            if car_slot in parking_lot:
                if 'driverAge' in parking_lot[car_slot]:
                    parking_lot, vrn = vacantTheSpot(parking_lot, car_slot)
                    if not isinstance(vrn, int):
                        vrn_array.remove(vrn)
                else:
                    print(f"Car Slot {car_slot} is already empty")
            else:
                print("Invalid Value of Car Slot")


        elif line.strip().lower().startswith('slot_numbers_for_driver_of_age'):
            # Code section to fetch slot numbers of drivers with a particular age

            driver_age = line.split()[-1]
            driver_age = validateForInteger(driver_age)

            if driver_age == -1:
                print("Driver Age must be a Number!")
                continue

            slot_numbers = returnSlotNumbers(parking_lot, driver_age)
            if slot_numbers == -1:
                continue  
            elif slot_numbers == 0:
                print(f"No Slot Numbers found for driver(s) of age {driver_age}")
            else:
                print(f"Slot numbers for driver(s) of age {driver_age} are: ", slot_numbers)


        elif line.strip().lower().startswith('slot_number_for_car_with_number'):
            # Code section to fetch slot number of the car with a particular reg. number

            car_number = line.split()[-1]
            slot_number = returnSlotNumberForACar(parking_lot, car_number)
            if slot_number < 0:
                print(f"Vehical with Registration number '{car_number}' not found")
                continue
            else:
                print(f"Slot Number where the vehicle '{car_number}' is parked is ", slot_number)


        elif line.strip().lower().startswith('vehicle_regi'):
            # Code section to fetch vehicle reg. numbers of drivers having a particular age

            driver_age = line.split()[-1]
            driver_age = validateForInteger(driver_age)

            if driver_age == -1:
                print("Driver Age must be a Number!")
                continue

            vrn = returnVRNsForDriver(parking_lot, driver_age)
            if isinstance(vrn, int) and vrn == -2:
                print(f"No vehicles found that have driver_age: {driver_age}")
                continue
            print("Vehical Registration Numbers: ", vrn)

        else:
            pass