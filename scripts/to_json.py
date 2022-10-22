import json
from pathlib import Path

import yaml

repo_root = Path(__file__).parent.parent
yaml_schema_file = repo_root / "schema.yaml"
if __name__ == "__main__":
    with open(yaml_schema_file) as f:
        print(json.dumps(yaml.safe_load(f), indent=2))
