# CS50 Web Programming Capstone Project

## Project Name - DigiDocs

### Project Description - 
 The photo and file upload Django application is designed to allow users to upload and share photos and files. It provides a user-friendly interface for uploading, storing, and managing photos and files within the application.

### Technologies - 
    1) Django
    2) Bootstrap (via cdn)
    3) Python
    4) HTML
    5) CSS
    6) JS

### Distinctiveness and Complexity - 
Our photo and file upload Django application stands out with its unique user experience and advanced sharing capabilities. We have designed a user-friendly interface that allows users to easily upload, manage, and share their photos and files.

One of the distinctive features of our application is the customizable user experience. We have implemented features like drag-and-drop file upload, image previews, and intuitive navigation to ensure a seamless and enjoyable user journey.

In terms of sharing and permissions, the application goes beyond the basics. Users have the ability to set granular permissions, choose between public and private sharing settings, and even share entire folders or albums. This level of control sets our application apart from others in the market.

The complexity of our project lies in various areas. We have implemented a secure user authentication system and role-based access control. Our file storage and management system efficiently handles file uploads, storage optimization, versioning, and retrieval.

Security is another crucial aspect of our application. We have taken measures to handle user-uploaded files securely and protect against common vulnerabilities such as cross-site scripting (XSS) and cross-site request forgery (CSRF).

Overall, our photo and file upload Django application offers a distinctive user experience with advanced sharing capabilities. We have tackled complexities in user authentication, file storage, scalability, performance, testing, error handling, and security. Our goal is to provide a seamless and secure solution for users to upload, manage, and share their photos and files.

### Specification - 
Introduction: Our File and Photo Upload Django Application is a user-friendly solution that enables users to upload, manage, and share files and photos. This specification outlines the key functionalities of our application.

1) User Authentication and Authorization:
  Users can create accounts and securely log in to the application.
  Passwords are hashed and stored securely.
  Role-based access control is implemented to control user permissions and restrict access to certain features or files.

2) File and Photo Upload:
  Users can easily upload files and photos from their local devices.
  The application supports various file formats, including images (JPEG, PNG) and commonly used file types (PDF, DOCX, etc.).
  File and photo uploads are validated to ensure data integrity and security.

3) File and Photo Management:
  Users can view and manage their uploaded files and photos.
  Uploaded files and photos are organized into categories for easy navigation and retrieval.
  Users can add, edit, and delete categories to customize their file organization.
  The application provides search and filtering capabilities to help users find specific files and photos based on metadata or category.

4) File and Photo Download:
 Users can download their uploaded files and photos to their local devices.
 The application ensures secure and reliable file downloads, protecting the integrity of the files.
 Users can choose to download individual files or a collection of files within a specific category.

5) Navigation:
 The application provides seamless navigation between the photo store app and the document store app.
 Users can easily switch between the two sections to manage and access their files and photos.
 Clear and intuitive navigation menus and links are implemented to ensure a smooth user experience.

6) Security:
 User-uploaded files and photos are handled securely, with measures in place to prevent common vulnerabilities such as cross-site scripting (XSS) and cross-site request forgery (CSRF).
 User authentication and authorization mechanisms are implemented following best practices to ensure the security of user accounts and data.

By adhering to this specification, we aim to deliver a reliable and user-friendly file and photo upload Django application that allows users to manage their files and photos efficiently, share them securely, and navigate seamlessly between the photo and document store apps.

### Youtube video link - 

https://youtu.be/zmRSRYlBgfs


### Setup - 
 a) Dowload the Zip and Extract

 b) In the IDE type - 

    1) python manage.py makemigrations

    2) python manage.py migrate

    3) python manage.py createsuperuser  (multiple times)
    
    4) python manage.py runserver

