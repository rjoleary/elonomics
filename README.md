# Elonomics

Chess is a great game to play with friends and colleagues! This software keeps
track of the scores.


# Deployment Steps

In the elonomics/settings.py file, you will want to change the following
variables:

- `SECRET_KEY` to your own secret
- `DEBUG` to `false`
- `ALLOWED_HOSTS`
- `DATABASES` to a proper RDBMS
- `TIME_ZONE` to your local timezone
