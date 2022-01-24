__author__ = 'Ella Seaman'
# Program that recommends where your house plant
# should live in your home.
#
# Input: plant_location
# Output: plant_location, counter

#   Constant Integer MAX_PLANTS = 200
MAX_PLANTS = 200

#   Class Plant_Location
#       Private Integer _room_in_house = 0
#       Private Plants _plants[MAX_PLANTS]
#       Private Integer _total_light
#       Private Integer _total_size
#
#       Public Module get_plant_type()
#           Declare Boolean done = False
#           Declare Plants plant
#           Declare Boolean is_tree_bush = False
#
#           While not done
#               Set is_tree_bush = y_or_n("Is the plant a bush or tree? (Y/N)? ")
#               If is_tree_bush Then
#                   Set plant = New TreeAndBush()
#               Else
#                   Set plant = New Plant()
#               End If
#               Call plant.input()
#               Set _plants[_room_in_house] = plant
#               Set _room_in_house = _room_in_house + 1
#               Set done = y_or_n("Are you finished adding plants (Y/N)? ")
#           End While
#       End Function
#
#       Public Module display()
#             Declare Integer counter = 0
#             Declare Plant plants
#
#               While counter < _room_in_house
#                   Set plant = _plants[counter]
#                   Display "Plant", counter, "-", plant.get_sunlight(), "recommended light level at," plant.get_size()"
#                   Set counter = counter + 1
#               End While
#               Display "Total light:", _total_light
#               Display "Total size:", _total_size
#                 If plant.get_sunlight() >= 10:
#                        Display "Keep your plant in a window sill or outside."
#                 Else If plant.get_sunlight() <= 5 and plant.get_sunlight() >= 9:
#                        Display "Keep your plant in a shady room that gets some light."
#                 Else
#                        Display "Keep your plant in a low light room."
#                 End If
#       End Module
#
#       Public Module calculate()
#               Declare Integer counter = 0
#               Declare Plants plant
#
#               While counter < _room_in_house
#                   Set plant = plants[counter]
#                   Set _total_light = _total_light + plant.get_sunlight()
#                   Set _total_size = _total_size + plant.get_sunlight() + plant.get_size()
#                   Set counter = counter + 1
#               End While
#        End Function

class Plant_Location:
    _room_in_house = 0
    _plants = [None for x in range(MAX_PLANTS)]
    _total_light = 0
    _total_size = 0

    def get_plant_type(self):
        done = False
        plant = None
        is_tree_bush = False

        while not done:
            is_tree_bush = y_or_n("Is the plant a bush or tree? (Y/N)? ")
            if(is_tree_bush):
                plant = TreeAndBush()
            else:
                plant = Plants()
            plant.input()
            self._plants[self._room_in_house] = plant
            self._room_in_house = self._room_in_house + 1
            done = y_or_n("Are you finished adding plants (Y/N)? ")

    def display(self):
        counter = 0
        while counter < self._room_in_house:
            plant = self._plants[counter]
            print("Plant", (counter + 1), ":", plant.get_plant(), "-", plant.get_sunlight(),
                  "hours of recommended light level at,", plant.get_size(), "inches tall")
            counter = counter + 1
            if plant.get_sunlight() >= 10:
                print("Keep your plant in a window sill or outside.")
            elif plant.get_sunlight() >= 5 and plant.get_sunlight() <= 9:
                print("Keep your plant in a shady room that gets some light.")
            else:
                print("Keep your plant in a low light room.")
        print("Total Light:", self._total_light)
        print("Total Size:", self._total_size)
    def calculate(self):
        counter = 0
        plant = None
        while counter < self._room_in_house:
            plant = self._plants[counter]
            self._total_light = self._total_light + plant.get_sunlight()
            self._total_size = self._total_size + plant.get_sunlight() + plant.get_size()
            counter = counter + 1

#   Class Plants
#       Private String _plant
#       Private Integer _sunlight
#       Private Integer _size
#
#       Public Module input()
#          Set _plant = get_string("What is the type of plant? ")
#          Set _sunlight = get_int("How many hours of sun does " + _plant + " require? ")
#          Set _size = get_int("How many inches tall is " + _plant + "? ")
#       End Module
#
#       Public Function String get_plant()
#           Return _plant
#       End Function
#
#       Public Function Integer get_sunlight()
#           Return _sunlight
#       End Function
#
#       Public Function Integer get_size()
#           Return _size
#       End Function
#   End Class

class Plants:
    _plant = ""
    _sunlight = 0
    _size = 0

    def input(self):
        self._plant = get_string("What is the type of plant? ")
        self._sunlight = get_int("How many hours of sun does " + self._plant + " require? ")
        self._size = get_int("How many inches tall is " + self._plant + "? ")

    def get_plant(self):
        return self._plant

    def get_sunlight(self):
        return self._sunlight

    def get_size(self):
        return self._size

# Class TreeAndBush Extends Plants
#       Public Module input()
#          Set _plant = get_string("What is the type of plant? ")
#          Set _sunlight = get_int("How many hours of sun does " + _plant + " require? ")
#       End Module
#
class TreeAndBush (Plants):
    def input(self):
        self._plant = get_string("What is the type of plant? ")
        self._sunlight = get_int("How many hours of sun does " + self._plant + " require? ")

#   Function String get_string(String prompt)
#       Declare String value
#       Display prompt
#       Input value
#       Return value
#   End Function
def get_string(prompt):
    value = ""

    value = input(prompt)
    return value

#   Function Integer get_int(String prompt)
#       Declare String value
#
#       Display prompt
#       Input value
#       While not value is an integer
#           Display value, "is not an integer. Please try again."
#           Display prompt
#           Input value
#       End While
#       Return value
#    End Function

def valid_int(value):
    try:
        int(value)
        return True
    except:
        return False

def get_int(prompt):
    value = ""

    value = input(prompt)
    while not valid_int(value):
        print(value, "is not an integer. Please try again.")
        value = input(prompt)
    return int(value)

#   Function Boolean y_or_n(String prompt)
#       Declare string Value
#
#       Display prompt
#       Input value
#       While True
#           If value == "Y" or value == "y" Then
#               Return true
#           Else If value == "N" or value == "n" Then
#               Return False
#           Else
#               Display "Please enter Y or N!"
#               Display prompt
#               Input value
#           End If
#        End While
#     End Function

def y_or_n(prompt):
    value = ""

    value = input(prompt)
    while True:
        if value == "Y" or value == "y":
            return True
        elif value == "N" or value == "n":
            return False
        else:
            print("Please enter Y or N!")
            value = input(prompt)


#   Module location ()
#       Declare Plants plants[MAX_PLANTS]
#       Declare Integer room_in_house
#       Declare Integer total_light
#       Declare Integer total_size
#       Declare Plant_Location plant_location
#
#       Set plant_location = Plant_Location()
#       Call plant_location.get_plants()
#       Call plant_location.calculate()
#       Call plant_location.display()
#   End Module
#
#
def location():
    plant_location = None

    plant_location = Plant_Location()
    plant_location.get_plant_type()
    plant_location.calculate()
    plant_location.display()




location()


