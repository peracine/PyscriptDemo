from datetime import datetime, timedelta
from typing import Dict
import random
   
def get_timeseries(serie_id: int, start_date: datetime, end_date: datetime) -> Dict[datetime, int]:
    data = {}
    val = serie_id
    while start_date <= end_date:
        val = random.randrange(val, val + 5, 1)
        data[start_date] = val
        start_date += timedelta(days=7)
    
    return data