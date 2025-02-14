FROM python:latest

LABEL create_from="Pavel_Prosvetov"

RUN apt update -y && apt upgrade -y
WORKDIR /root/5lb_bot

COPY . .

RUN pip install requirements.txt -r

CMD ["python3", "run_bot.py"]