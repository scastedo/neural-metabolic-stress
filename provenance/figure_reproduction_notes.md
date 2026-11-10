# Figure reproduction

Run each notebook's path, import, and style cells first. Raw-data panels also need
their loaders and helper functions. Data are supplied separately; filenames are
listed in [DATA_MANIFEST.json](../DATA_MANIFEST.json), and input directories are
configured as described in the [README](../README.md).

## Inputs by figure

| Notebook | Figures | Inputs |
| --- | --- | --- |
| `data_analysis.ipynb` | Figure 1, Figure 2b–c; ED 1, 2a–b, 4 | Neural recordings and stimulus labels (`data.raw` in the manifest) |
| `data_analysis.ipynb` | ED 2c | `maleMovieData.mat` |
| `data_analysis.ipynb` | ED 7 | `results_all_30_recovery_1_bin.pkl` |
| `data_analysis.ipynb` | Figure 3a | `results_all_30_sated_1_bin_geometry.pkl` |
| `data_analysis.ipynb` | Figure 3b and inset | `results_all_30_sated_1_bin.pkl` |
| `data_analysis.ipynb` | ED 8a–c | SATED/RECOVERY subsample geometry caches |
| `mean_field_figures.ipynb` | Figure 2d–e; ED 8d | None; calculated from model parameters |
| `mean_field_figures.ipynb` | ED 3 | `jun8_overlap_cos2_no_top_mode.npz` |
| `mean_field_figures.ipynb` | ED 6a main | `static_snr_ratio_FR_over_CTR_data.npz` |
| `mean_field_figures.ipynb` | ED 6a insets | Static simulation runs |
| `continuous_attractor_figures.ipynb` | Figure 3c and inset; ED 6b | Dynamic simulation runs |

Static runs need one subfolder per run containing `run_metadata.json` and
`state_history.npy`. Dynamic runs also need `energy_metrics.npy`, or the energy
file named in the run metadata.

Figure 1a shows activity traces. Figure 2a is a schematic.

## Analysis notes

-  Figure 3a and ED 8a–c. Run Setup and the ED 1a recovery-data loader first, then
  enable `RUN_GEOMETRY_CACHE_GENERATION`. Existing output files are not overwritten.
- The Wishart generator belongs to a separate paper and is not included.

Numerical settings are recorded in the notebook code.
