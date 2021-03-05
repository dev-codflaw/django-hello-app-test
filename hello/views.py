from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView



class HelloView(APIView):
    
    def get(self, request):
        content = {'message': 'hello world! '}
        return Response(content)