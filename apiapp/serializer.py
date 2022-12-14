from rest_framework import serializers
from apiapp.models import Studentinfo

#create or define serializer class

class Studentserializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    rno=serializers.IntegerField()
    per=serializers.FloatField()

    def create(self, validated_data):
        return Studentinfo.objects.create(**validated_data)



    def update(self, instance, validated_data):

        instance.name=validated_data.get('name',instance.name)
        instance.rno=validated_data.get('rno',instance.rno)
        instance.per=validated_data.get('per',instance.per)
        instance.save()
        return instance