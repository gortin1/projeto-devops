FROM python:3.9-slim

RUN python -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 1313

CMD ["python", "app/app.py"]