from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

# Create your views here.

app_name = 'votingapp'
urlpatterns = [
	path('home/', views.home, name='home'),
	path('login/', login, {'template_name': 'votingapp/login.html'}),
	path('login/', logout, {'template_name': 'votingapp/login.html'}, name='logout'),
	#position
	path('home/position_page/', views.position_page, name='position_page'),
	path('home/position_page/<int:position_id>',
		views.vote_position_page, name='vote_position_page'),
	path('home/position_page/vote/position/<int:position_id>/candidate/<int:candidate_id>',
		views.vote_position_post, name='vote_position_post'),
	#party
	path('home/party_page/', views.party_page, name='party_page'),
	path('home/party_page/<int:party_id>',
		views.vote_party_page, name='vote_party_page'),
	path('home/party_page/party/<int:party_id>',
		views.vote_party_post, name='vote_party_post'),
	path('home/position_page/unvote/position/<int:position_id>/candidate/<int:candidate_id>',
		views.unvote_position_post, name='unvote_position_post'),
]
