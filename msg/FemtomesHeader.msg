# On the wire, this header is preceeded by three sync bytes, which are 0xAA
# 0x44 0x12, and a uint8 which is the header length.

# Message ID
uint16 message_id

# Message Type
int8 message_type

# Reserved
uint8 reserved_1

# Message Length
uint16 message_length

# Reserved
uint16 reserved_2

# Idle Time
uint8 idle_time

# Time Status
uint8 TIME_STATUS_UNKNOWN = 20
uint8 TIME_STATUS_APPROXIMATE = 60
uint8 TIME_STATUS_COARSE = 100
uint8 TIME_STATUS_COARSESTEERING = 120
uint8 TIME_STATUS_FINE = 160
uint8 TIME_STATUS_FINESTEERING = 180
uint8 TIME_STATUS_SATTIME = 200
uint8 time_status

# Week
uint16 week

# ms
uint32 ms

# Receiver Status
uint32 receiver_status

# Reserved
uint16 reserved_3

# FWVersion
uint16 fwversion



