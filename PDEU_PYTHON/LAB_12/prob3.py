import math

class Solid:
    def surface_area(self):
        pass

    def volume(self):
        pass

class Sphere(Solid):
    def _init_(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius**2

    def volume(self):
        return (4/3) * math.pi * self.radius**3

class Cube(Solid):
    def _init_(self, side):
        self.side = side

    def surface_area(self):
        return 6 * self.side**2

    def volume(self):
        return self.side**3

class Cylinder(Solid):
    def _init_(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius**2 * self.height

sphere = Sphere(3)
print("Sphere Surface Area:", sphere.surface_area())
print("Sphere Volume:", sphere.volume())

cube = Cube(2)
print("Cube Surface Area:", cube.surface_area())
print("Cube Volume:", cube.volume())

cylinder = Cylinder(2, 5)
print("Cylinder Surface Area:", cylinder.surface_area())
print("Cylinder Volume:", cylinder.volume())