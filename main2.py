import json
import matplotlib.pyplot as plt
import matplotlib.colors

f = open('1/buildRoute.json', 'r')

j = json.loads(f.read())


def get_jam(len_route):
    f = open('1/buildRoute.json', 'r')
    j = json.loads(f.read())
    probka = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3,
              3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1,
              1, 2, 3, 2, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 2, 2, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0, 0, 0]
    # set_p = set()
    # road_type = {'UNKNOWN': 0.1,
    #              'HARD': 0.3,
    #              'FREE': 0.1,
    #              'LIGHT': 0.2}
    # for i in j["data"]["routes"][0]["colorizeInfo"]:
    #     ch = road_type.get(i["type"])
    #     for j in range(i["count"]):
    #         probka.append(ch)

    f.close()
    print(len(probka))
    return probka


def get_route():
    route = []
    f = open('1/alongRoute.json', 'r')
    j = json.loads(f.read())
    x_min, x_max, y_min, y_max = 200,0,200,0

    for i in j["data"]:
        x = i["properties"]["pos"][0]
        if x < x_min and x != 0:
            x_min = x
        elif x > x_max:
            x_max = x
        y = i["properties"]["pos"][1]
        if y < y_min and y != 0:
            y_min = y
        elif y > y_max:
            y_max = y
        route.append(i["properties"]["pos"])
    f.close()
    limits = [[x_min, y_min],[x_max, y_max]]
    print(len(route))
    print(limits)
    return route, limits


def draw():
    get_route()
    print(max(get_route()))


def strech(jam, len_route):
    k = len_route/ len(jam)
    print(k)
    new = []
    c = 1
    for i in range(len(jam)-1):
        if jam[i] == jam[i+1]:
            c += 1
        else:
            new.append([jam[i], c])
            c = 1
    sum = 0
    for i in new:
        i[1] = round(i[1]*k)
        sum += i[1]
    new.append([0, len_route-sum])
    new_2 = []
    for i in new:
        for j in range(i[1]):
            new_2.append(i[0])
    print(new_2)
    print(len(new_2))
    return new_2

lim = [[82.875162, 54.94078899999477],
       [82.92177664157678, 54.99498199999472]]
r, l = get_route()
jam = get_jam(len(r))
d_x = lim[1][0] - lim[0][0]
d_y = lim[1][1] - lim[0][1]
strech(jam, len_route=len(r))
colors_i = strech(jam, len_route=len(r))
colormap = []
plt.scatter(x=[i[0] for i in r], y=[i[1] for i in r], c=colors_i)
plt.show()
