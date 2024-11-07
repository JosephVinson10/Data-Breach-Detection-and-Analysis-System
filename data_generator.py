import pandas as pd
import random
from datetime import datetime, timedelta

def generate_data(num_entries=10000):
    # Generate a smaller list of unique users
    user_ids = [f'{1000 + i}' for i in range(250)]  # Unique IDs starting from 1000
    ip_addresses = ['192.168.1.' + str(i) for i in range(1, 200)]  # Expanded IP range
    timestamps = [datetime.now() - timedelta(minutes=random.randint(0, 1440)) for _ in range(num_entries)]
    login_results = [random.choice(['Success', 'Failure']) for _ in range(num_entries)]
    
    data = {
        'user_id': [random.choice(user_ids) for _ in range(num_entries)],
        'timestamp': timestamps,
        'login_result': login_results,
        'ip_address': [random.choice(ip_addresses) for _ in range(num_entries)],
    }
    return pd.DataFrame(data)
