import json
import os
from django.db import models
from django.conf import settings
import sys

# Konfiguracja kodowania, jeśli używasz Windows
sys.stdout.reconfigure(encoding='utf-8')

def load_countries():
    file_path = os.path.join(settings.BASE_DIR, 'DjangoProject_1', 'country_info.json')
    try:
        with open(file_path, encoding='utf-8') as country_file:
            return json.load(country_file)
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Błąd w pliku JSON: {e}")
        return []

# Ładowanie danych tylko raz
all_countries = load_countries()

def find_by_name(name):
    for country in all_countries:
        if country['country'].casefold() == name.casefold():
            return country
    return None

