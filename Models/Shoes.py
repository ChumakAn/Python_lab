from Models import Item
from Models import enum_gender
from Models import enum_country
from Models import enum_target
from Models import enum_size
from Models import enum_season

class Shoes(Item):
    def __init__(self, _gender: enum_gender.Gender = None, _name = None, _color = None, _material = None,
                 _brand = None, _origin_country: enum_country.Country = None, _price = None ,
               _target: enum_target.Target = None, _size = None , _season: enum_season.Season = None):
      super().__init__(self, _gender, _name, _color, _material, _brand, _origin_country, _price,_target)
      self._size = _size
      self._season = _season


    @property
    def size(self):
        return self._size
    @property
    def season(self):
        return self._season

    def __str__(self):
        return super().__str__() , "Size:" , self._size , "Season:" , self._season