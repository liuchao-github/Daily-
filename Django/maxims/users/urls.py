#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/31 0031 上午 9:03

base Info
"""
from django.conf.urls import url
from . import views, service

__author__ = 'liuchao'
__version__ = '1.0'

app_name = "users"
# urlpatterns = [url(r'^$', views.index, name="index")]
urlpatterns = [url(r'^$', views.IndexView.as_view(), name='index'),
               url(r'^ajax/$', service.ajax, name='ajax'),
               # url(r'get_or_memberNum/$', service.get_or_memberNum, name='get_or_memberNum'),
               # url(r'get_ta_memberNum/$', service.get_ta_memberNum, name='get_ta_memberNum'),
               # url(r'get_dp_memberNum/$', service.get_dp_memberNum, name='get_dp_memberNum'),
               # url(r'get_mfw_memberNum/$', service.get_mfw_memberNum, name='get_mfw_memberNum'),
               url(r'get_or_favorite/$', service.get_or_favorite, name='get_or_favorite'),
               url(r'get_or_location/$', service.get_or_location, name='get_or_location'),
               url(r'get_ta_location/$', service.get_ta_location, name='get_ta_location'),
               url(r'get_dp_location/$', service.get_dp_location, name='get_dp_location'),
               url(r'get_mfw_location/$', service.get_mfw_location, name='get_mfw_location'),
               url(r'get_all_memberNum/$',service.get_all_memberNum, name='get_all_memberNum'),
               url(r'get_all_sex/$',service.get_all_sex, name='get_all_sex'),
               url(r'get_dp_province/$', service.get_dp_province, name='get_dp_province'),
               url(r'get_mfw_province/$', service.get_mfw_province, name='get_mfw_province'),
               ]
