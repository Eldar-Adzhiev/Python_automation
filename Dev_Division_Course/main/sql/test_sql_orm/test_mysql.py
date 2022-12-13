from sqlalchemy import func

from main.sql.models.model import Student, Prepod
from main.sql.test_sql_orm.base import MysqlBase


class TestMysqlCreate(MysqlBase):

    # is called from setup fixture
    def prepare(self):
        self.prepod = self.mysql_builder.create_prepod()
        self.students = []
        for _ in range(10):
            student = self.mysql_builder.create_student(prepod_id=self.prepod.id)
            self.students.append(student)

    # def test(self):
    #     # tests should be independent and run in parallel, so
    #     # we need to get data by concrete prepod_id, created in current test
    #     students = self.get_students(prepod_id=self.prepod.id)
    #     assert len(students) == 10
    #     for s in students:
    #         assert s.prepod_id == self.prepod.id
    #
    #     # print(self.mysql.session.query(Student).first())
    #     # print(self.mysql.session.query(Prepod).first().surname)
    #
    #     prepods = self.mysql.session.query(Prepod).filter_by(id=1).all()
    #     for p in prepods:
    #         print(p)
    #         print(type(p))
    #         print(dir(p))
    #
    #     # print(self.mysql.session.query(Prepod).filter_by(id=10))
    #     #
    #     # print(self.mysql.session.query(Student.prepod_id, func.count(Student.id)) # SELECT s.prepod_id, COUNT(s.id)
    #     #       .filter_by(prepod_id=self.prepod.id) # WHERE
    #     #       .group_by(Student.prepod_id) # GROUP BY
    #     #       .all())


# class TestMysqlDelete(TestMysqlCreate):

    # inherits prepare method from TestMysqlCreate

    def test(self):
        # tests should be independent, so
        # we need to delete data created by this test
        student_to_delete = self.students[0].id
        self.mysql.session.query(Student).filter_by(id=student_to_delete).delete()

        # and get data by concrete prepod_id, created in current test
        assert len(self.get_students(prepod_id=self.prepod.id)) == 9

        # this code is wrong, we can't delete all students,
        # cause there can be data from other tests running in parallel
        self.mysql.session.query(Student).delete()
        assert len(self.get_students()) == 0
