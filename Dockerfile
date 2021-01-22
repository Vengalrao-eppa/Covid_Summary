FROM python:3.7
WORKDIR /folder
COPY . /folder
EXPOSE 5000
# .env file loading doesn't work in docker... Need to set it here
ENV COVID_API=https://coronavirus.data.gov.uk/details/developers-guide
ENV HOST_IP=0.0.0.0

RUN pip install -r requirements.txt
RUN python -m unittest

ENTRYPOINT ["python","mainscript.py"]