from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

import views
import api

web_urls = [

    url(r'^item/$', views.ItemList.as_view(), name='item_list'),
    # url(r'^item/add/$', views.ItemCreate.as_view(), name='item_add'),
    # url(r'^item/(?P<pk>[0-9]+)/$', views.ItemUpdate.as_view(), name='item_edit'),
    url(r'^item/add/$', views.item, name='item_add'),
    url(r'^item/(?P<pk>[0-9]+)/$', views.item, name='item_edit'),
    url(r'^item/search/$', views.item_search, name='search-item'),
    url(r'^item/delete/(?P<pk>\d+)/$', views.ItemDelete.as_view(), name='item_delete'),

    url(r'^unit/add$', views.UnitCreate.as_view(), name='unit_add'),
    url(r'^unit/$', views.UnitList.as_view(), name='unit_list'),
    url(r'^unit/edit/(?P<pk>\d+)/$', views.UnitUpdate.as_view(), name='unit_edit'),
    url(r'^unit/delete/(?P<pk>\d+)/$', views.UnitDelete.as_view(), name='unit_delete'),

    url(r'^unit_conversion/$', views.UnitConversionList.as_view(), name='unit_conversion_list'),
    url(r'^unit_conversion/add/$', views.UnitConversionCreate.as_view(), name='unit_conversion_add'),
    url(r'^unit_conversion/edit/(?P<pk>\d+)/$', views.UnitConversionUpdate.as_view(), name='unit_conversion_edit'),
    url(r'^unit_conversion/delete/(?P<pk>\d+)/$', views.UnitConversionDelete.as_view(), name='unit_conversion_delete'),

    url(r'^accounts/$', views.list_inventory_accounts, name='list_inventory_accounts'),
    url(r'^accounts/(?P<id>[0-9]+)/$', views.view_inventory_account, name='view_inventory_account'),
    url(r'^accounts/(?P<id>[0-9]+)/rate/$', views.view_inventory_account_with_rate,
        name='view_inventory_account_with_rate'),
]

api_urls = [
    url(r'^api/items/$', api.ItemListAPI.as_view()),
    url(r'^api/units/$', api.UnitListAPI.as_view()),
]

api_urls = format_suffix_patterns(api_urls)

urlpatterns = web_urls + api_urls
