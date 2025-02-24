FROM python:3.13-bookworm

ADD src/logger.py .
RUN pip install python-cowsay python-json-logger

CMD ["python", "./logger.py"]