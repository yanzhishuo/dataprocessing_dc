from gendata.inherit import *
import string
from random import *

head =['','我本次申请的贷款金额是','金额是','贷款','借款','金额啊','申请贷款','贷款金额','','','','','','','','','','','']
tail =['','','','块钱','块钱','元','元','啊','元的','元整']

def money(number):
    if number == 4:
        money = choice(['5','6','7','8','9'])+choice(string.digits)+'00'
    elif number == 5:
        money = choice(['1','2','3','4','5', '6', '7', '8', '9'])\
                + choice(string.digits) + choice(string.digits)+ '00'
    else:
        money1 = '1'+ choice(string.digits) +choice(['0','0','0','0','0','0','0','1','2','3','4','5', '6', '7', '8', '9'])+ '000'
        money2 = '200000'
        money = choice([money1,money2])
    return money

# print(money(choice([4,5,6])))
if __name__=="__main__":
    dataneed_data = list()
    num = 5000
    path = 'loanamount'
    for i in range(num):
        dataneed_dict = dict()
        a = money(choice([4,5,6]))
        b= choice(head)+a+choice(tail)
        dataneed_dict['label_name'] = path
        dataneed_dict['id'] = i
        dataneed_dict['ref'] = b
        dataneed_dict['write'] = a
        dataneed_data.append(dataneed_dict)
    obj = json.dumps(dataneed_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/gendata/' + path + '_gen_' + str(datenow()) + '_' + str(num) + '.json', 'w')
    file.write(obj)
    file.close()
