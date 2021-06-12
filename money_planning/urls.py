from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('sort_filter/<str:tag>', views.sort_filter, name="sort_filter"),
   path('users', views.users, name="users"),
   path('transactions', views.transactions, name="transactions"),
   path('create_user', views.create_user, name="create_user"),
   path('create_transact', views.create_transact, name="create_transact"),
   path('user/<int:pk>', views.user_view, name="user_view"),
   path('transaction/<int:pk>', views.transact_view, name="transact_view"),
   path('edit_user/<int:pk>', views.edit_user, name="edit_user"),
   path('edit_transact/<int:pk>', views.edit_transact, name="edit_transact"),
   path('delete_user/<int:pk>', views.delete_user, name="delete_user"),
   path('delete_transac/<int:pk>', views.delete_transact, name="delete_transact"),
]
