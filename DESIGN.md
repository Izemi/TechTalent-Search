# Design Document for CS50 TechTalent Connect

## Overview
CS50 TechTalent Connect is designed with a focus on functionality and ease of use for Yale students enrolled in CS50. The design incorporates Yale's traditional blue color and aims to provide a straightforward and effective user experience.

## Flask Framework and SQLite Database Integration:
- **Flask Usage**: Flask is used to handle server-side logic, including routing and database interactions.
- **SQLite Integration**: SQLite, a lightweight database, is integrated to manage user data and job listings. This combination allows for efficient data retrieval and manipulation.

## User Authentication and Session Management:
- **User Registration, Login, and Logout**: These functionalities are implemented.
- **Session Management**: Flask's session management capabilities are utilized to track user login status and provide personalized experiences.

## Front-End Design using HTML, CSS, and Bootstrap:
- **UI Development**: The user interface is developed using HTML and styled with CSS, adhering to Yale's color scheme, particularly Yale Blue.
- **Responsive Design**: Bootstrap, a front-end framework, is incorporated to ensure the application is responsive and accessible on various devices.

## Job Search Functionality:
- **Search by Keywords**: Users can search for jobs based on different keywords like 'Software', 'Web', 'Data', 'Engineer', etc., through a form submission.
- **Backend Processing**: The backend processes these queries and fetches relevant job listings from the SQLite database.

## Interactive Elements and User Feedback:
- **Interactive Elements**: Buttons and dropdown menus are styled for user engagement.
- **Visual Feedback**: Visual feedback, such as hover effects on buttons, enhances the user experience.

## Code Structure and File Organization:
- **Project Organization**: The project is organized into different files for HTML templates, CSS styles, and Flask application logic.
- **Flask Application**: The Flask application (`app.py`) serves as the entry point, handling routes and integrating various components.

## Design Elements

### Color Scheme
- **Main Color - Yale Blue**: This color is used for the navigation bar and buttons, aligning with Yale's identity.
- **Background and Text Colors**: The background is a light gray, and the text is a standard dark gray, ensuring readability.

### Typography
- **Font Choice**: Arial, a sans-serif font, is used throughout the application for its wide availability and legibility.

### Layout and Structure
- **Responsive Design**: The layout adjusts for different screen sizes, ensuring usability on both desktop and mobile devices.
- **Form Styling**: Forms, used for job searches, are styled to be clear and easy to use with labeled fields and simple, rounded borders.

### Interactive Elements
- **Buttons**: The buttons are in Yale Blue, with a color change on hover to provide visual feedback.
- **Dropdown Menus**: Dropdown menus are styled for clarity, with a focus on functionality.

### Navigation Bar
- **Functionality**: The navigation bar is simple, providing easy access to home, account settings, and login or registration options.

### Imagery
- **Use of Images**: Images related to programming are used to add visual interest and context.

## Conclusion
The design of CS50 TechTalent Connect is practical, aligning with the needs of Yale students in CS50. It uses Yale's colors to create a familiar environment while ensuring the application is easy to navigate and use. The focus is on functionality and providing a user-friendly experience for job searching.
