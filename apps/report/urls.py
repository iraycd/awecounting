from django.conf.urls import url
import views

web_urls = [
    url(r'^save_settings/$', views.save_report_settings, name='save_report_settings'),
    url(r'^trial_balance/$', views.trial_balance, name='trial_balance'),
    url(r'^trial_balance.json$', views.trial_balance_json, name='trial_balance_json'),
]

urlpatterns = web_urls
