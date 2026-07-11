FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ./
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY main.py ./
COPY app/ ./app/

CMD [ "main.lambda_handler" ]