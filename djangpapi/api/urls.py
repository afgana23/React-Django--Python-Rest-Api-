from django.urls import path,include
from . import views
from api import views

from rest_framework.routers import DefaultRouter


#create routing object
router=DefaultRouter()
#register view with router

router.register('stapi',views.secureview,basename='stapi')

urlpatterns = [
    path('',views.home,name="index"),
     path('infoapi/<int:pk>',views.infoapi),
         path('addapi/',views.customer_add),
           path('funapi/',views.fun_api),
            path('crudapi/',views.crud_api),
           #path('cust',include(router.urls)),
           #class based urls
           path('custapi/',views.CustomerApi.as_view()),
            path('custapi/<int:pk>/',views.CustomerApi.as_view()),
     #Generic based urls
           #path('genapi/',views.DataList.as_view()),
             #('genapi/',views.CreateDataList.as_view()),

              #path('genapi/<int:pk>/',views.RetrieveDataList.as_view()),
               path('genapi/<int:pk>/',views.UpdateDataList.as_view()),
      #Generic based urls with single urls
      path('showgenapi/',views.DataListtogether.as_view()),
  #viewset based urls
      path('cust/',include(router.urls)),
      path('auth/',include('rest_framework.urls',namespace='rest_framework'))

     

      
] 