# er_spack_packages

Making it easier for colleagues to contribute to modules on CREATE HPC (and potentially upstreaming to https://github.com/spack/spack-packages)
as well as encouraging more transparency in module building.

The `production` branch is currently used for installing the next iteration of modules on CREATE HPC that will become live when CREATE is updated to Ubuntu 24.04. The produciton branch will then become `v1.1.1` and it is anticipated htat a new branch (e.g. `v1.2.1` will be created for the next iteration of Spack packages).

## `package_installs/<package>.yaml` format

Supported keys:

- `versions` (required): mapping of version string to a list of *flag entries*.
  - Example: `versions: { "1.3": ["", "^mpi@4.1.5", "+feature=on"] }`
  - The empty string `""` means “no extra flags”.
- `archs` (optional): list of allowed architectures (e.g. `["zen2", "zen4"]`).
  - If `--arch` is omitted, it is inferred from the host CPU; this is then validated against `archs` when present.
- `gpus` (optional): integer number of GPUs for the job.

The following keys are expected but not interpreted specially by this repo:
- the flag strings are appended directly after `target=<arch>` in the rendered `spack install` command.

## Using with er-spack-development

`er-spack-development` is a repository that allows deployment of Spack packages in a very similar environment to that provided on CREATE HPC.

`submit_example.py` in `er-spack-development` reads `package_installs/<package>.yaml` and submits one Slurm job for each entry in `versions[<selected_version>]`.

  - If the `gpus` fag is set, `submit_example.py` uses `--partition interruptible_gpu` and appends `#SBATCH --gres gpu:<gpus>` to `slurm_args`.
