import math
from abc import ABC, abstractmethod


class IShape(ABC):
    """Abstract base class defining the shape interface."""
    
    @abstractmethod
    def calculate_area(self):
        """Calculate the surface area of the shape."""
        pass
    
    @abstractmethod
    def calculate_volume(self):
        """Calculate the volume of the shape."""
        pass


class Sphere(IShape):
    """A sphere with a given radius."""
    
    def __init__(self, radius):
        self._radius = radius
    
    def calculate_area(self):
        return 4 * math.pi * math.pow(self._radius, 2)
    
    def calculate_volume(self):
        return (4.0 / 3.0) * math.pi * math.pow(self._radius, 3)


class Cylinder(IShape):
    """A cylinder with a given radius and height."""
    
    def __init__(self, radius, height):
        self._radius = radius
        self._height = height
    
    def calculate_area(self):
        return 2 * math.pi * self._radius * (self._radius + self._height)
    
    def calculate_volume(self):
        return math.pi * math.pow(self._radius, 2) * self._height


class Rectangle(IShape):
    """A rectangle with given length and width (2D shape)."""
    
    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    def calculate_area(self):
        return self._length * self._width
    
    def calculate_volume(self):
        # For 2D shapes, volume is not applicable.
        # Height of 2D shape is 0, therefore volume is 0
        return 0


class Cube(IShape):
    """A cube with a given side length."""
    
    def __init__(self, side):
        self._side = side
    
    def calculate_area(self):
        return 6 * math.pow(self._side, 2)
    
    def calculate_volume(self):
        return math.pow(self._side, 3)


def main():
    # Create a Sphere with radius 5
    sphere = Sphere(5)
    print("Sphere:")
    print(f"Area: {sphere.calculate_area():.3f}")
    print(f"Volume: {sphere.calculate_volume():.3f}")
    print()
    
    # Create a Cylinder with radius 3 and height 7
    cylinder = Cylinder(3, 7)
    print("Cylinder:")
    print(f"Area: {cylinder.calculate_area():.3f}")
    print(f"Volume: {cylinder.calculate_volume():.3f}")
    print()
    
    # Create a Rectangle with length 4 and width 8
    rectangle = Rectangle(4, 8)
    print("Rectangle:")
    print(f"Area: {rectangle.calculate_area():.3f}")
    # Rectangle is a 2D shape, so volume is 0
    print(f"Volume: {rectangle.calculate_volume():.3f}")
    print()
    
    # Create a Cube with side 4
    cube = Cube(4)
    print("Cube:")
    print(f"Area: {cube.calculate_area():.3f}")
    print(f"Volume: {cube.calculate_volume():.3f}")


if __name__ == "__main__":
    main()