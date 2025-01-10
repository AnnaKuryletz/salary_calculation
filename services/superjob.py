import os
import requests
from utils.salary import predict_rub_salary_for_superjob
from dotenv import load_dotenv


def get_superjob_statistics(language, api_superjob, town_id=4, catalogue_id=48):
    base_url = "https://api.superjob.ru/2.0/vacancies/"
    headers = {"X-Api-App-Id": api_superjob}
    params = {
        "town": town_id,
        "catalogues": catalogue_id,
        "keyword": language,
        "count": 100,
    }

    total_vacancies = 0
    processed_vacancies = 0
    total_salary = 0
    page = 0
    has_more = True

    while has_more:
        params["page"] = page
        response = requests.get(base_url, params=params, headers=headers)
        if response.status_code != 200:
            print(f"Ошибка {response.status_code}: {response.text}")
            break
        data = response.json()

        for vacancy in data.get("objects", []):
            total_vacancies += 1
            salary = predict_rub_salary_for_superjob(vacancy)
            if salary is not None:
                processed_vacancies += 1
                total_salary += salary

        has_more = data.get("more", False)
        page += 1

    average_salary = (
        int(total_salary / processed_vacancies) if processed_vacancies > 0 else None
    )

    return {
        "vacancies_found": total_vacancies,
        "vacancies_processed": processed_vacancies,
        "average_salary": average_salary,
    }
