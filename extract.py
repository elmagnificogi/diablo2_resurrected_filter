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

with open('./ori/item-names.json','r',encoding='utf-8-sig')as dp:
    or_json_data = json.load(dp)

light = []
mid = []
heavy = []
epic = []
ext = []
material = []
comment = {}
float_value = {}
for item in my_json_data:
    # print(item["zhCN"])
    name = item["zhCN"]

    t = name.split("|")
    if len(t)>1:
        #print(t)
        # 抽出来所有轻型装备id
        if '轻' in t[1]:
            light.append(item['id'])
        # 抽出来所有中型装备id
        if '中' in t[1]:
            mid.append(item['id'])
        # 抽出来所有重型装备id
        if '重' in t[1]:
            heavy.append(item['id'])
        # 抽出来所有扩展装备id
        if '扩' in t[1]:
            ext.append(item['id'])
        # 抽出来所有精华装备id
        if '精' in t[1]:
            epic.append(item['id'])

    # 抽出来所有优质底材id
    t = name.find("*")
    if t > 0:
        if name.find("UP*2") != -1:
            continue
        #print(name)
        material.append(item['id'])

    # 抽出来所有浮动数值id
    t = name.find("MAX:")
    if t != -1:
        t1 = item["zhTW"].find("MAX:")
        n1 = item["zhTW"].find("]")

        #print(name)
        n = name.find("]")
        float_value[item['id']]=[name[t:n],item["zhTW"][t1:n1]]
        #print(float_value[item['id']])

    t = name.find("ÿc2")
    if t != -1:
        n = name.find("\n",t+1,len(name))
        t1 = item["zhTW"].find("ÿc2")
        n1 = item["zhTW"].find("\n",t1+3,len(item["zhTW"]))
        #print(name[t+3:n])
        comment[item['id']] = [name[t+3:n],item["zhTW"][t1+3:n1],0]
    else:
        t = name.find("\n")
        n = name.find("MAX:")
        if t != -1 and n==-1:
            #print(name)
            t1 = item["zhTW"].find("\n")
            comment[item['id']] = [name[:t], item["zhTW"][:t1],1]
        elif t!=-1 and n!=-1:
            m = name.find("\n",t+1,len(name))
            if m!=-1:
                #print(name)
                comment[item['id']] = [name[t:m], item["zhTW"][t:m],2]

print("所有轻型装备id")
print(light)
print("所有中型装备id")
print(mid)
print("所有重型装备id")
print(heavy)
print("所有扩展装备id")
print(ext)
print("所有精华装备id")
print(epic)
print("所有好底材id")
print(material)
print("所有装备浮动数值")
print(float_value)
print("所有吐槽")
print(json.dumps(comment, ensure_ascii=False))

with open('./float_value.json','w',encoding='utf-8')as fp:
    fp.write(json.dumps(float_value,ensure_ascii=False))

with open('./comment.json','w',encoding='utf-8')as fp:
    fp.write(json.dumps(comment,ensure_ascii=False))