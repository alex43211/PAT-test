'''
1051 复数乘法 （15 分）
复数可以写成 (A+Bi) 的常规形式，其中 A 是实部，B 是虚部，i 是虚数单位，满足 i
​2
​​ =−1；也可以写成极坐标下的指数形式 (R×e
​(Pi)
​​ )，其中 R 是复数模，P 是辐角，i 是虚数单位，其等价于三角形式 (R(cos(P)+isin(P))。

现给定两个复数的 R 和 P，要求输出两数乘积的常规形式。

输入格式：
输入在一行中依次给出两个复数的 R
​1
​​ , P
​1
​​ , R
​2
​​ , P
​2
​​ ，数字间以空格分隔。

输出格式：
在一行中按照 A+Bi 的格式输出两数乘积的常规形式，实部和虚部均保留 2 位小数。注意：如果 B 是负数，则应该写成 A-|B|i 的形式。

输入样例：
2.3 3.5 5.2 0.4
输出样例：
-8.68-8.23i
'''

#两个复数乘积
#z = R1*R2*[cos(P1)+i*sin(P1)]*[(cos(P2)+i*sin(P2)]
#  = R1*R2*{cos(P1)cos(P2)+i*[cos(P1)sin(P2)+cos(P2)sin(P1)]-sin(P1)sin(P2)}

import math

#将输入转换为列表，方便取出系数计算
a = input().split()

R1 = float(a[0])
P1 = float(a[1])
R2 = float(a[2])
P2 = float(a[3])

#计算复数成绩，提取实部和虚部分别取两位小数赋值给A与B
A = R1*R2*(math.cos(P1)*math.cos(P2)-math.sin(P1)*math.sin(P2))
A = round(A,2)
B = R1*R2*(math.cos(P1)*math.sin(P2)+math.cos(P2)*math.sin(P1))
B = round(B,2)

#定义输出结果的样式
def z():
    if B < 0:
        return str(A)+'-'+str(abs(B))+'i'
    else:
        return str(A)+'+'+str(B)+'i'

print(z())
