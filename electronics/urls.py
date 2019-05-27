from django.urls import path

from .views import ElectronicsView, show_electronics_item_with_stock_status


app_name = "electronics"


urlpatterns = [
    path('', ElectronicsView.as_view()),
    path('<int:pk>', ElectronicsView.as_view()),
    path('<int:pk>/stock/', show_electronics_item_with_stock_status),
]
