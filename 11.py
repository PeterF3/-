A=int(input('请输入第一条边'))
d=int(input('请输入第二条边'))
C=int(input('请输入第三条边'))
if A+d>C and d+C>A and A+C>d:
    print('可以构成三角形')
else:
    print('不能构成三角形')