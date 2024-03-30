from django.urls import path
from rest_framework import routers
from post import views

router = routers.SimpleRouter()
router.register(r'api/posts', views.PostViewSet)

urlpatterns = [
    path('list/', views.post_list, name='post_list')
]

urlpatterns += router.urls