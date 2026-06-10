# WC Task Manager

A small FastAPI task manager that stores tasks in SQLite and supports basic CRUD operations.

## Features

- Create, list, view, update, and delete tasks
- Filter tasks by status with `?task_status= todo | in_progress | done`
- Automatic SQLite database creation in `database.db`
- Interactive API docs via FastAPI at `/docs`

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Setup

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Start the development server:

   ```bash
   uv run fastapi dev
   ```

3. Open the API in your browser:

   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/tasks` | List all tasks (optionally filter by status) |
| GET | `/tasks/{task_id}` | Get one task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Example Requests

### Create a task

```bash
curl - L -X POST "http://127.0.0.1:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Write README",
    "description": "Document project setup and API usage",
    "status": "in_progress"
  }'
```

### List tasks

```bash
curl -L "http://127.0.0.1:8000/tasks"

```

### Filter tasks by status

```bash
curl -L "http://127.0.0.1:8000/tasks?task_status=done"
```

### Update a task

```bash
curl -L -X PUT "http://127.0.0.1:8000/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "done"
  }'
```
### Delete task
```bash
curl -L -X DELETE "http://127.0.0.1:8000/tasks/3"
```
## Notes

- The app uses SQLite, so data persists in the local `database.db` file.
- The health check endpoint `/` returns `{"status": "ok"}`.
