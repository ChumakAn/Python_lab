from abc import ABC
from abc import abstractmethod
from Models import enum_country
from Models import enum_gender
from Models import enum_size
from Models import enum_target

class Item(ABC):

    def __init__(self, _size: enum_size.Size , _gender: enum_gender.Gender, _name, _color, _material,
                 _brand, _origin_country: enum_country.Country, _price, _target: enum_target.Target):
        self._size = _size
        self._gender = _gender
        self._name = _name
        self._color = _color
        self._material = _material
        self._brand = _brand
        self._origin_country = _origin_country
        self._price = _price
        self._target = _target

    @property
    def size(self):
        return self._size

    @property
    def gender(self):
        return self._gender

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color
    @property
    def material(self):
        return self._material
    @property
    def brand(self):
        return self._brand
    @property
    def origin_country(self):
        return self._origin_country

    @property
    def price(self):
        return self._price

    @property
    def target(self):
        return self._target


    @abstractmethod
    def __str__(self):
        print("Name:", self._name)
        print("Size:", self._size)
        print("Gender:", self._gender)
        print("Color:", self._color)
        print("Material:", self._material)
        print("Brand:", self._brand)
        print("Origin country:", self._origin_country)
        print("Price:", self._price)
        print("Target:", self._target)
