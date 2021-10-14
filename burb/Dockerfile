FROM python:3.8
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code
# RUN pip install .
# ENTRYPOINT python docker-main.py
# ENV DW_PGSQL='postgresql://postgres:mypassword@postgres-db:5432/tap3_import'
# ENTRYPOINT python dockermain.py
ENTRYPOINT [ "python", "./server.py" ]
