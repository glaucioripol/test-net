"""Persist on json file"""
from time import time

from .base import PersistSpeedTestResult

class PersistOnJson(PersistSpeedTestResult):
    """Persist on json file"""
    def persist(self, data: str):
        file_name = f'./results/result_{time()}.json'
        with open(file_name, 'w+', encoding="utf-8") as log_file:
            log_file.write(data)
