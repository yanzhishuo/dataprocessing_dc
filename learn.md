linux命令:` find . -type f -exec chmod a-x {} \;`
==================================================
find
-----
### 1.type

-type 是find命令的一个参数：

-type:查找某一类型文档
b:块设备文档
d:目录
c:字符设备文档
P：管道文档
l:符号链接文档
f:普通文档

-type f 就是查找type为普通类型的文档。 

### 2.exec
exec选项后面跟随着所要执行的命令或脚本，然后是一对儿{ }，一个空格和一个，最后是一个分号。为了使用exec选项，必须要同时使用print选项。如果验证一下find命令，会发现该命令只输出从当前路径起的相对路径及文件名。
-exec： find命令对匹配的文件执行该参数所给出的shell命令。相应命令的形式为'command' { } ;，注意{ }和；之间的空格. ` 这样做会报错 `*怎么解决*
` 例如 find . -type f -exec ls -l { } ;`


chmod
----------
“chmod a-x”表示所有用户对此文件或目录将没有执行权限

“a”表示所有用户，“u”表示创建者、“g”表示创建者同组用户、“o”表示其他用户；“+”表示添加权限，“-”表示取消权限；“r”表示读权限、“w”表示写权限、“x”表示写权限

` sudo chmod -R 770 *` -rwx------ (700) -- 只有属主有读、写、执行权限
 
` sudo find -type d -exec chmod g+s {} \; `

 操作这些标志与操作文件权限的命令是一样的, 都是 chmod. 有两种方法来操作,

1) chmod u+s temp — 为temp文件加上setuid标志. (setuid 只对文件有效)

chmod g+s tempdir — 为tempdir目录加上setgid标志 (setgid 只对目录有效)

chmod o+t temp — 为temp文件加上sticky标志 (sticky只对文件有效)

2) 采用八进制方式. 对一般文件通过三组八进制数字来置标志, 如 666, 777, 644等. 如果设置这些特殊标志, 则在这组数字之外外加一组八进制数字. 如

4666, 2777等. 这一组八进制数字三位的意义如下,

abc

a - setuid位, 如果该位为1, 则表示设置setuid

b - setgid位, 如果该位为1, 则表示设置setgid

c - sticky位, 如果该位为1, 则表示设置sticky

设置完这些标志后, 可以用 ls -l 来查看. 如果有这些标志, 则会在原来的执行标志位置上显示. 如

rwsrw-r– 表示有setuid标志

rwxrwsrw- 表示有setgid标志

rwxrw-rwt 表示有sticky标志

#### tree -L 2 看结构

#### touch命令不常用，用来修改文件时间戳，或者新建一个不存在的文件。

# Git 用法
第一次建立仓库:
### Git global setup

git config --global user.name "yzs"

git config --global user.email "1353847394@qq.com"

### Create a new repository
git clone ssh://git@vcs.fore.run:18622/yzs/dataprocessing.git

cd dataprocessing

touch README.md

git add README.md

git commit -m "add README"

git push -u origin master

### Existing folder
cd existing_folder

git init

git remote add origin ssh://git@vcs.fore.run:18622/yzs/dataprocessing.git

git add .

git commit -m "Initial commit"

git push -u origin master

之后使用:
git remote -v 看有没有远程连接

重置远程链接:$ git remote set-url origin ssh://git@vcs.fore.run:18622/yzs/dataprocessing.git

git add 

git commit -m '随意写'

git pull

git push

另:git log 看改动

   git status 看状态
### git pull 时候出现冲突: 
Please, commit your changes or stash them before you can merge.
#### 解决办法
1.stash

通常遇到这个问题，你可以直接commit你的修改；但我这次不想这样。

看看git stash是如何做的。

git stash
git pull
git stash pop

接下来diff一下此文件看看自动合并的情况，并作出相应修改。

git stash: 备份当前的工作区的内容，从最近的一次提交中读取相关内容，让工作区保证和上次提交的内容一致。同时，将当前的工作区内容保存到Git栈中。
git stash pop: 从Git栈中读取最近一次保存的内容，恢复工作区的相关内容。由于可能存在多个Stash的内容，所以用栈来管理，pop会从最近的一个stash中读取内容并恢复。
git stash list: 显示Git栈内的所有备份，可以利用这个列表来决定从那个地方恢复。
git stash clear: 清空Git栈。此时使用gitg等图形化工具会发现，原来stash的哪些节点都消失了。


2.放弃本地修改，直接覆盖之

git reset --hard
git pull
   
 
# python
## 1.choice()
import random

random.choice( seq  )
seq -- 可以是一个列表，元组或字符串
## 2.pickle
python3.2中的pickle模块简单的理解是为了序列化/反序列化一个对象的，作用是可以把一个对象持久化存储。

pickle模块对数据的简单存储处理的方法：
import pickle
 
shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']
 

f = open(shoplistfile, 'wb')
 
pickle.dump(shoplist, f) # dump the object to a file
f.close()
 
del shoplist # remove the shoplist
 
f = open(shoplistfile, 'rb')

storedlist = pickle.load(f)

print(storedlist)

装工厂函数:
================
pip install fake-factory==0.7.4