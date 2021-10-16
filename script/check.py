import json
# f = open("item-names.json",'r',encoding='utf8')
#
# data = f.readlines()
# jd = json.load(f)
# print(jd)

golds = []
greens = []
or_json_data = []
new_json_data = []

with open('./item-names.json','r',encoding='utf-8-sig')as fp:
    or_json_data = json.load(fp)

with open('./table/暗金物品名称.txt','r')as dp:
    golds = dp.readlines()
    #print(names)
with open('./table/绿色物品名称.txt','r')as dp:
    greens = dp.readlines()

for name in greens:
    find = True
    name = name[:-1]
    for item in or_json_data:
        # print(item["zhCN"])
        n = item["enUS"]
        #print(n)
        # if item["id"] == 2574:
        #     print(item["enUS"])
        if n == name:
            find = True
            break
        else:
            find=False
    if not find:
        print("cant find:",name)
