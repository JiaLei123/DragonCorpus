from django.conf.urls import url
import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^(?P<project_id>\w+)/project_overview_detail/$',views.project_overview_detail,name='project_overview_detail'),
    url(r'^project_overview_detail_table/$',views.project_overview_detail_table,name='project_overview_detail_table'),
    url(r'^utterance_table/$', views.utterance_table, name='utterance_table'),
    url(r'^(?P<testsuit_id>\w+)/testsuit_overview_detail/$', views.testsuit_overview_detail,name='testsuit_overview_detail'),
    url(r'^new_project/$',views.new_project,name='new_project'),
    url(r'^new_testsuit/$',views.new_testsuit,name='new_testsuit'),
    url(r'^utterance/$', views.utterance, name='utterance'),

    #filter
    url(r'^get_all_intent/$', views.get_all_intent, name='get_all_intent'),
    url(r'^table_refresh/$', views.table_refresh, name='table_refresh'),
]