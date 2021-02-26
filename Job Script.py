import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.ca/jobs/search/?q=Engineering&where=Vancouver__2C-BC'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
print(results.prettify())
x1= results.prettify()


#writing to a file
unRefinedFile_one = open("testing1.txt","w")
#f= open("testing1.txt","a")
unRefinedFile_one.write(x1)
unRefinedFile_one.close()
#print(results.prettify())


#writing to a file
unRefinedFile_two = open("testing.txt",'w')


findelemt = results.findAll('section',class_='card-content')
for job_elements in findelemt:
    print(job_elements, end='\n'*2)
    unRefinedFile_two.write(str(job_elements))
unRefinedFile_two.close()

refinedFile = open("List.txt",'w')

for job_elem in findelemt:
    title_elem = job_elem.find('h2',class_='title')
    company_elem = job_elem.find('div',class_='company')
    location_elem = job_elem.find('div',class_='location')
    if None in(title_elem,company_elem,location_elem):
        continue
    refinedFile.write(f'{title_elem.text.strip()}\n{location_elem.text.strip()}\n{company_elem.text.strip()}\n\n')
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
refinedFile.close()



