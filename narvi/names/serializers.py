from rest_framework import serializers
from . import models


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Name
        fields = ['id', 'name_text', 'folder']


class FolderSerializer(serializers.ModelSerializer):
    names = serializers.SerializerMethodField()

    def get_names(self, obj):
        return NameSerializer(obj.name_set.all(), many=True).data

    class Meta:
        model = models.Folder
        fields = ['id', 'title', 'names']
    