from django.test import TestCase

from agency.forms import RedactorCreationForm


class FormsTests(TestCase):
    def test_redactor_creation_form_with_valid_data(self):
        form_data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "years_of_experience": 5,
            "password1": "testpassword123",
            "password2": "testpassword123",
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
