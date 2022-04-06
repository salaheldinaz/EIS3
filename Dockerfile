FROM python:3.7

WORKDIR /app

COPY main.py requirements.txt  ./
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
CMD ["-h"]
