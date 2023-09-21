# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1



# Install pip requirements
COPY requirements.txt .

RUN python -m pip install -r requirements.txt

WORKDIR /stationary_store/stationary_store
COPY . /stationary_store


EXPOSE 8000

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "stationary_store/manage.py", "runserver", "0.0.0.0:8000"]
