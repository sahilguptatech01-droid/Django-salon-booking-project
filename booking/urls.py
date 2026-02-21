from django.urls import path 
from . import views

app_name='booking'


urlpatterns = [
   path('',views.index,name='index'),
   path('detail/<int:id>/',views.detail,name="detail_page"),
   path('book/',views.booking_form,name="book"),
   # path('booking_detail',views.booking_detail,name='booking_detail'),

]
