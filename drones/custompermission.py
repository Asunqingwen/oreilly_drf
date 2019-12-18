# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 0018 13:52
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: custompermission.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
from rest_framework import permissions

class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		else:
			return obj.owner == request.user
