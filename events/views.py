from rest_framework import generics
from .models import EventCategory, JobCategory, Event, EventImage, EventAgenda, EventJobCategoryLinking, EventMember, EventUserWishList, UserCoin
from .serializers import EventCategorySerializer, JobCategorySerializer, EventSerializer, EventImageSerializer, EventAgendaSerializer, EventJobCategoryLinkingSerializer, EventMemberSerializer, EventUserWishListSerializer, UserCoinSerializer


class EventCategoryListCreateView(generics.ListCreateAPIView):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer


class JobCategoryListCreateView(generics.ListCreateAPIView):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer


class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventImageListCreateView(generics.ListCreateAPIView):
    queryset = EventImage.objects.all()
    serializer_class = EventImageSerializer


class EventAgendaListCreateView(generics.ListCreateAPIView):
    queryset = EventAgenda.objects.all()
    serializer_class = EventAgendaSerializer


class EventJobCategoryLinkingListCreateView(generics.ListCreateAPIView):
    queryset = EventJobCategoryLinking.objects.all()
    serializer_class = EventJobCategoryLinkingSerializer


class EventMemberListCreateView(generics.ListCreateAPIView):
    queryset = EventMember.objects.all()
    serializer_class = EventMemberSerializer


class EventUserWishListListCreateView(generics.ListCreateAPIView):
    queryset = EventUserWishList.objects.all()
    serializer_class = EventUserWishListSerializer


class UserCoinListCreateView(generics.ListCreateAPIView):
    queryset = UserCoin.objects.all()
    serializer_class = UserCoinSerializer