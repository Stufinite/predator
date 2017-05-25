import requests, json
intern = []
for i in range(1, 6):
	intern += requests.get('https://www.yourator.co/api/v2/jobs?position[]=2&page={}'.format(i)).json()['jobs']

job = []
for i in range(1, 29):
	job += requests.get('https://www.yourator.co/api/v2/jobs?page={}'.format(i)).json()['jobs']

with open('intern.json', 'w') as f:
	json.dump(intern, f)
with open('job.json', 'w') as f:
	json.dump(job, f)
