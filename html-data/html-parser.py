from bs4 import BeautifulSoup


with open('pge_meter_details.html', 'r') as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, 'html.parser')


rate_element = soup.find('div', class_='module-body').find('h3')
rate_name = rate_element.get_text(strip=True)


ul_element = soup.find('div', class_='module-body sa-info').ul
li_elements = ul_element.find_all('li')
address_part1 = li_elements[0].get_text(strip=True)
address_part2 = li_elements[1].get_text(strip=True)
service_address = address_part1 + ', ' + address_part2


print("Rate Name:", rate_name)
print("Service Address:", service_address)
