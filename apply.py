import json

light = []
mid = []
heavy = []
epic = []
ext = []
material = []
comment = {}
float_value = {}

with open('./table/好底材id.json','r',encoding='utf8')as dp:
    material = json.load(dp)
with open('./table/精华装备id.json','r',encoding='utf8')as dp:
    epic = json.load(dp)
with open('./table/扩展装备id.json','r',encoding='utf8')as dp:
    ext = json.load(dp)
with open('./table/轻型装备id.json','r',encoding='utf8')as dp:
    light = json.load(dp)
with open('./table/中型装备id.json','r',encoding='utf8')as dp:
    mid = json.load(dp)
with open('./table/重型装备id.json','r',encoding='utf8')as dp:
    heavy = json.load(dp)
with open('./table/装备浮动数值.json','r',encoding='utf8')as dp:
    float_value = json.load(dp)
with open('./table/装备吐槽.json','r',encoding='utf8')as dp:
    comment = json.load(dp)

a = input()
a +=1
#
# for item in my_json_data:
#     # print(item["zhCN"])
#     name = item["zhCN"]
#
#     t = name.split("|")
#     if len(t)>1:
#         #print(t)
#         # 抽出来所有轻型装备id
#         if '轻' in t[1]:
#             light.append(item['id'])
#         # 抽出来所有中型装备id
#         if '中' in t[1]:
#             mid.append(item['id'])
#         # 抽出来所有重型装备id
#         if '重' in t[1]:
#             heavy.append(item['id'])
#         # 抽出来所有扩展装备id
#         if '扩' in t[1]:
#             ext.append(item['id'])
#         # 抽出来所有精华装备id
#         if '精' in t[1]:
#             epic.append(item['id'])
#
#     # 抽出来所有优质底材id
#     t = name.find("*")
#     if t > 0:
#         if name.find("UP*2") != -1:
#             continue
#         #print(name)
#         material.append(item['id'])
#
#     # 抽出来所有浮动数值id
#     t = name.find("MAX:")
#     if t != -1:
#         t1 = item["zhTW"].find("MAX:")
#         n1 = item["zhTW"].find("]")
#
#         #print(name)
#         n = name.find("]")
#         float_value[item['id']]=[name[t:n],item["zhTW"][t1:n1]]
#         #print(float_value[item['id']])
#
#     t = name.find("ÿc2")
#     if t != -1:
#         n = name.find("\n",t+1,len(name))
#         t1 = item["zhTW"].find("ÿc2")
#         n1 = item["zhTW"].find("\n",t1+3,len(item["zhTW"]))
#         #print(name[t+3:n])
#         comment[item['id']] = [name[t+3:n],item["zhTW"][t1+3:n1]]
#     else:
#         t = name.find("\n")
#         n = name.find("MAX:")
#         if t != -1 and n==-1:
#             print(name)
#             t1 = item["zhTW"].find("\n")
#             comment[item['id']] = [name[:t], item["zhTW"][:t1]]
#
# print("所有轻型装备id")
# print(light)
# print("所有中型装备id")
# print(mid)
# print("所有重型装备id")
# print(heavy)
# print("所有扩展装备id")
# print(ext)
# print("所有精华装备id")
# print(epic)
# print("所有好底材id")
# print(material)
# print("所有装备浮动数值")
# print(float_value)
# print("所有吐槽")
# print(comment)