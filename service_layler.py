import redis


class AlreadyExistException(Exception):
    code = 1


class OneLessThatItWasException(Exception):
    code = 2


def processing(db: redis.Redis, number: int) -> int:
    if db.get(number):
        raise AlreadyExistException('Number already exists')
    elif db.get(number + 1):
        raise OneLessThatItWasException('Number is 1 less than required')

    db.set(number, 'True')

    return number + 1
