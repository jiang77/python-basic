'''
set:类似dict，是一组key的集合，不存储value

本质：无序和无重复元素的集合

'''

# 创建
# 创建set需要一个list或者tuple或者dict作为输入集合
# 重复元素在set中会自动被过滤
s1 = set([1,2,3,4,5])
print(s1)    # 结果：{1, 2, 3, 4, 5}
s2 = set([1,2,3,4,5,2,2,23,5])
print(s2)   # 结果：{1, 2, 3, 4, 5, 23}
s3 = set((1,2,3,4,5,6,3,6))
print(s3)   # 结果：{1, 2, 3, 4, 5, 6}
s4 = set({1:"good",2:"nice",3:"handsome"})
print(s4)   #结果：{1, 2, 3}，只取了key


# 添加
s5 = set([1,2,3,4,5])
s5.add(6)
print(s5)    # 结果：{1, 2, 3, 4, 5, 6}
s5.add(3)    # 可以添加一个重复的元素,但不会有效果
print(s5)    # 结果：{1, 2, 3, 4, 5, 6}
# set的元素不能是列表，因为列表是可变的。
'''
s5.add([7,8,9])   # 不能添加list，因为list不能作为key。由于set就是key的集合，key是不能用可变对象的，list是可变对象
print(s5)    # 结果会报错
'''
# set的元素不能是字典，因为字典是可变的
'''
s5.add({7:"a"})
print(s5)   # 结果：{1, 2, 3, 4, 5, 6, (7, 8, 9)}
'''
# set的元素可以是元组，因为元组不可变
s5.add((7,8,9))
print(s5)   # 结果：{1, 2, 3, 4, 5, 6, (7, 8, 9)}

# 插入整个list、tuple、字符串。打碎插入（下例是把一个list和tuple打碎成三个元素插入）
s6 = set([1,2,3,4,5])
s6.update([6,7,8])
print(s6)   # 结果：{1, 2, 3, 4, 5, 6, 7, 8}
s6.update((9,10))
print(s6)   # 结果：{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s6.update("sunck")
print(s6)  # 结果：{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'u', 'c', 'k', 's', 'n'}，sunck是无序插入的，每次运行结果的排序不一样


# 删除
s7 = set([1,2,3,4,5])
s7.remove(3)
print(s7)   # 结果：{1, 2, 4, 5}

# 遍历
s8 = set([1,2,3,4,5])
for i in s8:
    print(i)   #打印出来的结果也是无序的
# set是没有索引的
# print(s7[3])   会报错

# 交集和并集
s9 = set([1,2,3])
s10 = set([2,3,4])
# 交集
a1 = s9 & s10
print(a1)         # 结果：{2, 3}
print(type(a1))   # 结果：<class 'set'>
# 并集
a2 = s9 | s10
print(a2)         # 结果：{1, 2, 3, 4}
print(type(a2))   # 结果：<class 'set'>

