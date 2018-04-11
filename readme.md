dataprocessing项目各个程序的功能
==============================================================

> 1.sqlite2json.py:数据库里面合并json文件 加入asr等
   quanjiao2banjiao.py:json文件的asr全角转半角,并去掉asr为空的数据

> 2.dataprocessing.py:提取每个asr为一句话放到anafora平台解析  (!!!!注意:要每次给一次权限)

> 3.parse.py:将anafora平台的.xml文件(加标签)转成json

<table>
   <tr>
      <th>                        </th>
      <th>代码名字</th>
      <th>函数定义</th>
      <th>使用参数</th>
      <th>主要代码</th>
       <th>说明</th>
       <th>地址</th>
       <th>附录</th>
  </tr>
   <tr>
      <td>1</td>
      <td>quanjiao2banjiao.py</td>
      <td>DBC2SBC</td>
      <td>输入是字符串</td>
      <td>ord(str)-0xfee0</td>
      <td>全角字符unicode编码从65281~65374 （十六进制 0xFF01 ~ 0xFF5E）半角字符unicode编码从33~126 （十六进制 0x21~ 0x7E）特例：空格比较特殊，全角为 12288（0x3000），半角为 32（0x20） </td>
      <td>ssh://git@vcs.fore.run:18622/yzs/dataprocessing.git</td>
      <td>hex(10):10进制->16   int('0x10', 16) 16进制->10 oct:10->8  chr(i)返回i对应的ASCII,与ord正好相反</td>
  </tr>
</table>

dataprocessing主要干的事情:
------------------------------
1. db -> json
2. json -> db 地址是 data@dc8:~/yanghongkai/recorder_server_data/dialog_record_20180408_5000
3. json -> anafora
4. anafora -> json


不要把.py文件命名为 库.py会被调用!!!
===============================================================