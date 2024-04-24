from bs4 import BeautifulSoup           # pip3 install beautifulsoup4
import requests

soup11 = BeautifulSoup("<p>Some<b>bad<i>HTML", "html.parser")
print(soup11.prettify())

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup12 = BeautifulSoup(page.content, "html.parser")
results11 = soup12.find(id="ResultsContainer")
# print(results11.prettify())

job_elements = results11.find_all("div", class_="card-content")
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()

python_jobs = results11.find_all("h2", string=lambda text: "python" in text.lower())
print(len(python_jobs))

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    links = job_element.find_all("a")
    for link in links:
        # print(link.text.strip())
        print("apply here ===> ", link["href"],"\n")
    print()