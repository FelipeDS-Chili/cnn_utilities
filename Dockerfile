FROM python:3.8.6-buster
COPY cnn_utilities /cnn_utilities
COPY api /api
COPY model.joblib /model.joblib
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host  0.0.0.0 --port $PORT