
from django.contrib import admin
from django.urls import path,include
import debug_toolbar
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', home, name = 'home')
]
