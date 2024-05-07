#### System Requirements
   - Python 3.8 or higher
   - Django 4.2.11
   - Django REST Framework
   - PostgreSQL

Setting Up the Project

1. **Clone the Repository:**
   git clone [https://github.com/your-repository-url/VMS.git](https://github.com/denishjpatel/VMS.git)
   cd VMS

2. **Create and Activate a Virtual Environment:**
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Required Packages:**
   pip install -r requirements.txt

4. **Setup Database:**

   - Ensure PostgreSQL is installed and running.
   - Create a database named `<db_name>`.
   - Update the `DATABASES` configuration in `VMS/settings.py` if necessary.


5. **Run Migrations:**
   - python manage.py migrate
   
6. **Create Superuser:**
   - python manage.py createsuperuser

7. **Run the Development Server:**
   - python manage.py runserver

#### Running Tests
To run the test suite and verify the functionality of the endpoints:

   - python manage.py test


# API documenatation

   - For the API documentation you can see file(postman collection) `test_task.postman_collection`
   - Just import it inside the postman collection 