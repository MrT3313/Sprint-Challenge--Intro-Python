# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# 1 # BASE CLASS --> Vehicle
class Vehicle:
    pass

# 1.1 # GROUND VEHICLE
class GroundVehicle(Vehicle):
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self):
        return "vroooom"

    def __str__(self):
        output = ''
        output += f'-*- GROUND VEHICLE CLASS -*-\n'
        output += f'A ground vehicle typically has {self.num_wheels} wheels'

        return output

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    # V1
    #pass

    #V2
    def __init__(self):
        super().__init__(2)
    
    def drive(self):
        return "BRAAAP!!"
    
    def __str__(self):
        output = ''
        output += f'-*- MOTORCYCLE CLASS -*-\n'
        output += f'A motorcycle has {self.num_wheels} wheels'

        return output


# 1.2 # FLIGHT VEHICLE
class  FlightVehicle(Vehicle):
    pass

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass