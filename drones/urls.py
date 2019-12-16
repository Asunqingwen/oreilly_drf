# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 0016 9:43
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: urls.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me

from django.urls import path

from drones import views

urlpatterns = [
	path('drone-categories/', views.DroneCategoryList.as_view(), name=views.DroneCategoryList.name),
	path('drone-categories/<int:pk>', views.DroneCategoryDetail.as_view(), name=views.DroneCategoryDetail.name),

	path('drones/', views.DroneList.as_view(), name=views.DroneList.name),
	path('drones/<int:pk>', views.DroneDetail.as_view(), name=views.DroneDetail.name),

	path('pilots/', views.PilotList.as_view(), name=views.PilotList.name),
	path('pilots/<int:pk>', views.PilotDetail.as_view(), name=views.PilotDetail.name),

	path('competitions/', views.CompetitionList.as_view(), name=views.CompetitionList.name),
	path('competitions/<int:pk>', views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),

	path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
