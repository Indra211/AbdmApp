from rest_framework import serializers
from .models import Patient,Doctor

class Doctorserializer(serializers.ModelSerializer):
    class Meta :
        model = Doctor
        fields = "__all__"

class Patientserializer(serializers.ModelSerializer):
    Doctor = Doctorserializer()
    class Meta :
        model = Patient
        fields = "__all__"
