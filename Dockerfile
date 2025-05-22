FROM python:3.11.12-alpine3.21
WORKDIR /usr/workspace
COPY ./ /usr/workspace
RUN pip install -r requirements.txt
CMD ["pytest", "-sv"]