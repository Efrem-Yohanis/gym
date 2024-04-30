
from django.urls import path,include
from . import views

urlpatterns = [
path('',views.home,name='home'),
path('manageMembers/',views.manageMembers,name='manageMembers'),
path('addNewMember/',views.addNewMembers,name='addNewMember'),
path('getIn/',views.getIn,name='getIn'),
path('plan/',views.plan,name='plan'),
path('payment/',views.payment,name='payment'),
path('attendance/',views.attendance,name='attendance'),
path('generateIdCard/',views.generateIdCard,name='generateIdCard'),
path('reports/',views.reports,name='reports'),



]