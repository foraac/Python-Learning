# 2019工资计算，三险一金缴费比例有差异，个税未计入专项抵扣附加
# 获取税前收入
salary = int(float(input('请输入你的税前收入：\n> ')))
print(f"你的税前收入为：\n\t{salary}。")

assert salary >= 0, "你输入的金额不正确，请重新输入。"

# 定义三险一金变量，判断工资是否超过7662并计算三险一金金额
def sanxian(salary):
    if salary > 7662:
        sxyj = 7662 * 0.225
    else:
        sxyj = salary * 0.225
    return sxyj

sxyj = sanxian(salary)
print(f"你的三险一金缴纳金额为：\n\t{sxyj}。")

# 计算应纳税所得额
def yingnashuisuode(salary, sxyj):
    suodee = salary - sxyj - 5000
    if suodee <= 0:
        suodee = 0
        print("你的应纳税所得额为\n\t0。")
    else:
        print(f"你的应纳税所得额为：\n\t{suodee}。")
    return suodee

suodee = yingnashuisuode(salary, sxyj)

# 计算个人所得税
def suodeshui(suodee):
    if suodee <= 0:
        sds = 0
        #print("你无需缴纳个人所得税。")
    elif 0 < suodee <= 3000:
        sds = suodee * 0.03 - 0
    elif 3000 < suodee <= 12000:
        sds = suodee * 0.1 - 105
    elif 12000 < suodee <= 25000:
        sds = suodee * 0.2 - 555
    elif 25000 < suodee <= 35000:
        sds = suodee * 0.25 - 1005
    elif 35000 < suodee <= 55000:
        sds = suodee * 0.3 - 2755
    elif 55000 < suodee <= 80000:
        sds = suodee * 0.35 - 5505
    else:
        sds = suodee * 0.45 - 13505        
    return sds

sds = suodeshui(suodee)
print(f"你的个人所得税为：\n\t{sds}")

# 计算实际所得工资
paid = salary - sxyj - sds
print(f"你的实发工资为：\n\t{paid}。")
