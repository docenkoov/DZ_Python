import pytest
from yougile_projects import YougileProjects

projects = YougileProjects()


@pytest.fixture
def project_id():
    data = {
        "title": "Новый проект",
        }
    response = projects.create_project(data)
    assert response.status_code == 201
    return response.json()["id"]


# Позитивные тесты
# Создание нового проекта
def test_create_project():
    data = {
        "title": "Новый проект",
        }
    response = projects.create_project(data)
    print(response.text)
    assert response.status_code == 201


# Получение списка проектов
def test_get_projects():
    response = projects.get_projects()
    assert response.status_code == 200


# Обновление существующего проекта
def test_update_project(project_id):
    data = {
        "title": "Обновленный Новый проект",
        "deleted": False
    }

    response = projects.update_project(project_id, data)
    print(response.text)
    assert response.status_code in [200, 400]


# Получение конкретного проекта по ID
def test_get_project(project_id):
    response = projects.get_project(project_id)
    assert response.status_code == 200


# Негативные тесты
# Создание проекта без названия
def test_create_project_without_name():
    data = {
        "description": "Описание проекта",
    }
    response = projects.create_project(data)
    assert response.status_code == 400


# Обновление несуществующего проекта
def test_update_nonexistent_project():
    project_id = "несуществующий_id"
    data = {
        "name": "Неизвестный проект"
    }
    response = projects.update_project(project_id, data)
    assert response.status_code == 400
