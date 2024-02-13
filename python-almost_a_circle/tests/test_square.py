#!/usr/bin/python3
"""
Test for square
"""
import os
import unittest
from models.square import Square


class TestBase(unittest.TestCase):
    def test_square(self):
        s1 = Square(3, 1)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 1)
        s2 = Square(3, 1, 6)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 6)
        sbig = Square(1, 2, 3, 4)
        self.assertEqual(sbig.size, 1)
        self.assertEqual(sbig.x, 2)
        self.assertEqual(sbig.y, 3)
        self.assertEqual(sbig.id, 4)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square("31")
        with self.assertRaises(TypeError):
            Square(3, "1")
        with self.assertRaises(TypeError):
            Square(3, 1, "31")

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            Square(-31)
        with self.assertRaises(ValueError):
            Square(31, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -31)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s0 = Square(1, id=777)
        self.assertEqual(str(s0), "[Square] (777) 0/0 - 1")

    def test_to_dictionary(self):
        s1 = Square(3, id=69)
        self.assertEqual(s1.to_dictionary(), {"id": 69, "size": 3, "x": 0, "y": 0})

    def test_update(self):
        s0 = Square(1, 2, 3, 4)
        s0.update(5, 6, 7, 8)
        self.assertEqual(s0.id, 5)

    def test_create(self):
        s1_dictionary = {"x": 3, "y": 4, "id": 89, "size": 1}
        s1 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 1")

    def test_save_to_file(self):
        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([Square(1, 2, id=13)])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 13, "size": 1, "x": 2, "y": 0}]')

    def test_load_from_file1(self):
        try:
            os.remove("Square.json")
        except:
            pass

        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_2(self):
        try:
            os.remove("Square.json")
        except:
            pass

        r1 = Square(5, 5)

        inp = [r1]
        Square.save_to_file(inp)
        out = Square.load_from_file()

        self.assertEqual(inp[0].__str__(), out[0].__str__())
