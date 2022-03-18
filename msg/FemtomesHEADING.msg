Header header
uint32 SOL_STATUS_SOL_COMPUTED = 0
uint32 SOL_STATUS_INSUFFICIENT_OBS = 1
uint32 SOL_STATUS_NO_CONVERGENCE = 2
uint32 SOL_STATUS_COV_TRACE = 4
uint32 SOL_STATUS_INTEGRITY_WARNING = 13
uint32 SOL_STATUS_INVALID_FIX = 19
uint32 SOL_STATUS_UNAUTHORIZED = 20

uint32 P_TYPE_NONE = 0
uint32 P_TYPE_FIXEDPOS = 1
uint32 P_TYPE_FIXEDHEIGHT = 2
uint32 P_TYPE_DOPPLER_VELOCITY = 8
uint32 P_TYPE_SINGLE = 16
uint32 P_TYPE_PSRDIFF = 17
uint32 P_TYPE_L1_FLOAT = 32
uint32 P_TYPE_IONOFREE_FLOAT = 33
uint32 P_TYPE_NARROW_FLOAT = 34
uint32 P_TYPE_L1_INT = 48
uint32 P_TYPE_WIDE_INT = 49
uint32 P_TYPE_NARROW_INT = 50
uint32 P_TYPE_INS_PSRSP = 53
uint32 P_TYPE_INS_PSRDIFF = 54
uint32 P_TYPE_INS_RTKFLOAT = 55
uint32 P_TYPE_INS_RTKFIXED = 56

# Sol stat
uint32 sol_stat

# Pos Type
uint32 pos_type

# Length
float32 length

# Heading
float32 heading

# Pitch
float32 pitch

# Reserved
float32 reserved_1

# HdgStdDev
float32 hgdstddev

# PtchStdDev
float32 ptchstddev

# Stn ID
int8[4] stn_id

# SVs
uint8 svs

# Soln SVs
uint8 soln_svs 

# Obs
uint8 obs

# Multi
uint8 multi

# Reserved
uint8 reserved_2

# Ext Sol Stat
uint8 ext_sol_stat

# Galibeo & Beidou Sig Mask
uint8 galibeo_beidou_sig_mask

# GPS & GLONASS Sig Mask
uint8 gps_glonass_sig_mask