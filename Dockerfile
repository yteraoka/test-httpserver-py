FROM python:3.8

COPY httpserver.py /httpserver.py

EXPOSE 8000

CMD ["python", "/httpserver.py"]
