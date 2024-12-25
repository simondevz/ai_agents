import random
import string


def generate_random_string(length=6):
    characters = (
        string.ascii_letters + string.digits
    )  # Includes uppercase, lowercase, and digits
    return "".join(random.choices(characters, k=length)).strip().lower()
