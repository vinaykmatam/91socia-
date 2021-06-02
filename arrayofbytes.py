import array
import binascii
org_array = array.array('i', [1,2,3,4,5,6])
print('original array', org_array)
bytes_array = org_array.tobytes()
print('Array of bytes:', binascii.hexlify(bytes_array))
