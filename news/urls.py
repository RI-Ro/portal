from django.conf.urls import url

from views import index, detail_post

urlpatterns = [
    url(r'post-id=(?P<post_id>[0-9]+)/$', detail_post, name='detail_post'),
    url('', index),
]
