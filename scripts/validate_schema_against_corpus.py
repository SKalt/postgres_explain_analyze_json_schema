from os import walk
from pathlib import Path

import jsonschema
import yaml
from genson import SchemaBuilder

repo_root = Path(__file__).parent.parent
schema_file = repo_root / Path("schema.yaml")
examples_dir = repo_root / Path("examples")


def main():
    assert schema_file.exists() and schema_file.is_file()
    with open(schema_file) as f:
        schema_json = yaml.safe_load(f)
    validator = jsonschema.Draft7Validator(schema=schema_json)

    assert examples_dir.exists() and examples_dir.is_dir()

    for root, _, files in walk(examples_dir, topdown=True):
        for file in files:
            with open(Path(root).joinpath(file)) as f:
                data = yaml.safe_load(f)
            assert type(data) is list, data
            # for some reason, all the plans are arrays of length 1
            # if len(data) != 1:
            #     print(f"{file}: {len(data)}")
            validator.validate(data)


if __name__ == "__main__":
    main()
