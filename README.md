# 🎓 Django Student CRUD

A simple Student Record Management app built with Django — my **first-ever Django project**, created while learning how Django's MVT (Model-View-Template) architecture and CRUD operations work.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-lightgrey?style=for-the-badge&logo=sqlite)

---

> 🎓 **Project Type: Learning**
>
> This project is built for learning purposes. I created it to understand and practice new concepts, tools, and technologies. The code may not follow production-level standards, and it's a work in progress as I keep exploring and improving.
> 

## 📝 About

This project was where I took my first real steps into Django. It's a basic Student Management app that performs full **CRUD (Create, Read, Update, Delete)** operations on student records — built to understand how Django models, views, URLs, and templates connect together.

---

## ✨ Features

- ➕ Add new student records
- 📋 View/list all students
- ✏️ Update existing student details
- 🗑️ Delete student records
- 🎨 Server-rendered pages using Django templates
- 🗄️ Data persistence with Django's ORM

---

## 🛠️ Tech Stack

### Backend
- Python
- Django
- SQLite (default Django database)

### Frontend
- HTML5
- CSS3
- Django Template Language (Jinja-style templating)

---

## 📂 Project Structure

```
Django_Student_CRUD_operation_project/
│
├── first_project/     # Django project (settings, main urls, wsgi/asgi)
├── app_1/               # Django app — models, views, urls for Student CRUD
├── static/               # CSS/JS/static assets
├── templates/            # HTML templates
├── manage.py             # Django's command-line utility
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```
git clone https://github.com/GouravK1107/Django_Student_CRUD_operation_project.git
```

Move into the project directory

```
cd Django_Student_CRUD_operation_project
```

Create a virtual environment

### Windows
```
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS
```
python3 -m venv venv
source venv/bin/activate
```

Install Django

```
pip install django
```

Apply migrations

```
python manage.py migrate
```

Run the development server

```
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

## 💡 Future Improvements

- Add form validation and error handling
- Add search and pagination for student lists
- Style the UI with Bootstrap/Tailwind
- Add authentication (admin-only access)
- Move to PostgreSQL for production use
- Add a REST API using Django REST Framework

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.
Feel free to fork the project and submit a pull request.

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

---

## 👨‍💻 Author

**Gourav R**

GitHub: [@GouravK1107](https://github.com/GouravK1107)
Portfolio: [gouravk1107.github.io/my-portfolio](https://gouravk1107.github.io/my-portfolio/)

---

Made with ❤️ — my first step into Django
