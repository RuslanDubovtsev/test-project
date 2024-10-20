from django.urls import path
from .views import home_page, tours_page, categories_page, tour_detail_page, tours_by_category_page, sign_up_page, logout_action, login_page, TourForms

urlpatterns = [
    path('', home_page, name='home_page' ),
    path('categories/', categories_page, name='categories_page' ),
    path('tours/', tours_page, name='tours_page'),
    path('tour/detail/<int:pk>', tour_detail_page, name="tour_detail_page"),
    path('category/tour/<slug:slug>/', tours_by_category_page, name="tours_by_category_page"),
    path('sign-up/', sign_up_page, name='sign_up_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_action, name='logout_page'),
    path('create_tour/', TourForms.as_view(), name='create_tour')
]
