import random
import string

#输出26个大写字母
def upperletter():
    letters_repeat = string.ascii_letters.upper()
    letters_out = list()
    for item in letters_repeat:
        if item not in letters_out:
            letters_out.append(item)
    return letters_out

def car_letter():
    carletter = upperletter()
    carletter.remove('O')
    carletter.remove('I')
    return carletter

def car_letter1():
    carletter1 = upperletter()[0:8] + upperletter()[9:14] + upperletter()[15:]
    return carletter1

def genpassword(length):
    numOfNum = random.randint(1,length)
    numOfLetter = length - numOfNum
    slcNum = [random.choice(string.digits) for i in range(numOfNum)]
    #slcNum += str(random.randint(0, 9))

    slcLetter = [random.choice(car_letter()) for i in range(numOfLetter)]
    #打乱组合
    slcChar = slcLetter + slcNum
    #li = random.shuffle(li)返回None
    random.shuffle(slcChar)
    genpwd = ''.join(i for i in slcChar)
    return  genpwd

def gennum(a,b):
    result = random.randint(a, b)
    return result

def genageCN(a,b):
    result = random.randint(a, b)
    cnr = u'零一二三四五六七八九'
    ten_bit = result // 10
    a = ''
    if ten_bit == 1:
        a = a.join('十')
    elif ten_bit != 0:
        r = cnr[int(ten_bit)]
        a = a + r + '十'
    one_bit = result % 10
    if  one_bit != 0:
        r1 = cnr[int(one_bit)]
        a=a+r1
    return a

if __name__ == "__main__":
    print(genpassword(5))
    print(car_letter())
    print(gennum(18,65))
    print(genage(18,65))


