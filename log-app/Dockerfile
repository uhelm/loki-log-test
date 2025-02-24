FROM python:3.13-bookworm

ADD src/logger.py .
RUN pip install cowsay python-json-logger

CMD ["python", "./logger.py"]