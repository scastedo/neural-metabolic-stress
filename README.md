# Neural mechanisms for resilient sensory computation under metabolic stress

Analysis notebooks and recurrent-network simulations for studying population
coding in mouse visual cortex under food restriction.

[Read the paper](https://doi.org/10.64898/2026.10.29.761790) ·
[Figure guide](provenance/figure_reproduction_notes.md) ·
[Data manifest](DATA_MANIFEST.json)

## Explore the notebooks

| Notebook | Analysis | Figures |
| --- | --- | --- |
| [Data analysis](notebooks/data_analysis.ipynb) | Neural recordings, population geometry, and decoding | 1, 2b–c, 3a–b; ED 1–2, 4, 7, 8a–c |
| [Mean-field models](notebooks/mean_field_figures.ipynb) | Mean-field theory, Wishart results, and temporal averaging | 2d–e; ED 3, 6a, 8d |
| [Continuous-attractor model](notebooks/continuous_attractor_figures.ipynb) | Simulated coding accuracy and energy use | 3c and inset; ED 6b |

ED denotes Extended Data. Figure 2d–e and ED 8d run directly from model parameters.

## Get started

Use **Python 3.12**. From the repository root:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-models.txt
jupyter lab notebooks
```

`requirements-models.txt` installs the analysis packages, PyTorch, and Plotly.
For the experimental-data and mean-field analyses, `requirements.txt` is sufficient.

To reproduce a figure:

1. Supply its inputs using the [figure guide](provenance/figure_reproduction_notes.md).
2. Open the corresponding notebook and run its path, import, and style cells.
3. Run the figure's cells in order, including its data loaders and helper functions.

## Data

Experimental recordings, saved analysis results, and simulation outputs are
supplied separately. For access, contact the corresponding author listed in the
[paper](https://doi.org/10.64898/2026.10.29.761790). Each figure uses a subset of the
files listed in [DATA_MANIFEST.json](DATA_MANIFEST.json).

| Inputs | Default directory | Optional environment variable |
| --- | --- | --- |
| Neural recordings and stimulus labels | `data/raw/` | `CALCIUM_DATA_DIR` |
| Natural-movie recordings | `data/movie/` | `CALCIUM_MOVIE_DIR` |
| Saved analysis results | `data/cache/` | `CALCIUM_CACHE_DIR` |
| Dynamic simulation runs | `data/continuous_attractor/` | `CALCIUM_RUNS_DIR` |
| Static simulation runs | `data/continuous_attractor_static/` | `CALCIUM_STATIC_RUNS_DIR` |

Place inputs in the default folders, or set the environment variables to your
existing data directories before starting Jupyter. Relative paths resolve from the
repository root. Restart the kernel after changing variables. The `data/` folder
is ignored by Git.

Check that the inputs are in place:

```bash
python src/check_inputs.py --section data
python src/check_inputs.py --section models --cached-only
python src/check_inputs.py --section all
```

Missing inputs produce exit status 1. `--cached-only` skips raw simulation runs.
The checker reads file information without running analyses.

Only load trusted input files; some use
[Python pickle](https://docs.python.org/3/library/pickle.html).

## Geometry-cache generation

The final section of `data_analysis.ipynb` computes geometry inputs for Figure 3a
and ED 8a–c. Run Setup and the ED 1a recovery-data loader, then set
`RUN_GEOMETRY_CACHE_GENERATION = True` in that section.

Generation is disabled by default. New files are saved under
`CACHE_DIR / "regenerated_geometry"`, with existing files preserved.

## Simulator

The simulator entry point is [main_gain.py](main_gain.py), with model code in
[src/](src/). Its default output directory is `data/continuous_attractor/`;
use `--outdir` to choose another location.

## Citation

Castedo, S. H., Padamsey, Z., Rochefort, N. L. & Monasson, R. (2026).
*Neural mechanisms for resilient sensory computation under metabolic stress.*
[bioRxiv](https://doi.org/10.64898/2026.10.29.761790).

## Licence

Code and documentation: [MIT](LICENSE). Separately supplied data and numerical
results are outside this code licence. Dependencies retain their own licences.
