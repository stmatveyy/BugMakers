FROM tensorflow/tensorflow:2.12.0

WORKDIR /app

COPY requirements_prod.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD python main.py

