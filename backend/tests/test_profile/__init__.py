from hypothesis.extra.django import TestCase
import pytest
from hypothesis import strategies as st, given
from profile.models import UserProfile

from mixer.backend.django import mixer


class TestUserProfileModel(TestCase):
    def user_profile_can_be_created(self):

        profile1 = mixer.blend(Student, first_name="Tom")

        student_result = Student.objects.last()  # getting the last student

        assert student_result.first_name == "Tom"
