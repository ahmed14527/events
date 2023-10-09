from rest_framework import serializers
from .models import EventCategory, JobCategory, Event, EventImage, EventAgenda, EventJobCategoryLinking, EventMember, EventUserWishList, UserCoin


class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = '__all__'


class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = '__all__'


class EventAgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAgenda
        fields = '__all__'


class EventJobCategoryLinkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventJobCategoryLinking
        fields = '__all__'


class EventMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventMember
        fields = '__all__'


class EventUserWishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUserWishList
        fields = '__all__'


class UserCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCoin
        fields = '__all__'