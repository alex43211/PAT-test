'''
1002 写出这个数 （20 分）
读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。

输入格式：
每个测试输入包含 1 个测试用例，即给出自然数 n 的值。这里保证 n 小于 10
​100
​​ 。

输出格式：
在一行内输出 n 的各位数字之和的每一位，拼音数字间有 1 空格，但一行中最后一个拼音数字后没有空格。

输入样例：
1234567890987654321123456789
输出样例：
yi san wu
'''

a = input()
#b用于存放a作为字符串拆开每个字符组成的列表
b = []
#用sum记录各位数字之和
sum = 0
#用于将拼音组成的新元素存入列表
c = []
ss = ' '

#dictsum将结果转为要求的拼音形式
dictsum = {'1':'yi', '2':'er', '3':'san', '4':'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '0':'ling'}

#将字符串a拆开，存入列表b中
for i in a:
    b.append(i)

#求和
for i in range(len(b)):
    sum += int(b[i])

#结果进行数字转拼音规定格式的转换
for i in str(sum):
    c.append(dictsum[i])

#用join的方法通过空格来拼接字符串
print(ss.join(c))
