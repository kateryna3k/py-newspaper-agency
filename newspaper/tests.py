from django.contrib.auth import get_user_model
from django.test import TestCase

from newspaper.models import Newspaper, Topic, Redactor


class PrivateNewspaperTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123",
            years_of_experience=8
        )
        self.client.force_login(self.user)

    def test_newspaper_search(self):
        res = self.client.get("/newspapers/?title=pets")
        self.assertEqual(res.status_code, 200)
        self.assertQuerysetEqual(
            res.context["newspaper_list"],
            Newspaper.objects.filter(title__icontains="pets")
        )


class PrivateRedactorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser2",
            password="password123",
            years_of_experience=8,
        )
        self.client.force_login(self.user)

    def test_redactor_search(self):
        res = self.client.get("/redactors/?username=testuser2")
        self.assertEqual(res.status_code, 200)
        self.assertQuerysetEqual(
            res.context["redactor_list"],
            Redactor.objects.filter(username__icontains="testuser2")
        )


class PrivateTopicTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser3",
            password="password123",
            years_of_experience=5,
        )
        self.client.force_login(self.user)

    def test_topic_search(self):
        res = self.client.get("/topics/?name=love")
        self.assertEqual(res.status_code, 200)
        self.assertQuerysetEqual(
            res.context["topic_list"],
            Topic.objects.filter(name__icontains="love")
        )
