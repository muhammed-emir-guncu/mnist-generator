FROM python:3.12

ADD  app.py .
ADD  req.txt .
ADD ./model ./model

RUN pip install -r req.txt

EXPOSE 8000

CMD ["fastapi", "run", "app.py", "--port", "8000"]
