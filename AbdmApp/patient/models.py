from django.db.models import *

class Doctor(Model):
    Name = CharField(max_length=255)
    Age = IntegerField(default=0)
    experience = IntegerField(default=0)
    Specialization = CharField(max_length=255)

    def __str__(self):
        return self.Name

class Patient(Model):
    Name = CharField(max_length=255)
    Age = IntegerField(default=0)
    Promblem = CharField(max_length=255)
    Doctor = ForeignKey(Doctor,on_delete=CASCADE)
    Doctor_prescription = TextField(max_length=1000)

    def __str__(self):
        return self.Name

