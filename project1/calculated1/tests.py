from django.test import TestCase
import requests

url = 'https://school.dek-d.com/'
web = requests.get('https://www.google.com')
print(list(web))
# Create your tests here.
