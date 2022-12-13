import pytest

from main.sql.models.model import Student
from main.sql.mysql_orm.client import MysqlORMClient
from main.sql.utils.builder_orm import MysqlORMBuilder


# noinspection PyAttributeOutsideInit
class MysqlBase:

    # is called from setup fixture on every test. test can override this method for its custom data prepare
    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql: MysqlORMClient = mysql_orm_client
        self.mysql_builder: MysqlORMBuilder = MysqlORMBuilder(self.mysql)
        self.prepare()

    def get_students(self, prepod_id=None):
        self.mysql.session.commit()  # need to expire current models and get updated data from MySQL
        students = self.mysql.session.query(Student)
        # students -> SELECT * FROM students;

        # additionally filter by prepod_id
        if prepod_id is not None:
            # students -> SELECT * FROM students WHERE prepod_id = prepod_id;
            students = students.filter_by(prepod_id=prepod_id)

        return students.all()
