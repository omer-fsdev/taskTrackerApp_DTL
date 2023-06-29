# Task Tracker App

The Task Tracker App is a web application built using Django Template Language (DTL) and Bootstrap. It provides a user-friendly interface for managing and organizing a todo list.

## Features

The Task Tracker App offers the following features:

- Create, list, update, and delete tasks
- Mark tasks as completed, on progress or waiting
- Mark priorities as high, medium or low
- View the details of a task

## Installation

1. Clone the repository:

```
git clone https://github.com/omer-fsdev/taskTrackerApp_DTL.git
```

2. Navigate to the project directory:

   ```
   cd taskTrackerApp_DTL
   ```

3. Create a virtual environment and activate it:

```

python -m venv env
source env/bin/activate # Linux/Mac
.\env\Scripts\activate # Windows

```

3. Install the required packages:

```

pip install -r requirements.txt

```

4. Run database migrations:

```

python manage.py migrate

```

5. Start the development server:

```

python manage.py runserver

```

6. Open your web browser and visit http://localhost:8000 to view the application..

## License

The Task Tracker App is released under the MIT License.
