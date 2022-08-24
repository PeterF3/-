a=int(input('请输入一个=>1900年的年份'))
if a%4==0:
    b=a/4
    print('是闰年')
elif a%400==0:
    c=a/4
    print('是闰年')
else:
    print('不是闰年')
    