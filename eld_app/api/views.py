from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import calculate_trip

class CalculateTripView(APIView):
    def post(self, request):
        try:
            data = request.data
            result = calculate_trip(
                data['current_location'],
                data['pickup_location'],
                data['dropoff_location'],
                float(data['current_cycle_used'])
            )
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)