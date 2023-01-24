import logging
import employee
from employee import logger 

# logging levels
# 1. debug
# 2. info
# 3. warning
# 4. error
# 5. critical

"""

logging.basicConfig(filename='test.log',level=logging.DEBUG)

"""

def add(x, y):
    return x + y



def subtract(x,y):
    return x - y



def multiply(x, y):
    return x * y


def divide(x, y ):
    return x / y


num_1 = 10
num_2 = 5


add_result = add(num_1, num_2)
logger.info('Add: {} + {} = {}'.format(num_1, num_2 , add_result))
sub_result = subtract(num_1, num_2)
logger.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
mul_result = multiply(num_1, num_2)
logger.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
div_result = divide(num_1, num_2)
logger.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))
