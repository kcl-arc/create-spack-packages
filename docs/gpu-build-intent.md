# GPU build intent in er-spack-packages

Use `package_installs/*.yaml` to express whether a package should be built with GPU support.

## Policy

- Keep GPU build intent here (`+cuda`, optional package-specific flags).
- Do not hard-code one global `cuda_arch` for all workloads.
- Let environment overlays in `er-spack-environments` choose preferred `cuda_arch` and CUDA toolkit per GPU family.

## Example

```yaml
versions:
  "20250722":
    - "+cuda"
```

If a package cannot build without a specific CUDA architecture, note that explicitly in comments and keep that exception local to the package.
