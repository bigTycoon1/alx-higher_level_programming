#!/usr/bin/python3


""" Module for test_base class """
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """ def test Class Base """

    def setUp(self):
        """ function to set up for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
<<<<<<< HEAD
        """ test_id assign """
=======
        """ test_id to assign """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """ test default id """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
<<<<<<< HEAD
        """ test nb object attr """
=======
        """ test id for nb object """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
<<<<<<< HEAD
        """ test nb obj attr and assign id """
=======
        """ test nb obj attrs and assigned id """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        """ test str id """
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
<<<<<<< HEAD
        """ test to pass more args """
=======
        """ test for more args method """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
<<<<<<< HEAD
        """ test to access private attrs """
=======
        """ test to access private attributes """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_1(self):
        """ test to save file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ test to save file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
