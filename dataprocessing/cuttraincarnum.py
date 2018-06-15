import json
import pathlib
import os
import shutil

with open('chuan.json') as f:
    data=json.load(f)
with open('carnum_gen_0528_1000_main.json') as f:
    data1=json.load(f)
data_id = []
id_all = []
for item in data:
    id_all.append(item["id"])
chuan_dc1 =[]
chuan_dc2 =[]
for item1 in data1:
    for item in data:
         if item1["write"]  == item["write"]:
             data_id.append(item["id"])
             chuan_dc1.append(item)
             # print('main'+str(item["id"]))
         else:
             chuan_dc2.append(item)

id_chuan=[]
print(len(id_all))
for e in id_all:
    if e not in data_id:
        id_chuan.append(e)
print(len(data_id))
print(data_id)
print(len(id_chuan))
print(id_chuan)

obj=json.dumps(chuan_dc1, ensure_ascii=False, indent=2)
file=open('chuan_dc1.json','w')
file.write(obj)
file.close()
obj=json.dumps(chuan_dc2, ensure_ascii=False, indent=2)
file=open('chuan_dc2.json','w')
file.write(obj)
file.close()

main_chuan = []
for i in data_id:
    stem = '{:05d}.wav'.format(i)
    main_chuan.append(stem)
print(main_chuan)
print(data_id)
p = pathlib.Path('./carnum_gen_0528_1000_main')
# wav_file = []
for file in p.glob('*.wav'):
   print(str(file).split('/')[1])
   # wav_file.append(str(file).split('/')[1])
   if str(file).split('/')[1] in main_chuan:
       print('1')
       os.rename(str(file), './carnum_dc_main'+str(file).split('/')[1])
       # shutil.move(file, '../carnum_dc_main'+str(file).split('/')[1])



