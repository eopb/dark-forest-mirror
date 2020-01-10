FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY GraphQL_Client_Server.py ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "/usr/src/app/src/GraphQL_Client_Server.py" ]