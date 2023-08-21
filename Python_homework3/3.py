# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:47:18 2023

@author: yuxin17
"""

#目标：{变量名1:{指标1:值,指标2:值,指标3:值},变量名2:{指标1:值,指标2:值,指标3:值}}

# 打开文件
f = open("./data/variable_summary.txt", encoding="utf-8")
line = f.read().split("==============================")

f.close()

result_dict = {}

# 遍历分块
for i in line[1:]:
    j = i.split("\n")
    key = j[1].strip()
    result_dict[key] = {}
    for a in j[3:]:
        if a:
            b = a.split("  ")
            result_dict[key][b[0].strip()] = b[-1].strip()

# 输出表头
print("{:<12}|{:<12}|{:<12}|{:<12}|{:<12}|{:<12}|{:<12}".format("", "Obs", "Sum of Wgt.", "Mean", "Std. Dev.", "Variance", "Skewness", "Kurtosis"))
print("-" * 100)

# 输出表格内容
for var_name, result in result_dict.items():
    obs = result["Obs"]
    sum_wgt = result["Sum of Wgt."]
    mean = result["Mean"]
    std_dev = result["Std. Dev."]
    variance = result["Variance"]
    skewness = result["Skewness"]
    kurtosis = result["Kurtosis"]
    print("{:<12}|{:<12}|{:<12}|{:<12}|{:<12}|{:<12}|{:<12}|{:<12}".format(var_name, obs, sum_wgt, mean, std_dev, variance, skewness, kurtosis))
