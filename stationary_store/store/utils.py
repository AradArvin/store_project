import random

def generate_otp() -> int:
    otp = random.randint(1000,9999)
    print(f"Your otp is {otp}")
    return otp

