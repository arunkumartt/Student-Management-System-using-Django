# 🎓 Student Management System using Django

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
</p>

<p align="center">
  A full-stack web application for managing student registrations in an institution, built with Python Django using the MVT architecture.
</p>

---

## 📸 Screenshots

| Student Registration | Student Details | Course Details |
|---|---|---|
| ![Student Registration](Student%20Registration.png) | ![Student Details](Student%20Details.png) | ![Course Details](Course%20Details.png) |

---

## ✨ Features

- **Student Registration** — add new students with course enrollment (one course per student)
- **Student Details Page** — view detailed information about each registered student
- **Course Details Page** — view all courses and enrolled students
- **Django Admin Interface** — manage all data through a built-in admin panel
- **SQLite Database** — lightweight database, zero configuration required
- **MVT Architecture** — clean separation of Models, Views, and Templates

---

## 🏗️ Project Structure

```
StudentRegistration/
└── StudentManagement/
    ├── models.py        # Student & Course data models
    ├── views.py         # Business logic
    ├── urls.py          # URL routing
    ├── admin.py         # Admin interface configuration
    └── templates/       # HTML templates
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/arunkumartt/Student-Management-System-using-Django.git
cd Student-Management-System-using-Django
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

**3. Install Django**
```bash
pip install django
```

**4. Run database migrations**
```bash
cd StudentRegistration
python manage.py migrate
```

**5. Create an admin superuser**
```bash
python manage.py createsuperuser
```

**6. Start the development server**
```bash
python manage.py runserver
```

**7. Open in your browser**
- App: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Admin: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🗄️ Database Schema

| Model | Fields |
|---|---|
| **Student** | name, email, phone, course (FK) |
| **Course** | course_name, description, duration |

Each student can enroll in only one course. Each course can have multiple students.

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Django |
| Database | SQLite |
| Frontend | HTML5, CSS3 |
| Admin | Django Admin |
| Architecture | MVT (Model-View-Template) |

---

## 📌 Topics

`python` `django` `sqlite` `student-management` `web-development` `mvt-architecture` `crud` `html` `css`

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Arunkumar TT**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arunkumartt)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/arunkumartt)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
