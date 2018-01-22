nums = []

for c in 'Daniel Szekely':
  nums.append(format(ord(c), '02X'))

num_len = len(nums) * 2

number = "0x149814A2 00000000 00000000 51020000"
number = number.replace(' ', '')
number = int(number, 16)

ports = number >> (3 * 4 * 8)
source_port = ports >> 16 & 0xFFFF 
target_port = ports & 0xFFFF

seq_number = number >> (2 * 4 * 8) & 0xFFFFFFFF
ack_number = number >> (1 * 4 * 8) & 0xFFFFFFFF

flags = number & 0xFFFFFFFF
data_offset = (flags & 0xF0000000) >> 28
ns = (flags & 0x0F000000) >> 24

f = (flags & 0x00FF0000) >> 16
cwr = (f & 0x80) >> 7 # 1000 0000 
ece = (f & 0x40) >> 6 # 0100 0000
urg = (f & 0x20) >> 5 # 0010 0000
ack = (f & 0x10) >> 4 # 0001 0000
psh = (f & 0x08) >> 3 # 0000 1000
rst = (f & 0x04) >> 2 # 0000 0100
syn = (f & 0x02) >> 1 # 0000 0010
fin = (f & 0x01) # 0000 0001

print (source_port)
print (target_port)
print (seq_number)
print(ack_number)
print(data_offset)