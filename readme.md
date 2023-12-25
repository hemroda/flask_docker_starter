# Maavita

Clone the repo.

Make sure you have Docker installed.

## Development

Build the image:

```sh
❯ docker-compose build
```

Run the container:

```sh
❯ docker-compose up -d
```

Build the new image and spin up the containers:

```sh
❯ docker-compose up -d --build
```

Check the logs

```sh
❯ docker-compose logs -f
```

### Database

Create the table:

```sh
❯ docker-compose exec web python manage.py create_db
```

Seed first user

```sh
❯ docker-compose exec web python manage.py seed_first_user
```

Access the DB

```sh
❯ docker-compose exec db psql --username=dbuser --dbname=db_dev
```

List the databases

```sql
db_dev=# \l
```

Connect to `db_dev` database

```sql
db_dev=# \c db_dev
```

```sql
db_dev=# \dt
```

Check that first user has been created

```sql
db_dev=# select * from users;
```
