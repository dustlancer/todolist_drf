# VeraReality test task

## Запуск

```bash
python -m venv venv
```
```bash
source env/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py runserver
```



## Описание эндпоинтов
### Получение списка задач

**URL:** `/api/tasks/`  
**Метод:** `GET`  
**Пример запроса:**
```bash
GET /api/tasks/
```
### Получение информации о конкретной задаче
**URL:** `/api/tasks/{id}/`  
**Метод:** `GET`  

### Создание новой задачи
**URL:** `/api/tasks/`  
**Метод:** `POST`  
**Тело запроса**
```json
{
    "name": "New task",
    "description": "Description for task",
}
```

### Редактирование задачи
**URL:** `/api/tasks/{id}/`  
**Метод:** `PATCH` 
Можно обновлять, как все поля сразу, так и выборочно. Например, чтобы отметить, что задача выполнена, нужно передать в тело запроса: 
```json
{
    "done": true
}
```

### Удаление задачи
**URL:** `/api/tasks/{id}/`  
**Метод:** `DELETE` 

### Добавление комментария к задаче
**URL:** `/api/comments/`  
**Метод:** `POST` 
**Тело запроса**
```json
{
    "task": 1,
    "text": "Comment for task 1"
}
```

### Фильтрация и сортировка
**URL:** `api/tasks/?search={keyword}`
**Метод:** `GET` 
– Получить задачи, в названии или описании которых содержится keyword


**URL:** `/api/tasks/?ordering=created_at`
**Метод:** `GET` 
– Получить задачи, отсортировав их по дате создания 

**URL:** `/api/tasks/?done=true`
**Метод:** `GET`
– Получить только выполненные задачи


