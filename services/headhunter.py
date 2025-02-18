import requests
from utils.salary import predict_rub_salary_for_hh


def get_hh_statistics(language, area=1):
    base_url = "https://api.hh.ru/vacancies"
    params = {"text": language, "area": area, "per_page": 100}

    processed_vacancies = 0
    total_salary = 0
    page = 0
    has_more = True
    total_vacancies = 0

    while has_more:
        params["page"] = page
        response = requests.get(base_url, params=params)
        vacancies_hh = response.json()

        total_vacancies = vacancies_hh.get("found", 0)

        for vacancy in vacancies_hh.get("items", []):
            salary = predict_rub_salary_for_hh(vacancy.get("salary"))
            if salary:
                processed_vacancies += 1
                total_salary += salary

        has_more = page < vacancies_hh["pages"] - 1
        page += 1

    average_salary = (
        int(total_salary / processed_vacancies) if processed_vacancies else None
    )

    return {
        "vacancies_found": total_vacancies,
        "vacancies_processed": processed_vacancies,
        "average_salary": average_salary,
    }
