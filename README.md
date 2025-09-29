# MyBlogApp

A full-featured **Django-based blogging application** that allows users to register, login, create, edit, and view blogs. The app is built with Python, Django, HTML, and Bootstrap, providing a clean and responsive interface.

---

## Features

- User **Registration** and **Login**
- Create, edit, and delete **blogs**
- Blog listing and **detail view**
- Author and publish date displayed for each blog
- **Responsive design** with Bootstrap
- Static files handling (CSS, images, favicon)

---

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, Bootstrap, CSS
- **Database:** SQLite (default Django DB)
- **Version Control:** Git & GitHub

---

## Folder Structure

MyBlogApp/
│
├── App_Blog/ # Blog application logic
├── App_Login/ # User authentication
├── My_Blog/ # User-specific blog content or profile
├── templates/ # HTML templates
├── static/ # CSS, JS, images
├── manage.py # Django management script
└── requirements.txt # Python dependencies

yaml
Copy code

---

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/code-shubhambhatt/MyBlogApp.git
cd MyBlogApp
Create and activate a virtual environment

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Apply migrations

bash
Copy code
python manage.py migrate
Create a superuser (optional, for admin access)

bash
Copy code
python manage.py createsuperuser
Run the development server

bash
Copy code
python manage.py runserver
Open your browser

cpp
Copy code
http://127.0.0.1:8000/
Usage
Register/Login: Create an account or login to access blog creation features.

Create Blog: Authenticated users can add new blog posts.

View Blogs: Browse all blogs and view details.

Edit/Delete Blogs: Users can manage their own posts.

Contributing
Contributions are welcome! Feel free to:

Improve UI/UX

Add new features like comments or likes

Optimize code and performance

License
This project is open-source and free to use.

Screenshots
(Add screenshots of your blog homepage, blog detail page, login/signup forms here for better presentation)

Author
Shubham Bhatt

GitHub

LinkedIn

Email: Shubhambhatt1000@gmail.com
