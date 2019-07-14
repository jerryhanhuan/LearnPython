#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# set 和 dict 类似，也是一组key的集合，但不存储 value，由于key 不能重复，所以在set 中，没有重复的key
# set 可以看作是 无序，不重复的元素的集合

# 要创建一个 set，需要提供一个 list 作为输入集合

L = [1,2,3,4,2]
print("list L:",L)  #list L: [1, 2, 3, 4, 2]

s = set(L)
print('set s:',s)  # 去掉了重复的key set s: {1, 2, 3, 4}

#add Add an element to a set. This has no effect if the element is already present.


element = 10

s.add(element)
s.add(element)
s.add(element)

print('set s:',s) #set s: {1, 2, 3, 4, 10}

#remove Remove an element from a set; it must be a member. If the element is not a member, raise a KeyError

s.remove(element)

print('set s:',s) #set s: {1, 2, 3, 4}




# set 可以做 交集，并集等操作

s1 = set([1,2,3])
s2 = set([2,3,4])

print(s1&s2) #{2, 3}
print(s1|s2) #{1, 2, 3, 4}
