#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/3 13:39
# @Author  : zhaoyan
# @File    : authentication.py

'''
    # 该文件是用来自定义用户的认证,需要实现两个函数：
    1. authenticate
    2. get_user
'''

from django.contrib.auth.models import User

class EmailAuthBackend(object):
    """
        Authenticate using e-mail account.
    """
    def authenticate(self, username= None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return User
            return None
        except User.DoesNotExist:
            return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None














