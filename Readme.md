<h1 align="center"> Waterdip AI Backend Assignment</h1>
<p align="center">
<a href="https://github.com/Ryuk-me"><img title="Author" src="https://img.shields.io/badge/Author-Ryuk--me-red.svg?style=for-the-badge&logo=github"></a>
</p>
<p align="center">
<a href="https://github.com/Ryuk-me"><img title="Followers" src="https://img.shields.io/github/followers/Ryuk-me?color=teal&style=flat-square"></a>
<a href="https://github.com/Ryuk-me/pocket-url/stargazers/"><img title="Stars" src="https://img.shields.io/github/stars/ryuk-me/pocket-url?color=brown&style=flat-square"></a>
<a href="https://github.com/Ryuk-me/pocket-url/network/members"><img title="Forks" src="https://img.shields.io/github/forks/ryuk-me/pocket-url?color=lightgrey&style=flat-square"></a>
<a href="https://github.com/Ryuk-me/pocket-url/issues"><img title="issues" src="https://img.shields.io/github/issues/Ryuk-me/pocket-url?style=flat-square">
</a>
<img src='https://visitor-badge.glitch.me/badge?page_id=ryuk-me.pocket-url'>
</p>
<a>


> ## Installation

```sh

# Install Virtual Env
$ pip install virtualenv

# Create Virtual Environment
$ py -3 -m venv waterdip-venv

# Activate Virtual Env [Windows]
$ .\waterdip-venv\Scripts\activate

# Activate Virtual Env [Linux]
$ source waterdip-venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Migrate Using Alembic
$ alembic upgrade head

# Start server
$ uvicorn server.main:app --host 0.0.0.0 --port ${PORT}

# Access
$ http://localhost:${PORT}/api/docs

# Using Docker
$ docker-compose build

# Start
$ docker-compose --env-file ./.env.docker up

# Access
$ http://localhost:${PORT}/api/docs

```


> ## Summary

You will be building a server that can keep track of tasks. Your server must be able to do the following:

1. - [x] Create a new task with a title property and a boolean determining whether the task has been completed. A new unique id would be created for each new task
1. - [x] List all tasks created
1. - [x] Get a specific task
1. - [x] Delete a specified task
1. - [x] Edit the title or completion of a specific task
1. - [x] Edit the title or completion of a specific task
1. - [x] (Extra Credit) Bulk add multiple tasks in one request
1. - [x] (Extra Credit) Bulk delete multiple tasks in one request



#### License

MIT © [Neeraj Kumar](https://github.com/ryuk-me)