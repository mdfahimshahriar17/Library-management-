# Django Library & Blog Management System

A simple Django project to manage **Books, Members, Borrowing/Returning** and **Blog Posts** with secure user authentication.

---

## Project Overview

This system is designed for small libraries or personal use.  
It combines a basic **library management system** with a simple **blog module** so that admins can share updates, news, or articles.

---

## This Project Includes

- User Authentication (login, logout, access control)
- Blog Management (create, edit, delete posts)
- Book Management (add, update, delete books)
- Member Management (add, update, delete members)
- Borrow & Return System
- Search & Filtering (books, members, borrowed records)
- Image upload support (books, members, blog posts)

---

## Core Features

### Authentication & Access Control

- Login with username & password
- Logout functionality
- Only logged-in users can:
  - Add / Edit / Delete books
  - Add / Edit / Delete members
  - Create / Edit / Delete blog posts

---

### Blog Management (Post Model)

- View all blog posts (latest first)
- Create new blog with:
  - Title
  - Content
  - Image
- Edit or delete existing posts
- Only authenticated users can manage posts

---

### Library Management

#### Book Management (Book Model)

- View all books in a list
- Search by **title**, **author**, or **ISBN**
- Add new books with:
  - Title
  - Author
  - ISBN
  - Quantity
  - Cover image
- Edit book details
- Delete books from the system

#### Member Management (Member Model)

- View all registered members
- Search members by **name**, **email**, or **phone**
- Add new member with:
  - Name
  - Email
  - Phone number
  - Photo
- Edit member information
- Delete members

#### Borrow & Return (BorrowRecord Model)

- Borrow a book if it is in stock → quantity decreases by 1
- View list of all borrowed books (with search support)
- Return a book:
  - Mark as returned
  - Set return date
  - Increase book quantity by 1

---

## Search & Filtering

- Search books by:
  - Title
  - Author
  - ISBN
- Search members by:
  - Name
  - Email
  - Phone
- Search borrowed records
- Implemented using Django’s **Q lookups** for multi-field search

---

## Image Support

The system supports image uploads for:

- Book cover images
- Member profile photos
- Blog post images

All images are stored in the **MEDIA** directory using Django’s `ImageField`.

---

## Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (default Django database)
- **Authentication:** Django’s built-in auth system
- **Media Handling:** Django MEDIA + `ImageField`

---

## What I Practiced / Learned

- Django Models, Views, Templates (MVT pattern)
- CRUD operations (Create, Read, Update, Delete)
- Django Authentication & access control
- Django ORM querying & `Q` lookup based search
- Working with `ImageField` and MEDIA files
- Structuring a small real-world Django project

---

## Example Project Structure (simplified)

```text
project_root/
│
├── library_app/
│   ├── models.py       # Book, Member, BorrowRecord
│   ├── views.py        # Library-related views
│   ├── urls.py
│   └── templates/
│
├── blog/
│   ├── models.py       # Post model
│   ├── views.py        # Blog views
│   ├── urls.py
│   └── templates/
│
├── media/              # Uploaded images (books, members, posts)
├── templates/          # Base templates
├── project_root/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
└── README.md
```

## Author

**MD Fahim Shahriar**
Python Developer ---If you found this project helpful, feel free to star the repository!
