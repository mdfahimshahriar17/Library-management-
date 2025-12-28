from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_list, name='book_list'),
    path('add_new_book/', views.add_new_book, name='add_new_book'),
    path('book/edit/<int:pk>', views.book_edit, name='book_edit'),
    path('add/member/',views.add_member, name='add_member'),
    path('membe/list/', views.member_list, name='member_list'),
    path('edit/member/<int:pk>', views.edit_member, name='edit_member'),
    path('delete/book/<int:pk>', views.delete_book, name='delete_book'),
    path('delete/member/<int:pk>', views.delete_member, name='delete_member'),
    path('give/borrow/book/<int:pk>', views.give_borrow_book, name='give_borrow_book'),
    path('borrwed/book/list/', views.borrwed_book_list, name='borrwed_book_list'),
    path('return-receive/<int:pk>', views.return_receive, name='return_receive'),
    path('login/form/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
]