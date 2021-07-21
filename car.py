class Car:
    def __init__(self, colour, headlight, mirror, music_system, owner, no_plate, tyre, model):
        self.colour = colour
        self.headlight = headlight
        self.mirror = mirror
        self.music_system = music_system
        self.owner = owner
        self.no_plate = no_plate
        self.tyre = tyre
        self.model = model

    def paintcar(self, new_colour):
        self.colour = new_colour

    def remove_music_sys(self):
        self.music_system = False

hambira = Car("red", True, True, True, "Hambiraaaa", "MH 14 CQ 8963", True, "BMW") #access the attributes
print(hambira.owner)
print(hambira.no_plate)

shital = Car("Olive", True, True, True, "Shital", "MH 14 CQ 8963", True, "Audi") #access the attributes
puja = Car("Black", True, True, True, "Puja", "JH 12 CQ 8842", True, "Honda City")

print(shital.no_plate)
print(puja.no_plate)

print(hambira.colour)
hambira.paintcar("Silver")
print(hambira.colour)

print(shital.music_system)
shital.remove_music_sys()
print(shital.music_system)


class Licence(Car):
    def __init__(self, colour, headlight, mirror, music_system, owner, no_plate, tyre, model, licence_no):#licence class attributes
        super().__init__(colour, headlight, mirror, music_system, owner, no_plate, tyre, model)#car class attributes
        self.licence_no = licence_no

    def apply_lights(self):
        self.headlight = "Fog Lights"

lp = Licence("Black", True, True, True, "Puja", "JH 12 CQ 8842", True, "Honda City", "Lic001")

print(lp.licence_no)
lp.paintcar("White")
print(lp.colour)