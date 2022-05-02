from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at', )

    def create(self, validated_data):

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):

        max_ads_online = 10
        if self.context['request'].method == 'POST' or data.get('status') == 'OPEN':
            ads_count = Advertisement.objects.filter(
                creator = self.context['request'].user,
                status = 'OPEN'
            ).count()
            if ads_count >= max_ads_online:
                raise ValidationError(
                    f'Вы превысили максимальное количество одновоременно открытых объявлений.'
                    f' Максимальное количество объявлений {max_ads_online}'
                )

        return data
