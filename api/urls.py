from django.urls import path,include

urlpatterns = [
    path('auth/',include('api.authn.urls')),
    path('doctors/',include('api.doctors.urls')),
    path('patients/',include('api.patients.urls')),
    path('mappings/',include('api.mappings.urls')),
]
