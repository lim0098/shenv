#users.urls.py
from taxdisplay import views
from rest_framework.routers import DefaultRouter

# 路由列表
urlpatterns = []

router = DefaultRouter()  # 可以处理视图的路由器
router.register('caigou', views.ProcurementViewsSet)  # 向路由器中注册视图集
router.register('xiaoshou', views.SalesViewsSet)  # 向路由器中注册视图集


urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中