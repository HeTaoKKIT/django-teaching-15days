
from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from stu import views

router = SimpleRouter()
router.register('student', views.StudentSource)

urlpatterns = [
    url(r'^s_index/', views.s_index, name='sindex'),
]

urlpatterns += router.urls
