# Airflow + Postgres + MinIO (Docker)

A local learning project: Airflow 3 DAGs that use Postgres and S3-compatible MinIO, all run with Docker Compose.

> Local use only. The credentials in this repo are demo values.

## Prerequisites
- Docker and Docker Compose
- A free MinIO AIStor license (https://min.io/pricing, Free tier)

## Run it
1. Create your env file:
   ```bash
   cp .env.example .env
   ```
2. Generate a Fernet key and paste it as `FERNET_KEY` in `.env`:
   ```bash
   python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
   ```
3. Save your MinIO license as `minio/minio.license` and create the data folder:
   ```bash
   mkdir -p minio/data
   ```
4. Build and start everything:
   ```bash
   docker compose up -d --build
   ```
5. Open the UIs:
   - Airflow: http://localhost:8080 (airflow / airflow)
   - MinIO console: http://localhost:9001 (admin / password123)
6. In MinIO, create a bucket named `airflow` and upload `data/data.csv`.
7. Unpause the DAGs in the Airflow UI.

## Postgres (optional, for DBeaver)
Host `localhost`, port `5432`, database `airflow`, user `airflow`, password `airflow`.

The Airflow connection `minioS3_Conn` is created automatically from `docker-compose.yaml`. For the Postgres DAG, create a connection `postgres_localhost` in Admin > Connections (host `postgres`, port `5432`, schema `airflow`, login/password `airflow`).

## Stop / reset
```bash
docker compose down        # stop, keep data
docker compose down -v     # stop and wipe the Postgres volume
```

## Project layout
```
dags/            Airflow DAGs
data/data.csv    Sample file for the MinIO sensor DAG
Dockerfile       Extends apache/airflow with extra providers
requirements.txt Extra Python packages
minio/           MinIO license and data (git-ignored)
```
