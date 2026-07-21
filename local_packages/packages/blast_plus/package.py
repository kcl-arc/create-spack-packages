# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class BlastPlus(AutotoolsPackage):
    """Basic Local Alignment Search Tool."""

    homepage = "https://blast.ncbi.nlm.nih.gov/"
    url = "https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.13.0/ncbi-blast-2.13.0+-src.tar.gz"

    maintainers("weijianwen")

    version("2.17.0", sha256="502057a88e9990e34e62758be21ea474cc0ad68d6a63a2e37b2372af1e5ea147")
    version("2.16.0", sha256="17c93cf009721023e5aecf5753f9c6a255d157561638b91b3ad7276fd6950c2b")
    version("2.15.0", sha256="6918c370524c8d44e028bf491e8f245a895e07c66c77b261ce3b38d6058216e0")
    version("2.14.1", sha256="712c2dbdf0fb13cc1c2d4f4ef5dd1ce4b06c3b57e96dfea8f23e6e99f5b1650e")
    version("2.13.0", sha256="89553714d133daf28c477f83d333794b3c62e4148408c072a1b4620e5ec4feb2")
    version("2.12.0", sha256="fda3c9c9d488cad6c1880a98a236d842bcf3610e3e702af61f7a48cf0a714b88")
    version("2.11.0", sha256="d88e1858ae7ce553545a795a2120e657a799a6d334f2a07ef0330cc3e74e1954")
    version("2.9.0", sha256="a390cc2d7a09422759fc178db84de9def822cbe485916bbb2ec0d215dacdc257")
    version("2.8.1", sha256="e03dd1a30e37cb8a859d3788a452c5d70ee1f9102d1ee0f93b2fbd145925118f")
    version("2.7.1", sha256="10a78d3007413a6d4c983d2acbf03ef84b622b82bd9a59c6bd9fbdde9d0298ca")
    version("2.6.0", sha256="0510e1d607d0fb4389eca50d434d5a0be787423b6850b3a4f315abc2ef19c996")
    version("2.2.30", sha256="26f72d51c81b9497f33b7274109565c36692572faef4d72377f79b7e59910e40")

    patch("blast-make-fix2.5.0.diff", when="@2.5.0:2.6.0")

    @when("@:2.2.31")
    def patch(self):
        filter_file(
            "2.95* | 2.96* | 3.* | 4.* )",
            "2.95* | 2.96* | 3.* | 4.* | 5.* )",
            "c++/src/build-system/configure",
            string=True,
        )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cpio", type="build")

    variant("static", default=False, description="Build with static linkage")
    variant("jpeg", default=True, description="Build with jpeg support")
    variant("png", default=True, description="Build with png support")
    variant("freetype", default=True, description="Build with freetype support")
    variant("gnutls", default=True, description="Build with gnutls support")
    variant("openssl", default=True, description="Build with openssl support")
    variant("zlib", default=True, description="Build with zlib support")
    variant("bzip2", default=True, description="Build with bzip2 support")
    variant("lzo", default=True, description="Build with lzo support")
    variant("pcre", default=True, description="Build with pcre support")
    variant("perl", default=True, description="Build with perl support")
    variant("python", default=True, description="Build with python support")
    variant("sqlite", default=False, description="Build with sqlite support")
    variant("zstd", default=False, when="@2.10:", description="Build with zstd support")

    depends_on("jpeg", when="+jpeg")
    depends_on("libpng", when="+png")
    depends_on("freetype", when="+freetype")
    depends_on("gnutls", when="+gnutls")
    depends_on("openssl", when="+openssl")
    depends_on("zlib-api", when="+zlib")
    depends_on("bzip2", when="+bzip2")
    depends_on("lzo", when="+lzo")
    depends_on("pcre", when="+pcre")

    depends_on("python@:3.11", when="+python")
    depends_on("py-setuptools@48:", when="+python ^python@3.12:", type="build")
    depends_on("perl", when="+perl")

    depends_on("lmdb", when="@2.7.1:")
    depends_on("sqlite", when="+sqlite")
    depends_on("zstd", when="+zstd")

    configure_directory = "c++"

    requires("+sqlite", when="@2.15.0:", msg="sqlite support is required in 2.15 and later")
    requires(
        "+zstd+zlib+bzip2",
        when="@2.17.0:",
        msg="zstd, zlib, and bzip2 are required 2.17 and later",
    )

    @run_before('configure')
    def scrub_test_dirs(self):
        import os
        import re
        # Walk the raw source code and permanently erase 'test' from all Makefile blueprints
        for root, dirs, files in os.walk('c++/src'):
            if 'Makefile.in' in files:
                filepath = os.path.join(root, 'Makefile.in')
                with open(filepath, 'r') as f:
                    lines = f.readlines()

                modified = False
                in_proj = False
                for i, line in enumerate(lines):
                    # Detect if we are inside a SUB_PROJ or EXPENDABLE_SUB_PROJ block
                    if re.match(r'^\s*(SUB_PROJ|EXPENDABLE_SUB_PROJ|POTENTIAL_SUB_PROJ)\s*=', line):
                        in_proj = True
                    
                    if in_proj:
                        # Remove the exact word 'test' (respecting word boundaries so we don't break 'test_boost')
                        if re.search(r'\btest\b', line):
                            lines[i] = re.sub(r'\btest\b', '', line)
                            modified = True
                        # If the line doesn't end with a continuation character '\', the block is over
                        if not line.rstrip().endswith('\\'):
                            in_proj = False

                if modified:
                    with open(filepath, 'w') as f:
                        f.writelines(lines)

    def configure_args(self):
        spec = self.spec

        config_args = ["--with-bin-release", "--without-debug", "--with-mt", "--without-boost", "--without-testing",]

        if spec.target.family != "aarch64":
            config_args.append("--with-64")
        if spec.satisfies("+static"):
            config_args.append("--with-static")
        else:
            config_args.extend(["--with-dll", "--without-static", "--without-static-exe"])

        if spec.satisfies("+jpeg"):
            config_args.append(f"--with-jpeg={self.spec['jpeg'].prefix}")
        else:
            config_args.append("--without-jpeg")

        if spec.satisfies("+png"):
            config_args.append(f"--with-png={self.spec['libpng'].prefix}")
        else:
            config_args.append("--without-png")

        if spec.satisfies("+freetype"):
            config_args.append(f"--with-freetype={self.spec['freetype'].prefix}")
        else:
            config_args.append("--without-freetype")

        config_args.append("--without-hdf5")

        if spec.satisfies("+zlib"):
            config_args.append(f"--with-z={self.spec['zlib-api'].prefix}")
        else:
            config_args.append("--without-z")

        if spec.satisfies("+bzip2"):
            config_args.append(f"--with-bz2={self.spec['bzip2'].prefix}")
        else:
            config_args.append("--without-bz2")

        if spec.satisfies("+lzo"):
            config_args.append(f"--with-lzo={self.spec['lzo'].prefix}")
        else:
            config_args.append("--without-lzo")

        if spec.satisfies("+gnutls"):
            config_args.append(f"--with-gnutls={self.spec['gnutls'].prefix}")
        else:
            config_args.append("--without-gnutls")

        if spec.satisfies("+openssl"):
            config_args.append(f"--with-openssl={self.spec['openssl'].prefix}")
        else:
            config_args.append("--without-openssl")

        if spec.satisfies("+pcre"):
            config_args.append(f"--with-pcre={self.spec['pcre'].prefix}")
        else:
            config_args.append("--without-pcre")

        if spec.satisfies("+python"):
            config_args.append(f"--with-python={self.spec['python'].home}")
        else:
            config_args.append("--without-python")

        if spec.satisfies("+perl"):
            config_args.append(f"--with-perl={self.spec['perl'].prefix}")
        else:
            config_args.append("--without-perl")

        if spec.satisfies("+sqlite"):
            config_args.append(f"--with-sqlite3={self.spec['sqlite'].prefix}")

        if spec.satisfies("+zstd"):
            config_args.append(f"--with-zstd={self.spec['zstd'].prefix}")

        return config_args