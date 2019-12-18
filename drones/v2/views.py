# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 0018 16:56
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: views.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from drones import views


class ApiRootVersion2(generics.GenericAPIView):
	name = 'api-root'

	def get(self, request, *args, **kwargs):
		return Response({
			'vehicle-categories': reverse(views.DroneCategoryList.name, request=request),
			'vehicles': reverse(views.DroneList.name, request=request),
			'pilots': reverse(views.PilotList.name, request=request),
			'competitions': reverse(views.CompetitionList.name, request=request)
		})
