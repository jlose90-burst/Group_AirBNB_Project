# 🏠 LairBnB

**A full-stack villain-themed accommodation booking platform** — users can list and book fictional lairs (Death Star overlooks, Isengard towers, secret mountain hideouts) with real-time availability, approvals, notifications, and in-app messaging.

Built in a one-week agile sprint using pair programming, Trello/Kanban, and test-driven development.

===============================

## 🚀 Overview

LairBnB demonstrates end-to-end web application skills: user authentication, relational data modelling, booking conflict prevention, external notifications, and real-time chat — all with a polished dark-themed UI.

**Tech stack:** Python · Flask · PostgreSQL · Jinja2 · Pytest + Playwright · smtplib

### Key Features
- **Authentication & profiles** — secure signup/login with session management
- **Lair listings** — multi-image support, descriptions, pricing, and location details
- **Smart booking workflow** — date availability, host approval/denial, and automatic double-booking prevention
- **Notifications** — email and SMS alerts for booking requests, confirmations, and updates
- **In-app chat** — direct messaging between hosts and confirmed guests
- **Responsive dark UI** — clean, themed interface with logo, cards, and intuitive navigation

### Demo

Headed Playwright end-to-end tests walk through the complete user journey (signup → list a lair → book a stay → manage requests → chat).

https://github.com/user-attachments/assets/80f46cf2-b905-4e78-bf89-5cdee51f77bf

===============================

## 🛠️ Setup & Running Locally

```shell
# Create and activate virtual environment
python -m venv makersbnb-venv
source makersbnb-venv/bin/activate

# Install dependencies
pip install -r requirements.txt
playwright install

# Create databases
createdb YOUR_PROJECT_NAME
createdb YOUR_PROJECT_NAME_TEST

# Update database names in lib/database_connection.py

# Run tests
pytest -sv

# Start the app
python app.py
```

Visit [http://localhost:5001/](http://localhost:5001/) in your browser.

**Headed presentation tests:**
```shell
pytest tests/test_presentation.py --headed
```

===============================
## 🎟️ Example Trello Ticket
<img width="1882" height="1222" alt="image" src="https://github.com/user-attachments/assets/1ae8da8e-b742-4f49-93e1-e04b9f1533ca" />
===============================

## 📋 Project Highlights 

- Full-stack ownership of features from database schema to UI
- Test-driven development with unit, integration, and end-to-end (Playwright) tests
- Real-world concerns handled: booking conflicts, notifications, multi-user flows
- Collaborative agile delivery (pair programming + Kanban)
- Clean architecture separating models, repositories, and routes
