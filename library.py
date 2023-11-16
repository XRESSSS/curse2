def can_drive_car(age: int) -> bool:
    if age < 1:
        raise ValueError("иди отсуда розбійник")
    if age > 130:
        raise ValueError("Я сказав іди звідси")
    print(f"{age+50=}")

    list_var = [
        "1111111",
        "7678678",
    ]
    # if age > 18:
    #     return True
    # return False
    return age > 18
