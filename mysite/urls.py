from django.contrib import admin #contrib은 contribute로 웹페이지 관리를 위한 선물 세트임 
from django.urls import path, include

#http://127.0.0.1:8000/ 아래의 단계는 사이트까지 들어왔다는 의미임
urlpatterns = [
    #http://127.0.0.1:8000/polls 앞의 polls/ 앞의 이름은 그냥 내가 붙이는 이름임 include 뒤에는 내가 가져오려는 것으로 값으로 고정값 
    #polls/에서 이름을 바꾸면 그냥 내가 그렇게 부르겠다는 얘기임
    path("polls/", include("polls.urls")), # polls 앱의 URL 연결
    path('admin/', admin.site.urls),
]
