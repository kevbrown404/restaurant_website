from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('view_menu/', views.ViewMenu.as_view(), name="view_menu"),
    path('reservation/new', views.ReservationCreate.as_view(), name="reservation_create"),
    path('reservation/<int:pk>/', views.ReservationDetail.as_view(), name="reservation_detail"),
    path('reservation/<int:pk>/update',views.ReservationUpdate.as_view(), name="reservation_update"),
    path('reservation/<int:pk>/delete',views.ReservationDelete.as_view(), name="reservation_delete"),
    path('reservation/search', views.ReservationSearch.as_view(), name = "reservation_search"),
    path('leave_review/', views.LeaveReview.as_view(), name="leave_review"),
    path('about/', views.About.as_view(), name="about"),
]