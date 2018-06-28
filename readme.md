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
      <td>全角字符unicode编码从65281~65374 （十
         
         
Goals
-----
Design Goals:

- easy to use
- easy to read (simple implementation, direct expression of algorithms)
- extensible

Non-Goals:

- efficiency
