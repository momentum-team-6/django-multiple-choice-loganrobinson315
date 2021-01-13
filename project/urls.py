"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.list_deck, name='list-deck'),
    path('<int:pk>/deck_detail/', views.deck_detail, name='deck-detail'),
    path('add_deck', views.add_deck, name="add-deck"),
    path('add_card/<int:deck_pk>/', views.add_card, name="add-card"),
    path('delete_card/<int:pk>/', views.delete_card, name="delete-card"),
    path('delete_deck/<int:pk>/', views.delete_deck, name="delete-deck"),
    path('edit_card/<int:pk>/', views.edit_card, name="edit-card"),
    path('edit_deck/<int:pk>/', views.edit_deck, name="edit-deck")
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
