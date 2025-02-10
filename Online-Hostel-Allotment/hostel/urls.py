from django.urls import re_path # Correct import
from . import views

app_name = 'hostel'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^logout/$', views.logout1, name='logout'),
    re_path(r'^allocate/$', views.allocate, name='allocate'),
    re_path(r'^student_details/$', views.student_details, name='student_details'),
    re_path(r'^change/$', views.change, name='change'),
    re_path(r'^change_req/$', views.change_request, name='change_req'),
    re_path(r'^swap/$', views.swap, name='swap'),
    re_path(r'^swap_req/$', views.swap_request, name='swap_request'),
    re_path(r'^success/$', views.success, name='success'),
    re_path(r'^swap_ack/$', views.swap_ack, name='swap_ack'),
    re_path(r'^deallocate/$', views.deallocate, name='deallocate'),
    re_path(r'^show_request/$', views.show_request, name='show_request'),
    re_path(r'^show_vacancy/$', views.vacant_room, name='show_vacancy'),
    re_path(r'^show_students/$', views.show_students, name='show_students'),
]
