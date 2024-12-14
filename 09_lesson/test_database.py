import pytest
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:1912@localhost:5432/mybase")
metadata = MetaData()
Session = sessionmaker(bind=engine)


student_table = Table('student', metadata, autoload_with=engine)


@pytest.fixture(scope="function")
def setup_database():

    session = Session()
    yield session

    session.execute(student_table.delete())
    session.commit()
    session.close()


def test_insert_student(setup_database):
    """Тест на добавление студента."""
    session = setup_database
    new_student = {'user_id': 123456, 'subject_id': 1}
    session.execute(student_table.insert().values(new_student))
    session.commit()

    inserted_student = session.query(
        student_table).filter_by(user_id=123456).first()
    assert inserted_student is not None


def test_update_student(setup_database):
    """Тест на обновление студента."""
    session = setup_database

    new_student = {'user_id': 123456, 'subject_id': 1}
    session.execute(student_table.insert().values(new_student))
    session.commit()

    session.execute(
        student_table.update().where(
            student_table.c.user_id == 123456).values(user_id=654321))
    session.commit()

    updated_student = session.query(
        student_table).filter_by(user_id=654321).first()
    assert updated_student is not None


def test_delete_student(setup_database):
    """Тест на удаление студента."""
    session = setup_database

    new_student = {'user_id': 123456, 'subject_id': 1}
    session.execute(student_table.insert().values(new_student))
    session.commit()

    session.execute(
        student_table.delete().where(student_table.c.user_id == 123456))
    session.commit()

    deleted_student = session.query(
        student_table).filter_by(user_id=123456).first()
    assert deleted_student is None
