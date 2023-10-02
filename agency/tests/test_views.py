from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import Topic, Newspaper


def data_for_tests(self) -> None:
    self.topic = Topic.objects.create(name="Sports")
    self.redactor = get_user_model().objects.create_user(
        username="testuser1",
        password="testpassword123",
        years_of_experience=5,
        first_name="first",
        last_name="last",
    )
    self.newspaper = Newspaper.objects.create(
        title="title1",
        content="content1",
        published_date="2023-01-01",
        topic=self.topic,
    )


class LoginRequiredTests(TestCase):
    def setUp(self) -> None:
        data_for_tests(self)

    def test_login_not_required_index(self):
        response = self.client.get(reverse("agency:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "agency/index.html")

    def test_login_not_required_topic_list(self):
        response = self.client.get(reverse("agency:topic-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "agency/topic_list.html")

    def test_login_not_required_topic_detail(self):
        response = self.client.get(
            reverse("agency:topic-detail", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "agency/topic_detail.html")

    def test_login_not_required_redactor_list(self):
        response = self.client.get(reverse("agency:redactor-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "agency/redactor_list.html")

    def test_login_not_required_redactor_detail(self):
        response = self.client.get(
            reverse("agency:redactor-detail", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "agency/redactor_detail.html")

    def test_login_not_required_newspaper_list(self):
        response = self.client.get(reverse("agency:newspaper-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "agency/newspaper_list.html")

    def test_login_not_required_newspaper_detail(self):
        response = self.client.get(
            reverse("agency:newspaper-detail", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "agency/newspaper_detail.html")

    def test_login_required_topic_create(self):
        response = self.client.get(reverse("agency:topic-create"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_topic_update(self):
        response = self.client.get(
            reverse("agency:topic-update", kwargs={"pk": 1})
        )
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_topic_delete(self):
        response = self.client.get(
            reverse("agency:topic-delete", kwargs={"pk": 1})
        )
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_redactor_create(self):
        response = self.client.get(reverse("agency:redactor-create"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_redactor_update(self):
        response = self.client.get(
            reverse("agency:redactor-update", kwargs={"pk": 1})
        )
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_redactor_delete(self):
        response = self.client.get(
            reverse("agency:redactor-delete", kwargs={"pk": 1})
        )
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_newspaper_create(self):
        response = self.client.get(reverse("agency:newspaper-create"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_newspaper_update(self):
        response = self.client.get(
            reverse("agency:newspaper-update", kwargs={"pk": 1})
        )
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_newspaper_delete(self):
        response = self.client.get(
            reverse("agency:newspaper-delete", kwargs={"pk": 1})
        )
        self.assertNotEqual(response.status_code, 200)


class ListViewTests(TestCase):
    def setUp(self) -> None:
        data_for_tests(self)
        self.topic2 = Topic.objects.create(name="Politics")
        self.redactor2 = get_user_model().objects.create_user(
            username="testuser2",
            password="testpassword123",
            years_of_experience=5,
            first_name="first",
            last_name="last",
        )
        self.newspaper2 = Newspaper.objects.create(
            title="title2",
            content="content2",
            published_date="2023-01-01",
            topic=self.topic2,
        )

    def test_retrieve_index_content(self):
        response = self.client.get(reverse("agency:index"))
        self.assertContains(response, self.newspaper.title)
        self.assertContains(response, self.newspaper2.title)

    def test_retrieve_topic_list(self):
        response = self.client.get(reverse("agency:topic-list"))
        self.assertContains(response, self.topic.name)

    def test_retrieve_topic_using_search(self):
        response = self.client.get(
            reverse("agency:topic-list"), {"name": "sp"}
        )
        self.assertContains(response, self.topic.name)
        self.assertNotContains(response, self.topic2)

    def test_retrieve_redactor_list(self):
        response = self.client.get(reverse("agency:redactor-list"))
        self.assertContains(response, self.redactor.username)

    def test_retrieve_redactor_using_search(self):
        response = self.client.get(
            reverse("agency:redactor-list"), {"username": "1"}
        )
        self.assertContains(response, self.redactor.username)
        self.assertNotContains(response, self.redactor2.username)

    def test_retrieve_newspaper_list(self):
        response = self.client.get(reverse("agency:newspaper-list"))
        self.assertContains(response, self.topic.name)

    def test_retrieve_newspaper_using_search(self):
        response = self.client.get(
            reverse("agency:newspaper-list"), {"title": "1"}
        )
        self.assertContains(response, self.newspaper.title)
        self.assertNotContains(response, self.newspaper2.title)


class DetailViewTests(TestCase):
    def setUp(self) -> None:
        data_for_tests(self)

    def test_retrieve_topic_detail_info(self):
        response = self.client.get(
            reverse("agency:topic-detail", kwargs={"pk": 1})
        )
        self.assertContains(response, self.topic.name)

    def test_retrieve_redactor_detail_info(self):
        response = self.client.get(
            reverse("agency:redactor-detail", kwargs={"pk": 1})
        )
        self.assertContains(response, self.redactor.username)

    def test_retrieve_newspaper_detail_info(self):
        response = self.client.get(
            reverse("agency:newspaper-detail", kwargs={"pk": 1})
        )
        self.assertContains(response, self.topic.name)
