import unittest
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    # Тесты на площадь
    def test_area_positive_integers(self):
        # Тестирование площади с положительными целыми числами
        self.assertEqual(area(5, 3), 15)
        self.assertEqual(area(10, 4), 40)
        self.assertEqual(area(1, 1), 1)
    
    def test_area_zero_values(self):
        # Тестирование площади с нулевыми значениями
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 0), 0)
    
    def test_area_large_numbers(self):
        # Тестирование площади с большими числами
        self.assertEqual(area(1000, 500), 500000)
        self.assertEqual(area(123, 456), 56088)

    def test_area_negative_values(self):
        # Тестирование обработки ошибок для площади с отрицательными числами
        with self.assertRaises(ValueError):
            area(-5, 3)
        with self.assertRaises(ValueError):
            area(5, -3)
        with self.assertRaises(ValueError):
            area(-5, -3)
        
    def test_area_float_values(self):
        # Тестирование площади с дробными числами
        self.assertEqual(area(5.5, 2), 11.0)
        self.assertEqual(area(3, 2.5), 7.5)
        self.assertEqual(area(2.5, 2.5), 6.25)
    
    # Тесты на периметр

    def test_perimeter_positive_integers(self):
        # Тестирование периметра с положительными целыми числами
        self.assertEqual(perimeter(5, 3), 16)
        self.assertEqual(perimeter(10, 4), 28)
        self.assertEqual(perimeter(1, 1), 4)
    
    def test_perimeter_zero_values(self):
        # Тестирование периметра с нулевыми значениями
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(5, 0), 10)
        self.assertEqual(perimeter(0, 0), 0)
    
    def test_perimeter_large_numbers(self):
        # Тестирование периметра с большими числами
        self.assertEqual(perimeter(1000, 500), 3000)
        self.assertEqual(perimeter(123, 456), 1158)

    def test_perimeter_negative_values(self):
        # Тестирование обработки ошибок для периметра с отрицательными числами
        with self.assertRaises(ValueError):
            perimeter(-5, 3)
        with self.assertRaises(ValueError):
            perimeter(5, -3)
        with self.assertRaises(ValueError):
            perimeter(-5, -3)

    def test_perimeter_float_values(self):
        # Тестирование периметра с дробными числами
        self.assertEqual(perimeter(5.5, 2), 15.0)
        self.assertEqual(perimeter(3, 2.5), 11.0)
        self.assertEqual(perimeter(2.5, 2.5), 10.0)

if __name__ == '__main__':
    unittest.main()