# Figure inputs, settings, and validation

The analysis and plotting code is retained; all data and numerical caches are
supplied separately. Input filenames and default locations are listed in
`../DATA_MANIFEST.json`. Configure directories using the environment variables
in `../README.md`.

## Figure mapping

| Notebook | Panels | Inputs |
| --- | --- | --- |
| `data_analysis.ipynb` | Figure 1; ED 1; Figure 2b–c; ED 4 | Experimental traces and stimulus metadata |
| `data_analysis.ipynb` | ED 2a–b | Experimental traces and stimulus metadata |
| `data_analysis.ipynb` | ED 2c | `maleMovieData.mat` |
| `data_analysis.ipynb` | ED 7 | `results_all_30_recovery_1_bin.pkl` |
| `data_analysis.ipynb` | Figure 3a | `results_all_30_sated_1_bin_geometry.pkl` |
| `data_analysis.ipynb` | Figure 3b and inset | `results_all_30_sated_1_bin.pkl` |
| `data_analysis.ipynb` | ED 8a–c | SATED/RECOVERY subsample geometry caches |
| `mean_field_figures.ipynb` | Figure 2d–e; ED 8d | Model parameters; no external data |
| `mean_field_figures.ipynb` | ED 3a–b | `jun8_overlap_cos2_no_top_mode.npz` |
| `mean_field_figures.ipynb` | ED 6a main | `static_snr_ratio_FR_over_CTR_data.npz` |
| `mean_field_figures.ipynb` | ED 6a covariance insets | Static state histories and run metadata |
| `continuous_attractor_figures.ipynb` | Figure 3c, its inset, and ED 6b | Dynamic state histories, energy metrics, and run metadata |

Figure 1a includes the activity traces; assembled illustrations and manual
annotations are omitted. Figure 2a is an illustration with no numerical plotting
section. Source notebook names and zero-based source-cell indices remain recorded
in notebook cell metadata.

## Scientific settings

- ED 7 uses recovery sessions following two weeks of ad libitum feeding. Dashed
  FR/CTR curves are animal means, with animal SEM shading and 50-ms bins.
- ED 3 uses the original 39-mode means and SEM arrays. Its Wishart-generation code
  belongs to a separate paper and is outside this release's scope.
- ED 6a retains the six plotted durations of 30, 60, 90, 120, 150, and 180 ms and
  the original sign convention. Covariance insets use `AVERAGE_SIZES=[25,100]`,
  converted to 75 and 300 ms, with `AMPAR=1.0`, `RIN=1.0`, `TEMP=0.02`,
  `ETA=0.02`, `THETA=0.01`, and `IDIR=0.5`. The main-curve cache compares
  CTR `(AMPAR,RIN)=(1.0,1.0)` with FR `(0.71,1.22)` at directions 0.5 and 0.52.
  The slow raw-data SNR sweep is not included in the default plotting path.
- Dynamic plots retain CTR `(AMPAR,RIN)=(1.0,1.0)`, FR `(0.71,1.22)`, and
  FR-alternative `(0.86,1.0)`, along with the source time conventions. Exact
  historical simulation commands, settings, seeds, and trial metadata must be
  supplied separately.
- Optional geometry-cache generation covers Figure 3a and ED 8a–c. It retains
  30-degree separation, frames 40–80, 1-frame bins at 20 Hz, 13 covariance modes,
  `MIN_EVAL=1e-14`, `ALPHA=1.0`, `RNG_SEED=1`, and five spatial frequencies.
  Subsampling uses up to 50 neurons, limited by the smallest available animal,
  with 50 repeats; all-neuron analysis uses one repeat. Generation is disabled
  by default and writes new files under `regenerated_geometry/`.

## Validation limits

The ED 6a main curve was previously replotted from the original saved data and its
six selected points agreed. Static covariance-inset processing, the slow SNR sweep,
dynamic analyses, and simulation generation have not been validated in this release.
The optional geometry-cache calculation has been checked statically; numerical
equality with historical caches remains unchecked. It does not recover the exact
generators of the non-geometry caches for Figure 3b, its inset, or ED 7.

A clean end-to-end run in the release environment and comparison with the paper
remain necessary once the external inputs and original run settings are available.
