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

with open('./table/好底材id.json', 'r', encoding='utf8') as dp:
    material = json.load(dp)
with open('./table/精华装备id.json', 'r', encoding='utf8') as dp:
    epic = json.load(dp)
with open('./table/扩展装备id.json', 'r', encoding='utf8') as dp:
    ext = json.load(dp)
with open('./table/轻型装备id.json', 'r', encoding='utf8') as dp:
    light = json.load(dp)
with open('./table/中型装备id.json', 'r', encoding='utf8') as dp:
    mid = json.load(dp)
with open('./table/重型装备id.json', 'r', encoding='utf8') as dp:
    heavy = json.load(dp)
with open('./table/装备浮动数值.json', 'r', encoding='utf8') as dp:
    float_value = json.load(dp)
with open('./table/装备吐槽.json', 'r', encoding='utf8') as dp:
    comment = json.load(dp)
with open('./table/名称缩短.json', 'r', encoding='utf8') as dp:
    abbreviation = json.load(dp)

with open('./table/暗金物品名称.txt', 'r') as dp:
    golds = dp.readlines()
    # print(names)
with open('./table/绿色物品名称.txt', 'r') as dp:
    greens = dp.readlines()

with open('./ori/item-names.json', 'r', encoding='utf-8-sig') as dp:
    item_names = json.load(dp)
# with open('./ori/item_modifiers.json','r',encoding='utf-8-sig')as dp:
#     item_modifiers = json.load(dp)
with open('./ori/item-nameaffixes.json', 'r', encoding='utf-8-sig') as dp:
    item_nameaffixes = json.load(dp)
with open('./ori/item-runes.json', 'r', encoding='utf-8-sig') as dp:
    item_runes = json.load(dp)


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


for item in item_names:
    # print(item["zhCN"])
    name = item
    if name["id"] in ext:
        name["zhCN"] = add_separator_suffix(name["zhCN"], "|", "扩")
        name["zhTW"] = add_separator_suffix(name["zhTW"], "|", "擴")
    if name["id"] in epic:
        name["zhCN"] = add_separator_suffix(name["zhCN"], "|", "精")
        name["zhTW"] = add_separator_suffix(name["zhTW"], "|", "精")
    if name["id"] in light:
        name["zhCN"] = add_separator_suffix(name["zhCN"], "|", "轻")
        name["zhTW"] = add_separator_suffix(name["zhTW"], "|", "輕")
    if name["id"] in mid:
        name["zhCN"] = add_separator_suffix(name["zhCN"], "|", "中")
        name["zhTW"] = add_separator_suffix(name["zhTW"], "|", "中")
    if name["id"] in heavy:
        name["zhCN"] = add_separator_suffix(name["zhCN"], "|", "重")
        name["zhTW"] = add_separator_suffix(name["zhTW"], "|", "重")
    if name["id"] in material:
        name["zhCN"] = add_separator_suffix(name["zhCN"], "", "ÿc1*")
        name["zhTW"] = add_separator_suffix(name["zhTW"], "", "ÿc1*")

    if str(name["id"]) in comment.keys():
        item_color = ""
        if find_item_color(name["enUS"]) == 0:
            item_color = "ÿc4"
        if find_item_color(name["enUS"]) == 1:
            item_color = "ÿc2"

        name["zhCN"] = "ÿc8" + comment[str(name["id"])][0] + "\n" + item_color + name["zhCN"]
        name["zhTW"] = "ÿc8" + comment[str(name["id"])][1] + "\n" + item_color + name["zhTW"]

    if str(name["id"]) in float_value.keys():
        item_color = ""
        if find_item_color(name["enUS"]) == 0:
            item_color = "ÿc4"
        if find_item_color(name["enUS"]) == 1:
            item_color = "ÿc2"

        name["zhCN"] = "ÿc3" + float_value[str(name["id"])][0] + "\n" + item_color + name["zhCN"]
        name["zhTW"] = "ÿc3" + float_value[str(name["id"])][1] + "\n" + item_color + name["zhTW"]

    index = find_index_in_array(name["id"], abbreviation)
    if index != -1:
        name = abbreviation[index]

    new_item_names.append(name)

for item in item_nameaffixes:
    # print(item["zhCN"])
    name = item
    index = find_index_in_array(name["id"], abbreviation)
    if index != -1:
        name = abbreviation[index]
    new_item_nameaffixes.append(name)

with open('./new_mod_files/item-names.json', 'w', encoding='utf-8-sig') as dp:
    dp.write(json.dumps(new_item_names, ensure_ascii=False, indent=2))
with open('./new_mod_files/item-nameaffixes.json', 'w', encoding='utf-8-sig') as dp:
    dp.write(json.dumps(new_item_nameaffixes, ensure_ascii=False, indent=2))
