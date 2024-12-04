import os
import requests
from dotenv import load_dotenv

# Загрузить из .env файла
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = os.getenv("BASE_URL")


class YougileProjects:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        }

    def create_project(self, data):
        response = requests.post(f"{
            BASE_URL}/projects", json=data, headers=self.headers)
        return response

    def get_projects(self):
        response = requests.get(f"{BASE_URL}/projects", headers=self.headers)
        return response

    def update_project(self, project_id, data):
        response = requests.put(f"{
            BASE_URL}/projects/{project_id}", json=data, headers=self.headers)
        return response

    def get_project(self, project_id):
        response = requests.get(f"{
            BASE_URL}/projects/{project_id}", headers=self.headers)
        return response
