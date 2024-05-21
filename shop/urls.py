from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, shop, detail, product_by_category, review_save, user_register, user_login, user_logout

urlpatterns = [
    path('', index, name="index"),
    path('shop/', shop, name="shop"),
    path('detail/<str:product_slug>/', detail, name="detail"),
    path('by-category/<str:category_slug>/', product_by_category, name="by_category"),
    path('review-save/<str:product_slug>/', review_save, name="review_save"),

    path('register/', user_register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),

    # start url Forgot password
    path('reset-password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('reset-password-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='shop/reset_done.html'),
         name="password_reset_complete"),
    # end url Forgot password
]
