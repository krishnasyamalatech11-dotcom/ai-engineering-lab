from dataclasses import dataclass
@dataclass
class Tablespace: 
    name: str 
    size_gb: float 
    used_gb: float 
    def used_pct(self) -> float: 
        return round(self.used_gb / self.size_gb * 100, 1)
ts = Tablespace("USERS", 50, 46)
print(ts, ts.used_pct())