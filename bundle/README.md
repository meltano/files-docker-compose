# Meltano Docker Compose

THIS FILE IS INCLUDED FOR CONVENIENCE AND REFERENCE ONLY FEEL FREE TO DELETE IT

## Getting started

Run `docker-compose up -d` to start all the containers in the background

### Helpful Commands

- Run `docker-compose exec meltano-ui /bin/bash` to get a bash terminal inside your meltano container
- Run `docker-compose exec meltano-ui meltano {some command}` to run a meltano command inside your container
  - replace {some command} with a command from the [CLI reference](https://meltano.com/docs/command-line-interface.html)
- Run `docker-compose logs` to see all logs
- Run `docker-compose logs {service name}` to see logs for a particular service
  - for example `docker-compose logs meltano-ui` will output the log stream for the meltano-ui service

## Adding services

### Airflow

1. Uncomment the airflow services
2. Uncomment the airflow database volume
3. Run `docker-compose up -d` to start the airflow containers

## Production usage

### Dependencies

The production compose file depends on a Dockerfile being present in the project. Please run `meltano add files docker` to add a Dockerfile to your project if you haven't already done so.

### Usage

A `docker-compose.prod.yml` file is included for production use. Please ensure you do the following when deploying to production.

1. Change all database passwords (look for "CHANGE ME")
2. Update the database connection strings to reflect the password changes under `x-meltano-env` and `x-airflow-env`
3. Include environment variables from .env and your local environment that are needed for production under the `x-meltano-env:` key where it says "Add your meltano .env variables here"
4. Change the image tag under `x-meltano-image` to something that makes sense for your project
5. Uncomment the airflow services, network, and volume if needed
6. Run `docker-compose -f docker-compose.prod.yml up -d` to start the services

If you need to rebuild your image due to changes after it has been deployed run `docker-compose up -d --build`.
