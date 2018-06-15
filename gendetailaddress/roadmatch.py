from weight_choice import *
from pyexcel import *
from genpassword import *
from random import *

road = readexcel(0,'/home/yzs/Downloads/data_require/addressdetail/road/全国路名.xlsx')
zhen = readexcel(3,'/home/yzs/Downloads/data_require/addressdetail/indetail.xlsx')
cun = readexcel(4,'/home/yzs/Downloads/data_require/addressdetail/indetail.xlsx')

def middle_address(index):
    if index==1:
        middle = choice(road)
    else:
        a = choice([1,2])
        if a ==1:
            middle = choice(zhen)+choice(cun)
        else:
            middle = choice(zhen)
    return middle

#路
#镇村
def mark():
    # tail =['号','','弄','巷']
    tail =['号','弄','巷']
    l = [1,2,3,4]
    num = gennumpassword(l[windex([3,1,1,1])])
    mark = num + tail[windex([6,1,1,1])]
    if num == '0':
        mark = '45号'
    return mark

def roadmatch(index):
    middle_out = middle_address(index)
    mark_out = mark()
    out = middle_out+mark_out
    if index==1:
        ref =out
        m_road =1
        m_roaddetail=1
    else:
        ref = middle_out
        m_road = 1
        m_roaddetail = 2
    return out,ref,middle_out,mark_out,m_road,m_roaddetail

def roadnomatch(index):
    mark_out = mark()
    if index==1:
        middle_out,ref=sample(road,2)
        m_road = 0
    else:
        a = choice([1, 2])
        if a == 1:
            middle_out,ref = sample(zhen+cun,2)
        else:
            middle_out,ref = sample(zhen,2)
        m_road = 0
    out = middle_out + mark_out
    return out,ref,middle_out,mark_out,m_road

if __name__=="__main__":
    l=[1,2]
    # print(roadmatch(l[windex([8,1])]))
    for i in range(10):
        a=windexint([2,1])
        print(a)
        print(roadnomatch(l[a]))
        # print(roadnomatch(choice([1,2])))
