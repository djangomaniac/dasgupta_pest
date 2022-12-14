import random
import string


def random_string_generator(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_order_id_generator(instance):
    order_new_id = random_string_generator().upper()

    class_obj = instance.__class__
    qs_exists = class_obj.objects.filter(uid=order_new_id).exists()
    if qs_exists:
        return unique_order_id_generator(instance)
    return order_new_id
