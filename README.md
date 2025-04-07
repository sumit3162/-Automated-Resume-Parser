# 🔐 Secure Authentication System

A secure user authentication system built using **Flask**, **JWT**, and **PostgreSQL**, designed to run in a **Jupyter Notebook** environment. This project implements user registration, login, and protected routes using encrypted credentials and token-based authentication.

---

## 📌 Features

- ✅ **User Registration** with password hashing (bcrypt)
- 🔐 **JWT Authentication** for secure and stateless session management
- 🧠 **Token Verification** for protected routes
- ⚠️ Handles token expiration and invalid access attempts
- 💾 **PostgreSQL Integration** using SQLAlchemy ORM

---

## 🧰 Technologies Used

| Tool            | Purpose                         |
|-----------------|---------------------------------|
| 🐍 Python       | Programming Language            |
| 🚀 Flask        | Web Framework                   |
| 🔐 bcrypt       | Password Hashing                |
| 🪪 PyJWT        | Token-based Authentication      |
| 🐘 PostgreSQL   | Relational Database             |
| 📒 Jupyter      | Interactive Dev Environment     |

---

## 🏗️ Folder Structure

secure-auth-system/ ├── app.py ├── models.py ├── routes/ │ └── auth_routes.py ├── utils/ │ ├── hashing.py │ └── token.py ├── config.py └── requirements.txt



---

## 🚀 Getting Started

1. **Install Dependencies**  
   Run this inside your notebook:
   ```python
   !pip install Flask flask_sqlalchemy pyjwt bcrypt psycopg2-binary
Configure Database
Update your PostgreSQL URI in:


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
Run the App
Use the Flask threaded method to run inside Jupyter:

python
from threading import Thread
def run_app():
    app.run(port=5000)
thread = Thread(target=run_app)
thread.start()
🔁 API Endpoints
Method	Endpoint	Description
POST	/register	Register a new user
POST	/login	Authenticate user & token
GET	/protected	Access with JWT token
🛡️ Security Measures
Passwords hashed with bcrypt 🔐

JWT signed with a secure secret key 🧪

Tokens include expiration time ⏳

Protected endpoints reject unauthorized access 🚫

💡 Author
👨‍💻 Developed by Sumit Patil

📬 Connect: Instagram

📄 License
This project is open-source and free to use under the MIT License.



---

Let me know if you want this README to include screenshots, a usage GIF, or how to deploy 
