import json
import zipfile

def count_people_in_moscow(zip_file):
    count = 0
    with zipfile.ZipFile(zip_file, 'r') as zf:
        for filename in zf.namelist():
            if not filename.endswith('.json'):
                continue
            with zf.open(filename) as f:
                data = json.load(f)
                if data.get('city', '') == 'Moscow':
                    count += 1
    return count

zip_file = '5.zip'
people_in_moscow = count_people_in_moscow(zip_file)
print(f"Людей в москве: {people_in_moscow}")