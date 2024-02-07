# Django and Vue Books

## How to Run Servers

To run the servers for the project, follow these steps:

1. Activate the virtual environment by running the following command:
  ```bash
  virtualenv environment_3_10_4
  source environment_3_10_4/bin/activate
  ```

2. Install the required dependencies by running the following command:
  ```bash
  cd pzaz_books_django
  pip install -r requirements.txt
  ```

3. Start the backend server by running the following command:
  ```bash
  python manage.py runserver
  ```

# Please note the following

> [!NOTE]  
> I did have a hard time trying to make the `CRUD` with uploading images, besides you could check in `views`, I do have the code there for the task `(without images)` 

> [!IMPORTANT]  
> I decided to go one step further to create a simple flow like an e-commerce page instead, using the admin console from Django to create books and the rest build in vue, you can create users there too, please do to see the `cart` functionality.

> [!TIP]
> You can create new users, but if you don't, use: `user: admin` for `Django` or `user:guest` for `vue-app`, and password for both`password: pzaspzaz`

Make sure to have Python, Django, and Node.js installed on your machine before running the servers.


## How to Run Servers

4. Install the required dependencies by running the following command:
  ```bash
  cd pzaz_books_vue
  npm install
  ```

5. Start the server by running the following command:
  ```bash
  npm run serve
```
