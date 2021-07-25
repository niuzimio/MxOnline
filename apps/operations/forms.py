# -*- coding: utf-8 -*-
# @Time : 2021/7/23 16:28
# @Author : LiTing
# @function:
import re
from django import forms

from apps.operations.models import UserFavorite


class UserFavForm(forms.ModelForm):
    class Meta:
        model = UserFavorite
        fields = ['fav_id', 'fav_type']

