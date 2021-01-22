import schedule
import time

from uk_covid19 import Cov19API

all_nations = [
    'areaType=nation'
]

cases_and_deaths = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeathsByDeathDate": "newDeathsByDeathDate",
    "cumDeathsByDeathDate": "cumDeathsByDeathDate"
}

api = Cov19API(
    filters=all_nations,
    structure=cases_and_deaths,
)

# def job():
#     api.get_csv(save_as="data.csv")
    
# # schedule.every().day.at("10:30").do(job)
# # schedule.every().minute.at(":17").do(job)
# schedule.every(5).to(10).seconds.do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
