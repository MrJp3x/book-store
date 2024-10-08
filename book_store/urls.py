from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home_module.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
]
# 09111070207
# 09112131501


