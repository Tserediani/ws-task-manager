For this homework, please build a simple backend web application using Flask, FastAPI, or Django.
The project should be completed in around 1 hour.
Requirements:
• Create tasks
• List all tasks
• View one task by ID
• Update task status
• Delete a task

Each task should have:
• id
• title
• description
• status: todo / in_progress / done
• created_at

API endpoints:
GET /tasks
GET /tasks/{id}
POST /tasks
PUT /tasks/{id}
DELETE /tasks/{id}

Use either an in-memory list, SQLite, or PostgreSQL.

Deliverables:
• Source code
• Short README with setup instructions
• 3–5 example API requests/responses

Bonus:
• Input validation
• Basic error handling
• Filtering tasks by status
The main goal is to practice routing, HTTP methods, request/response handling, simple data modeling, and clean API structure.