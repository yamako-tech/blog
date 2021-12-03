# Django Blog /w Book Search & Video Embed

<font color="Red">secret-key is set in the environment variable</font>
## Objectives:
1. Get used to the basic operations of django
2. Implement book search by linking external API
3. Embed YouTube video in specified size
4. Only admin can create posts by logging in (no registration function)

### ⭐Login and Create a blog
![giphy](https://user-images.githubusercontent.com/58015893/144588548-7d43dee9-df6c-4c07-8446-177fc3a0f14a.gif)

### ⭐Book search and order API (Rakuten)
![django-book](https://user-images.githubusercontent.com/58015893/144588795-05623436-4085-4879-be7a-ca6cae99d551.gif)

### ⭐Category and Search Blog
![django-category-search](https://user-images.githubusercontent.com/58015893/144588853-d26c694a-3db9-40f4-958d-c78561155a5e.gif)
## Basic Setup
[Click here for the turtorial with codes and images](https://www.askdjapy.com/django-blog-site/)
1. Create Blog folder Go to the folder
```python:shell
mkdir blog
cd blog
```

2. Create and activate virtual environment
```python:shell
python3 -m venv/myvenv
source myvenv/bin/activae
```

3. Create, copy and paste requirements.text, and install dependencies: 
```python:shell
pip install -r requirements.txt
```

4. Start project and edit settings
```python:shell
django-admin startproject blog .
```

5. Edit settings

6. Run server
```python:shell
python3 manage.py runserver
```

7. Set Database: 
```pythn:shell
python3 manage.py makemigrations
python3 manage.py migrate
```
8. Start app
```python:shell
python3 startapp app
```
9. Add 'app' to INSTALLED_APPS in settings

10. Make directories for static and template files, and urls.py, forms.py, and context_processors.py:
```python:folder-tree
📦app
 ┣ 📂migrations
 ┃ ┗ 📜__init__.py
 ┣ 📂static
 ┃ ┣ 📂css
 ┃ ┃ ┗ 📜style.css
 ┃ ┣ 📂img
 ┃ ┃ ┣ 📜logo.svg
 ┃ ┃ ┗ 📜logo8.png
 ┃ ┗ 📜favicon.ico
 ┣ 📂templates
 ┃ ┗ 📂app
 ┃ ┃ ┣ 📜base.html
 ┃ ┃ ┣ 📜index.html
 ┃ ┃ ┣ 📜post_delete.html
 ┃ ┃ ┣ 📜post_detail.html
 ┃ ┃ ┣ 📜post_form.html
 ┃ ┃ ┗ 📜video.html
 ┣ 📜admin.py
 ┣ 📜apps.py
 ┣ 📜context_processors.py
 ┣ 📜forms.py
 ┣ 📜models.py
 ┣ 📜tests.py
 ┣ 📜urls.py
 ┣ 📜views.py
 ┗ 📜__init__.py
```
11. Once you've written the code you need for your app, it's time to create a book app and follow the same steps.

12. When adding or changing 'models.py', be sure to make migration and migrate.

13. When deploying, save information such as private keys and passwords in environment variables and save them in your local environment.


