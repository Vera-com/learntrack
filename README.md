# LearnTrack

## Overview

LearnTrack is a simple web app I built using Django to help track study sessions in an organised way.

As someone learning new skills, I realised it’s easy to forget what you’ve studied and how much time you’ve spent. This project solves that by allowing users to record their study sessions with details like course, title, duration, date, and a short description.

The goal is to keep everything in one place and make learning progress more visible and structured.

---

## Project Goals

The main goal of this project is to create a simple and user-friendly study tracker that allows users to:

- Add new study sessions
- View all recorded sessions
- Stay consistent with their learning
- Build a habit of tracking progress

---

## User Experience

The application was designed to be simple and easy to use. Users can quickly add and manage their study sessions without confusion.

Study sessions are displayed in a card layout to improve readability and organisation.

A confirmation message is shown before deleting a session to prevent accidental data loss.

The layout is responsive, allowing users to access the application comfortably on mobile devices, tablets, and desktops.

---

## Target Users

This app is designed for:
- Students
- Self-learners
- Anyone taking online courses
- People trying to stay consistent with learning

---

## User Stories

- As a user, I want to add a study session so I can track what I’ve learned.
- As a user, I want to see all my study sessions so I can review my progress.
- As a user, I want to edit a session in case I made a mistake.
- As a user, I want to delete a session I no longer need.

---

## Features

At the current stage, the application includes:

- Users can create, view, edit, and delete study sessions
- Study sessions are displayed in a responsive card layout using Bootstrap
- Each session includes title, course, duration, date, and description
- A dropdown is used for selecting course categories
- A date picker is included to simplify date selection
- A confirmation prompt appears before deleting a session to prevent accidental loss of data
- The layout is responsive across mobile, tablet, and desktop devices
- Custom styling has been applied for improved presentation
- A custom favicon has been added for better branding

---

## Data Model

The main model used is:

**StudySession**, which includes:
- Course (dropdown choice)
- Title
- Description
- Duration (in minutes)
- Date

---

## Technologies Used

- HTML
- CSS
- Bootstrap
- Python
- Django
- SQLite
- Git & GitHub

---

## Design

The design was kept simple and clean to ensure ease of use. Study sessions are displayed as cards so each entry is clearly separated and easy to read. Bootstrap was used to create a responsive and consistent layout across different screen sizes.

—

## Challenges and Solutions

During the development of this project, I encountered a few challenges which helped me understand Django and web development better.

### 1. Form Submission and Data Saving
At first, I had issues getting the form to save data correctly to the database. The page would reload, but no new data appeared.

**Solution:**  
I ensured that the form was properly connected to the view using `request.POST`, and added form validation using `form.is_valid()` before saving.

---

### 2. Redirect After Form Submission
After submitting the form, the page was not redirecting back to the main list view.

**Solution:**  
I used Django’s `redirect()` function to send users back to the study list page after successfully saving a session.

---

### 3. Template Structure Confusion
Understanding how `base.html` and other templates connect using `{% extends %}` was initially confusing.

**Solution:**  
I structured all templates inside `templates/tracker/` and used template inheritance correctly so that all pages share a consistent layout.

---

### 4. Static Files Not Loading Properly
At one point, my CSS was not applying to the page.

**Solution:**  
I fixed this by correctly setting up the static folder (`static/tracker/`) and using `{% load static %}` along with the proper static path in the template.

---

### 5. Date Input Format Issue
The date field required manual input in a specific format, which was not user-friendly.

**Solution:**  
I improved the user experience by adding a date picker widget in `forms.py` using:
```python
widgets = {
    'date': forms.DateInput(attrs={'type': 'date'})
}
```
This allowed users to select dates easily from a calendar instead of typing manually.

---

### 6. Understanding Django Project Structure
At the beginning, it was difficult to understand how models, views, templates, and URLs all connect together.

**Solution:**
By building the project step by step, I was able to understand how each part interacts, especially how data flows from the database to the frontend.

---

### 7. Delete Functionality and User Experience

Initially, the delete functionality redirected users to a separate page where they had to choose between "Yes, delete" or "Cancel". While this worked, it interrupted the user flow and felt slow.

**Solution:**
This was improved by replacing it with a JavaScript confirmation prompt that appears instantly when the delete button is clicked. This made the process faster and more user-friendly while still preventing accidental deletion.

---

### 8. Responsive Layout Issues

The initial layout did not display well on smaller screens.

**Solution:**
Bootstrap grid classes were used to ensure the layout adapts properly across mobile, tablet, and desktop devices.

---

### 9. Favicon Clarity Issue

The favicon initially appeared blurry due to incorrect sizing and resolution.

**Solution:**
This was improved by replacing it with a clearer, properly scaled icon to ensure better visibility in the browser tab.



## Project Status

This project is currently functional and includes full CRUD (Create, Read, Update, Delete) functionality.

Users can add, view, edit, and delete study sessions. The application also includes responsive design and basic user experience improvements such as confirmation prompts for deletion.

Further improvements may include enhanced validation, user authentication, and additional features.


---

## Deployment

Deployment will be handled later in the project.

---

## Testing

Testing will be documented as development progresses.

---

## Credits

- Django documentation
- Bootstrap documentation
- Code Institute course materials








