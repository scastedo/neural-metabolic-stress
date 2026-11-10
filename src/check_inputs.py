"""Check input-file presence without loading arrays, fitting, plotting, or simulating."""
import argparse
import json
from pathlib import Path

from reproduction_paths import BUNDLE_ROOT, CANN_RUNS_DIR, CANN_STATIC_RUNS_DIR, INPUT_DIRS


def check_simulation_runs(runs_dir=CANN_RUNS_DIR, require_energy=True):
    metadata_files = sorted(runs_dir.glob("*/run_metadata.json"))
    if not metadata_files:
        required = "run_metadata.json and state_history.npy"
        if require_energy:
            required += ", plus energy_metrics.npy or its recorded metadata path"
        return {"ok": False, "directory": str(runs_dir), "run_count": 0,
                "missing": [f"Run subfolders containing {required} are required."]}
    missing = []
    for metadata_file in metadata_files:
        folder = metadata_file.parent
        if not (folder / "state_history.npy").is_file():
            missing.append(str(folder / "state_history.npy"))
        try:
            metadata = json.loads(metadata_file.read_text())
        except (OSError, ValueError) as error:
            missing.append(f"Unreadable metadata {metadata_file}: {error}")
            continue
        if require_energy:
            recorded_path = metadata.get("network_params", {}).get("energy_metrics_path")
            recorded_exists = bool(recorded_path) and Path(recorded_path).is_file()
            if not recorded_exists and not (folder / "energy_metrics.npy").is_file():
                missing.append(str(folder / "energy_metrics.npy"))
    return {"ok": not missing, "directory": str(runs_dir),
            "run_count": len(metadata_files), "missing": missing}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--section", choices=["all", "data", "models", "static", "continuous-attractor"], default="all")
    parser.add_argument("--cached-only", action="store_true",
                        help="Check the listed files without requiring raw dynamic or static simulation run folders.")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    manifest = json.loads((BUNDLE_ROOT / "DATA_MANIFEST.json").read_text())
    rows = []
    for item in manifest["inputs"]:
        if args.section != "all" and args.section not in item["sections"]:
            continue
        path = INPUT_DIRS[item["path_group"]] / item["relative_path"]
        rows.append({"path": str(path), "present": path.is_file(),
                     "included_in_bundle": item["included_in_bundle"]})
    simulation = (check_simulation_runs()
                  if not args.cached_only and args.section in ["all", "continuous-attractor"] else None)
    static_simulation = (check_simulation_runs(CANN_STATIC_RUNS_DIR, require_energy=False)
                         if not args.cached_only and args.section in ["all", "models", "static"] else None)
    ok = (all(row["present"] for row in rows)
          and (simulation is None or simulation["ok"])
          and (static_simulation is None or static_simulation["ok"]))
    report = {"ok": ok, "section": args.section, "cached_only": args.cached_only,
              "files": rows, "simulation_runs": simulation, "static_simulation_runs": static_simulation}
    if args.as_json:
        print(json.dumps(report, indent=2))
    else:
        for row in rows:
            print(f"{'FOUND' if row['present'] else 'MISSING'}  {row['path']}")
        if simulation is not None:
            print(f"Simulation runs: {simulation['run_count']} metadata files under {simulation['directory']}")
            for missing in simulation["missing"]:
                print(f"MISSING  {missing}")
        if static_simulation is not None:
            print(f"Static runs (ED 6a insets): {static_simulation['run_count']} metadata files under {static_simulation['directory']}")
            for missing in static_simulation["missing"]:
                print(f"MISSING  {missing}")
        print("Inputs available." if ok else "Some inputs must be supplied or configured; no analysis was run.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
