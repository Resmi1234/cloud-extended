from django.conf.urls.static import static
from django.urls import path
from extendedcloudapp import views
from extendedcloudpro import settings

urlpatterns = [

    path('', views.index, name='index'),
    path('central_authority', views.cenrtal_authority, name='central_authority'),
    path('data_owner_register', views.data_owner_register, name='data_owner_register'),
    path('login_view', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('data_owner_panel', views.data_owner_panel, name='data_owner_panel'),
    # path('view_receiver_registration', views.view_receiver_registration, name='view_receiver_registration'),
    path('data_receiver_register', views.data_receiver_register, name= 'data_receiver_register'),
    path('data_receiver_panel', views.data_receiver_panel, name='data_receiver_panel'),
    path('upload_files_owner', views.upload_files_owner, name='upload_files_owner'),
    path('view_file', views.view_file, name='view_file'),
    path('receiver_view_file',views.receiver_view_file, name= 'receiver_view_file'),
    path('profile_view',views.profile_view, name='profile_view'),
    path('file_delete/<int:id>/', views.file_delete, name='file_delete'),





]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
