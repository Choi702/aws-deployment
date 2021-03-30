from django.urls import path
from .views import auth_blogList, auth_blogDetail

urlpatterns = [
    path('', auth_blogList.as_view(), name='auth_blog_list'),
    path('<int:pk>/', auth_blogDetail.as_view(), name='auth_blog_detail')
]