import unittest
import math
from project_code import Sphere, Cylinder, Rectangle, Cube, IShape


class TestSphere(unittest.TestCase):
    """Test cases for the Sphere class."""
    
    def test_sphere_area(self):
        """Test sphere surface area calculation."""
        sphere = Sphere(5)
        expected_area = 4 * math.pi * math.pow(5, 2)
        self.assertAlmostEqual(sphere.calculate_area(), expected_area, places=5)
    
    def test_sphere_volume(self):
        """Test sphere volume calculation."""
        sphere = Sphere(5)
        expected_volume = (4.0 / 3.0) * math.pi * math.pow(5, 3)
        self.assertAlmostEqual(sphere.calculate_volume(), expected_volume, places=5)
    
    def test_sphere_with_unit_radius(self):
        """Test sphere with radius 1."""
        sphere = Sphere(1)
        self.assertAlmostEqual(sphere.calculate_area(), 4 * math.pi, places=5)
        self.assertAlmostEqual(sphere.calculate_volume(), (4.0 / 3.0) * math.pi, places=5)
    
    def test_sphere_implements_interface(self):
        """Test that Sphere implements IShape interface."""
        sphere = Sphere(5)
        self.assertIsInstance(sphere, IShape)


class TestCylinder(unittest.TestCase):
    """Test cases for the Cylinder class."""
    
    def test_cylinder_area(self):
        """Test cylinder surface area calculation."""
        cylinder = Cylinder(3, 7)
        expected_area = 2 * math.pi * 3 * (3 + 7)
        self.assertAlmostEqual(cylinder.calculate_area(), expected_area, places=5)
    
    def test_cylinder_volume(self):
        """Test cylinder volume calculation."""
        cylinder = Cylinder(3, 7)
        expected_volume = math.pi * math.pow(3, 2) * 7
        self.assertAlmostEqual(cylinder.calculate_volume(), expected_volume, places=5)
    
    def test_cylinder_with_equal_dimensions(self):
        """Test cylinder where radius equals height."""
        cylinder = Cylinder(5, 5)
        expected_area = 2 * math.pi * 5 * (5 + 5)
        expected_volume = math.pi * 25 * 5
        self.assertAlmostEqual(cylinder.calculate_area(), expected_area, places=5)
        self.assertAlmostEqual(cylinder.calculate_volume(), expected_volume, places=5)
    
    def test_cylinder_implements_interface(self):
        """Test that Cylinder implements IShape interface."""
        cylinder = Cylinder(3, 7)
        self.assertIsInstance(cylinder, IShape)


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""
    
    def test_rectangle_area(self):
        """Test rectangle area calculation."""
        rectangle = Rectangle(4, 8)
        self.assertEqual(rectangle.calculate_area(), 32)
    
    def test_rectangle_volume_is_zero(self):
        """Test that rectangle volume is always 0 (2D shape)."""
        rectangle = Rectangle(4, 8)
        self.assertEqual(rectangle.calculate_volume(), 0)
    
    def test_rectangle_square(self):
        """Test rectangle with equal sides (square)."""
        square = Rectangle(5, 5)
        self.assertEqual(square.calculate_area(), 25)
        self.assertEqual(square.calculate_volume(), 0)
    
    def test_rectangle_with_decimals(self):
        """Test rectangle with decimal dimensions."""
        rectangle = Rectangle(3.5, 2.5)
        self.assertAlmostEqual(rectangle.calculate_area(), 8.75, places=5)
    
    def test_rectangle_implements_interface(self):
        """Test that Rectangle implements IShape interface."""
        rectangle = Rectangle(4, 8)
        self.assertIsInstance(rectangle, IShape)


class TestCube(unittest.TestCase):
    """Test cases for the Cube class."""
    
    def test_cube_area(self):
        """Test cube surface area calculation."""
        cube = Cube(4)
        expected_area = 6 * math.pow(4, 2)
        self.assertEqual(cube.calculate_area(), expected_area)
    
    def test_cube_volume(self):
        """Test cube volume calculation."""
        cube = Cube(4)
        expected_volume = math.pow(4, 3)
        self.assertEqual(cube.calculate_volume(), expected_volume)
    
    def test_cube_unit_side(self):
        """Test cube with side length 1."""
        cube = Cube(1)
        self.assertEqual(cube.calculate_area(), 6)
        self.assertEqual(cube.calculate_volume(), 1)
    
    def test_cube_with_decimals(self):
        """Test cube with decimal side length."""
        cube = Cube(2.5)
        self.assertAlmostEqual(cube.calculate_area(), 37.5, places=5)
        self.assertAlmostEqual(cube.calculate_volume(), 15.625, places=5)
    
    def test_cube_implements_interface(self):
        """Test that Cube implements IShape interface."""
        cube = Cube(4)
        self.assertIsInstance(cube, IShape)


class TestPolymorphism(unittest.TestCase):
    """Test polymorphic behavior across all shapes."""
    
    def test_all_shapes_have_calculate_area(self):
        """Test that all shapes can calculate area."""
        shapes = [Sphere(5), Cylinder(3, 7), Rectangle(4, 8), Cube(4)]
        for shape in shapes:
            self.assertTrue(hasattr(shape, 'calculate_area'))
            self.assertTrue(callable(getattr(shape, 'calculate_area')))
    
    def test_all_shapes_have_calculate_volume(self):
        """Test that all shapes can calculate volume."""
        shapes = [Sphere(5), Cylinder(3, 7), Rectangle(4, 8), Cube(4)]
        for shape in shapes:
            self.assertTrue(hasattr(shape, 'calculate_volume'))
            self.assertTrue(callable(getattr(shape, 'calculate_volume')))
    
    def test_shapes_return_numeric_values(self):
        """Test that all shapes return numeric values for calculations."""
        shapes = [Sphere(5), Cylinder(3, 7), Rectangle(4, 8), Cube(4)]
        for shape in shapes:
            area = shape.calculate_area()
            volume = shape.calculate_volume()
            self.assertIsInstance(area, (int, float))
            self.assertIsInstance(volume, (int, float))
            self.assertGreaterEqual(area, 0)
            self.assertGreaterEqual(volume, 0)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)