# -*- coding: utf-8 -*-
# @Author: 境
# @Date:   2018-11-24 09:36:37
lst=[{'Id':1,'name':'jing','age':18,'major':'Python'}]
class Student():
    def __init__(self,Id,name,age,major):
        self.Id=Id
        self.name=name
        self.age=age
        self.major=major
def appd():
    ls=[]
    lit=[]
    def inp():
        print('-----input student massage!-----')
        Id=input('学生ID:')
        name=input('姓名:')
        age=input('年龄:')
        major=input('专业:')

        return Id,name,age,major

    print('-'*10,'是否继续添加？','-'*10,)
    print()
    print('#'*5,'继续，请输入“yes”-----返回，请输入“exit”','#'*5)
    print()

    while True:
        x=input('是否继续>>>')
        if x=='yes':
            lit=inp()
            stu=Student(lit[0],lit[1],lit[2],lit[3])
            ls.append(stu.__dict__)
        elif x=='exit':
            break
        else:
            print('请输入正确的选择：')
        print()

    return ls



if __name__ == '__main__':
    print(appd())





