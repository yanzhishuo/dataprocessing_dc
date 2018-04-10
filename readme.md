dataprocessing项目各个程序的功能
==============================================================

> 1.sqlite2json.py:数据库里面合并json文件 加入asr等
   quanjiao2banjiao.py:json文件的asr全角转半角,并去掉asr为空的数据

> 2.dataprocessing.py:提取每个asr为一句话放到anafora平台解析  (!!!!注意:要每次给一次权限)

> 3.parse.py:将anafora平台的.xml文件(加标签)转成json(具体操作还有*疑问*???)

<table><tr><th>Tables</th><th>Are</th><th>Cool</th></tr><tr><td>col 1 is</td><td>left-aligned</td><td>$1600</td></tr><tr><td>col 2 is</td><td>centered</td><td>$12</td></tr><tr><td>col 3 is</td><td>right-aligned</td><td>$1</td></tr></table>


dataprocessing主要干的事情:
------------------------------
1. db -> json
2. json -> db 地址是 data@dc8:~/yanghongkai/recorder_server_data/dialog_record_20180408_5000
3. json -> anafora
4. anafora -> json


不要把.py文件命名为 库.py会被调用!!!
===============================================================