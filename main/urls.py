from django.conf.urls import patterns, include, url

from views import CompanyListView, CompanyDetailView, UserListView, UserDetailView, EventListView, EventDetailView, CallListView, \
                 CallDetailView, CompanyTypesListView, CompanyTypesDetailView, MaterialListView, MaterialDetailView

urlpatterns = patterns('',
		url(r'^companies/$', CompanyListView.as_view(), name='companies-list-view'),
		url(r'^companies/(?P<company_id>\d+)/$', CompanyDetailView.as_view(), name='companies-detail-view'),

		url(r'^users/$', UserListView.as_view(), name='users-list-view'),
		url(r'^users/(?P<user_id>\d+)/$', UserDetailView.as_view(), name='users-detail-view'),

		url(r'^events/$', EventListView.as_view(), name='events-list-view'),
		url(r'^events/(?P<event_id>\d+)/$', EventDetailView.as_view(), name='events-detail-view'),

		url(r'^calls/', CallListView.as_view(), name='calls-list-view'),
		url(r'^calls/(?P<call_id>\d+)/$', CallDetailView.as_view(), name='calls-detail-view'),

		url(r'^company-type/$', CompanyTypesListView.as_view(), name='company-type-list-view'),
		url(r'^company-type/(?P<company_type_id>\d+)/$', CompanyTypesDetailView.as_view(), name='company-type-detail-view'),

		url(r'^materials/$', MaterialListView.as_view(), name='materials-list-view'),
		url(r'^materials/(?P<material_id>\d+)/$', MaterialDetailView.as_view(), name='materials-detail-view'),

	)