def predict_rub_salary_for_superjob(vacancy):
    payment_from = vacancy.get("payment_from")
    payment_to = vacancy.get("payment_to")
    currency = vacancy.get("currency")

    if currency != "rub":
        return None

    if payment_from and payment_to:
        return (payment_from + payment_to) / 2
    elif payment_from:
        return payment_from * 1.2
    elif payment_to:
        return payment_to * 0.8
    else:
        return None


def predict_rub_salary_for_hh(salary):
    if not salary or salary["currency"] != "RUR":
        return None

    payment_from = salary.get("from")
    payment_to = salary.get("to")

    if payment_from and payment_to:
        return (payment_from + payment_to) / 2
    elif payment_from:
        return payment_from * 1.2
    elif payment_to:
        return payment_to * 0.8
    else:
        return None
