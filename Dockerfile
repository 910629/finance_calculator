FROM pypy:latest
WORKDIR /app
COPY . /app
CMD python finance_calculator.py