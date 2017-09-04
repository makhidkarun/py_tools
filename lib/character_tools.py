import random

def roll_upp():
  return [random.randint(1,6) + random.randint(1,6) for _ in range(6)]
