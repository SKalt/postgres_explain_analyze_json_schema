import json
from pathlib import Path

import yaml

repo_root = Path(__file__).parent.parent
json_schema_file = repo_root / "schema.json"
if __name__ == "__main__":
    print(yaml.safe_dump(json.loads(json_schema_file.read_text()), indent=2))
