import requests
from bs4 import BeautifulSoup as BS
import mysql.connector
import csv


url='https://www.cuspide.com/cienmasvendidos'

respuesta=requests.get(url)

respuesta.econding='utf-8'
html=respuesta.text

dom= BS(html,features='html.parser')
    
url2='https://www.cuspide.com/'

articulos=dom.find_all('article')

lista=[]
for libros in articulos:
    titulos=libros.a['href']
    lista.append(titulos)
    
lista_links=[]
for links in lista:
    links_libros=url2+links
    lista_links.append(links_libros)


lista_unido=[]
for linksa in lista_links:
    libros_links=requests.get(linksa)
    libros_links.econding='utf-8'
    html2=libros_links.text
    dom2=BS(html2,features='html.parser')
    
    titulos=dom2.find('div', class_='md-datos')
    titulos2=titulos.a['title']
        
    
   
    
    label=dom2.find('span', text='AR$')
    precios=label.next_sibling.strip()
    
    #print(precios)
    
    unido=(titulos2+";"+precios)
    lista_unido.append(unido)

archivo=open('listaspreciosylibross.csv','w')
for linea in lista_unido:
    fila=linea.split(';')
    archivo.write(fila[0]+';'+fila[1])
    archivo.write('\n')

archivo.close()


conexion = mysql.connector.connect(
                    host = 'your_host',
                    database = 'your_data_base',
                    user = 'your_user',
                    password = 'your_password')

cursor = conexion.cursor()  


archivo_open= open('listaspreciosylibross.csv','r')
libros_csv=csv.reader(archivo_open,delimiter=';')


 

for libros in libros_csv:
    
    pre=libros[1].replace('.','')

    

    sql = "INSERT INTO libros2 (nombres,precios) VALUES (%s,%s)"
    
    tu=(libros[0],pre)
    
    
    
    cursor.execute(sql,tu)
    conexion.commit()


    
cursor.close()
conexion.close()
archivo_open.close()

    
    

    
  


    
    
            
       
        
     
        
    

    
    
 
  
 
    
