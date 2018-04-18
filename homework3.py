import pandas as pd
import sqlite3
import os.path

def create_dataframe(db_path):
    if not os.path.exists(db_path):
        raise ValueError("Invalid Path")
    else:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("""
        SELECT video_id, category_id, 'US' as language
        FROM USvideos
        UNION
        SELECT video_id, category_id, 'GB' as language
        FROM GBvideos
        UNION
        SELECT video_id, category_id, 'FR' as language
        FROM FRvideos
        UNION
        SELECT video_id, category_id, 'DE' as language
        FROM DEvideos
        UNION
        SELECT video_id, category_id, 'CA' as language
        FROM CAvideos;
        """, conn)
        return df