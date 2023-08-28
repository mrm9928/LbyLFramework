# LbyLFramework

## Output Directories Structure
For each TRExFit object, a directory is created, with the same name as the Fit Name.
Inside this directory, at every step, some outputs are created, following the structure described above:

| **Folder** | **Content** |
| ---------- | ----------- |
| `Plots/`              | data/MC plots, pre- and post-fit, for all the Signal, Control and Validation regions, including the summary plots |
| `Tables/`             | tables in txt and tex format |
| `RooStats/`           | workspace(s) and the xmls |
| `Fits/`               | output from fits |
| `Limits/`             | outputs from the limit-setting code |
| `Significance/`       | outputs from the significance code |
| `Systematics/`        | plots for the syst variations |
| `Toys/`               | plots and ROOT files with pseudoexperiments output |
| `Histograms/`         | root file(s) with all the inputs |
| `LHoodPlots/`         | likelihood scan with respect to the specified parameter |
| `UnfoldingHistograms/`| folded histograms produced during `u` step |
