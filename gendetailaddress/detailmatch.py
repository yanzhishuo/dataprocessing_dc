from weight_choice import *
from pyexcel import *
from genpassword import *
from random import *
import string

building = readexcel(0,'/home/yzs/Downloads/data_require/addressdetail/国内主要大厦中英文名称对照.xls')
zuo = '座'
qu = '区'
upper = chr(randint(65,90))
a= str(choice(string.digits))
# detail = [chr(randint(65,90))+'座',chr(randint(65,90))+'区',str(choice(string.digits))+upper,str(choice(string.digits))+choice(['单元','层','楼']),
#           str(gennum(1, 2000)),str(gennum(1,2000))+choice(['室','号','栋','号楼'])]
detail = [chr(randint(65,90))+'座',chr(randint(65,90))+'区',str(choice(string.digits))+upper,str(choice(string.digits))+choice(['单元','层','楼']),
          str(gennum(1, 2000))+choice(['室','号','栋','号楼'])]
def detailmatch(index):
    detailmatch = sample(detail,index)
    detailmatched =str()
    for e in detailmatch:
        detailmatched = detailmatched+e
    return detailmatched,detailmatch[0],detailmatch[len(detailmatch)-1]
def detailaddress(index):
    a = choice(building)
    b,c,d = detailmatch(choice([1,2,3]))
    detailaddress= a+b
    if index==1:
        ref =detailaddress
        m_road =1
        m_roaddetail=1
    elif index ==2:
        ref = a
        m_road = 1
        m_roaddetail = 2
    elif index==3:
        ref = a+c
        m_road = 1
        m_roaddetail = 1.5
    else:
        ref = a + d
        m_road = 1
        m_roaddetail = 1.5
    return detailaddress,ref,a,b,m_road,m_roaddetail

def detailnomatch(index):
    a, no_a = sample(building,2)
    b,c,d = detailmatch(choice([1,2,3]))
    detailaddress= a+b
    if index==1:
        ref = no_a
        m_roaddetail = 2
    elif index ==2:
        ref = no_a + b
        m_roaddetail = 1
    elif index==3:
        ref = no_a+c
        m_roaddetail = 1.5
    else:
        ref = no_a + d
        m_roaddetail = 1.5
    return detailaddress,ref,a,b,m_roaddetail

if __name__=="__main__":
    # print(choice(building)+detailmatch(choice([1,2,3])))
    # print(detailaddress(1))
    print(detailnomatch(3))
