# -*- coding: utf-8 -*-
# @Time : 2021/7/20 20:25
# @Author : LiTing
# @function: 表单验证
import redis
from django import forms

from captcha.fields import CaptchaField
from MxOnline.settings import REDIS_HOST, REDIS_PORT
from apps.users.models import UserProfile


class RegisterGetForm(forms.Form):
    captcha = CaptchaField()


class RegisterPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)
    password = forms.CharField(required=True)

    # 对手机号码进行验证
    def clean_mobile(self):
        mobile = self.data.get('mobile')
        # 验证手机号码是否已经注册
        user = UserProfile.objects.filter(mobile=mobile)
        if user:
            raise forms.ValidationError('该手机号码已经注册')
        return mobile

    # 对验证码进行验证
    def clean_code(self):
        mobile = self.data.get('mobile')
        code = self.data.get('code')
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
        redis_code = r.get(str(mobile))
        if code != redis_code:
            raise forms.ValidationError('验证码不正确')
        return code


class LoginForm(forms.Form):
    # 必须与form表单的input的name保持一致
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)


# 动态验证码登录
# 验证验证码和手机号是否正确
class DynamicLoginForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    captcha = CaptchaField()


# 动态验证码登录
# 验证用户提交的手机号和验证码
class DynamicLoginPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)

    # 对某字段进行验证
    def clean_code(self):
        mobile = self.data.get('mobile')
        code = self.data.get('code')
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
        redis_code = r.get(str(mobile))
        if code != redis_code:
            raise forms.ValidationError('验证码不正确')
        return self.cleaned_data

    # def clean(self):
    #     mobile = self.cleaned_data['mobile']
    #     code = self.cleaned_data['code']
    #     r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
    #     redis_code = r.get(str(mobile))
    #     if code != redis_code:
    #         raise forms.ValidationError('验证码不正确')
    #     return self.cleaned_data
