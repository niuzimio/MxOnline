# -*- coding: utf-8 -*-
# @Time : 2021/7/20 20:25
# @Author : LiTing
# @function: 表单验证

from django import forms

from captcha.fields import CaptchaField


# 动态验证码登录
class DynamicLoginForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    captcha = CaptchaField()


class LoginForm(forms.Form):
    # 必须与form表单的input的name保持一致
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)
