# 계산기
def add(a, b):
  return a+b
def subtract(a, b):
  return a-b
def multiply(a, b):
  return a*b
def divide(a, b):
  return a/b
def get_median(x):
    # 리스트를 오름차순으로 정렬
    x = sorted(x)
    
    # 리스트의 길이를 계산
    n = len(x)
    
    # 길이가 홀수일 경우, 가운데 값 반환
    if n % 2 == 1:
        return x[n // 2]
    # 길이가 짝수일 경우, 가운데 두 값의 평균 반환
    else:
        return (x[n // 2 - 1] + x[n // 2]) / 2
def get_abs(x):
    if x < 0:
        return -x
    else:
        return x