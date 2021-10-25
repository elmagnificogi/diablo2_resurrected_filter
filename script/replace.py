import json

light = []
mid = []
heavy = []
epic = []
ext = []
material = []
comment = {}
float_value = {}
abbreviation = []
item_names = {}
item_modifiers = {}
item_nameaffixes = {}
item_runes = {}

item_names = {}
item_modifiers = {}
item_nameaffixes = {}
item_runes = {}

new_item_names = []
new_item_nameaffixes = []

golds = []
greens = []

with open('../table/暗金物品名称.txt', 'r') as dp:
    golds = dp.readlines()
    # print(names)
with open('../table/绿色物品名称.txt', 'r') as dp:
    greens = dp.readlines()

with open('../开荒/item-names.json', 'r', encoding='utf-8-sig') as dp:
    item_names = json.load(dp)

def add_separator_suffix(name, separator, suffix):
    if separator != "":
        if name.find(separator) != -1:
            return name + suffix
    return name + separator + suffix


def find_index_in_array(id, array):
    index = 0
    for index in range(len(array)):
        if array[index]["id"] == int(id):
            return index
    return -1


def find_item_color(n):
    find = False
    for name in golds:
        name = name[:-1]
        if n == name:
            find = True
            break
    if find:
        return 0

    for name in greens:
        name = name[:-1]
        if n == name:
            find = True
            break
    if find:
        return 1

    return -1

def remove_color(name):
    temp = name
    index = []
    n = -2
    while(n!=-1):
        n=temp.find("ÿc")
        if n!= -1:
            index.append(n)
            temp = temp[0:n]+temp[n+3:]
    return temp   

for item in item_names:
    # print(item["zhCN"])
    name = item

    if find_item_color(name["enUS"]) == 1:
        # green item
        name["zhCN"] = remove_color(name["zhCN"])
        name["zhTW"] = remove_color(name["zhTW"])

    new_item_names.append(name)

with open('./item-names.json', 'w', encoding='utf-8-sig') as dp:
    dp.write(json.dumps(new_item_names, ensure_ascii=False, indent=2))
