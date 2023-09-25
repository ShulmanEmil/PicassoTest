from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer
from .tasks import process_file


@api_view(['POST'])
def upload(request):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
        file_serializer.save()
        process_file.delay(file_serializer.data['id'])
        return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def files(request):
    files_list = File.objects.all()
    file_serializer = FileSerializer(files_list, many=True)
    return Response(file_serializer.data)
