import flask
import math
import json
from concurrent.futures import ProcessPoolExecutor

app = flask.Flask(__name__)


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    sqrt_number = int(math.floor(math.sqrt(number)))
    for i in range(3, sqrt_number + 1, 2):
        if number % i == 0:
            return False
    return True


@app.route("/is_prime/<number>")
def api_is_prime(number):
    number_list = [int(x) for x in number.split(",")]
    result = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, result)))


if __name__ == "__main__":
    process_pool = ProcessPoolExecutor()
    app.run()

