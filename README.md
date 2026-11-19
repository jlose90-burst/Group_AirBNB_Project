#
LairBnB is a full-stack web application built in Python using Flask, PostgreSQL, and Jinja, designed as a villain-themed twist on an accommodation booking platform where users can list and hire lairs for the night—such as Emperor Palpatine hosting guests on the Death Star. Developed over a one-week sprint using a Trello board and Kanban methodology, the team worked through pair programming to pick up feature tickets and deliver core functionality including user authentication, multi-listing management with date availability, and a booking approval workflow that prevents double-booking once a request is confirmed. Beyond the core specification, we integrated local email and SMS notifications via smtplib for booking updates, alongside an in-app chat system allowing hosts and confirmed guests—like Palpatine and Dr. Evil—to coordinate stay details directly.
















MakersBnB Python Project Seed

This repo contains the seed codebase for the MakersBnB project in Python (using 
Flask and Pytest).



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

# Create a test and development database
(makersbnb-venv); createdb YOUR_PROJECT_NAME
(makersbnb-venv); createdb YOUR_PROJECT_NAME_TEST

# Open lib/database_connection.py and change the database names
(makersbnb-venv); open lib/database_connection.py

# Run the tests (with extra logging)
(makersbnb-venv); pytest -sv

# Run the app
(makersbnb-venv); python app.py

# Now visit http://localhost:5001/index in your browser
```
