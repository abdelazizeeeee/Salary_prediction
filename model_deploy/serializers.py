from rest_framework import serializers
from .models import Features


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ("id", "age", "gender", "exp", "educ_lvl", "job",)
