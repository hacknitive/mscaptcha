from random import choices


async def random_code_generator(allowable_charachters: str, number_of_charachters: int):
    return "".join(
        choices(
            population=allowable_charachters,
            k=number_of_charachters,
        )
    )
