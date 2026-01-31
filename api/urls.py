from django.urls import path,include
from .views import TransactionCreateListView, TransactionDeleteView


urlpatterns = [
    path('transactions/', TransactionCreateListView.as_view(), name='create_list_trans'),
    path('transaction/<int:pk>/', TransactionDeleteView.as_view(), name='delete_t')
]
