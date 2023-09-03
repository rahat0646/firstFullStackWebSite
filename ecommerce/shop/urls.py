from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('product/<int:pk>/<name>',views.ProductView,name="product"),
    path('category/<int:id>/<categoryName>',views.CategoryView.as_view(),name="category"),
    path('brand/<int:id>/<brandName>',views.BrandView,name='brand'),
    path('menu/<int:id>/<menuName>',views.MenuView.as_view(),name="menu"),
    path('all-product-brand/<int:id>/<brandName>',views.BrandViewAll.as_view(),name="brandAll"),
    path('category/<int:categoryId>/<categoryName>/filter-data',views.filter_product,name="filter_data_category"),
    path('menu/<int:id>/<menuName>/filter-data',views.filter_product_menu,name="filter_data_menu"),
    path('all-product-brand/<int:id>/<brandName>/filter-data',views.filter_product_brand,name="filter_data_brand"),
    path('review/',views.Review_rate,name="Review"),
    path('adress/',views.Adressa.as_view(),name="adress"),
    path('exchange/',views.exchange_page,name="exchange"),
    path('aboutus/',views.aboutus_page,name="aboutus"),
    path('cargofee/',views.cargofee_page,name="cargofee"),
    path('contact/',views.contacts,name="contact"),
    path('adress/get_cities/',views.get_cities,name="get_cities"),
    path('checkout/',views.CheckOut,name="checkout"),
    path("help/", views.help_page, name="help"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("search/", views.search_results, name="search"),
    path("brand/<int:id>/searchBrand/", views.search_results_brand, name="searchBrand"),
    path("user/order",views.order_page,name="order"),
    path('register/',views.register,name="register"),
    path('login/',views.giris,name="login"),
    path('add-to-cart/',views.add_to_cart,name="add-to-cart"),
    path('cart/',views.show_cart,name='cart'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('pluscart/',views.plus_cart,name='pluscart'),
    path('minuscart/',views.minus_cart,name='minuscart'),
    path('removecart/',views.remove_cart,name='removecart'),
    path('pluswishlist/',views.plus_wishlist,name='pluswishlist'),
    path('minuswishlist/',views.minus_wishlist,name='minuswishlist'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)