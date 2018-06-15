from gendata.inherit import *

def carbrand_cut(filename,path1,path2):
    with open(filename) as fp:
        data = json.load(fp)
    home_output = list()
    inherit_out = list()
    i=0
    j=0
    for item in data:
        if item['write'][0:2] in ['进口'] or  item['ref'][0:2] in ['进口']:
            item['id'] = i
            inherit_out.append(item)
            i = i+1
        else:
            item['id'] = j
            home_output.append(item)
            j = j+1
    # return home_output,inherit_ou
    obj1=json.dumps(home_output,ensure_ascii=False,indent=2)
    file1= open(path1, 'w')
    file1.write(obj1)
    file1.close()
    obj = json.dumps(inherit_out, ensure_ascii=False, indent=2)
    file = open(path2, 'w')
    file.write(obj)
    file.close()

if __name__ =="__main__":
    filename = '/home/yzs/gendata/carbrand/carbrand_wrong/carbrandwrong_series_gen_0514_2472.json'
    path1='/home/yzs/gendata/10_phone_carbrand_out/homebrandwrong_0530.json'
    path2='/home/yzs/gendata/10_phone_carbrand_out/inheritbrandwrong_0530.json'
    carbrand_cut(filename,path1,path2)
