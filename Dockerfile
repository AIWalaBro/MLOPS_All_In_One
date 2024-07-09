FROM Python:3.10

COPY . /app.py

WORKDIR /app.py

RUN pip install -r requirements.txt

CMD ['Python','app.py']