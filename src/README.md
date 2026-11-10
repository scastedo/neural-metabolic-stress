# Source code

`network.py`, `simulator.py`, `update_strategies.py`, `visualisation.py`, and
`__init__.py`, plus `../main_gain.py`, provide the continuous-attractor simulator.
The default output directory is `data/continuous_attractor`, relative to the working
directory; use `--outdir` to choose another location. Exact paper run settings and
seed/trial metadata must be supplied separately.

`reproduction_paths.py` is the portable directory configuration used by the notebooks.
`check_inputs.py` checks file presence using only the standard library. Neither helper
imports or executes the simulator when used as documented.

No input data or numerical caches are distributed with the code. The notebooks
retain their analysis and plotting code for use with separately supplied inputs.
