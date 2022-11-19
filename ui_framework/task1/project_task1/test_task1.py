# coding=utf-8
import pytest

from ..project_task1.pages.home_page import HomePage
from ..project_task1.pages.email_and_password_form_page import EmailAndPasswordFormPage
from ..project_task1.pages.interests_and_avatar_form_page import InterestsAndAvatarFormPage
from ..project_task1.pages.personal_details_form_page import PersonalDetailsFormPage
from .tests.config.test_data import TestData


class TestTask1:

    @pytest.mark.need_review
    def test_filling_out_forms_on_the_game_page(self):
        home_page = HomePage()
        assert home_page.is_home_page_presented(), "Home page is not presented"

        home_page.go_to_next_page()
        email_and_password_form_page = EmailAndPasswordFormPage()
        assert email_and_password_form_page.is_email_and_password_form_page(), \
            "Email and password form page is not presented"

        email_and_password_form_page.fill_in_the_form()
        email_and_password_form_page.go_to_interests_and_avatar_card()
        interests_and_avatar_form_page = InterestsAndAvatarFormPage()
        assert interests_and_avatar_form_page.is_interests_and_avatar_form_page_presented(), \
            "Interests and avatar form page is not presented"

        interests_and_avatar_form_page.click_upload_image()
        interests_and_avatar_form_page.upload_image(TestData.WINDOW_HANDLE, TestData.PATH_TO_FILE)
        interests_and_avatar_form_page.select_interests(3)
        interests_and_avatar_form_page.go_to_personal_details_card()
        personal_details_form_page = PersonalDetailsFormPage()
        assert personal_details_form_page.is_personal_details_form_page_presented(), \
            "Personal details form page is not presented"

    @pytest.mark.need_review
    def test_closing_the_help_form(self):
        home_page = HomePage()
        assert home_page.is_home_page_presented(), "Home page is not presented"

        home_page.go_to_next_page()
        email_and_password_form_page = EmailAndPasswordFormPage()
        assert email_and_password_form_page.is_email_and_password_form_page(), \
            "Email and password form page is not presented"

        email_and_password_form_page.hide_the_help_form()
        assert email_and_password_form_page.HELP_FORM_ATTR_IS_HIDDEN in \
               email_and_password_form_page.get_attr_help_form_is_hidden(), \
               "Help form is not hidden"

    @pytest.mark.need_review
    def test_accepting_cookies(self):
        home_page = HomePage()
        assert home_page.is_home_page_presented(), "Home page is not presented"

        home_page.go_to_next_page()
        email_and_password_form_page = EmailAndPasswordFormPage()
        assert email_and_password_form_page.is_email_and_password_form_page(), \
            "Email and password form page is not presented"

        email_and_password_form_page.accept_cookies()
        assert not email_and_password_form_page.is_cookies_banner_presented(), "Cookies banner is presented"

    @pytest.mark.need_review
    def test_checking_timer_on_game_page(self):
        home_page = HomePage()
        assert home_page.is_home_page_presented(), "Home page is not presented"

        home_page.go_to_next_page()
        email_and_password_form_page = EmailAndPasswordFormPage()
        assert email_and_password_form_page.is_email_and_password_form_page(), \
            "Email and password form page is not presented"

        assert TestData.TIMER_START in email_and_password_form_page.get_time_in_timer(), \
            f"The timer does not start from {TestData.TIMER_START}"
