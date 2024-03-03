## Project Documentation
LittleLemon is a project developed in association with the Meta Back-End Developer Capstone course on Coursera. Using Django and DRF, the project involved creating APIs for menu and booking functionalities. By completing this project, valuable experience was gained in developing RESTful APIs and demonstrating proficiency in backend development concepts. The LittleLemon Restaurant API serves as a practical example of building scalable and robust backend systems.

### Installation
Here's how to get yourself started with Litlelemon on your machine.

1. Clone the project repository:
   ```
   git clone https://github.com/Nolulamo/littleLemon.git
   ```

2. Navigate to the project directory:
   ```
   cd litlelemon
   ```

3. Create a virtual environment and activate it:
   - For Windows:
     ```
     python -m venv env
     .\env\Scripts\activate
     ```
   - For macOS and Linux:
     ```
     python3 -m venv env
     source env/bin/activate
     ```

4. Install project dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Test the APIs:
   - Open your web browser or insomnia and access the following API endpoints:
     ```
     http://127.0.0.1:8000/restaurant/menu/menu/
     ```
     ```
     http://127.0.0.1:8000/restaurant/menu/menu/1
     ```
     ```
     http://127.0.0.1:8000/restaurant/booking/booking/
     ```
     ```
     http://127.0.0.1:8000/restaurant/booking/booking/1
     ```
  - Open the link below on your browser to see if web application use Django to serve static HTML content?:
    ```
     http://127.0.0.1:8000/restaurant/menu/
     ```
