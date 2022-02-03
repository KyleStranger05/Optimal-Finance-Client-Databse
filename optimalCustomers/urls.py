from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login and Reg
    path('', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Main
    path('home', views.home , name='home'),
    path('nCopt' , views.newCustomer, name='newCustomer'),

    #Add Customers
    path('newCompany', views.newCompany , name='newCompany'),
    path('newIndividual', views.newIndividual , name='newIndividual'),

    #Checklists
    path('checklistHome' , views.checklistHome , name='checklistHome'),

    #Company
    path('companyIT14', views.companyIT14.as_view(), name='companyIT14'),
    path('companyFIN', views.companyFIN, name='companyFIN'),
    path('companyPROV', views.companyPROV, name='companyPROV'),
    path('companyANNR', views.companyANNR, name='companyANNR'),

    #Individual
    path('individualIT12', views.individualIT12, name='individualIT12'),
    path('individualPROV', views.individualPROV, name='individualPROV'),

    #Reports
    path('reportsHome', views.reportsHome, name='reportsHome'),
    path('printAllpdf', views.printAllpdf, name='printAllpdf'),

]
