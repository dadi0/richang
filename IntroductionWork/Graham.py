import math
from operator import *

def area(ans_list):#以选出正确点且按包围顺序排好
    s1 = ans_list[:2]
    del ans_list[0:2]
    s = 0
    for i in ans_list:
        x1 = s1[1][0] - s1[0][0]
        y1 = s1[1][1] - s1[0][1]
        x2 = i[0] - s1[0][0]
        y2 = i[1] - s1[0][1]
        s += x1 * y2 - x2 * y1
        s1.pop()
        s1.append(i)
    s = s / 2
    return s

def convex_hull(point_list):#已经排好序
    if len(point_list) < 3:
        return -1
    end_point = point_list[:2]
    del point_list[:2]
    for i in point_list:
        x1 = end_point[-1][0] - end_point[-2][0]
        y1 = end_point[-1][1] - end_point[-2][1]
        x2 = i[0] - end_point[-2][0]
        y2 = i[1] - end_point[-2][1]
        tag = x1 * y2 - x2 * y1
        while tag <= 0:
            end_point.pop()
            x1 = end_point[-1][0] - end_point[-2][0]
            y1 = end_point[-1][1] - end_point[-2][1]
            x2 = i[0] - end_point[-2][0]
            y2 = i[1] - end_point[-2][1]
            tag = x1 * y2 - x2 * y1
        end_point.append(i)
    return area(end_point)

def psort(enter_list):
    enter_list.sort(key=itemgetter(1, 0))
    point = enter_list[0]
    tag1 = []
    for i in range(1, len(enter_list)):
        lengthc = math.sqrt((enter_list[i][0]-point[0])**2+(enter_list[i][1]-point[1])**2)
        if lengthc == 0:
            continue
        else:
            cos = (enter_list[i][0]-point[0])/lengthc
        tag1.append((i, -cos))
    tag1.sort(key=itemgetter(1))
    tag2 = []
    for i in range(len(tag1)-1):
        if tag1[i][1] != tag1[i+1][1]:
            tag2.append(tag1[i])
    tag2.append(tag1[-1])
    tag3 = [0]
    for i in range(len(tag2)):
        tag3.append(tag2[i][0])
    enter_list_sort = []
    for i in tag3:
        enter_list_sort.append(enter_list[i])
    return convex_hull(enter_list_sort)
