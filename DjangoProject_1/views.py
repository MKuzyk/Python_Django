from django.http import HttpResponse,HttpResponseNotFound, JsonResponse
from datetime import datetime
from .models import all_countries
from .models import find_by_name

call_counter = 0

def current_time(request):
    return HttpResponse(f"Aktualny czas: {datetime.now()}")

def call_count(request):
    global call_counter
    call_counter += 1
    return HttpResponse(f"Ta strona została wywołana {call_counter} razy.")

def country_by_name(request, country_name):
    found_country = find_by_name(country_name)

    if found_country is None:
        return HttpResponseNotFound(f"Nie znaleziono kraju o nazwie {country_name}.")

    return JsonResponse(found_country)

def country_name(request, country_name):
    found_country = find_by_name(country_name)

    if found_country is None:
        return HttpResponseNotFound(f"Nie znaleziono kraju o nazwie {country_name}.")

    return JsonResponse({"country": found_country["country"]})


def country(request, country_name):
    found_country = find_by_name(country_name)

    if found_country is None:
        return HttpResponseNotFound(f"Nie znaleziono kraju o nazwie {country_name}.")

    return HttpResponse(found_country["country"])


def country_by_index(request, country_index):
    if country_index < 0 or country_index >= len(all_countries):
        return HttpResponseNotFound(f"Nie znaleziono kraju o indeksie {country_index}.")

    found_country = all_countries[country_index]
    return HttpResponse(found_country['country'])

def first_html(request):
    response_data = """
    <h1>To jest HTML</h1>
    <ul>
        <li>jeden</li>
        <li>dwa</li>
        <li>trzy</li>
        <li>cztery</li>
        <li><a href='/country/Afghanistan'>Afghanistan</a></li>
    </ul>
    """
    return HttpResponse(response_data)


def country_list(request, max_countries):
    countries_to_display = all_countries[:max_countries]

    response_data = "<h1>Lista Krajów</h1><ul>"

    for country in countries_to_display:
        response_data += f"<li><a href='/country/{country['country']}'> {country['country']} </a></li>"

    response_data += "</ul>"

    return HttpResponse(response_data)

def country_list_json(request, max_countries):
    countries_to_display = all_countries[:max_countries]

    response_data = "<h1>Lista Krajów</h1><ul>"

    for country in countries_to_display:
        response_data += f"<li><a href='/country-one/json/{country['country']}'> {country['country']} </a></li>"

    response_data += "</ul>"

    return HttpResponse(response_data)

