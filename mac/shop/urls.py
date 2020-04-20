
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="shopHome"),
    path("about/",views.about,name="aboutus"),
    path("contact/",views.contact,name="contactus"),
    path("tracker/",views.tracker,name="tracking status"),
    path("search/",views.search,name="search"),
    path("products/<int:id>",views.products,name="products"),
    path("checkout/",views.checkout,name="checkout"),
    path("handlerequest/",views.handlerequest,name="handlerequest"),
]