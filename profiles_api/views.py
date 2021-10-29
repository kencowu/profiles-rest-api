from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return as list of APIView features"""
        an_apiview =[
            'Uses HTTP methods as function (get, post, patch...)'
            'Is similar to a traditional Django view'
        ]

        return Response({'message': 'Hello', 'an_apiview':an_apiview})