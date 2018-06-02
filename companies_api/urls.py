from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from companies_api import views

urlpatterns = [
    url(r'^postal_addresses/$', views.PostalAddressList.as_view()),
    url(r'^postal_addresses/(?P<pk>[0-9]+)/$',
        views.PostalAddressDetail.as_view()),
    url(r'^companies/filter/$', views.CompanyFilterView.as_view()),
    url(r'^companies/$', views.CompanyList.as_view()),
    url(r'^companies/(?P<pk>[0-9]+)/$', views.CompanyDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
