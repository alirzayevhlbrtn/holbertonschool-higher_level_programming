#!/usr/bin/python3
"""
test for Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id(self):
        ins = Base(31)
        self.assertEqual(ins.id, 31)
        ins = Base(69)
        self.assertEqual(ins.id, 69)

    def test_idn(self):
        ins = Base(-31)
        self.assertEqual(ins.id, -31)

    def test_id0(self):
        ins = Base()
        self.assertEqual(ins.id, 1)
        ins = Base(None)
        self.assertEqual(ins.id, 2)

    def test_str(self):
        ins = Base("Hesenoglandi")
        self.assertEqual(ins.id, "Hesenoglandi")
        ins = Base("Huseynoglandeyilamma")
        self.assertEqual(ins.id, "Huseynoglandeyilamma")

    def test_json(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')

    def test_json2(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])


if __name__ == "__main__":
    unittest.main()
