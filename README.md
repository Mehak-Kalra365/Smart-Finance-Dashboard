# Smart Finance Tracker

Smart Finance Tracker (Full-Stack)
A modern, role-based financial management system built with FastAPI and SQLite. This project allows users to track their income and expenses with real-time analytics and a clean, responsive dashboard.

Key Features
Role-Based Access Control (RBAC): Different access levels for Admin, Analyst, and Viewer.

Complete CRUD: Add, View, Edit, and Delete financial transactions.

Live Analytics: Dynamic Doughnut Chart using Chart.js for income vs. expense visualization.

Secure Authentication: JWT token-based login with password hashing (Bcrypt).

Real-time Summary: Instant calculation of Total Income, Total Expense, and Net Balance.

Tech Stack
Backend: FastAPI (Python)

Database: SQLite with SQLAlchemy ORM

Frontend: HTML5, Tailwind CSS, JavaScript (ES6+)

Visualization: Chart.js

📂 Project Structure
Plaintext
FinanceProject/
├── src/
│ ├── api/ # API Endpoints (auth.py, records.py)
│ ├── core/ # Security, Database config
│ ├── models/ # SQLAlchemy Models
│ └── schemas/ # Pydantic Schemas
├── static/ # Frontend (index.html)
├── main.py # Application Entry Point
└── finance.db # SQLite Database File
⚙️ Setup & Installation
Clone the project:

Bash
git clone <your-repo-link>
cd FinanceProject
Create a Virtual Environment:

Bash
python -m venv venv
source venv/Scripts/activate # For Windows: venv\Scripts\activate
Install Dependencies:

Bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-multipart python-jose[cryptography]
Run the Server:

Bash
uvicorn main:app --reload --port 8001
Access the app at: http://127.0.0.1:8001

Role Permissions (Assumptions)
Admin: Full access to Create, Read, Update, and Delete all records.

Analyst: Can view all records and access the Analytics Dashboard.

Viewer: Read-only access to the summary and personal records.

Author
Mehak Kalra BCA Final Year Student, JMIETI (Kurukshetra University)
