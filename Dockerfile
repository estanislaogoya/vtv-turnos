FROM python:3.11.3-slim-buster as pybase
WORKDIR .
COPY . .
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
COPY . ${LAMBDA_TASK_ROOT}
ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD ["app.lambda_handler"]