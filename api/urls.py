from rest_framework.documentation import include_docs_urls
from django.urls import path, include

urlpatterns = [
    path('delivery-company/', include('delivery_company.urls')),
    path('docs/', include_docs_urls(title="Medical Drones API")),
]
