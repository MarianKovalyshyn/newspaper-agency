from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Topic, Newspaper


class ModelsTests(TestCase):
    def setUp(self) -> None:
        self.topic = Topic.objects.create(name="Sports")
        self.redactor = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword123",
            years_of_experience=5,
            first_name="first",
            last_name="last",
        )
        self.newspaper = Newspaper.objects.create(
            title="title",
            content="content",
            published_date="2023-01-01",
            topic=self.topic,
        )

    def test_topic_str(self):
        self.assertEqual(str(self.topic), "Sports")

    def test_topic_get_absolute_url(self):
        self.assertEqual(self.topic.get_absolute_url(), "/topics/1/")

    def test_redactor_str(self):
        self.assertEqual(str(self.redactor), "testuser (first last)")

    def test_redactor_get_absolute_url(self):
        self.assertEqual(self.redactor.get_absolute_url(), "/redactors/1/")

    def test_newspaper_str(self):
        self.assertEqual(str(self.newspaper), "title")

    def test_newspaper_get_absolute_url(self):
        self.assertEqual(self.newspaper.get_absolute_url(), "/newspapers/1/")

    def test_newspaper_preview(self):
        self.assertEqual(self.newspaper.preview(), "content ...")
