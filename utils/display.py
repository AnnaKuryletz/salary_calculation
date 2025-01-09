from terminaltables import AsciiTable


def display_statistics_table(statistics, title):
    table_data = [
        [
            "Язык программирования",
            "Найдено вакансий",
            "Обработано вакансий",
            "Средняя зарплата",
        ]
    ]

    for language, stats in statistics.items():
        table_data.append(
            [
                language,
                stats["vacancies_found"],
                stats["vacancies_processed"],
                stats["average_salary"] or "N/A",
            ]
        )

    table = AsciiTable(table_data)
    table.title = title
    print(table.table)
