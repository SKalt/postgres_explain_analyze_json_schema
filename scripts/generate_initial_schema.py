from os import walk
from pathlib import Path

import yaml
from genson import SchemaBuilder

examples_dir = Path(__file__).parent.parent / Path("examples")


def main():
    assert examples_dir.exists() and examples_dir.is_dir()
    builder = SchemaBuilder()
    builder.add_schema({"type": "object", "properties": {}})
    for root, _, files in walk(examples_dir, topdown=True):
        for file in files:
            with open(Path(root).joinpath(file)) as f:
                data = yaml.safe_load(f)
                assert type(data) is list, data
                for i in data:
                    builder.add_object(i)
    print(builder.to_json(indent=2))


if __name__ == "__main__":
    main()
