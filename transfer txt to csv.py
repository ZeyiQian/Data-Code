


*No csv means there is no data in that district in that combination


****district_X93-X95_15-24_Male_white***
from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_X93-X95_15-24_Male_white'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_X93-X95_15-24_Male_white\{value}_X93-X95_15-24_Male_white.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    soup = BeautifulSoup(html_text, 'html.parser')
    table = soup.find('table', class_='tabdados')
    headers = [header.text.strip() for header in table.select('thead th')]
    rows = []
    for row in table.select('tbody tr'):
        data = [cell.text.strip() for cell in row.select('td')]
        rows.append(data)
    output_file = rf'{output_folder}\{value}_X93-X95_15-24_Male_white.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Conversion completed for {file_path}! Saved as {output_file}")




****district_X93-X95_15-24_Male_blackbrown*** 
from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_X93-X95_15-24_Male_blackbrown'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_X93-X95_15-24_Male_blackbrown\{value}_X93-X95_15-24_Male_blackbrown.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    soup = BeautifulSoup(html_text, 'html.parser')
    table = soup.find('table', class_='tabdados')
    headers = [header.text.strip() for header in table.select('thead th')]
    rows = []
    for row in table.select('tbody tr'):
        data = [cell.text.strip() for cell in row.select('td')]
        rows.append(data)
    output_file = rf'{output_folder}\{value}_X93-X95_15-24_Male_blackbrown.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Conversion completed for {file_path}! Saved as {output_file}")




****district_X93-X95_15-24_Female_white***  
from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_X93-X95_15-24_Female_white'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_X93-X95_15-24_Female_white\{value}_X93-X95_15-24_Female_white.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_X93-X95_15-24_Female_white.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue









****district_X93-X95_15-24_Female_blackbrown***


from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_X93-X95_15-24_Female_blackbrown'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_X93-X95_15-24_Female_blackbrown\{value}_X93-X95_15-24_Female_blackbrown.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_X93-X95_15-24_Female_blackbrown.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue






****district_X93-X95_25-34_Male_white***


from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_X93-X95_25-34_Male_white'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_X93-X95_25-34_Male_white\{value}_X93-X95_25-34_Male_white.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_X93-X95_25-34_Male_white.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue







****district_X93-X95_25-34_Male_blackbrown***


from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_X93-X95_25-34_Male_blackbrown'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_X93-X95_25-34_Male_blackbrown\{value}_X93-X95_25-34_Male_blackbrown.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_X93-X95_25-34_Male_blackbrown.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue





****district_X93-X95_25-34_Female_white***


from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_X93-X95_25-34_Female_white'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_X93-X95_25-34_Female_white\{value}_X93-X95_25-34_Female_white.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_X93-X95_25-34_Female_white.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue





****district_X93-X95_25-34_Female_blackbrown***


from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_X93-X95_25-34_Female_blackbrown'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_X93-X95_25-34_Female_blackbrown\{value}_X93-X95_25-34_Female_blackbrown.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_X93-X95_25-34_Female_blackbrown.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue

















****district_All_15-24_Male_white***

from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_All_15-24_Male_white'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_All_15-24_Male_white\{value}_All_15-24_Male_white.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_All_15-24_Male_white.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue



****district_All_15-24_Male_blackbrown***

from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_All_15-24_Male_blackbrown'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_All_15-24_Male_blackbrown\{value}_All_15-24_Male_blackbrown.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_All_15-24_Male_blackbrown.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue


****district_All_15-24_Female_white***

from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_All_15-24_Female_white'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_All_15-24_Female_white\{value}_All_15-24_Female_white.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_All_15-24_Female_white.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue



****district_All_15-24_Female_blackbrown***

from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_All_15-24_Female_blackbrown'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_All_15-24_Female_blackbrown\{value}_All_15-24_Female_blackbrown.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_All_15-24_Female_blackbrown.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue


****district_All_25-34_Male_white***

from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_All_25-34_Male_white'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_All_25-34_Male_white\{value}_All_25-34_Male_white.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_All_25-34_Male_white.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue



****district_All_25-34_Male_blackbrown***


from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_All_25-34_Male_blackbrown'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_All_25-34_Male_blackbrown\{value}_All_25-34_Male_blackbrown.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_All_25-34_Male_blackbrown.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue


****district_All_25-34_Female_white***

from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_All_25-34_Female_white'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_All_25-34_Female_white\{value}_All_25-34_Female_white.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_All_25-34_Female_white.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue



****district_All_25-34_Female_blackbrown***

from bs4 import BeautifulSoup
import csv

output_folder = r'C:\Users\QIAN\Dropbox\Gun control\data\crawler\CSV\District_All_25-34_Female_blackbrown'

for value in range(1, 99):
    file_path = rf'C:\Users\QIAN\Dropbox\Gun control\data\crawler\District_All_25-34_Female_blackbrown\{value}_All_25-34_Female_blackbrown.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find('table', class_='tabdados')
        headers = [header.text.strip() for header in table.select('thead th')]
        rows = []
        for row in table.select('tbody tr'):
            data = [cell.text.strip() for cell in row.select('td')]
            rows.append(data)
        output_file = rf'{output_folder}\{value}_All_25-34_Female_blackbrown.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Conversion completed for {file_path}! Saved as {output_file}")
    except Exception as e:
        print(f"Error occurred while converting {file_path}: {str(e)}")
        continue