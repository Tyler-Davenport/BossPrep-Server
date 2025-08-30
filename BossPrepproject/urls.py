
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bossprepapi.views.questions import QuestionViewSet
from bossprepapi.views.trials import TrialViewSet
from bossprepapi.views.responses import ResponseViewSet
from bossprepapi.views.trial_questions import TrialQuestionViewSet
from bossprepapi.views.users import UserView
from bossprepapi.views.auth import google_auth_check

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'questions', QuestionViewSet, 'question')
router.register(r'trials', TrialViewSet, 'trial')
router.register(r'responses', ResponseViewSet, 'response')
router.register(r'trial-questions', TrialQuestionViewSet, 'trialquestion')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('users/<str:uid>', UserView.as_view()),
    path('users', UserView.as_view()),
    path('auth/google', google_auth_check),
]

