# er_spack_packages

Making it easier for colleagues to contribute to modules on CREATE HPC (and potentially upstreaming to https://github.com/spack/spack-packages)
as well as encouraging more transparency in module building.

## `package_installs/<package>.yaml` format

`submit_example.py` reads `package_installs/<package>.yaml` and submits one Slurm job for each entry in `versions[<selected_version>]`.

Supported keys:

- `versions` (required): mapping of version string to a list of *flag entries*.
  - Example: `versions: { "1.3": ["", "^mpi@4.1.5", "+feature=on"] }`
  - The empty string `""` means “no extra flags”.
- `archs` (optional): list of allowed architectures (e.g. `["zen2", "zen4"]`).
  - If `--arch` is omitted, it is inferred from the host CPU; this is then validated against `archs` when present.
- `gpus` (optional): integer number of GPUs for the job.
  - If set, `submit_example.py` uses `--partition interruptible_gpu` and appends `#SBATCH --gres gpu:<gpus>` to `slurm_args`.

The following keys are expected but not interpreted specially by this repo:
- the flag strings are appended directly after `target=<arch>` in the rendered `spack install` command.
