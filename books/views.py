from rest_framework.views import APIView
from rest_framework.response import Response

class CreateBooksAPIView(APIView):
    def get(self, request):
            return Response({"message": "Hello for today! See you tomorrow!"})
