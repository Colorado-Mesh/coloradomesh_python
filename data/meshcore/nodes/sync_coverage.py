import argparse
import json

import objectrest

MESHMAPPER_COVERAGE_URL = "https://co.meshmapper.net/?ajax=1&request=map_data"  # Coverage in Denver region

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cache MeshCore coverage in Denver.")
    parser.add_argument(
        "--coverage-data-file",
        type=str,
        help="Path to the data file to store coverage information.",
        required=True
    )
    args = parser.parse_args()

    data_file = args.coverage_data_file

    print("Caching coverage...")

    # For now, no processing of data here (done by library at runtime), simply cache the API response JSON
    data: list[dict] = objectrest.get_json(url=MESHMAPPER_COVERAGE_URL)  # type: ignore
    with open(data_file, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
