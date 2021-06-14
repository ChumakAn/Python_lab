from Models import Item
from Models import enum_gender
from Models import enum_country
from Models  import enum_target
from Models import enum_size
from Models import enum_sleeves
from Models import enum_length
class Shirts (Item):
    def __init__(self,_size: enum_size.Size = None, _gender: enum_gender.Gender = None, _name = None,_color = None,
                 _material = None, _brand = None,_origin_country: enum_country.Country = None, _price = None ,
                 _target: enum_target.Target = None, _type_of_sleeves: enum_sleeves.Sleeves = None,
                 _length: enum_length.Length = None):
        super().__init__( _size, _gender, _name, _color, _material, _brand, _origin_country, _price, _target)
        self._type_of_sleeves = _type_of_sleeves
        self._length = _length



    @property
    def type_of_sleeves(self):
        return self._type_of_sleeves

    @property
    def length(self):
        return self._length

    def __str__(self):
        return super().__str__() , "Type of sleeves:" , self._type_of_sleeves
        f , "Length:" , self._length