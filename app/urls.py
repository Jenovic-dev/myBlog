
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from. import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
]
urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
