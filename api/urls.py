from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,ProductViewSet,OrderViewSet,HomeVideoViewSet,AdminProfileViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API uchun Swagger dokumentatsiyasi",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="marimovdev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# schema_view = get_schema_view(
#     openapi.Info(
#         title="API Documentation",
#         default_version='v1',
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )




router = DefaultRouter()
router.register(r'categories',CategoryViewSet)
router.register(r'products',ProductViewSet)
router.register(r'orders',OrderViewSet)
router.register(r'homepage-video',HomeVideoViewSet)
router.register(r'admin-profile',AdminProfileViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('auth/', include("dj_rest_auth.urls"), name="auth"),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   
]