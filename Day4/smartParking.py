from abc import ABC, abstractmethod
import time 

class Vehicle:
    def __init__(self,license_plate,owner_name):
        self.__license_plate=license_plate 
        self.__owner_name=owner_name 
    def get_license_plate(self):
        return self.__license_plate 
    def set_license_plate(self,plate):
        self.__license_plate=plate
    def get_owner_name(self):
        return self.__owner_name 
    def set_owner_name(self,name):
        self.__owner_name=name
    def display(self):
        print(f"Vehicle: {self.__license_plate}, Owner: {self.__owner_name}") 
    def calculate_parking_fee(self,hours):
        return 0  
class Bike(Vehicle):
    def __init__(self, license_plate, owner_name,helmet_required=True):
        super().__init__(license_plate, owner_name)
        self.helmet_required=helmet_required 
    def display(self):
        print(f"Bike --> License: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Helmet_Required: {self.helmet_required}") 
    def calculate_parking_fee(self, hours):
        return 20*hours
class Car(Vehicle):
    def __init__(self, license_plate, owner_name,seats=4):
        super().__init__(license_plate, owner_name)
        self.seats=seats 
    def display(self):
        print(f"Car --> License: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Seats: {self.seats}") 
    def calculate_parking_fee(self, hours):
        return 50*hours 
class SUV(Vehicle):
    def __init__(self, license_plate, owner_name,four_wheel_drive=True):
        super().__init__(license_plate, owner_name)
        self.four_wheel_drive=four_wheel_drive 
    def display(self):
        print(f"SUV --> License: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Four_wheel_drive: {self.four_wheel_drive}") 
    def calculate_parking_fee(self, hours):
        return 70*hours
class Truck(Vehicle):
    def __init__(self, license_plate, owner_name,max_load_capacity=1000):
        super().__init__(license_plate, owner_name)
        self.max_load_capacity=max_load_capacity 
    def display(self):
        print(f"Truck --> License: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Max_load_capacity: {self.max_load_capacity}") 
    def calculate_parking_fee(self, hours):
        return 100*hours
    
     
class ParkingSpot:
    def __init__(self, spot_id, size):
        self.__spot_id = spot_id
        self.__size = size
        self.__occupied = False
        self.__vehicle = None
        self.start_time = None

    def get_spot_id(self):
        return self.__spot_id

    def is_occupied(self):
        return self.__occupied

    def assign_vehicle(self, vehicle):
        if not self.__occupied and self.is_size_compatible(vehicle):
            self.__vehicle = vehicle
            self.__occupied = True
            self.start_time = time.time()
            print(f"Vehicle {vehicle.get_license_plate()} parked in Spot {self.__spot_id}")
            return True
        return False

    def remove_vehicle(self):
        if self.__occupied:
            end_time = time.time()
            hours = max(1, int((end_time - self.start_time) // 3600 + 1))  # simulate hours
            vehicle = self.__vehicle
            self.__vehicle = None
            self.__occupied = False
            self.start_time = None
            return vehicle, hours
        return None, 0

    def is_size_compatible(self, vehicle):
        if isinstance(vehicle, Bike) and self.__size in ["S", "M", "L", "XL"]:
            return True
        if isinstance(vehicle, Car) and self.__size in ["M", "L", "XL"]:
            return True
        if isinstance(vehicle, SUV) and self.__size in ["L", "XL"]:
            return True
        if isinstance(vehicle, Truck) and self.__size == "XL":
            return True
        return False

    def show_status(self):
        status = "Occupied" if self.__occupied else "Free"
        print(f"Spot {self.__spot_id} [{self.__size}] → {status}")


# -------------------- Task 3: ParkingLot --------------------
class ParkingLot:
    def __init__(self):
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        for spot in self.spots:
            spot.show_status()

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.assign_vehicle(vehicle):
                return True
        print(f"No suitable spot available for {vehicle.get_license_plate()}")
        return False

    def unpark_vehicle(self, vehicle, payment_method):
        for spot in self.spots:
            if spot.is_occupied() and spot._ParkingSpot__vehicle == vehicle:
                v, hours = spot.remove_vehicle()
                fee = v.calculate_parking_fee(hours)
                print(f"Parking Fee for {hours} hour(s): ₹{fee}")
                payment_method.process_payment(fee)
                return True
        print(f"Vehicle {vehicle.get_license_plate()} not found in parking lot.")
        return False


# -------------------- Task 4: Payment Abstraction --------------------
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} in Cash")


class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Card")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI")


# -------------------- Task 5: Main Program --------------------
if __name__ == "__main__":
    # Create parking lot
    lot = ParkingLot()
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "L"))
    lot.add_spot(ParkingSpot(4, "XL"))

    # Create vehicles
    bike = Bike("KA01AB1234", "Ravi")
    car = Car("KA02CD5678", "Priya", 5)
    suv = SUV("KA03EF9012", "John")
    truck = Truck("KA04GH3456", "LogisticsCo", 5000)

    # Show Encapsulation (direct access fails)
    # print(bike.__license_plate)   #  AttributeError
    print(bike.get_license_plate())  #  works via getter

    # Park vehicles
    lot.park_vehicle(bike)
    lot.park_vehicle(car)
    lot.park_vehicle(suv)
    lot.park_vehicle(truck)

    print("\n--- Parking Lot Status ---")
    lot.show_spots()

    print("\n--- Unparking with Payments ---")
    lot.unpark_vehicle(bike, UPIPayment())
    lot.unpark_vehicle(car, CardPayment())
    lot.unpark_vehicle(suv, CashPayment())
