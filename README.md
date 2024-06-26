# Forum System API

## Description

This is a RESTful API for a Forum System, built with FastAPI and SQLAlchemy ORM, using SQLite as the database. The client-side is developed using React.

## Features

- User authentication
- Users can read and create topics and message other users
- Administrators manage users and categories
- Commenting on topics
- Upvoting/Downvoting replies and setting best reply

## Used Technologies

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **SQLAlchemy ORM**: The Python SQL toolkit and Object-Relational Mapper that gives application developers the full power and flexibility of SQL.
- **SQLite**: A C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language.
- **React**: A JavaScript library for building user interfaces.

## Installation
1. Clone the repository:
    
    ```git clone```

2. Install the requirements:

    ```pip install -r requirements.txt```

    ```npm install```

3. Run the client-side and server-side applications in separate terminals:

    ```cd backend``` -> ```uvicorn main:app```

    ```cd frontend``` -> ```npm start```


## API Endpoints

Authentication:
- `/auth` <span style="background-color:green; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">POST</span>: Endpoint for user registration and login
- `/auth/token` <span style="background-color:green; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">POST</span>: Endpoint for token generation

Categories:
- `/categories` <span style="background-color:green; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">POST</span>: Endpoint for category creation
- `/categories` <span style="background-color:blue; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">GET</span>: Endpoint for retrieving a list of all categories and pagination, filtering, and sorting options
- `/categories/{category_id}` <span style="background-color:blue; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">GET</span>: Endpoint for retrieving information about a specific category and topics related to it
- `/categories/{category_id}/visibility` <span style="background-color:orange; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">PUT</span>: Endpoint for changing the visibility of a category to public or private
- `/categories/{category_id}/users/{user_id}/read-access` <span style="background-color:orange; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">PUT</span>: Endpoint for giving a user read access to a specific private category
- `/categories/{category_id}/users/{user_id}/write-access` <span style="background-color:orange; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">PUT</span>: Endpoint for giving a user write access to a specific private category
- `/categories/{category_id}/users/{user_id}/access/{access_type}` <span style="background-color:orange; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">PUT</span>: Endpoint for revoking type of access to a specific private category
- `/categories/privilaged-users/{category_id}` <span style="background-color:blue; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">GET</span>: Endpoint for retrieving a list of users with access to a specific private category along with their access type
- `/categories/lock/{category_id}` <span style="background-color:orange; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">PUT</span>: Endpoint for locking a category

Topics:
- `/topics` <span style="background-color:green; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">POST</span>: Endpoint for topic creation
- `/topics` <span style="background-color:blue; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">GET</span>: Endpoint for retrieving a list of all topics and pagination, filtering, and sorting options
- `/topics/{topic_id}` <span style="background-color:blue; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">GET</span>: Endpoint for retrieving information about a specific topic and its replies
- `topics/{topic_id}/lock` <span style="background-color:orange; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">PUT</span>: Endpoint for locking a topic

Replies:
- `/replies` <span style="background-color:green; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">POST</span>: Endpoint for reply creation
- `/replies/{reply_id}` <span style="background-color:blue; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">GET</span>: Endpoint for retrieving information about a specific reply
- `/replies/{reply_id}/vote` <span style="background-color:green; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">POST</span>: Endpoint for upvoting/downvoting a reply once per user
- `/replies/{reply_id}/best-reply` <span style="background-color:green; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">POST</span>: Endpoint for setting a reply as the best reply by the topic author

Messages:
- `/messages` <span style="background-color:green; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">POST</span>: Endpoint for message creation
- `/messages/conversations` <span style="background-color:blue; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">GET</span>: Endpoint for retrieving a list of all conversations for the authenticated user
- `/messages/conversation/{user_id}` <span style="background-color:blue; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">GET</span>: Endpoint for retrieving a conversation with a specific user

Users:
- `/users/info` <span style="background-color:blue; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">GET</span>: Endpoint for retrieving information about the authenticated user
- `/users/{user_id}/role` <span style="background-color:orange; color:white; border-radius: 10px; padding: 2px 8px; font-weight: bold;">PUT</span>: Endpoint for changing the role of a user


## Contributors

|       Name            |                   Github Username                 |
|:---------------------:|:-------------------------------------------------:|
| Alexander Videnov     | [AlexVidenov1](https://github.com/AlexVidenov1)   |
| Konstantin Ivanov     | [dnrubinart](https://github.com/dnrubinart)       |
| Radostin Mihaylov     | [radoooo11](https://github.com/radoooo11)         |