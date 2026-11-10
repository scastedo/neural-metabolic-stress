# Paper figure analysis and simulation code

Three notebooks reproduce the paper's analysis and plots, accompanied by the
continuous-attractor simulator, plotting style, dependency lists, and an input manifest.
**No experimental data, stimulus metadata, numerical caches, or simulation outputs
are included.** These inputs are available from the author on request.

## Contents

| Location | Purpose |
| --- | --- |
| `notebooks/data_analysis.ipynb` | Experimental-data analysis, figure plots, and optional geometry-cache generation |
| `notebooks/mean_field_figures.ipynb` | Mean-field/Wishart plots and ED 6a analysis |
| `notebooks/continuous_attractor_figures.ipynb` | Figure 3c, its inset, and ED 6b analysis/plots |
| `src/` and `main_gain.py` | Simulator, portable input paths, and input checker |
| `styles/` | Paper plotting style |
| `DATA_MANIFEST.json` | Required input filenames, expected locations, sizes, and available checksums |
| `provenance/` | Figure mapping, scientific settings, validation limits, and recorded package versions |

## Install and open

Use Python 3.12. From this folder:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-models.txt
jupyter lab notebooks
```

`requirements-models.txt` includes the base packages plus PyTorch for the simulator
and Plotly for simulator visualisation. `requirements.txt` covers the data notebook
and NumPy/SciPy model sections. Package pins were recorded from existing environments;
the combined environment has not been freshly installed and tested.

## Supply the inputs

`DATA_MANIFEST.json` lists the required files. Create the indicated `data/`
subfolders locally and add the inputs, or configure existing directories before
starting the notebook kernel:

```bash
export CALCIUM_DATA_DIR="/path/to/experimental_data"
export CALCIUM_CACHE_DIR="/path/to/analysis_caches"
export CALCIUM_MOVIE_DIR="/path/to/movie_data"
export CALCIUM_RUNS_DIR="/path/to/dynamic_simulation_runs"
export CALCIUM_STATIC_RUNS_DIR="/path/to/static_simulation_runs"
```

These paths are read by `src/reproduction_paths.py` when a notebook imports it.
Restart the kernel after changing them. Without overrides, inputs are expected
under this repository's `data/` directory. Relative overrides are resolved from
the repository root. The entire `data/` directory is ignored by Git.

Check file presence without loading arrays or running analyses:

```bash
python src/check_inputs.py --section all
python src/check_inputs.py --section data
python src/check_inputs.py --section models
python src/check_inputs.py --section models --cached-only
python src/check_inputs.py --section static
python src/check_inputs.py --section continuous-attractor
```

The checker reports missing inputs and exits with status 1 until they are supplied.
`--cached-only` skips checks for raw simulation run folders; it still requires the
listed plotting inputs. The checker does not validate data contents or dependencies.

## Run the figures

Start each notebook with its path-setup and import cells, then run the relevant
analysis cells in order. All stored notebook outputs are cleared.

- Figure 2d–e and ED 8d in `mean_field_figures.ipynb` compute their results from
  model parameters and do not need external data.
- ED 3 needs `jun8_overlap_cos2_no_top_mode.npz` in `CALCIUM_CACHE_DIR` (default:
  `data/cache/`). Its Wishart-generation code belongs to a separate paper and is
  outside this release's scope.
- ED 6a's main curve needs `static_snr_ratio_FR_over_CTR_data.npz` in the same cache
  directory. Its covariance insets additionally need static run folders containing
  `run_metadata.json` and `state_history.npy`.
- Experimental-data figures need the raw data, stimulus metadata, movie data, and/or
  analysis caches listed in the manifest and figure notes.
- Figure 3c and ED 6b need dynamic run folders containing `run_metadata.json`,
  `state_history.npy`, and `energy_metrics.npy` (or the energy path recorded in metadata).

The final optional section of `data_analysis.ipynb` contains the geometry-cache
calculation for Figure 3a and ED 8a–c. Run the Setup cells and recovery-data loader
under ED Figure 1a, then that section. `RUN_GEOMETRY_CACHE_GENERATION` defaults to
`False`; when enabled, results go under `CACHE_DIR / "regenerated_geometry"`
without overwriting existing files. Exact equality with historical caches has not
been checked. This section does not provide the exact generators of the different
non-geometry caches used by Figure 3b, its inset, and ED 7.

## Simulator and validation

`main_gain.py` defaults to writing under `data/continuous_attractor`, relative to
the working directory. Use `--outdir` to choose another location. Obtain the original
paper settings and seed/trial metadata before attempting to reproduce simulations;
the simulator defaults do not constitute that record.

See `provenance/figure_reproduction_notes.md` for the figure mapping, retained settings,
and validation limits. A full clean run and comparison with the paper still require
the external inputs and original simulation settings. Add the manuscript citation
and DOI when available.

## Licence

The source code and documentation use the [MIT License](LICENSE), credited to the
neural-metabolic-stress contributors. Separately supplied experimental data, caches,
and simulation outputs are outside this code licence. Dependencies retain their
own licences.
