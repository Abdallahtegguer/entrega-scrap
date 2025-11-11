import requests
from bs4 import BeautifulSoup
import os

# Dataset page URL
url = "https://open.canada.ca/data/en/dataset/1eb9eba7-71d1-4b30-9fb1-30cbdab7e63a" 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers) # enviar a get request fo fetch la pagina html
response.raise_for_status() # to stop the execution if its unsuccessful

soup = BeautifulSoup(response.text, "html.parser") # parse la pagina con beatifulsoup para extraer download links

download_links = []  # guardar todos los enlaces directos 

# scan el codigo html paara <a> enlaces que tiene ficheros apra descargar
for a in soup.find_all("a", href=True):
    href = a["href"]
    filename = href.lower() # normalize to lowercase para comparar
    # verificar si le enlace corresponde con typo de datos
    if (
        ("csv" in filename or "zip" in filename or "xls" in filename)
        and (href.startswith("http") or href.startswith("/sites"))
    ):
        if href.startswith("/"): # convesion de url a url absolute si necessario
            href = f"https://open.canada.ca{href}"
        download_links.append(href)

# print todos los enlaces 
print("Found dataset/resource links:")
for link in download_links:
    print(link)

# Create 'dataset' folder if it does not exist
if not os.path.exists("dataset"):
    os.makedirs("dataset")

# Download each file into the  the dataset  folder i created
for file_url in download_links:
    file_name = file_url.split("/")[-1].split("?")[0]  # Get filename from URL
    path = os.path.join("dataset", file_name)
    print(f"Downloading {file_name} ...")
    file_response = requests.get(file_url, headers=headers, stream=True)
    file_response.raise_for_status()
    with open(path, "wb") as f: # save file to disk
        for chunk in file_response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"{file_name} downloaded to dataset/.")

print("All available files downloaded into the 'dataset' folder.")
