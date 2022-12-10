# -*- coding: utf-8 -*-
import pytest
from barancev_python_training_course.model.group import Group
from barancev_python_training_course.fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="dfgdfg", header="dfgdfg", footer="dfgfghgfhg"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
