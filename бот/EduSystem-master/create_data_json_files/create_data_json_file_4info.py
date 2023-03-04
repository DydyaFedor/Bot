import json
categories = []
item_cat1 = {}
item_cat1["id"] = 1
item_cat1["name"] = "Хобби"
item_cat1["desc"] = "Ваши увлечения"
sub_categories = []
item_sub_cat1 = {}
item_sub_cat1["id"] = 1
item_sub_cat1["name"] = "Коллекционирование марок"
item_sub_cat1["desc"] = "История и оценки марок"
# item_sub_cat1["image"] = "История и оценки марок"

sub_categories.append(item_sub_cat1)
item_sub_cat2 = {}
item_sub_cat2["id"] = 2
item_sub_cat2["name"] = "Вышивание"
item_sub_cat2["desc"] = "Примеры ручных работ"
sub_categories.append(item_sub_cat2)
item_cat1["sub_categories"] = sub_categories
categories.append(item_cat1)

item_cat2 = {}
item_cat2["id"] = 2
item_cat2["name"] = "Домашние животные"
item_cat2["desc"] = "Увлечения с вашими любимцами"
sub_categories = []
item_sub_cat1 = {}
item_sub_cat1["id"] = 1
item_sub_cat1["name"] = "Кошки"
item_sub_cat1["desc"] = "Обсуждают своих домашних питомцев"
sub_categories.append(item_sub_cat1)
item_sub_cat2 = {}
item_sub_cat2["id"] = 2
item_sub_cat2["name"] = "Собаки"
item_sub_cat2["desc"] = "Обсуждают своих домашних питомцев"
sub_categories.append(item_sub_cat2)
item_sub_cat3 = {}
item_sub_cat3["id"] = 3
item_sub_cat3["name"] = "Хомячки"
item_sub_cat3["desc"] = "Обсуждают своих домашних питомцев"
sub_categories.append(item_sub_cat3)
item_cat2["sub_categories"] = sub_categories
categories.append(item_cat2)
jsonstring = json.dumps(categories, ensure_ascii=False)
with open('categories.json', 'w+', encoding='utf-8') as f:
    f.write(jsonstring)
