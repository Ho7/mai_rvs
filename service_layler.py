import redis


class AlreadyExistException(Exception):
    pass


class OneLessThatItWasException(Exception):
    pass


def check_number(db: redis.Redis, number: int) -> bool:
    if db.get(number):
        raise AlreadyExistException('Число уже было')
    elif db.get(number + 1):
        raise OneLessThatItWasException('Число на единицу меньше обработаннаго')

    return True
