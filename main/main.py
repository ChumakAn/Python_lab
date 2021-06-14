from Models import *
from Manager import *

def main():
    object1 = Shoes(enum_gender.Gender.FEMALE,"Botinki","grey", "leather","Zara", enum_country.Country.TURKEY,1250,enum_target.Target.SPECIAL_OCCASION,39,enum_season.Season.AUTUMN)
    object2 = Trousers(enum_size.Size.M,enum_gender.Gender.MALE,"Oficials","black","denim","Reserved",enum_country.Country.BANGLADESH,3400,enum_target.Target.SPORT,enum_type.Type.JEANS)
    object3 = Shirts(enum_size.Size.L,enum_gender.Gender.UNISEX, "Blousyy","light pink", "cotton","Zara",enum_country.Country.CHINA,790,enum_target.Target.SPECIAL_OCCASION,enum_sleeves.Sleeves.LONG,enum_length.Length.STANDART)
    goods = [object1, object2, object3]
    list = ShopManager(goods)
    print(list.search_by_occasion(enum_target.Target.SPECIAL_OCCASION))
    print ("\n")
    print(list.sort_by_price(enum_sort_order.SortOrder.DESC))
    print("\n")
    print(list.sort_by_brand(enum_sort_order.SortOrder.ASC))
if __name__ == '__main__':
    main()
