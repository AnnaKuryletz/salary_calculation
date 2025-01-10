def predict_rub_salary(payment_from, payment_to, currency, expected_currency):
    if currency != expected_currency:
        return None

    if payment_from and payment_to:
        return (payment_from + payment_to) / 2
    elif payment_from:
        return payment_from * 1.2
    elif payment_to:
        return payment_to * 0.8
    else:
        return None


def predict_rub_salary_for_superjob(vacancy):
    return predict_rub_salary(
        payment_from=vacancy.get("payment_from"),
        payment_to=vacancy.get("payment_to"),
        currency=vacancy.get("currency"),
        expected_currency="rub",
    )


def predict_rub_salary_for_hh(salary):
    if not salary:
        return None

    return predict_rub_salary(
        payment_from=salary.get("from"),
        payment_to=salary.get("to"),
        currency=salary.get("currency"),
        expected_currency="RUR",
    )
