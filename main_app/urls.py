from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finches_index, name='index'),
  path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
  path('finches/create/', views.FinchCreate.as_view(), name="finches_create"),
  path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name="finches_update"),
  path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name="finches_delete"),
  path('finches/<int:finch_id>/add_sighting/', views.add_sighting, name='add_sighting'),
  path('finches/<int:finch_id>/add_photo/', views.add_photo, name='add_photo'),
  path('finches/<int:finch_id>/assoc_feather/<int:feather_id>/', views.assoc_feather, name='assoc_feather'),
  path('finches/<int:finch_id>/unassoc_feather/<int:feather_id>/', views.unassoc_feather, name='unassoc_feather'),
  path('feathers/', views.FeatherList.as_view(), name='feathers_index'),
  path('feathers/<int:pk>/', views.FeatherDetail.as_view(), name='feathers_detail'),
  path('feathers/create/', views.FeatherCreate.as_view(), name='feathers_create'),
  path('feathers/<int:pk>/update/', views.FeatherUpdate.as_view(), name='feathers_update'),
  path('feathers/<int:pk>/delete/', views.FeatherDelete.as_view(), name='feathers_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]
