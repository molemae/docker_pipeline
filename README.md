# Dockerized ETL Pipeline

This repository contains a Dockerized ETL (Extract, Transform, Load) pipeline designed to collect data from Mastodon, perform sentiment analysis using VADER, and load the processed data into a PostgreSQL database.

## Overview

The ETL pipeline consists of three main components:

1. **reddit_collector**: Collects data from Mastodon using the Mastodon API and stores it in MongoDB.
2. **etl_job**: Performs sentiment analysis on the collected data using VADER and loads it into a PostgreSQL database.
3. **Docker Compose Configuration**: Orchestrates the setup and interaction between the services.


## Usage

1. [Install Docker](https://docs.docker.com/get-docker/)
2. Navigate to the repository root in your terminal.
3. Run `docker compose up`  to exectue docker-compose.yml
    
4. To stop the services, run: `docker-compose down`


## License

This project is licensed under the [MIT License](LICENSE).

## Requirements
- Docker
- python 3.8
### Docker Images:
 - python:3.9
 - mongo:latest
 - postgres:latest

## License

This project is licensed under the [MIT License](LICENSE).