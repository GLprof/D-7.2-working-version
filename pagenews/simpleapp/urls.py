from django.urls import path
from .views import PList, PDetail

urlpatterns = [path('p/', PList.as_view()),
               path('p/<int:pk>/', PDetail.as_view(), name='p_detail'), ]