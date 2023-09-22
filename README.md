
### SkyproTODOLIST

Приложение для планирования целей и отслеживание прогресса по ним.

### Предварительные требования к будущему приложению

1. Вход/регистрация/аутентификация через вк.
2. Создание целей.
   - Выбор временного интервала цели с отображением кол-ва дней до завершения цели.
   - Выбор категории цели (личные, работа, развитие, спорт и т. п.) с возможностью добавлять/удалять/обновлять категории.
   - Выбор приоритета цели (статичный список minor, major, critical и т. п.).
   - Выбор статуса выполнения цели (в работе, выполнен, просрочен, в архиве).

3. Изменение целей.
   - Изменение описания цели.
   - Изменение статуса.
   - Дать возможность менять приоритет и категорию у цели.

4. Удаление цели.
   - При удалении цель меняет статус на «в архиве».
 
5. Поиск по названию цели.
6. Фильтрация по статусу, категории, приоритету, году.
7. Выгрузка целей в CSV/JSON.
8. Заметки к целям.
9. Все перечисленный функции должны быть реализованы в мобильном приложении.
10. Настроить локальную разработку с помощью Docker Compose и настроить автоматический деплой всего приложения на сервер по пушу в GitHub.
_________________________________________________________________________________________________________________________

### стек
*     Python 3.10, Django 4.1.7, DRF, Postgres.
_________________________________________________________________________________________________________________________

Как запустить:
   - python3 -m venv venv
   - source venv/bin/activate
   - pip install poetry
   - poetry install
   - pytest
   - запустить проект - ./manage.py runserver
