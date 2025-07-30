import math

class Solid:
    def accept_data(self):
        pass

    def surface_area(self):
        pass

    def volume(self):
        pass


class Sphere(Solid):
    def accept_data(self):
        self.radius = float(input("Enter radius of the sphere: "))

    def surface_area(self):
        return 4 * math.pi * self.radius**2

    def volume(self):
        return (4/3) * math.pi * self.radius**3


class Cube(Solid):
    def accept_data(self):
        self.side = float(input("Enter side length of the cube: "))

    def surface_area(self):
        return 6 * self.side**2

    def volume(self):
        return self.side**3


class Cylinder(Solid):
    def accept_data(self):
        self.radius = float(input("Enter radius of the cylinder: "))
        self.height = float(input("Enter height of the cylinder: "))

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius**2 * self.height


def main():
    print("Choose a solid:")
    print("1. Sphere")
    print("2. Cube")
    print("3. Cylinder")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        solid = Sphere()
    elif choice == '2':
        solid = Cube()
    elif choice == '3':
        solid = Cylinder()
    else:
        print("Invalid choice!")
        return

    solid.accept_data()
    print(f"Surface Area: {solid.surface_area():.2f}")
    print(f"Volume: {solid.volume():.2f}")

main()