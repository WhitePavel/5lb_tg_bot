FROM python:latest

LABEL PavelProsvetov_from_pet_project

RUN apt update && apt upgrade

COPY . .








