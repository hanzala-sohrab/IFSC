from django.conf.urls import re_path
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    re_path(r'^api/ifsc/(?P<ifs_code>\w+)$', views.bank_details, name='bank'),
    re_path(r'^api/branches/(?P<bank>[-\w]+)/(?P<city>[-\w]+)$', views.details_of_branches, name='branches'),
    re_path(r'^branches/(?P<bank>[-\w]+)/(?P<city>[-\w]+)$', views.branch, name='branch'),
    re_path(r'^ifsc/(?P<ifs_code>\w+)$', views.bank, name='ifsc'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
