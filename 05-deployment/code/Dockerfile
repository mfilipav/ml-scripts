FROM python:3.11.2-slim
RUN pip install pipenv

# creates a dir `app` and `cd app`
WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

# install at system level and with deploy flag
# https://docs.pipenv.org/advanced/#deploying-system-dependencies
RUN pipenv install --system --deploy
COPY ["predict_server.py", "model_C=1.0.bin", "./"]

# if port not exposed, cannot access
EXPOSE 9696
# previously it was ["bash"]
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict_server:app"]