import pytest
from rest_framework.test import APIClient
from model_bakery import baker
import random
from students.models import Course, Student

api_url = '/api/v1/courses/'


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory()

    response = client.get(api_url)

    assert response.status_code == 200

    data = response.json()
    assert len(data) == 1
    assert course.name == data[0]['name']


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get(api_url)

    assert response.status_code == 200

    data = response.json()
    assert len(courses) == len(data)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_course_id(client, course_factory):
    courses = course_factory(_quantity=10)
    random_course = random.choice(courses)
    response_url = f'{api_url}?id={random_course.id}'

    response = client.get(response_url)

    assert response.status_code == 200

    data = response.json()
    assert len(data) == 1
    assert random_course.name == data[0]['name']


@pytest.mark.django_db
def test_filter_course_name(client, course_factory):
    courses = course_factory(_quantity=10)
    random_course = random.choice(courses)
    response_url = f'{api_url}?name={random_course.name}'

    response = client.get(response_url)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['id'] == random_course.id


@pytest.mark.django_db
def test_create_course(client):
    data = {'name': 'django'}

    response = client.post(api_url, data)

    assert response.status_code == 201
    assert response.json()['name'] == data['name']


@pytest.mark.django_db
def test_update_course(client, course_factory, student_factory):
    students = student_factory(_quantity=10)
    student_ids = [student.id for student in students]
    course = course_factory()
    course.students.add(*student_ids)

    data = {'name': 'django', 'students': student_ids}
    response_url = f'{api_url}{course.id}/'

    response = client.patch(response_url, data)

    response_data = response.json()
    assert response.status_code == 200
    assert response_data['name'] == 'django'
    assert len(response_data['students']) == len(students)


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    students = student_factory(_quantity=10)
    student_ids = [student.id for student in students]
    course = course_factory()
    course.students.add(student_ids)
    response_url = f'{api_url}{course.id}/'

    response = client.delete(response_url)

    assert response.status_code == 204

# @pytest.mark.django_db
# def test_api(client):
#     # Arrange
#     # client = APIClient()
#
#     # Act
#     response = client.get(api_url)
#
#     # Assert
#     assert response.status_code == 200
#     data = response.json()
#     assert len(data) == 0


