# create-spack-packages

Making it easier for colleagues to contribute to modules on CREATE HPC (and potentially upstreaming to https://github.com/spack/spack-packages)
as well as encouraging more transparency in module building.

The tag `v1.2.1` is the current position used for installing the modules AlmaLinux 10 nodes on CREATE HPC. Ongoing work now targets the `develop` branch (renamed from `production`) ahead of the next release.

## Using with create-spack-development

`create-spack-development` is a repository that allows deployment of Spack packages in a very similar environment to that provided on CREATE HPC.

Instructions are available on the README.md in that repo.

## Local versions of upstream packages

Most packages come from Spack's builtin repository ([spack-packages](https://github.com/spack/spack-packages)), pinned to the `v2026.06.0` release. Some packages in this repo have the same name as a builtin one (e.g. `py-tensorflow`, in `py_tensorflow/`). `local_packages` is listed before `builtin` in `repos.yaml`, so the local recipe replaces the builtin one completely.

We keep a local version when one of these applies:

- **We need a newer version.** The builtin repo is pinned to a release, so versions added upstream since then, or never added, go here. Some recipes are copied from the upstream `develop` branch and say so at the top of the file (e.g. `fox`, `opencarp`, `sumo`). Other examples: `cellranger`, `dorado`, `gcta`, `rstudio`, `seqtk`.
- **It doesn't build here.** Upstream recipes are often tested with only one toolchain, and fail with our compilers, CUDA or Python versions, or CPU targets. Examples: `py-ml-dtypes` (GCC 13+ with `-march=sapphirerapids`), `namd` (CUDA 13 and GCC 14), `lammps` (CUDA driver stub not found), `mysql` (ABI check fails outside Oracle's toolchain), `blast-plus`, `bowtie2`, `py-boto`.
- **It's licensed or restricted software.** The upstream recipes expect you to download the file yourself and put it in the current directory or a mirror. Ours fetch it from the cluster's local software store, where access is controlled: `aretomo`, `cellranger`, `gurobi`, `motioncor2`, `namd`, `orca`, `spaceranger`, `xplor-nih`.
- **It has to behave differently on the cluster.** Examples: `quantum-espresso` (adds `cuda_arch`, because build nodes have no GPU to detect), `py-triton` (limits parallel compile jobs to Spack's `-j` rather than every core on the node), `rstudio` (server build with a PAM helper).
- **It was carried over from the previous build system.** A few recipes (e.g. `kraken2`, `psi4`, `regenie`) predate the current upstream recipe and have drifted from it.

### Example: `py-tensorflow`

TensorFlow is tested upstream with clang. We build it with GCC, for several Intel and AMD CPU generations and for GPUs up to Blackwell. For 2.20, the local recipe:

- sets TensorFlow's own downloaded ("hermetic") CUDA to 12.8.1. The default, 12.5.1, can't parse GCC 14's headers or target `sm_100`.
- keeps the runtime CUDA at 12 (`cuda@:12`), because TensorFlow loads `libcudart.so.12` and our environments otherwise prefer CUDA 13.
- turns off XNNPACK's AVX-VNNI-INT8 kernels with GCC 12, which doesn't support `-mavxvnniint8`. None of our GCC 12 targets have that instruction set.
- adds two source patches that GCC needs and clang doesn't: a backport of [tensorflow/tensorflow#125229](https://github.com/tensorflow/tensorflow/pull/125229), and a GCC 12 fix in XLA that isn't upstream yet.

### Keeping them in step

A local version doesn't pick up upstream fixes. Comment each change with the reason, as `py-tensorflow` does. When the builtin pin moves, check whether each local version is still needed and delete it once upstream has caught up. Where a fix would help others, consider contributing it to spack-packages.
