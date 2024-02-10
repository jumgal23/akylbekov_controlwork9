from django.urls import path
from .views import (
    AnnouncementListView, AnnouncementDetailView, AnnouncementCreateView,
    AnnouncementUpdateView, AnnouncementDeleteView, CommentCreateView,
    CommentDeleteView
)

app_name = 'webapp'

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement_list'),
    path('announcement/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('announcement/create/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('announcement/<int:pk>/update/', AnnouncementUpdateView.as_view(), name='announcement_update'),
    path('announcement/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement_delete'),
    path('announcement/<int:pk>/comment/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
