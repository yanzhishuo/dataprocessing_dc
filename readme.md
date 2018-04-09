#dataprocessing 各个程序的功能

-1.sqlite2json.py:数据库里面合并json文件 加入asr等
   quanjiao2banjiao.py:json文件的asr全角转半角,并去掉asr为空的数据

-2.dataprocessing.py:提取每个asr为一句话放到anafora平台解析  (!!!!注意:要每次给一次权限)

-3.parse.py:将anafora平台的.xml文件(加标签)转成json(具体操作还有疑问???)