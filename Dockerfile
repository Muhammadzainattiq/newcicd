FROM python:3.12
WORKDIR /app
RUN pip install poetry
COPY . /app/
RUN poetry config virtualenvs.create false
RUN poetry install
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "new.main:app", "--host", "0.0.0.0", "--reload"]