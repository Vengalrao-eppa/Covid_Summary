# Task
User story:
As a Data Scientist I would like to read a summary of newCasesByPublishDate from the UK Government’s COVID-19 data in CSV format from an AWS S3 bucket.

Acceptance Criteria:
• Data should be obtained from the API here - https://coronavirus.data.gov.uk/details/developers-guide
• The script should be scheduled to run once per day

#### Running the Application
NOTE: There is an included dockerfile if you don't want to deal with all the dependencies on your system. Simply build
the image from the file and run the application by publishing the 5000 port to a port of your choice. The tests are run
as part of the build process - The IP for this method is `0.0.0.0:5000`

The script was managed by pipenv, and written in Python 3.7, so I recommend using that to install dependencies and 
managing the venv.

Save or clone the repository and save it in directory/folder 
> Ensure you're in the folder as this is the workdir

# Create a Virtual Environment

If you don't have pipenv installed simply run:
> `pip install pipenv`
> You might also need to `pip3 install pipenv` depending on your setup.

There is an included requirements.txt file if you wish to run the application on a system installed interpreter through
pip.
Simply run the `pip install -r requirements.txt`

To create a virtual environment 
    > open terminal and navigate to the folder location 
    > Ensure you're in the folder as this is the workdir
    > `python -m venv .venv`
    > To Activate the Virtual environment 
    > `source .venv/bin/activate` 

# To run the script 
To run the script 
Please run mainscript.py  
> 'python mainscript.py'  
It will generate a data.csv file with the most recent data available at the api 

To read the file from the AWS S3 bucket please run 
> 'python aws_bucket3.py'
In the script please provide  
aws_access_key_id='XX',
aws_secret_access_key='XX',
region_name='XX')
as these credentials are required to read a file from the S3 bucket. 


To Run tests:
> `python -m unittest test_covid19uk.py`
 

To install the dependencies individually please run the following commands
> `pip install schedule` or `pip3 install schedule`
> `pip install boto3` or `pip3 install boto3`
> `pip install uk-covid19` or `pip3 install uk-covid19`
> `pip install pytest` or `pip3 install pytest`
Depending on the set up or simply run `pip install -r requirements.txt`

# Schedule 
Schedule is an in-process scheduler for periodic jobs that uses the builder pattern for configuration. 
Schedule lets you run Python functions (or any other callable) periodically at pre-determined intervals

# boto3 
Boto is the Amazon Web Services (AWS) SDK for Python. 
It enables to create, configure, and manage AWS S3 services