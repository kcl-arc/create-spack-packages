# er_spack_packages

Making it easier for colleagues to contribute to modules on CREATE HPC (and potentially upstreaming to https://github.com/spack/spack-packages)
as well as encouraging more transparency in module building.

The `production` branch was used for installing the modules that went live with the Alma 10 upgrade on CREATE HPC and has been tagged `v1.2.1`. Ongoing work now targets the `develop` branch (renamed from `production`) ahead of the next release.

## Using with er-spack-development

`er-spack-development` is a repository that allows deployment of Spack packages in a very similar environment to that provided on CREATE HPC. It will be updated to reflect the latest changes in how builds are managed as soon as possible after the impending Alma 10 upgrade is completed.

Currently to use this repo with `er-spack-development` use teh `original_pkgs` branch.

`submit_example.py` in `er-spack-development` reads `package_installs/<package>.yaml` and submits one Slurm job for each entry in `versions[<selected_version>]`.

  - If the `gpus` fag is set, `submit_example.py` uses `--partition interruptible_gpu` and appends `#SBATCH --gres gpu:<gpus>` to `slurm_args`.

**Previous iterations used a `package_installs/<package>.yaml` format, this has now been deprecated for entirely environment based management**
