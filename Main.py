import json

f = open('route.json','r')

j = json.loads(f.read())
ff = open('data3.txt', 'w')
c = 0
for i in j['data']:
    l = str(i['properties']['pos'][0]) +';'+ str(i['properties']['pos'][1]) +';'+ str(i['properties']['heading'])
    c += 1
    if c%5 == 0:
        ff.write(l.replace('.',',')+'\n')
        c = 0
