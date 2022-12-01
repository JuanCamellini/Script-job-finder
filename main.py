import enum
from bs4 import BeautifulSoup
import requests
import time


print("Welcome!")
print(" ")
unfamiliar_skill = input("Put some skill that you are not interested in: ")
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():
    html_text = requests.get("https://ar.bebee.com/jobs?term=django&location=Buenos+Aires%2C+Buenos+Aires+C.F.&geoname_id=3435910&search=1&only_remote=&freelancer=&no_freelancer=&sub_services=&sub_service_item=&distance=")
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ ="nf-job list-group-item mb-3 clickable-job")
    print (jobs)
    for index, job in enumerate(jobs):
        published_data = job.find('div', class_= 'd-flex flex-column justify-content-center').p.small.text
        if '2 meses' not in published_data:
            job_name = job.find('h2', class_ = 'mb-0').a.text
            url = job.find('h2', class_ = 'mb-0').a['href']
            company = job.find('div', class_='nf-job-list-desc mb-3').div.span.text
            text_skills = job.find('p', _class= 'mt-2 mb-0').text
            if unfamiliar_skill not in text_skills:
                with open(f'posts/{index}.text', 'w') as f:
                    f.write(f"Job Name: {job_name}\n")
                    f.write(f"Company: {company}\n")
                    f.write(f"Info position: {text_skills}\n")
                    f.write(f"URL: {url}")
                print(f"File saved: {index}")

if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 30
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)