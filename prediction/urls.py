from django.urls import path

from . import views

urlpatterns =[
      path('',views.index,name='index'),
      path('decision/',views.decision,name='decision'),
      path('svm/',views.svm,name='svm'),
      path('randamforest/',views.randamforest,name='randamforest')
]