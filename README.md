# Mail Handler

Mail Handler is a scalable bulk email sending service built with a REST API. It allows admins to send emails to multiple recipients in a single request, secured using JWT authentication. The project is designed for clean integration with web or mobile applications.

---

## 🚀 Features

* Bulk email sending in one API call
* REST API architecture
* JWT-based authentication
* Admin-only email sending
* Supports multiple recipients
* Easy to integrate with frontend or third-party systems

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Authentication:** JWT (JSON Web Tokens)
* **Email Service:** SMTP (Gmail / Outlook / Custom provider)
* **Database:** SQLite / PostgreSQL

---

## 🔐 Authentication

* JWT authentication is used for API security
* Only authenticated users can access the API
* Any authenticated user can send bulk emails

---

## 📡 API Endpoint

### Send Bulk Email

**Endpoint**

```
POST /mail/
```

**Headers**

```
Authorization: Bearer <your_jwt_token>
Content-Type: application/json
```

**Request Body**

```json
{
  "subject": "Important Update",
  "message": "This is a bulk email message.",
  "recipients": [
    "user1@example.com",
    "user2@example.com",
    "user3@example.com"
  ]
}
```

**Response**

```json
{
  "status": "success",
  "sent": 3,
  "failed": 0
}
```

---

## ⚙️ Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/your-username/mail-handler.git
cd mail-handler
```

2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure email settings in `settings.py` or `.env`

5. Apply migrations

```bash
python manage.py migrate
```

6. Run the server

```bash
python manage.py runserver
```

---

## 🔧 Environment Variables

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
EMAIL_USE_TLS=True
```

---

## 🧪 Testing

* Use Postman or any API client
* Authenticate and obtain a JWT token
* Send a POST request to the bulk mail endpoint

---

## 📈 Future Enhancements

* Email templates
* Background tasks using Celery & Redis
* Email delivery logs and tracking
* File attachments

---

## 📄 License

This project is licensed under the MIT License.

---

## ✨ Summary

Mail Handler provides a secure and efficient solution for sending bulk emails using a REST API with JWT authentication, making it suitable for admin-driven communication systems.
