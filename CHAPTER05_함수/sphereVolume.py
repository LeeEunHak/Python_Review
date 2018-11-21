#구의 부피를 계산하는 함수

import math

def sphereVolume(radius):
    volume = (4.0 / 3.0) * math.pi * radius * radius * radius
    return volume

radius = float(input("구의 반지름을 입력하세요: "))

print(sphereVolume(radius))
