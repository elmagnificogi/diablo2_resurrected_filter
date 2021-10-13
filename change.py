import json
# f = open("item-names.json",'r',encoding='utf8')
#
# data = f.readlines()
# jd = json.load(f)
# print(jd)

my_json_data = []
or_json_data = []
new_json_data = []

with open('./item-names.json','r',encoding='utf-8-sig')as fp:
    my_json_data = json.load(fp)
    #print('这是文件中的json数据：',my_json_data)
    #print('这是读取到文件数据的数据类型：', type(json_data))


with open('./ori/item-names.json','r',encoding='utf8')as dp:
    or_json_data = json.load(dp)

light = []
mid = []
heavy = []
for item in my_json_data:
    #print(item["zhCN"])
    name = item["zhCN"]
    # 抽出来所有扩展装备id
    t = name.split("|")
    if len(t)>1:
        print(t)
        if '轻' in t[1]:
            light.append(item['id'])
    # 抽出来所有精华装备id
        if '中' in t[1]:
            mid.append(item['id'])
        if '重' in t[1]:
            heavy.append(item['id'])

    # 抽出来所有轻型装备id

    # 抽出来所有中型装备id

    # 抽出来所有重型装备id

    # 抽出来所有吐槽装备id

    # 抽出来所有优质底材id
print("所有轻型装备id")
print(light)