from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *

class PyBoltz(PythonPackage):
    """Boltz is a family of models for biomolecular interaction prediction.
    Boltz-2 is the first deep learning model to approach the accuracy of physics-based free-energy perturbation (FEP) methods.
    Citation: Saro Passaro, et al., Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction
    bioRxiv 2025.06.14.659707; doi: https://doi.org/10.1101/2025.06.14.659707"""

    # url for the package's homepage here.
    homepage = "https://github.com/jwohlwend/boltz"
    pypi = "boltz/boltz-2.2.1.tar.gz"

    # Maintainer information
    maintainers("paulynamagana")

    version("2.2.1", sha256="355a033ce2b49543a927470d585136794521d8639b2eeb5a1818d74dc3e513c3")
    variant("cuda", default=True, description="Enable GPU support via CUDA")

    # License
    license("MIT", checked_by="paulynamagana")

    # Opython/pip/wheel dependencies
    depends_on("python@3.10:3.12", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")

    # dependencies on the CUDA toolkit
    depends_on("py-torch@2.2:+cuda", when="+cuda")
    depends_on("py-torch@2.2:~cuda", when="~cuda")
    depends_on("cuda@12:", when="+cuda")

    # Adding all the python dependencies for Boltz-2
    depends_on("py-numpy@1.26:1", type=("build", "run"))
    depends_on("py-scipy@1.13.1", type=("build", "run"))
    depends_on("py-pandas@2.2.2:", type=("build", "run"))
    depends_on("py-scikit-learn@1.6.1", type=("build", "run"))
    depends_on("py-numba@0.61.0", type=("build", "run"))
    depends_on("py-biopython@1.84", type=("build", "run"))
    depends_on("py-gemmi@0.6.5:", type=("build", "run"))
    depends_on("py-triton", type=("build", "run"), when="+cuda platform=linux")

    # added this too to rebuild the package
    def setup_run_environment(self, env):
            """Set up the runtime environment for the generated module file."""
            if self.spec.satisfies("+cuda"):
                cuda_libs = self.spec["cuda"].libs.directories
                for lib_dir in cuda_libs:
                    env.prepend_path("LD_LIBRARY_PATH", lib_dir)
                
                # Specifically for Boltz/Torch
                env.set("CUDA_HOME", self.spec["cuda"].prefix)