from .models import Catalog
from .serializers import CatalogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getCatalog(request):
    catalog = Catalog.objects.all()
    catalog_serializer = CatalogSerializer(catalog, many=True)
    return Response(catalog_serializer.data)