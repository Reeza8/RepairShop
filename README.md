# RepairShop
This is a RESTful API for managing a repair shop, designed for your second experience in developing an API using Django Rest Framework (DRF). The API allows customers to create their own repair files, upload images, and track the progress of their repair requests online. Additionally, managers have the ability to change the status of repair files online. Authentication is implemented using Simple JWT for securing all views.

Features
Dynamic Filters: The API leverages Django's Q query to provide managers with the capability to perform completely dynamic filters. This feature allows for versatile and efficient searching and sorting of repair files based on various criteria.

User Authentication: Authentication is implemented using Simple JWT, ensuring that every view is protected and only accessible to authorized users. This adds a layer of security to your API.

Customer Features:

Create Repair Files: Customers can create repair files with relevant information about their repair requests.
Upload Images: Customers can attach images related to their repair requests.
Track File Progress: Customers can monitor the status and progress of their repair files online.
Manager Features:

Change File Phases: Managers have the ability to change the phases of repair files online, providing a seamless way to manage repair requests.
