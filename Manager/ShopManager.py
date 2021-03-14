from Models import enum_target
from Models import enum_sort_order
class ShopManager():
    def __init__(self, goods : list):
        self.goods = goods

    def search_by_ocassion(self,target:enum_target.Target):
       result = [ x for x in self.goods if x.target == target]
       for object in result:
           print(object.__str__())


    def sort_by_brand(self,sort_order:enum_sort_order.SortOrder):
        if sort_order == enum_sort_order.SortOrder.ASC:
           sorted_list = sorted(self.goods, key=lambda  x:x.brand, reverse= False)
        else:
           sorted_list = sorted(self.goods, key=lambda x: x.brand, reverse=True)

        for object in sorted_list:
            print(object.__str__())

    def sort_by_price(self,sort_order:enum_sort_order.SortOrder):
        if sort_order == enum_sort_order.SortOrder.ASC:
           sorted_list = sorted(self.goods, key=lambda  x:x.price, reverse= False)
        else:
           sorted_list = sorted(self.goods, key=lambda x: x.price, reverse=True)

        for object in sorted_list:
            print(object.__str__())