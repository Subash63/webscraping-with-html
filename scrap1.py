import requests
from bs4 import BeautifulSoup
import json
def parts(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        heading = soup.find('h1').text.strip()
        paragraphs = soup.find_all('p',class_="pn-detail-sub-desc")
        price = soup.find('span', class_="price-section-price").text.strip()
        price_save = soup.find('span', class_="price-section-retail")
        price_bar = price_save.text.strip()

        describe = soup.find('li',class_="pn-detail-description").div.text.strip()


        product = soup.find('table',class_="pn-spec-list")
        product_data=[]
        for rows in product:
            cells= rows.find_all('td')
            rows_data=[cells.text.strip() for cells in cells]
            product_data.append(rows_data)


        vehicle = soup.find('table',class_="fit-vehicle-list-table")
        Vehicle_data=[]
        for rows2 in vehicle:
            cell_data=rows2.find_all('td')
            rows_data1=[cell_data.text.strip() for cell_data in cell_data]
            Vehicle_data.append(rows_data1)
        Model_details = {
            'Title': heading,
            'Model and Part Number': [p.text.strip() for p in paragraphs if p.text.strip()],
            'price': price,
            'MRP price': price_bar,
            'Part description': describe,
        }
        Product_description = {
            'Product_descrition': product_data
        }

        vehicle_fitment = {
            'Vehicle Fit': Vehicle_data
        }
        Part_details = {
            'Model_details': Model_details,
            'Product_description': Product_description,
            'Vehicle_fitment':vehicle_fitment

        }
    json_output = json.dumps(Part_details, indent=2,ensure_ascii=False )
    with open('output.json','w')as json_file:
        json_file.write(json_output)
if __name__ == "__main__":
    parts_url = 'https://www.moparpartsgiant.com/parts/mopar-belt-serpentine~68232297aa.html'
    parts(parts_url)

