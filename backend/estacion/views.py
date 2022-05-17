# Django

# Django RestFramework
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response

# app
from estacion import serializer as serializer_estacion
from estacion import models as models_estacion

from ticket.template import TemplateResponse 
from rest_framework import status

class LevelViewSet(viewsets.ModelViewSet):
    queryset =  models_estacion.Level.objects.all()
    serializer_class = serializer_estacion.LevelSerializer

class SectorViewSet(viewsets.ModelViewSet):
    queryset =  models_estacion.Sector.objects.all()
    serializer_class = serializer_estacion.SectorSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset =  models_estacion.Position.objects.all()
    serializer_class = serializer_estacion.PositionSerializer

class EstacionViewSet(viewsets.ModelViewSet):
    queryset =  models_estacion.Estacion.objects.all()
    serializer_class = serializer_estacion.EstacionSerializer


class EstacionFreeView(generics.ListAPIView):
    serializer_class = serializer_estacion.EstacionSerializer
    queryset =  models_estacion.Estacion.objects.all()
    
    def get_queryset(self):
        free = models_estacion.Estacion.objects.all().filter(state=False).first()
        free.identificador = str(free)
        return [free]


class EstacionBussyView(generics.ListAPIView):
    serializer_class = serializer_estacion.EstacionSerializer
    queryset =  models_estacion.Estacion.objects.all()
    
    def get_queryset(self):
        bussy = models_estacion.Estacion.objects.all().filter(state=True)
        return bussy


class EstacionDetailCurrent(viewsets.ModelViewSet):
    queryset =  models_estacion.Estacion.objects.all()
    serializer_class = serializer_estacion.EstacionSerializer

    def list(self,request,*args,**kwargs):
        total = models_estacion.Estacion.objects.all().count()
        bussy = models_estacion.Estacion.objects.all().filter(state=True).count()

        response= TemplateResponse(
                    status=status.HTTP_400_BAD_REQUEST,
                    error=False,
                    message="Datos de Estado",
                    body= {
                        "total": total,
                        "ocupados": bussy,
                        "libres": total-bussy
                    })  
        return Response(response.getResponse())