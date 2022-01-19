from rest_framework import serializers
from . import models

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        # fields는 데이터베이스 속성을 제어합니다.
        fields = ('id', 'title', 'image','description')
        model = models.Movie