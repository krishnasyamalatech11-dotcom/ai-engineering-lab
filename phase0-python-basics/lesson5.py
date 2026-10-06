def usage_status(used_pct: float) -> str: 
    """Return OK, WARNING or CRITICAL for a usage percent.""" 
    if used_pct >= 90: 
        return "CRITICAL" 
    if used_pct >= 80: 
        return "WARNING" 
    return "OK"
print(usage_status(92))
print(usage_status(40))