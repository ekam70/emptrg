from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.EmployeeListView.as_view(), name='employees'),
    path('departments/', views.DepartmentListView.as_view(), name='departments'),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('department/<str:pk>', views.DepartmentDetailView.as_view(), name='department-detail'),

]

urlpatterns += [
    path('nominate/<int:employeepsnumber>/<str:programcode>/', views.EmployeeProgramNominate, name='employee-program-nominate'),
]

urlpatterns += [
    path('empproglist/', views.EmployeeProgramList, name='empproglist'),
]

urlpatterns += [
    path('emplistjson/', views.EmployeeListJson, name='emplistjson'),
]

urlpatterns += [
    path('proglistjson/', views.ProgramListJson, name='proglistjson'),
]

router = routers.DefaultRouter()
router.register(r'emplist', views.EmployeeViewSet)

# Wire up our API using automatic URL routing.

urlpatterns += [
    path('restapi/', include(router.urls)),
]
