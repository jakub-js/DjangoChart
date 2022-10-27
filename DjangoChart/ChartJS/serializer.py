from .models import Chart
from rest_framework import serializers


class ChartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chart
        fields = ['id', 'title', 'description']
