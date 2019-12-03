import redis


class AlreadyExistException(Exception):
    code = 1


class OneLessThatItWasException(Exception):
    code = 2


def _do(p: redis.client.Pipeline, number):
    p.watch(number)
    if p.get(number):
        raise AlreadyExistException('Number already exists')
    elif p.get(number + 1):
        raise OneLessThatItWasException('Number is 1 less than required')
    p.execute()
    p.unwatch()
    p.set(number, 'True')
    p.execute()


def processing(db: redis.Redis, number: int) -> int:
    with db.pipeline(transaction=True) as p:
        try:
            _do(p, number)
        except redis.WatchError:
            _do(p, number)

    return number + 1
