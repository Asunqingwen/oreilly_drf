# -*- coding: utf-8 -*-
# @Time    : 2019/12/14 0014 15:45
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: urls.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
from django.urls import path
from toys import views

urlpatterns = [
    path('toys/', views.toy_list),
    path('toys/<int:pk>', views.toy_detail),
]
