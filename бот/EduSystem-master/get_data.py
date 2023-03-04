import json


def load_data():
    content = ""
    with open('categories.json', 'r', encoding='utf-8') as f:
        content = f.read()
    # print(content)
        categories = json.loads(content)
        return categories


def get_categories(categories):
    str1 = "Выберите раздел: \n"
    for category in categories:
        str1 += f"{category['id']} {category['name']} - {category['desc']} \n"
    return str1


def get_sub_categories(categories, cat_id):
    str1 = "Выберите интересующую тему: \n"

    for category in categories:
        if category['id'] == cat_id:
            for sub_category in category['sub_categories']:
                str1 = str1 + \
                    f"{sub_category['id']} - {sub_category['name']} \n"
    return str1


def get_desc(categories, cat_id, theme_id):
    for category in categories:
        if category['id'] == cat_id:
            for sub_category in category['sub_categories']:
                if sub_category['id'] == theme_id:
                    return sub_category['desc'], sub_category['img']


if __name__ == "__main__":
    categories = load_data()
    str1 = get_categories(categories)
    print(str1)
    cat_id = int(input("Введите номер катергории: "))
    str1 = get_sub_categories(categories, cat_id)
    print(str1)
    theme_id = int(input("Введите номер темы для общения: "))
    data = get_desc(categories, cat_id, theme_id)
    print(data)
    # for item in data:
    #     desc = item[0]
    #     img = item[1]
    #     print(f"{desc} - {img}")
