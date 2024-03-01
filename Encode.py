def shift(message, shift_value):
  res = ""

  for car in message:
    res += chr(ord(car) + shift_value)
    
  return res

def xor(message, xor_value):
  res = ""

  for car in message:
    res += chr(ord(car)^xor_value)

  return res