# https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python

def is_valid_IP(strng):
    parts = strng.split(".")
    if len(parts) != 4:
        return False
    for group in parts:
        if not group.isdigit() or group != str(int(group)) or not 0 <= int(group) <= 255:
            return False
    return True


print(is_valid_IP('12.255.56.1'))
print(is_valid_IP('0.34.82.53'))
print(is_valid_IP('192.168.1.300'))
print(is_valid_IP(''))
print(is_valid_IP('abc.def.ghi.jkl'))
print(is_valid_IP('123.456.789.0'))
