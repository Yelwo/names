from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

class NameViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NameSerializer
    queryset = models.Name.objects.all()

    class Meta:
        fields = '__all__'
        model = models.Name


class FolderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FolderSerializer
    queryset = models.Folder.objects.all()

    class Meta:
        fields = '__all__'
        model = models.Folder
