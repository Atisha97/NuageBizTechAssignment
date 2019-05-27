from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from .models import Electronics
from .serializers import ElectronicsSerializer


class ElectronicsView(APIView):
    def get(self, request, pk=None):
        if pk:
            electronics = get_object_or_404(Electronics.objects.all(), pk=pk)
            serializer = ElectronicsSerializer(electronics)
            return Response({"electronics": serializer.data})
        electronics = Electronics.objects.all()
        serializer = ElectronicsSerializer(electronics, many=True)
        return Response({"electronics": serializer.data})

    def post(self, request):
        electronics = request.data.get('electronics')

        # Create an electronics from the above data
        serializer = ElectronicsSerializer(data=electronics)
        if serializer.is_valid(raise_exception=True):
            electronic_saved = serializer.save()
        return Response({"success": "Electronics '{}' created successfully".format(electronic_saved.name)})

    def put(self, request, pk):
        saved_electronic = get_object_or_404(Electronics.objects.all(), pk=pk)
        data = request.data.get('electronics')
        serializer = ElectronicsSerializer(instance=saved_electronic, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            electronic_saved = serializer.save()
        return Response({"success": "Electronics '{}' updated successfully".format(electronic_saved.name)})

    def delete(self, request, pk):
        # Get object with this pk
        electronics = get_object_or_404(Electronics.objects.all(), pk=pk)
        electronics.delete()
        return Response({"message": "Electronics with id `{}` has been deleted.".format(pk)},status=204)


@api_view(['GET'])
def show_electronics_item_with_stock_status(request, pk):
    if pk:
        electronics = get_object_or_404(Electronics.objects.all(), pk=pk)
        serializer = ElectronicsSerializer(electronics)
        name = serializer.data["name"]
        stock = serializer.data["stock"]
        return Response({name: stock})
        
        

