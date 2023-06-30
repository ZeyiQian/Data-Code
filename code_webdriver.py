
*download chrome webdriver and change the path in your system
*pip install selenium


*python
*open web driver first in case

import subprocess

p = subprocess.Popen(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver_win32\\chromedriver.exe"])












********test code: district_X93-X95_15-24_Male_white***********

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 


driver = webdriver.Chrome()

url = 'http://tabnet.saude.prefeitura.sp.gov.br/cgi/deftohtm3.exe?secretarias/saude/TABNET/SIMMUL/Tabmul.def'
driver.get(url)


select_content = Select(driver.find_element(By.NAME, 'Linha'))
select_content.select_by_value('Causa_básica_da_Morte')

select_content = Select(driver.find_element(By.NAME, 'Coluna'))
select_content.select_by_value('Ano_do_obito')

select_files = Select(driver.find_element(By.NAME, 'Incremento'))
select_files.deselect_by_value('Menções')
select_files.select_by_value('Óbitos')

select_files = Select(driver.find_element(By.NAME, 'Arquivos'))
select_files.select_by_value('camu21.dbf')
select_files.select_by_value('camu20.dbf')
select_files.select_by_value('camu19.dbf')
select_files.select_by_value('camu18.dbf')
select_files.select_by_value('camu17.dbf')
select_files.select_by_value('camu16.dbf')
select_files.select_by_value('camu15.dbf')
select_files.select_by_value('camu14.dbf')
select_files.select_by_value('camu13.dbf')
select_files.select_by_value('camu12.dbf')
select_files.select_by_value('camu11.dbf')
select_files.select_by_value('camu10.dbf')
select_files.select_by_value('camu09.dbf')
select_files.select_by_value('camu08.dbf')
select_files.select_by_value('camu07.dbf')
select_files.select_by_value('camu06.dbf')
select_files.select_by_value('camu05.dbf')
select_files.select_by_value('camu04.dbf')
select_files.select_by_value('camu03.dbf')
select_files.select_by_value('camu02.dbf')


image_element = driver.find_element(By.ID, 'fig3')
image_element.click()

select_files = Select(driver.find_element(By.NAME, 'SDiagnóstico_mencionado'))
select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
select_files.select_by_value('1723')
select_files.select_by_value('1724')
select_files.select_by_value('1725')


image_element = driver.find_element(By.ID, 'fig6')
image_element.click()
select_files = Select(driver.find_element(By.NAME, 'SFaixa_Etária_(9)'))
select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
select_files.select_by_value('4')

image_element = driver.find_element(By.ID, 'fig10')
image_element.click()
select_files = Select(driver.find_element(By.NAME, 'SSexo'))
select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
select_files.select_by_value('1')



image_element = driver.find_element(By.ID, 'fig11')
image_element.click()
select_files = Select(driver.find_element(By.NAME, 'SRaça/Cor'))
select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
select_files.select_by_value('1')


image_element = driver.find_element(By.ID, 'fig12')
image_element.click()
select_files = Select(driver.find_element(By.NAME, 'SDistr_Adm_Res'))
select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
select_files.select_by_value('1')


submit_button = driver.find_element(By.NAME, 'mostre')
submit_button.click()

time.sleep(20)

result = driver.page_source
with open('1_X93-X95_15-24_Male_white.txt', 'w', encoding='utf-8') as f:
    f.write(result)

driver.quit()










***LOOP***


****district_X93-X95_15-24_Male_white***
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

for value in range(1, 99):
    driver = webdriver.Chrome()
    url = 'http://tabnet.saude.prefeitura.sp.gov.br/cgi/deftohtm3.exe?secretarias/saude/TABNET/SIMMUL/Tabmul.def'
    driver.get(url)
    select_content = Select(driver.find_element(By.NAME, 'Linha'))
    select_content.select_by_value('Causa_básica_da_Morte')
    select_content = Select(driver.find_element(By.NAME, 'Coluna'))
    select_content.select_by_value('Ano_do_obito')
    select_files = Select(driver.find_element(By.NAME, 'Incremento'))
    select_files.deselect_by_value('Menções')
    select_files.select_by_value('Óbitos')
    select_files = Select(driver.find_element(By.NAME, 'Arquivos'))
    select_files.select_by_value('camu21.dbf')
    select_files.select_by_value('camu20.dbf')
    select_files.select_by_value('camu19.dbf')
    select_files.select_by_value('camu18.dbf')
    select_files.select_by_value('camu17.dbf')
    select_files.select_by_value('camu16.dbf')
    select_files.select_by_value('camu15.dbf')
    select_files.select_by_value('camu14.dbf')
    select_files.select_by_value('camu13.dbf')
    select_files.select_by_value('camu12.dbf')
    select_files.select_by_value('camu11.dbf')
    select_files.select_by_value('camu10.dbf')
    select_files.select_by_value('camu09.dbf')
    select_files.select_by_value('camu08.dbf')
    select_files.select_by_value('camu07.dbf')
    select_files.select_by_value('camu06.dbf')
    select_files.select_by_value('camu05.dbf')
    select_files.select_by_value('camu04.dbf')
    select_files.select_by_value('camu03.dbf')
    select_files.select_by_value('camu02.dbf')
    image_element = driver.find_element(By.ID, 'fig3')
    image_element.click()
    select_files = Select(driver.find_element(By.NAME, 'SDiagnóstico_mencionado'))
    select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
    select_files.select_by_value('1723')
    select_files.select_by_value('1724')
    select_files.select_by_value('1725')
    image_element = driver.find_element(By.ID, 'fig6')
    image_element.click()
    select_files = Select(driver.find_element(By.NAME, 'SFaixa_Etária_(9)'))
    select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
    select_files.select_by_value('4')
    image_element = driver.find_element(By.ID, 'fig10')
    image_element.click()
    select_files = Select(driver.find_element(By.NAME, 'SSexo'))
    select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
    select_files.select_by_value('1')
    image_element = driver.find_element(By.ID, 'fig11')
    image_element.click()
    select_files = Select(driver.find_element(By.NAME, 'SRaça/Cor'))
    select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
    select_files.select_by_value('1')
    image_element = driver.find_element(By.ID, 'fig12')
    image_element.click()
    select_files = Select(driver.find_element(By.NAME, 'SDistr_Adm_Res'))
    select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
    select_files.select_by_value(str(value))
    submit_button = driver.find_element(By.NAME, 'mostre')
    submit_button.click()
    time.sleep(20)
    result = driver.page_source
    with open(f'C:/Users/QIAN/Dropbox/Gun control/data/crawler/District_X93-X95_15-24_Male_white/{value}_X93-X95_15-24_Male_white.txt', 'w', encoding='utf-8') as f:
        f.write(result)
    driver.quit()





****district_X93-X95_15-24_Male_blackbrown***

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

for value in range(1, 99):
    driver = webdriver.Chrome()
    url = 'http://tabnet.saude.prefeitura.sp.gov.br/cgi/deftohtm3.exe?secretarias/saude/TABNET/SIMMUL/Tabmul.def'
    driver.get(url)
    select_content = Select(driver.find_element(By.NAME, 'Linha'))
    select_content.select_by_value('Causa_básica_da_Morte')
    select_content = Select(driver.find_element(By.NAME, 'Coluna'))
    select_content.select_by_value('Ano_do_obito')
    select_files = Select(driver.find_element(By.NAME, 'Incremento'))
    select_files.deselect_by_value('Menções')
    select_files.select_by_value('Óbitos')
    select_files = Select(driver.find_element(By.NAME, 'Arquivos'))
    select_files.select_by_value('camu21.dbf')
    select_files.select_by_value('camu20.dbf')
    select_files.select_by_value('camu19.dbf')
    select_files.select_by_value('camu18.dbf')
    select_files.select_by_value('camu17.dbf')
    select_files.select_by_value('camu16.dbf')
    select_files.select_by_value('camu15.dbf')
    select_files.select_by_value('camu14.dbf')
    select_files.select_by_value('camu13.dbf')
    select_files.select_by_value('camu12.dbf')
    select_files.select_by_value('camu11.dbf')
    select_files.select_by_value('camu10.dbf')
    select_files.select_by_value('camu09.dbf')
    select_files.select_by_value('camu08.dbf')
    select_files.select_by_value('camu07.dbf')
    select_files.select_by_value('camu06.dbf')
    select_files.select_by_value('camu05.dbf')
    select_files.select_by_value('camu04.dbf')
    select_files.select_by_value('camu03.dbf')
    select_files.select_by_value('camu02.dbf')
    image_element = driver.find_element(By.ID, 'fig3')
    image_element.click()
    select_files = Select(driver.find_element(By.NAME, 'SDiagnóstico_mencionado'))
    select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
    select_files.select_by_value('1723')
    select_files.select_by_value('1724')
    select_files.select_by_value('1725')
    image_element = driver.find_element(By.ID, 'fig6')
    image_element.click()
    select_files = Select(driver.find_element(By.NAME, 'SFaixa_Etária_(9)'))
    select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
    select_files.select_by_value('4')
    image_element = driver.find_element(By.ID, 'fig10')
    image_element.click()
    select_files = Select(driver.find_element(By.NAME, 'SSexo'))
    select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
    select_files.select_by_value('1')
    image_element = driver.find_element(By.ID, 'fig11')
    image_element.click()
    select_files = Select(driver.find_element(By.NAME, 'SRaça/Cor'))
    select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
    select_files.select_by_value('2')
    select_files.select_by_value('4')
    image_element = driver.find_element(By.ID, 'fig12')
    image_element.click()
    select_files = Select(driver.find_element(By.NAME, 'SDistr_Adm_Res'))
    select_files.deselect_by_value('TODAS_AS_CATEGORIAS__')
    select_files.select_by_value(str(value))
    submit_button = driver.find_element(By.NAME, 'mostre')
    submit_button.click()
    time.sleep(20)
    result = driver.page_source
    with open(f'C:/Users/QIAN/Dropbox/Gun control/data/crawler/District_X93-X95_15-24_Male_blackbrown/{value}_X93-X95_15-24_Male_blackbrown.txt', 'w', encoding='utf-8') as f:
        f.write(result)
    driver.quit()







