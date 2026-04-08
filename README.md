<h1 align="center">🎓 Student Management System</h1>
<p align="center">
  A robust, role-based academic portal built with <b>Django</b> and ❤️.
</p>

<p align="center">
  <a href="https://github.com/ursmaheshj/Student_Management/issues/new/choose">🐞 Report Bug</a>
  ·
  <a href="https://github.com/ursmaheshj/Student_Management/issues/new/choose">🚀 Request Feature</a>
  ·
  <a href="https://github.com/ursmaheshj/Student_Management/issues/new/choose">💡 Propose Idea</a>
</p>

<hr>

## 🌟 Overview
This platform streamlines communication between administrators, teachers, and students. It features a professional dashboard for managing academic results, notes, and real-time notifications.

## 🧐 Key Features
- **Multi-Role Dashboards:** Customized interfaces for Admin, Teacher, and Student.
- **Secure Auth:** Email-based authentication with role-based access control.
- **Academic Management:** Seamless result publishing and notification broadcasting.
- **Responsive Design:** Fully adaptive UI

## 🛠️ Installation and Usage

Before you begin, ensure you have **Python** and **Django** installed on your system.

1. *Clone the Repository:* `git clone https://github.com/ursmaheshj/Student_Management.git`
2. *Navigate to the Root Directory:* Ensure you are inside the `Student_Management` folder before running the following commands.
3. *Set Up Virtual Environment (Optional but Recommended):* Create and activate a virtual environment using `venv` or `virtualenv`.
4. *Install Dependencies:* `pip install -r requirements.txt`
5. *Setup and Configuration:* Run following commands in order to prepare the application:
6. *Collect Static Files:* `python manage.py collectstatic`
7. *Generate Migrations:* `python manage.py makemigrations`
8. *Apply Migrations:* `python manage.py migrate`
9. *Create Admin Account:* Run `python manage.py createsuperuser` and follow the prompts to set your email and password.
10. *Start the server:* `python manage.py runserver`



## 👥 User Roles & Access

| Role | Default Password | Permissions |
| --- | --- | --- |
| **Admin** | *(User Created)* | System-wide management & account creation. |
| **Teacher** | `Teacher@100` | Manage students, post results, and send alerts. |
| **Student** | `Student@100` | View personal results and teacher notifications. |

> **Security Note:** Users are required to change their default passwords immediately upon their first login.


## 💻 Built with
- <a href="https://www.python.org/" target="blank">Python</a>
- <a href="https://www.djangoproject.com/" target="blank">Django</a>
- <a href="https://adminlte.io/" target="blank">Adminlte</a>
- <a href="https://getbootstrap.com/" target="blank">Bootstrap</a>

---

## 🍰 Contributing

Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow); Create a branch, add commits, and [open a pull request](https://github.com/ursmaheshj/Student_Management/compare).

## 🙏 Support
Dont hesitate to [fork](https://github.com/login?return_to=%2Fursmaheshj%2FStudent_Management) this repository and Give a ⭐[star](https://github.com/login?return_to=%2Fursmaheshj%2FStudent_Management) if you like it..
