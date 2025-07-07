import json
from pathlib import Path

DB_FILE = Path(__file__).parent / 'data' / 'banco.json'


def load_db():
    if DB_FILE.exists():
        with open(DB_FILE) as f:
            return json.load(f)
    return {'usuarios': [], 'estoque': [], 'pedidos': []}


def save_db(db):
    DB_FILE.write_text(json.dumps(db, indent=2, ensure_ascii=False))