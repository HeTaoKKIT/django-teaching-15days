
from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from stu import views

router = SimpleRouter()
router.register('student', views.StudentSource)
router.register('grade', views.GradeSource)

urlpatterns = [
    url(r'^s_index/', views.s_index, name='sindex'),
    url(r'^s_add/', views.s_add, name='s_add'),
]

urlpatterns += router.urls
