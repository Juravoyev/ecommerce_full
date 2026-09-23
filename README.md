# 🛒 E-Commerce Full-Stack System (Django)

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Database](https://img.shields.io/badge/PostgreSQL-SQLite-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A robust, production-ready full-stack E-Commerce web application built with **Django**, featuring custom user authentication, product management, shopping cart, billing/checkout system, and Docker containerization.

---

## 🌟 Key Features

- **🔐 Custom Authentication (`custom_auth`)**: User registration, login, profile management, and role-based permissions.
- **📦 Product Catalog & Categories (`products`)**: Dynamic product listing, category filtering, search, and image storage.
- **💳 Billing & Checkout (`billing`)**: Order creation, payment processing integration, and order history tracking.
- **🐳 Docker Ready**: `Dockerfile` & `docker-compose.yml` included for multi-container orchestration.
- **🎨 Templating & Media Support**: Dynamic HTML5/CSS3 templates with Django template engine and media upload handlers.

---

## 🏗 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend Framework** | Django 4.2+ |
| **Programming Language** | Python 3.11+ |
| **Database** | PostgreSQL / SQLite |
| **Containerization** | Docker & Docker Compose |
| **Frontend Templates** | Django HTML Templates, CSS3, JavaScript |

---

## 🚀 Quick Start & Installation

### Option 1: Running locally with Virtual Environment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Juravoyev/ecommerce_full.git
   cd ecommerce_full
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration:**
   Copy `.env.example` to `.env` and fill in database credentials and secret key:
   ```bash
   cp .env.example .env
   ```

5. **Apply Database Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create Superuser (Admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser.

---

### Option 2: Running with Docker 🐳

```bash
docker-compose up --build -d
```
The application will be accessible at `http://localhost:8000`.

---

## 👨‍💻 Author

**Shams Juravoyev**  
- Telegram: [@Juravoyev](https://t.me/Juravoyev)  
- LinkedIn: [Shams Juravoyev](https://www.linkedin.com/in/shams-juravoyev-3017473ab/)  
- GitHub: [@Juravoyev](https://github.com/Juravoyev)  
