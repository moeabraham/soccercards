from django.urls import path
from . import views

# urlpatterns has to be here otherwise app will crash
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),

    path('teams/', views.teams_index, name="teams_index"),
    path('teams/<int:team_id>/add_fixture/', views.add_fixture, name='add_fixture' ),
    path('teams/create', views.TeamCreate.as_view(), name="teams_create"),
    path('teams/<int:team_id>', views.teams_detail, name="teams_detail"),
    path('teams/<int:pk>/update', views.TeamUpdate.as_view(), name="teams_update"),
    path('teams/<int:pk>/delete', views.TeamDelete.as_view(), name="teams_delete"),
    path('teams/<int:team_id>/add_photo', views.add_photo, name="add_photo"),

    path('teams/<int:team_id>/assoc_card/<int:card_id>/', views.assoc_card, name="assoc_card"),



    path('cards/', views.cards_index, name="index"),
    path('cards/<int:card_id>/', views.cards_detail, name="detail"),
    path('cards/create/', views.CardCreate.as_view(), name="cats_create"),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name="cards_update"),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name="cards_delete"),

    # path('teams/<int:team_id>/crop', views.crop, name="crop"),
    # path('image_upload', views.img, name = 'img'),
    # path('success', views.success, name = 'success'),









]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT)