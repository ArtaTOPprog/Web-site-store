from django.urls import path
from web_app.views import *

urlpatterns = [
    path('', main, name='main'),
    path('product_list', product_list, name='product'),
    path('<int:category_id>/', product_list, name='category'),
    
    path('registration', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout_akk'),
    path('user', im_user, name='user_section'),

    path('basket', basket, name='basket'),
    path('basket_add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket_delete/<int:id>/', basket_delete, name='basket_delete'),

    
]