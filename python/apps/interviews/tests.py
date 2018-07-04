from rest_framework.test import APITestCase
from django.utils import timezone

from apps.base_tests import ListTestMixin, CreateTestMixin, GetInstanceTestMixin
from apps.departments.models import Department
from .models import Criteria, Interview
from apps.candidates.models import Candidate
from .serializers import CriteriaSerializer, InterviewerSerializer, InterviewDetailSerializer


class CriteriaCreateListTestCase(ListTestMixin, CreateTestMixin, APITestCase):
    url = '/criterias/'
    model = Criteria
    serializer = CriteriaSerializer

    def setUp(self):
        department = Department.objects.create(name='Python')
        self.request_body = {
            "name": "OOP",
            "department": department.id
        }


class InterviewListTestCase(ListTestMixin, APITestCase):
    url = '/interviews/'
    model = Interview
    serializer = InterviewerSerializer


class InterviewDetailTest(GetInstanceTestMixin, APITestCase):
    url = '/interviews/'
    model = Interview
    serializer = InterviewDetailSerializer

    fixtures = ['candidates.json', 'departments.json', 'requests.json', 'users.json', 'interviews.json',
                'vacancies.json']

    def setUp(self):
        self.instance = Interview.objects.create(
            date=timezone.now(),
            candidate=Candidate.objects.get(pk=1)
        )
