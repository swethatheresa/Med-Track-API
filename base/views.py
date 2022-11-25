
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

@api_view(['GET'])
def patient_list(request):
    patient=Patient.objects.all()
    serializer=PatientSerializer(patient,many=True)
    return Response(serializer.data) 
    
@api_view(['GET'])
def patient_detail(request,pk):
    patient=Patient.objects.get(patient_id=pk)
    serializer=PatientSerializer(patient,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def patient_create(request):
    serializer=PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def patient_update(request,pk):
    patient=Patient.objects.get(patient_id=pk)
    serializer=PatientSerializer(instance=patient,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def patient_delete(request,pk):
    patient=Patient.objects.get(patient_id=pk)
    patient.delete()
    return Response('Deleted')

@api_view(['GET'])
def medicine_list(request,pk):
    medicine=Medicine.objects.filter(patient_id=pk)
    serializer=MedicineSerializer(medicine,many=True)
    return Response(serializer.data) 

@api_view(['POST'])
def medicine_create(request,pk):
    serializer=MedicineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    