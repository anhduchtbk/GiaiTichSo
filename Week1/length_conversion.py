def length_conversion(m):
    print(meterToinch(m), "inch,", meterTofoot(m), "feet,", meterTomile(m), "mile")

# 1inch <=> 0.0254m
def meterToinch(m):
    return float(m / 0.0254)

# 12inch <=> 1f
def meterTofoot(m):
    return float(meterToinch(m) / 12)

# 1yard <=> 3f
def meterToyard(m):
    return float(meterTofoot(m) / 3)

# 1mile <=> 1760yard
def meterTomile(m):
    return float(meterToyard(m) / 1760)

length_conversion(640)