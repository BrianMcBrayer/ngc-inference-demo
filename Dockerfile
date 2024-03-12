FROM python:3.12-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt

# install uv
RUN pip3 install -r requirements.txt

# copy everything
COPY ./src .

# set environment variables
ARG NVIDIA_API_KEY
ENV NVIDIA_API_KEY=$NVIDIA_API_KEY

ENV FLASK_APP=index.py

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]