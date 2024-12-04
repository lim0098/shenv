#users.urls.py
from django.urls import path
from users import views
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView,TokenObtainPairView # type: ignore

urlpatterns = [
    # path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterViews.as_view()),
    
    # path('token/refresh/',TokenRefreshView.as_view()),
    # path('token/verify/',TokenVerifyView.as_view()),
    # path('users/<int:pk>/',views.UserView.as_view({'get': 'retrieve'})),
    # path('<int:pk>/name/',views.UserView.as_view({'put': 'update_name'})),
    # path('<int:pk>/email/',views.UserView.as_view({'put': 'update_email'})),
    # path('<int:pk>/password/',views.UserView.as_view({'put': 'update_password'})),
    # path('address/',views.addrview.as_view({'post':'coreate','get':'list'}))
    # path('address/<int:pk>/',views.addrview.as_view({'put':'destroy','delete':'update'}))
    
    path(r'token/obtain', TokenObtainPairView.as_view(), name="obtain_token"),
    path(r'detail',views.DetailsView.as_view(),name="detail"),
    path(r'login',views.LoginView.as_view()),

]
from rest_framework.routers import DefaultRouter
router = DefaultRouter()  # 可以处理视图的路由器

router.register('menu', views.MenuViewsSet)  # 向路由器中注册视图集
router.register('role', views.RoleViewsSet)  # 向路由器中注册视图集

urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中