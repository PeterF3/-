a=int(input("请输入您的体重"))
b=float(input("请输入您的身高"))
BMI=a/(b**2)
_BMI=str(BMI)
if BMI>=28:
    print("您的BMI指数为"+_BMI+" 肥胖")
elif BMI>24:
    print("您的BMI指数为"+_BMI+" 超重")
elif BMI>=18.5:
    print("您的BMI指数为"+_BMI+" 正常")
else:
    print("您的BMI指数为"+_BMI+" 偏瘦")