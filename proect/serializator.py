from rest_framework import serializers
from proect.models import Proect

class PersonSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Proect # manzil
        fields = "__all__" # hammasini ol degani



# class PersonSerializers(serializers.Serializer):
#     name = serializers.CharField()
#     content = serializers.CharField()
#     is_published = serializers.BooleanField()
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Proect.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name),
#         instance.content = validated_data.get("content", instance.content),
#         instance.is_published = validated_data.get("is_published", instance.is_published),
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id),
#         instance.save()
#         return instance