#!/usr/bin/env python3
# -*- coding: utf-8 -*-




def ShowClassmates(classmates):
    num = len(classmates)
    print('class has',num,'students')
    for index in range(num):
        print('serail:',index,'name:',classmates[index])
    return

# define a list,with []

# empty list

L = []
print('empty list len is:',len(L))

classmates = ['yudf','mohz','yexb','zhaoyp']

# len of a list

student_num = len(classmates)

print('class has',student_num," students")


for index in range(len(classmates)):
    print('serial:',index,"name:",classmates[index])



# list 是一个可变列表，可以往 list 尾部 追加元素
# append

new_student = 'zhouj'

classmates.append(new_student)


ShowClassmates(classmates)


# insert 插入元素到指定位置  L.insert(index, object)

foreigner = 'jack'

classmates.insert(1,foreigner)

ShowClassmates(classmates)



# pop() 删除 list 末尾元素
# L.pop([index]) -> item -- remove and return item at index 

item = classmates.pop()
print(item,' has graduated')

print('============= ungraduated students =============')
ShowClassmates(classmates)

# pop(index) 删除指定索引元素

item = classmates.pop(0)
print(item,' has graduated')

print('============= ungraduated students =============')
ShowClassmates(classmates)



# 要修改某个元素的值，可以直接赋值给对应的索引元素

classmates[0]='yudf'
ShowClassmates(classmates)



# list 的元素类型可以不同

L1 = [1,2,3,'jack',True,23.1]

print('List can have different elements:',L1)

# list 可以包含 list

L2 = ['good','job',L1]
print('List can include a list:',L2)













