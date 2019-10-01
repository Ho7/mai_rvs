import redis


class AlreadyExistException(Exception):
    code = 1


class OneLessThatItWasException(Exception):
    code = 2


def processing(db: redis.Redis, number: int) -> int:
    if db.get(number):
        raise AlreadyExistException('Число уже было')
    elif db.get(number + 1):
        raise OneLessThatItWasException('Число на единицу меньше обработаннаго')

    db.set(number, 'True')

    return number + 1
