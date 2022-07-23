FROM python:3.8-slim-buster

WORKDIR /code

RUN python3 -m venv /opt/venv
# This is wrong!
RUN . /opt/venv/bin/activate
RUN /usr/local/bin/python -m pip install --upgrade pip

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
CMD ["python", "main.py"]

