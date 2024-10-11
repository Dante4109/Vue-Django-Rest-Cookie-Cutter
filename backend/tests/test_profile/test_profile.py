import os, django

django.setup()

from hypothesis.extra.django import TestCase
import pytest
from hypothesis import strategies as st, given
from backend.profile.models import UserProfile

from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestUserProfile(TestCase):
    # def setUp(self):

    #     self.student1 = Student.objects.create(
    #         first_name="Tom", last_name="Mboya", admission_number=12345
    #     )

    # setting up new users
    # getting access tokens / logged in users
    # setup up timers

    def test_profile_can_be_created(self):
        """
        Tests if a UserProfile can be created.
        This will not write to the DB.
        """

        profile1 = mixer.blend(UserProfile, first_name="Tom")

        profile1 = UserProfile.objects.last()  # getting the last student

        assert profile1.first_name == "Tom"
