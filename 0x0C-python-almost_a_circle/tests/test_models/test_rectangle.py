#!/usr/bin/python3


<<<<<<< HEAD
""" Module for Rectangle Class Tests """
=======
""" Module for test Rectangle class """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """ Function to test Rectangle class """

    def setUp(self):
<<<<<<< HEAD
        """ Method instance for each test """
=======
        """ Instance method for each test """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """ test new rectangle """
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_rectangle_2(self):
<<<<<<< HEAD
        """ test new rectangle with all attrs """
=======
        """ test new rectangle """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        new = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_rectangles(self):
        """ test new rectangles """
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """ test Rectangle is a Base instance """
        new = Rectangle(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amount_attrs(self):
<<<<<<< HEAD
        """ test incorrect raise with 1 arg passed """
=======
        """ test incorrecte with a arg passed """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        with self.assertRaises(TypeError):
            new = Rectangle(1)

    def test_incorrect_amount_attrs_1(self):
<<<<<<< HEAD
        """ test incorrect raised with no args passed """
=======
        """ test incorect args passed """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_access_private_attrs(self):
<<<<<<< HEAD
        """ test to access to a private attribute """
=======
        """ test to access private attribute """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
<<<<<<< HEAD
        """ test to access to a private attribute """
=======
        """ test to access private attribute """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
<<<<<<< HEAD
        """ test to access to a private attribute """
=======
        """ test to access private attribute """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
<<<<<<< HEAD
        """ test to access to a private attribute """
=======
        """ test to access private attribute """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valide_attrs(self):
<<<<<<< HEAD
        """ test valide attr """
=======
        """ test valid attr """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        with self.assertRaises(TypeError):
            new = Rectangle("2", 2, 2, 2, 2)

    def test_valide_attrs_2(self):
<<<<<<< HEAD
        """ test valide attr """
=======
        """ test valid attr """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        with self.assertRaises(TypeError):
            new = Rectangle(2, "2", 2, 2, 2)

    def test_valide_attrs_3(self):
<<<<<<< HEAD
        """ test valide attribute """
=======
        """ test valid attr """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, "2", 2, 2)

    def test_valide_attrs_4(self):
<<<<<<< HEAD
        """ tets valide attribute """
=======
        """ test valid attr """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, 2, "2", 2)

    def test_value_attrs(self):
<<<<<<< HEAD
        """ test value attributes """
=======
        """ test values attr """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        with self.assertRaises(ValueError):
            new = Rectangle(0, 1)

    def test_value_attrs_1(self):
<<<<<<< HEAD
        """ test value attribute """
=======
        """ test values attr """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        with self.assertRaises(ValueError):
            new = Rectangle(1, 0)

    def test_value_attrs_2(self):
<<<<<<< HEAD
        """ test value attribute """
=======
        """ test value attr """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, -1)

    def test_value_attrs_3(self):
<<<<<<< HEAD
        """ test value attribute """
=======
        """ test value attr """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, 1, -1)

    def test_area(self):
<<<<<<< HEAD
        """ Check the return value of test area """
=======
        """ test the value of area method """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        new = Rectangle(4, 5)
        self.assertEqual(new.area(), 20)

    def test_area_2(self):
<<<<<<< HEAD
        """ Check the return value of test area """
=======
        """ test the value of area method """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        new = Rectangle(2, 2)
        self.assertEqual(new.area(), 4)
        new.width = 5
        self.assertEqual(new.area(), 10)
        new.height = 5
        self.assertEqual(new.area(), 25)

    def test_area_3(self):
<<<<<<< HEAD
        """ Check the return value of test area """
=======
        """ test the value of area method """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        new = Rectangle(3, 8)
        self.assertEqual(new.area(), 24)
        new2 = Rectangle(10, 10)
        self.assertEqual(new2.area(), 100)

    def test_display(self):
<<<<<<< HEAD
        """ Test str displayed """
=======
        """ test str display printed """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
<<<<<<< HEAD
        """ test str displsyed """
=======
        """ test str display printed """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        r1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ test __str__ value """
        r1 = Rectangle(2, 5, 2, 4)
        res = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        """ test __str__ value """
        r1 = Rectangle(3, 2, 8, 8, 10)
        res = "[Rectangle] (10) 8/8 - 3/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r1.id = 1
        r1.width = 7
        r1.height = 15
        res = "[Rectangle] (1) 8/8 - 7/15\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        """ test __str__ value """
        r1 = Rectangle(5, 10)
        res = "[Rectangle] (1) 0/0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(25, 86, 4, 7)
        res = "[Rectangle] (2) 4/7 - 25/86\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r3 = Rectangle(1, 1, 1, 1)
        res = "[Rectangle] (3) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r3)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        """ test __str__ value """
        r1 = Rectangle(3, 3)
        res = "[Rectangle] (1) 0/0 - 3/3"
        self.assertEqual(r1.__str__(), res)

    def test_display_3(self):
<<<<<<< HEAD
        """ test str displayed """
=======
        """ test str display printed """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        r1 = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
<<<<<<< HEAD
        """ test str displayed """
=======
        """ test str display printed """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        r1 = Rectangle(3, 2)
        res = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.x = 4
        res = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.y = 2
        res = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary(self):
        """ test to dict """
        r1 = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ test to dict """
        r1 = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(5, 7)
        res = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
<<<<<<< HEAD
        """ test dict to JSON str """
=======
        """ test dictionary to JSON """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_check_value(self):
<<<<<<< HEAD
        """ test check value """
=======
        """ check test value """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_check_value_2(self):
<<<<<<< HEAD
        """ test check value """
=======
        """ check test value """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)

    def test_create(self):
<<<<<<< HEAD
        """ test to create """
=======
        """ create test method """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        dictionary = {'id': 89}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)

    def test_create_2(self):
<<<<<<< HEAD
        """ test to create """
=======
        """ create test method """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        dictionary = {'id': 89, 'width': 1}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_create_3(self):
<<<<<<< HEAD
        """ test to create """
=======
        """ create test method """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        dictionary = {'id': 89, 'width': 1, 'height': 2}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_create_4(self):
<<<<<<< HEAD
        """ test to create """
=======
        """ create test method """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_create_5(self):
<<<<<<< HEAD
        """ test to create """
=======
        """ create test method """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_load_from_file(self):
        """ test load frm file """
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_load_from_file_2(self):
<<<<<<< HEAD
        """ test load frm file """
=======
        """ test load from file """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        linput = [r1, r2]
        Rectangle.save_to_file(linput)
        loutput = Rectangle.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
