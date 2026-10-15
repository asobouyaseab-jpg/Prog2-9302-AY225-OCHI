import math
import random
import time

grades_dict = {
                "Dwein": 80,
                "Seagal": 85,
                "Arnold": 90,
                "Statham": 60,
                "Randy": 65
                }


for name, grades in grades_dict.items():
  if grades >= 85:
    print(name)