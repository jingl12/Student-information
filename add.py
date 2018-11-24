# -*- coding: utf-8 -*-
# @Author: 境
# @Date:   2018-11-24 09:36:37
lst=[]
class Student():
    def __init__(self,Id,name,age,major):
        self.Id=Id
        self.name=name
        self.age=age
        self.major=major

def inp():
    print('-----input student massage!-----')
    Id=input('学生ID:')
    name=input('姓名:')
    age=input('年龄:')
    major=input('专业:')

    return Id,name,age,major

ls=inp()
stu=Student(ls[0],ls[1],ls[2],ls[3])

lst.append(stu.__dict__)
print('-'*10,'是否继续添加？','-'*10,)
print()
print('#'*5,'继续，请输入“yes”-----返回，请输入“exit”','#'*5)
print()

while True:
    x=input('是否继续>>>')
    if x=='yes':
        ls=inp()
        stu=Student(ls[0],ls[1],ls[2],ls[3])
        lst.append(stu.__dict__)
    elif x=='exit':
        break
    else:
        print('请输入正确的选择：')
    print()

#引入main模块



if __name__ == '__main__':
    print(lst)




