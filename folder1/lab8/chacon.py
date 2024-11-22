import json

with open('../../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as csvfile:
    for repo in data[:5]:
        name = repo.get('name')
        html_url = repo.get('html_url')
        updated_at = repo.get('updated_at')
        visibility = repo.get('visibility')
        
        
        csv_line = f"{name},{html_url},{updated_at},{visibility}\n"
        csvfile.write(csv_line)

