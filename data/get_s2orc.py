import requests
import os
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

base_url = "https://api.semanticscholar.org/datasets/v1/release"
response = requests.get(base_url)
if response.status_code == 200:
   release_id = response.json()[-1]
else:
    raise Exception(f"Failed to get latest release ID: Status code {response.status_code}")

headers = {"x-api-key": os.environ.get("SEMANTIC_SCHOLAR_API_KEY")}
base_url = f"{base_url}/{release_id}"
response = requests.get(f"{base_url}/dataset/s2orc", headers=headers)

if response.status_code == 200:
   response_data = response.json()
   print(response_data.keys())
   print(len(response_data['files']))
else:
    raise Exception(f"Failed to get dataset info: Status code {response.status_code}")

for i, url in enumerate(response_data['files'], start=1):
    if i > 10: break # don't want to download all 260GB
    filename = url.split('/')[-1].split('?')[0]  
    response = requests.get(url, stream=True)  

    if response.status_code == 200:
        print(f"Downloading chunk{i}: {filename}")
        with open(f"chunk{i}.gz", 'wb') as file:
            for chunk in tqdm(response.iter_content(chunk_size=128)):
                file.write(chunk)
        print(f"Downloaded chunk{i}: {filename}")
    else:
        print(f"Failed to download {filename}: Status code {response.status_code}")
