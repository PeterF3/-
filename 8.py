a=float(input('请输入a的值'))
b=float(input('请输入b的值'))
c=float(input('请输入c的值'))
d=b**2-4*a*c
if d<0:
    print('无解')
elif d==0:
    e=(d**2-b)/a*2
    print('有解，且解为 '+str(e))
else:
    f=(d**2-b)/a*2
    g=-(d**2-b)/a*2
    print('有解，且解为 '+str(f)+'和'+str(g))