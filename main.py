from services.superjob import get_superjob_statistics
from services.headhunter import get_hh_statistics
from utils.display import display_statistics_table


def main():
    languages = ["Python", "C", "C#", "C++", "Java", "JavaScript", "Ruby", "Go", "1С"]

    superjob_statistics = {lang: get_superjob_statistics(lang) for lang in languages}

    headhunter_statistics = {lang: get_hh_statistics(lang) for lang in languages}

    print("\nСтатистика по SuperJob:")
    display_statistics_table(superjob_statistics, "SuperJob Moscow")

    print("\nСтатистика по HeadHunter:")
    display_statistics_table(headhunter_statistics, "HeadHunter Moscow")


if __name__ == "__main__":
    main()
