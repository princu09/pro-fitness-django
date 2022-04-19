from django.views.decorators.csrf import csrf_exempt
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic import RedirectView


urlpatterns = [
    # Basic Page For Everyone
    url(r'^$', RedirectView.as_view(url='home')),
    path('home', views.index, name="Main Page"),

    path('shop', views.shop, name="Shop Page"),
    path('single_product/<int:id>', views.single_product,
         name="Single Product Page"),

    path('my_wishlist', views.my_wishlist, name="My Wishlist Page"),
    path('add_wishlist', views.add_wishlist, name="Add Wishlist Page"),
    path('removeFromWishlist/<int:id>',
         views.removeFromWishlist, name="Remove Wishlist Item"),

    path('cart', views.cart, name="Cart Page"),
    path('add_cart', views.add_cart, name="Add Cart Page"),
    path('removeFromCart/<int:id>', views.removeFromCart, name="Add Cart Page"),

    path('checkout', views.checkout, name="Checkout Checking"),


    # My Account Page
    path('my_account', views.my_account, name="My Account Page"),
    path('my_account/make_changes', views.my_account, name="My Account Page"),
    path('make_changes', views.make_changes, name="Make Changes Page"),
    path('account_setting', auth_views.PasswordChangeView.as_view(
        template_name='include/account_setting.html',
        success_url='/'
    ), name="Account Setting Page"),
    path('my_orders', views.my_orders, name="My Orders Page"),
    path('view_bill/<int:id>', views.view_bill, name="View Bill"),

    path('handle_signup', views.handle_signup, name="Sign Up Page"),
    path('handle_login', views.handle_login, name="Login Page"),
    path('handle_logout', views.handle_logout, name="Logout Page"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
