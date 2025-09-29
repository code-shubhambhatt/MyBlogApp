# MyBlogApp

A full-featured **Django-based blogging application** that allows users to register, login, create, edit, and view blogs. Built with Python, Django, HTML, and Bootstrap, it provides a clean and responsive interface.

---

## Features

* User **Registration** and **Login**
* Create, edit, and delete **blogs**
* Blog listing and **detail view**
* Author and publish date displayed for each blog
* **Responsive design** with Bootstrap
* Static files handling (CSS, images, favicon)

---

## Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, Bootstrap, CSS
* **Database:** SQLite (default Django DB)
* **Version Control:** Git & GitHub

---

## Folder Structure

```
MyBlogApp/
│
├── App_Blog/        # Blog application logic
├── App_Login/       # User authentication
├── My_Blog/         # User-specific blog content or profile
├── templates/       # HTML templates
├── static/          # CSS, JS, images
├── manage.py        # Django management script
└── requirements.txt # Python dependencies
```

---

## Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/code-shubhambhatt/MyBlogApp.git
cd MyBlogApp
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create a superuser (optional, for admin access)**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

7. **Open your browser**

```
http://127.0.0.1:8000/
```

---

## Usage

* **Register/Login:** Create an account or login to access blog creation features.
* **Create Blog:** Authenticated users can add new blog posts.
* **View Blogs:** Browse all blogs and view details.
* **Edit/Delete Blogs:** Users can manage their own posts.

---

## Contributing

Contributions are welcome! Feel free to:

* Improve UI/UX
* Add new features like comments or likes
* Optimize code and performance

---

## License

This project is open-source and free to use.

---

## Screenshots

*(Add screenshots of your blog homepage, blog detail page, login/signup forms here for better presentation)*

---

## Author

**Shubham Bhatt**

* [GitHub](https://github.com/code-shubhambhatt)
* [LinkedIn](https://www.linkedin.com/in/codingshubham)
* Email: [Shubhambhatt1000@gmail.com](mailto:Shubhambhatt1000@gmail.com)
