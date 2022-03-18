Header header 

uint32 SOL_STATUS_SOL_COMPUTED = 0
uint32 SOL_STATUS_INSUFFICIENT_OBS = 1
uint32 SOL_STATUS_NO_CONVERGENCE = 2
uint32 SOL_STATUS_COV_TRACE = 4
uint32 SOL_STATUS_INTEGRITY_WARNING = 13
uint32 SOL_STATUS_INVALID_FIX = 19
uint32 SOL_STATUS_UNAUTHORIZED = 20

uint32 PV_TYPE_NONE = 0
uint32 PV_TYPE_FIXEDPOS = 1
uint32 PV_TYPE_FIXEDHEIGHT = 2
uint32 PV_TYPE_DOPPLER_VELOCITY = 8
uint32 PV_TYPE_SINGLE = 16
uint32 PV_TYPE_PSRDIFF = 17
uint32 PV_TYPE_L1_FLOAT = 32
uint32 PV_TYPE_IONOFREE_FLOAT = 33
uint32 PV_TYPE_NARROW_FLOAT = 34
uint32 PV_TYPE_L1_INT = 48
uint32 PV_TYPE_WIDE_INT = 49
uint32 PV_TYPE_NARROW_INT = 50
uint32 PV_TYPE_INS_PSRSP = 53
uint32 PV_TYPE_INS_PSRDIFF = 54
uint32 PV_TYPE_INS_RTKFLOAT = 55
uint32 PV_TYPE_INS_RTKFIXED = 56

# P-sol Status
uint32 psol_status

# Pos Type
uint32 pos_type

# P-XYZ
float64 p_x
float64 p_y
float64 p_z

# P-XYZ-Std
float32 p_x_std
float32 p_y_std 
float32 p_z_std

# V-sol Status
uint32 vsol_status

# Vel Type
uint32 vel_type

# V-XYZ
float64 v_x 
float64 v_y 
float64 v_z 

# V-XYZ-Std
float32 v_x_std
float32 v_y_std
float32 v_z_std

# Stn ID
int8[4] stn_id

# V-Latency
float32 v_latency

# Diff Age
float32 diff_age

# Sol Age
float32 sol_age

# SVs
uint8 svs 

# Soln SVs
uint8 soln_svs

# SolnMultiSVs
uint8 soln_multi_svs

# Reserved
int8 reserved

# Ext Sol Stat
uint8 ext_sol_stat

# Galibeo & Beidou Sig Mask
uint8 galibeo_beidou_sig_mask

# GPS & GLONASS Sig Mask
uint8 gps_glonass_sig_mask