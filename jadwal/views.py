from django.shortcuts import render
from . models import jadwalModels
from . serializers import jadwalserializer

# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def readjadwal(request):
    jadwalImsyak = jadwalModels.objects.all()
    serializer =jadwalserializer(jadwalImsyak, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def readjadwallol(request, id):
    jadwalImsyak = jadwalModels.objects.get(pk=id)
    serializer =jadwalserializer(jadwalImsyak, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createjadwal(request):
    serializer = jadwalserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updatejadwal(request, id):
    jadwalImsyak = jadwalModels.objects.get(pk=id)
    serializer = jadwalserializer(instance=jadwalImsyak, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletejadwal(request, id):
    jadwalImsyak = jadwalModels.objects.get(pk=id)
    jadwalImsyak.delete()

    return Response('data di hapus cuy', status=204)














# @api_view(['GET','POST'])
# def readjadwal(request):

    # Menampilkan semua data
    # if request.method == 'GET':
    #     jadwalImsyak = jadwalModels.objects.all()
    #     serializer = jadwalserializer(jadwalImsyak, many=True)
    #     return Response(serializer.data)

    # Menambahkan data
    # if request.method == 'POST':
    #     serializer = jadwalserializer (data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)