from django.conf.urls import patterns, include, url
from OES.views import *
from OES.examView import *
from OES.tests import *

urlpatterns = patterns('',
                       url(r'^logout/$', logout_page),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       url(r'^register/$', register),
                       url(r'^register/success/$', register_success),
                       url(r'^home/$', home),
                        #Test Creation

                       url(r'^createExams/', createExamDetails),
                       url(r'^listexams/$', ListUserExamDetails.as_view()),
                       url(r'^listresultuser/$',list_result_user),

                        # Test taker
                       url(r'^testhome/$',test_home),
                       url(r'^tests/$', ListExamDetails.as_view()),
                       url(r'^startTest/$', ListQuestions.as_view()),
                       url(r'^result/$',result),
                       url(r'^listresult/$',list_result),
        )