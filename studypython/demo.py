# 是注释
print(520)
print("hello")
print(3 + 1)
print("3+1")

# 将数据输出到文件中
fp = open("E:/Python/study/text.txt", "a+")  # a+ 如果文件不存在就创建，存在就在文件内容的后面追加
print("helloworld", file=fp)
fp.close()

# 不进行换行输出
print("1", "world", "Python")
