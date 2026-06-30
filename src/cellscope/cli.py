import json


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="cellscope")
    sub = parser.add_subparsers(dest="command", required=True)

    inspect = sub.add_parser("inspect", help="Inspect pipeline e2e")
    inspect.add_argument("--input", required=True, type=Path)
    args = parser.parse_args(argv)

    if args.command == "inspect":
        adata = io.read_file(args.input)
        validated_adata = validation.validate_adata(adata)
        print(f"Validation summary: {validated_adata}")
        print(json.dumps(validated_adata, indent=1))
    return 0