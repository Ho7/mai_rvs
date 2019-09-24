import redis


class AlreadyExistException(Exception):
    pass


class OneLessThatItWasException(Exception):
    pass


def processing(db: redis.Redis, number: int) -> int:
    if db.get(number):
        raise AlreadyExistException('Число уже было')
    elif db.get(number + 1):
        raise OneLessThatItWasException('Число на единицу меньше обработаннаго')

    db.set(number, 'True')

    return number + 1
