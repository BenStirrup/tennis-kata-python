FROM python:3.6-slim

CMD ["bash"]

COPY /kata /kata

WORKDIR /kata

RUN pip install mypy
 