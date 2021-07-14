from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing",views.create_listing,name = "create_listing"),
    path("create_listing_send",views.create_listing_send,name= "create_listing_send"),
    path("categories",views.categories,name = "categories"),
    path("category_list",views.category_list,name = "category_list"),
    path("watchlist_show",views.watchlist_show,name = "watchlist_show"),
    path("listing_page",views.listing_page,name="listing_page"),
    path("watchlist_add" , views.watchlist_add, name= "watchlist_add"),
    path("watchlist_remove",views.watchlist_remove, name = "watchlist_remove"),
    path("add_comments",views.add_comments, name = "add_comments"),
    path("add_bid",views.add_bid, name = "add_bid"),
    path("delete_listing",views.delete_listing, name = "delete_listing")
    
]
