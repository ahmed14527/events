from django.urls import path
from .views import (
    EventCategoryListCreateView,
    JobCategoryListCreateView,
    EventListCreateView,
    EventImageListCreateView,
    EventAgendaListCreateView,
    EventJobCategoryLinkingListCreateView,
    EventMemberListCreateView,
    EventUserWishListListCreateView,
    UserCoinListCreateView,
)

urlpatterns = [
    path('event-categories/', EventCategoryListCreateView.as_view(), name='event-category-list'),
    path('job-categories/', JobCategoryListCreateView.as_view(), name='job-category-list'),
    path('events/', EventListCreateView.as_view(), name='event-list'),
    path('event-images/', EventImageListCreateView.as_view(), name='event-image-list'),
    path('event-agendas/', EventAgendaListCreateView.as_view(), name='event-agenda-list'),
    path('event-job-category-linking/', EventJobCategoryLinkingListCreateView.as_view(), name='event-job-category-linking-list'),
    path('event-members/', EventMemberListCreateView.as_view(), name='event-member-list'),
    path('event-user-wish-lists/', EventUserWishListListCreateView.as_view(), name='event-user-wish-list'),
    path('user-coins/', UserCoinListCreateView.as_view(), name='user-coin-list'),
]