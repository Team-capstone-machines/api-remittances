
FROM python:3.7

WORKDIR /app

COPY . .

RUN python3 -m pip install --upgrade pip

RUN apt-get update

RUN apt-get -y install unixodbc-dev

RUN pip install --no-cache-dir -r requirements-prod.txt

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update

RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17

RUN ACCEPT_EULA=Y apt-get install -y mssql-tools

RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

EXPOSE 80

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]
