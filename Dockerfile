FROM python:3.10-slim

COPY requirements.txt .
COPY src /mac_address_client

RUN pip install -r requirements.txt

RUN export PYTHONPATH=/mac_address_client:$PYTHONPATH

ENTRYPOINT ["python3", "/mac_address_client/main.py"]