# er_spack_packages

Making it easier for colleagues to contribute to modules on CREATE HPC (and potentially upstreaming to https://github.com/spack/spack-packages)
as well as encouraging more transparency in module building.

The `production` branch is currently used for installing the next iteration of modules on CREATE HPC that will become live when CREATE is updated to Alma 10. The produciton branch will then become `v1.2.1` and it is anticipated that a new branch (e.g. will be created for the next iteration of Spack packages).

## Using with er-spack-development

`er-spack-development` is a repository that allows deployment of Spack packages in a very similar environment to that provided on CREATE HPC.

`submit_example.py` in `er-spack-development` reads `package_installs/<package>.yaml` and submits one Slurm job for each entry in `versions[<selected_version>]`.

  - If the `gpus` fag is set, `submit_example.py` uses `--partition interruptible_gpu` and appends `#SBATCH --gres gpu:<gpus>` to `slurm_args`.

**Previous iterations used a `package_installs/<package>.yaml` format, this has now been deprecated for entirely environment based management**
