# -*- coding: utf-8 -*-
from barancev_python_training_course.model.group import Group


def test_add_group(app):
    app.group.create(Group(name="dfgdfg", header="dfgdfg", footer="dfgfghgfhg"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
