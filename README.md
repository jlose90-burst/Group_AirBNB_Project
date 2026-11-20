# 🏠 LairBnB

**A villain-themed twist on accommodation booking** — list and hire lairs for the night, from Emperor Palpatine hosting on the Death Star to Dr. Evil’s volcano lair.

===============================

## 🚀 About the Project

LairBnB is a full-stack web application built in **Python** with **Flask**, **PostgreSQL**, and **Jinja**. Developed over a one-week sprint using Trello and Kanban methodology with pair programming, the team delivered:

- 🔐 User authentication and multi-listing management with date availability
- ✅ Booking approval workflow that prevents double-booking once confirmed
- 📧 Local email and SMS notifications (via smtplib) for booking updates
- 💬 In-app chat system for hosts and confirmed guests to coordinate stays

Perfect for fans of over-the-top evil lairs and seamless booking experiences.

### Demo Video

The headed Playwright tests (run via `pytest tests/test_presentation.py --headed`) show the full user flow in a real browser: a new user signs up, lists a location (lair), and books a stay.



https://github.com/user-attachments/assets/80f46cf2-b905-4e78-bf89-5cdee51f77bf



===============================

## MakersBnB Python Project Seed

This repo contains the seed codebase for the MakersBnB project in Python (using Flask and Pytest).

## Setup

```shell
# Set up the virtual environment
; python -m venv makersbnb-venv

# Activate the virtual environment
; source makersbnb-venv/bin/activate 

# Install dependencies
(makersbnb-venv); pip install -r requirements.txt

# Install the virtual browser we will use for testing
(makersbnb-venv); playwright install
# If you have problems with the above, contact your coach

# Run the tests (with extra logging)
(makersbnb-venv); pytest -sv

# Run the app
(makersbnb-venv); python app.py

# Now visit http://localhost:5001/ in your browser
```
