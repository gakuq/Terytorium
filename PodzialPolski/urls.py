from django.urls import path
from PodzialPolski.views import WojListView, WojDetailView, PowDetailView, GmiDetailView, MiastoDetailView

urlpatterns = [
    path('', WojListView.as_view(), name='woj'),
    path('woj/<int:pk>', WojDetailView.as_view(), name='pow'),
    path('pow/<int:pk>', PowDetailView.as_view(), name='gmi'),
    path('gmi/<int:pk>', GmiDetailView.as_view(), name='gmina'),
    path('miasto/<int:pk>', MiastoDetailView.as_view(), name='miasto')
]



