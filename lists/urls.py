from django.conf.urls import include, url


urlpatterns = [
    # url(r'^accounts/', include('authtools.urls')),
    url(r'^new$', 'lists.views.new_list', name='new_list'),
    url(r'^(\d+)/$', 'lists.views.view_list', name="view_list"),
]