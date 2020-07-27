from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.NoticeListView.as_view(), name='home'),
    path('notice/<int:pk>', views.NoticeDetail.as_view(), name='notice'),
    path('profile/edit/<int:pk>', views.ProfileUpdate.as_view(success_url="/"), name='profileedit'),
]