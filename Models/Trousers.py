from Models import Item
from Models import enum_gender
from Models import enum_country
from Models import enum_target
from Models import enum_size
from Models import enum_type
class Trousers(Item):
     def __init__(self,_size: enum_size.Size = None, _gender: enum_gender.Gender = None, _name = None,_color = None,
                 _material = None, _brand = None,_origin_country: enum_country.Country = None, _price = None ,
                 _target: enum_target.Target = None, _type: enum_type.Type = None):
         super().__init__(_size, _gender, _name, _color, _material, _brand, _origin_country, _price, _target)
         self._type = _type

     @property
     def type(self):
         return self._type


     def __str__(self):
         return super().__str__() , "Type:" , self._type