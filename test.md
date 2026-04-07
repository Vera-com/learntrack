# LearnTrack – Testing

## Overview

Testing was carried out throughout the development of this project to ensure that all functionality works as expected.  

The application was tested manually on both local and deployed environments.

---

## CRUD Functionality Testing

### 1. Create (Add Study Session)

- User can fill out the form and submit a new study session  
- Required fields prevent empty submissions  
- Date picker allows easy date selection  
- After submission, the session appears on the homepage  

**Result:** ✅ Pass  

---

### 2. Read (View Study Sessions)

- All study sessions are displayed on the homepage  
- Sessions are shown in a clear card layout  
- Each card displays:
  - Title  
  - Course  
  - Duration  
  - Date  
  - Description  

**Result:** ✅ Pass  

---

### 3. Update (Edit Study Session)

- User can click the "Edit" button  
- Existing data is pre-filled in the form  
- Changes are saved correctly  
- User is redirected back to the homepage  
- Success message is displayed  

**Result:** ✅ Pass  

---

### 4. Delete (Remove Study Session)

- User clicks "Delete" button  
- JavaScript confirmation prompt appears  
- Django confirmation page is displayed  
- User can confirm or cancel deletion  
- After deletion, session is removed  
- Success message is displayed  

**Result:** ✅ Pass  

---

## Form Validation Testing

- Empty fields trigger validation errors  
- Required fields must be completed before submission  
- Error messages are displayed clearly  

**Result:** ✅ Pass  

---

## Database Testing

- Data is successfully stored in PostgreSQL database  
- Relationships between Course and StudySession work correctly  
- Each study session is linked to a course  

**Result:** ✅ Pass  

---

## Responsiveness Testing

The application was tested on different screen sizes:

- Mobile devices  
- Tablets  
- Desktop  

Bootstrap grid system ensures layout adapts correctly across all devices.

**Result:** ✅ Pass  

---

## Deployment Testing

- Application deployed successfully on Render  
- All CRUD operations work on the live site  
- Database (PostgreSQL) persists data correctly  
- Admin panel is accessible and functional  

**Result:** ✅ Pass  

---

## Bugs and Fixes

### 1. Course Dropdown Not Showing Options
**Issue:**  
Course dropdown was empty when adding a study session  

**Cause:**  
No course records existed in the database  

**Fix:**  
Added course entries via Django admin  

---

### 2. Admin Login Not Working
**Issue:**  
Unable to log into Django admin after deployment  

**Cause:**  
Database reset after switching from SQLite to PostgreSQL  

**Fix:**  
Implemented signal to automatically create superuser during deployment  

---

### 3. Data Loss After Deployment
**Issue:**  
Study sessions disappeared after redeploy  

**Cause:**  
SQLite database was not persistent on Render  

**Fix:**  
Switched to PostgreSQL database for persistent storage  

---

### 4. Static Files Not Loading
**Issue:**  
CSS was not applied correctly  

**Fix:**  
Configured static files properly using Django static settings  

---

### 5. Favicon Appearing Blurry
**Issue:**  
Favicon was unclear in browser tab  

**Fix:**  
Replaced with a properly scaled and optimised icon  

---

## Validator Testing

- HTML validated using W3C Validator (via deployed URL)  
- CSS validated using W3C CSS Validator  
- Python code follows PEP8 guidelines  

---

## Conclusion

All core features of the application are functioning as expected.  

The project successfully meets the requirements for:
- CRUD functionality  
- Database integration  
- Deployment  
- User experience and validation  
