# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 23:24:19 2023

@author: yuxin17
"""


class CampusForum:
    # a.
    def __init__(self):
        self.__user_pwd = {}
        self.__post_info = {}
    
        # 子任务1：
        with open('data/user_pwd.txt', 'r', encoding=' utf-8') as f:
            for line in f:
                name, pwd = line.strip().split('\t')
                self.__user_pwd[name] = pwd
        with open('data/post_info.txt', 'r', encoding=' utf-8') as f:
            for line in f:
                post_id, content, date, user, comments = line.strip().split('\t')
                self.__post_info[post_id] = {
                    'content': content,
                    'date': date,
                    'user': user,
                    'comments': comments.split(',')
                    }
    
        # 子任务2：
        output = []
        for post_id, post_info in self.__post_info.items():
            output.append(f"#{post_id}: {post_info['content']}")
            output.append(
                f"\t(发帖人：{post_info['user']}\t日期：{post_info['date']}\t评论数：{len(post_info['comments'])})")
            output.append("--------------------------------------------------")
        self.__post_list = '\n'.join(output)
    
        # 子任务3：
        def show_posts(self):
            print(self.__post_list)
    
        self.show_posts = show_posts
    
    # b.
    def watch_review(self, post_id):
        def __present_post(post_id):
            post = self.__post_info[post_id]
            print(f"#{post_id}: {post['content']}")
            print(f"\t (发帖人：{post['user']}\t日期：{post['date']}\t评论数：{len(post['comments'])})")
            print('-' * 50)
    
        __present_post(post_id)
    
        # 假设用户名为 u100903，密码为 YjbyIu45Nl
        user = 'u100903'
        pwd = 'YjbyIu45Nl'
        if user not in self.__user_pwd or self.__user_pwd[user] != pwd:
            print('登录失败！无权限查看评论！')
        else:
            post = self.__post_info[post_id]
            print(f"帖子#{post_id}的评论：")
            for i, comment in enumerate(post['comments'], start=1):
                print(f"{i}楼：{comment}")
    
    # c.
    def delete_post(self, post_id):
        # 假设用户名为 u100903，密码为 YjbyIu45Nl
        user = 'u100903'
        pwd = 'YjbyIu45Nl'
        if user not in self.__user_pwd or self.__user_pwd[user] != pwd:
            print('登录失败！无权限删除帖子！')
        elif self.__post_info[post_id]['user'] != user:
            print('您无权限删除该帖！')
        else:
            del self.__post_info[post_id]
            print('删除成功！')
            
# 以下代码仅用于测试
U1 = CampusForum()
U1.watch_review("#702")
# #702发帖用户及密码：u100903, YjbyIu45Nl
U1.delete_post("#702")
U1.delete_post("#768")
