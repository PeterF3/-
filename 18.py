#18.输入三个整数，把这三个数从小到大输出。
a=int(input('x'))
b=int(input('y'))
c=int(input('z'))
a1=str(a)
b1=str(b)
c1=str(c)
if a<b<c:
    print(a1+b1+c1)
elif a<c<b:
    print(a1+c1+b1)
elif b<a<c:
    print(b1+c1+a1)
elif b<c<a:
    print(b1+c1+a1)
elif c<a<b:
    print(c1+a1+b1)
elif c<b<a:
    print(c1+b1+a1)
else:
    print('都相等')