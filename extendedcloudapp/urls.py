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
    path('owner_view', views.owner_view, name='owner_view'),
    path('owner_delete/<int:id>/', views.owner_delete, name='owner_delete'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('receiver_view', views.receiver_view, name='receiver_view'),
    path('receiver_delete/<int:id>/', views.receiver_delete, name='receiver_delete'),
    path('send_request', views.send_request, name='send_request'),
    path('view_request', views.view_request, name='view_request'),
    path('confirm_request/<int:id>/', views.confirm_request, name='confirm_request'),
    path('reject_request/<int:id>/', views.reject_request, name='reject_request'),
    path('admin_view_file', views.admin_view_file, name='admin_view_file'),
    path('view_status', views.view_status, name='view_status'),
    path('view_user_download', views.view_user_download, name='view_user_download'),
    # path('clean_my_file', views.clean_my_file, name='clean_my_file'),
    path('send_mail', views.send_mail, name='send_mail'),
    path('send_mail_plain', views.SendPlainEmail, name='send_mail_plain'),
    path('send_mail_plain_with_stored_file', views.send_mail_plain_with_stored_file, name='send_mail_plain_with_stored_file'),
    path('send_mail_plain_with_file', views.send_mail_plain_with_file, name='send_mail_plain_with_file'),
    path('download_file',views.download_file, name='download_file')





]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
