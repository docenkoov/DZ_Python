# DZ_Python

ИНФОРМАЦИЯ ПО РАБОТЕ С ПРОЕКТОМ


Запуск тестов для формирования отчета

Установить необходимые зависимости:
Убедиться, что установлены все необходимые библиотеки. Для этого выполнить команду: pip install -r requirements.txt


Запустить тесты:

Для запуска тестов использовать следующую команду: pytest --alluredir allure-result
Это создаст папку allure-result, в которой будут храниться результаты тестов.


Просмотр сформированного отчета

Чтобы просмотреть отчет, выполнить следующую команду: allure serve allure-result
Это откроет отчет в браузере по умолчанию.


Примечания

Убедиться, что установлен Allure. Если он не установлен, следовать инструкциям на официальном сайте Allure.


СТРУКТУРА ПРОЕКТА

Проект состоит из следующих основных компонентов:
pages: Содержит классы страниц, которые описывают элементы и действия на страницах приложения.
tests: Содержит тестовые сценарии, которые используют классы страниц для выполнения действий и проверок.
conftest.py: Содержит общие фикстуры, используемые в тестах, например, настройка WebDriver.



Следуйте данным инструкциям для успешного запуска и просмотра тестов в вашем проекте!

