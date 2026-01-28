"""
Temperature module:
===================
Converting from C° to F°
"""

def temperature(degrees, unit):
    if unit.lower() == "c":
        return (degrees - 32) * 5/9
    elif unit.lower() == "f":
        return (degrees * 9/5) + 32
    raise ValueError ("Unit must be 'C' or 'F'!")