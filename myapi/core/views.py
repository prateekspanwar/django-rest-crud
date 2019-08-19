from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .models import Inventory
from .serializers import InventorySerializer


class HelloView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		content = {'message': 'Hello, World!'}
		return Response(content)


class InventoryView(APIView):
	permission_classes = (IsAuthenticated,)
	
	def get(self, request, pk=None):
		if pk:
			inventory = get_object_or_404(Inventory.objects.all(), pk=pk)
			serializer = InventorySerializer(inventory)
			return Response({"inventory": serializer.data})
		inventories = Inventory.objects.all()
		serializer = InventorySerializer(inventories, many=True)
		return Response({"inventory": serializer.data})

	def post(self, request):
		print('herer####################3',request)
		inventory = request.data.get('inventory')

		# Create an inventory from the above data
		serializer = InventorySerializer(data=inventory)
		if serializer.is_valid(raise_exception=True):
			inventory_saved = serializer.save()
		return Response({"success": "inventory '{}' created successfully".format(inventory_saved.title)})

	def put(self, request, pk):
		saved_inventory = get_object_or_404(Inventory.objects.all(), pk=pk)
		data = request.data.get('inventory')
		serializer = InventorySerializer(instance=saved_inventory, data=data, partial=True)

		if serializer.is_valid(raise_exception=True):
			inventory_saved = serializer.save()
		return Response({"success": "inventory '{}' updated successfully".format(inventory_saved.title)})


	def delete(self, request, pk):
		# Get object with this pk
		inventory = get_object_or_404(Inventory.objects.all(), pk=pk)
		inventory.delete()
		return Response({"message": "inventory with id `{}` has been deleted.".format(pk)},status=204)