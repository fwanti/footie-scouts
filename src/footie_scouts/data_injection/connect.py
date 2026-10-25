import os
import re
import urllib.parse
from pathlib import Path
from typing import Any, Literal, overload

import pandas as pd
import pyodbc
from dotenv import load_dotenv
from pandas import DataFrame
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import (
    OperationalError,
    ProgrammingError,
    SQLAlchemyError
)

root_dir = Path(__file__).resolve().parents[3]
load_dotenv(root_dir / ".env")

def create_connection(
    conn_name: str = "POSTGRESQL",
    user: str | None = None,
    password: str | None = None,
    hostname: str | None = None,
    db: str | None = None,
    port: int | None = None
):

    user = user or os.getenv("POSTGRES_USER")
    password = password or os.getenv("POSTGRES_PASSWORD")
    hostname = hostname or os.getenv("POSTGRES_HOST")
    db = db or os.getenv("POSTGRES_DB")
    try:
        port = port or os.getenv("POSTGRES_PORT")
    except ValueError:
        raise ValueError(f"INVALID PORT FOR '{conn_name}' CONNECTION")

    if user is None:
        raise ValueError(".ENV ERROR: NO USER FOUND")
    if password is None:
        raise ValueError(".ENV ERROR: NO PASSWORD FOUND")
    if hostname is None:
        raise ValueError(".ENV ERROR: NO HOST FOUND")
    if db is None:
        raise ValueError(".ENV ERROR: NO DATABASE FOUND")


    return create_engine(
        f'postgresql+psycopg2://{user}:{password}@{hostname}:{port}/{db}'
    )


ParamsType = dict[str, Any] | list[dict[str, Any]]
def run_query(
        engine, 
        query,
        params: ParamsType | None = None,
        generate_df=True):

        with engine.begin() as conn:
            result = conn.execute(text(query), params or {})
            if generate_df and result.returns_rows:
                return pd.DataFrame(result.mappings().all())
            return None

engine = create_connection()
df = run_query(engine, "SELECT 1")
print(df)