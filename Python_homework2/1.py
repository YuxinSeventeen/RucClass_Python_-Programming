# -*- coding: utf-8 -*-


Files = ['第一次作业+刘彦俊+2022000406','第一次作业+李宇鸣+2022000552','第一次作业+王云桐+2022000941','第一次作业+刘云桐+2022000456','第一次作业+刘含梓+2022000356','第一次作业+刘诗诗+2022000584','第一次作业+张云桐+2022000656','第一次作业+张宇鸣+2022000593','第一次作业+张诗诗+2022000675','第一次作业+李诗诗+2022000344','第一次作业+王彦俊+2022000156','第一次作业+赵宇鸣+2022000406','第一次作业+李云桐+2022000411','第三次作业+刘含梓+2022000356','第三次作业+刘云桐+2022000456','第三次作业+刘彦俊+2022000406','第三次作业+刘诗诗+2022000584','第三次作业+周彦俊+2022000789','第三次作业+张含梓+2022000728','第三次作业+张宇鸣+2022000593','第三次作业+张诗诗+2022000675','第三次作业+李云桐+2022000411','第三次作业+王云桐+2022000941','第三次作业+王彦俊+2022000156','第三次作业+赵宇鸣+2022000406','第三次作业+张云桐+2022000656','第三次作业+李宇鸣+2022000552','第二次作业+刘彦俊+2022000406','第二次作业+李宇鸣+2022000552','第二次作业+刘云桐+2022000456','第二次作业+刘含梓+2022000356','第二次作业+周彦俊+2022000789','第二次作业+张云桐+2022000656','第二次作业+张含梓+2022000728','第二次作业+张宇鸣+2022000593','第二次作业+李云桐+2022000411','第二次作业+李诗诗+2022000344','第二次作业+王彦俊+2022000156','第二次作业+张诗诗+2022000675','第二次作业+王云桐+2022000941']
Scores = [85, 88, 95, 71, 86, 94, 76, 75, 90, 78, 88, 96, 87, 93, 87, 79, 81, 70, 88, 88, 74, 76, 72, 72, 86, 99, 93, 76, 81, 99, 89, 88, 85, 76, 96, 98, 78, 74, 80, 87]


#(a)
Homework = {}
for file, score in zip(Files, Scores):
    # 从文件名中提取作业编号、姓名和学号信息
    homework_num, name, student_id = file.split("+")
    # 如果学生信息已经存在于Homework字典中，则直接添加新的作业分数
    if student_id in Homework and homework_num in Homework[student_id]:
        Homework[student_id][homework_num]["score"] = score
    # 否则，需要先创建学生信息的字典
    else:
        if student_id not in Homework:
            Homework[student_id] = {}
        Homework[student_id][homework_num] = {"name": name, "score": score}
print(Homework)

#(b)
# 计算每位同学的平时成绩
averages = {}
for student_id in Homework:
    total_score = 0
    num_homeworks = 0
    for homework_num in Homework[student_id]:
        if "score" in Homework[student_id][homework_num]:
            total_score += Homework[student_id][homework_num]["score"]
    averages[student_id] = total_score / 3
# 按照平时成绩的排名打印输出
rankings = sorted(averages.items(), key=lambda x: x[1], reverse=True)
for i, (student_id, average) in enumerate(rankings):
    name = Homework[student_id][list(Homework[student_id].keys())[0]]["name"]
    print("第{}：{}({}) {:.1f}分".format(i+1, name, student_id, average))