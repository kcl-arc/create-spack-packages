# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Rstudio(CMakePackage):
    """RStudio is an integrated development environment (IDE) for R."""

    homepage = "https://www.rstudio.com/products/rstudio/"
    url = "https://github.com/rstudio/rstudio/archive/refs/tags/v2026.09.0+174.tar.gz"

    # Upstream tags are vYYYY.MM.P+BUILD; "+" isn't valid in a Spack version, so "_" is used
    # instead and mapped back in url_for_version
    version(
        "v2026.09.0_174",
        sha256="c7da74fc2f1ab8d4decf89db561807d58015b83632b9fef1509977c3b7a66a81",
    )
    version(
        "v2024.12.1_563",
        sha256="195e1b839dc183e12b7fb4c3cddfb2f2c53f85866779450be84b14aaae524883",
    )
    version(
        "v2023.03.0_386",
        sha256="62a67f3b528dec3957e2ea0b172cedca792e4af6b50542d65d5a53e8ae0901dd",
    )
    version(
        "v2022.07.1_554",
        sha256="1c3fd3fc64e3553ec1ec35758d177a3d4713ae5203493291d7b3b622478f4185",
    )

    variant("notebook", default=False, description="Enable notebook support.")
    variant("desktop", default=False, description="Enable desktop build.")

    # Deploy pam-env-helper based on
    # https://github.com/rocker-org/rocker-versioned2/blob/master/scripts/pam-helper.sh
    # to provide a very basic auth model
    variant(
        "pamenvhelper",
        default=True,
        description="Enable pam environment helper for server build.",
    )
    variant("texlive", default=True, description="Enable texlive with pandoc for RStudio.")

    # The Qt desktop (RSTUDIO_TARGET=Desktop) was replaced by an Electron one
    conflicts("+desktop", when="@v2024.12.1_563:", msg="Only the server build is supported")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("r+X+rmath@4.1.1:", type=("build", "run"))
    depends_on("cmake@3.21.4:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("ant", type="build")
    depends_on(
        "boost+pic+atomic+chrono+date_time+filesystem+iostreams+program_options+random+regex"
        "+system+thread"
    )
    depends_on("boost@1.78: cxxstd=11", when="@:v2023.03.0_386")
    depends_on("boost@1.83: cxxstd=11", when="@v2024.12.1_563")
    # 2026.09 asks for Boost 1.91.0, which Spack doesn't have yet (see cmake_args)
    depends_on("boost@1.90: +url cxxstd=17", when="@v2026.09.0_174:")
    depends_on("qt+webkit@5.12.8:", when="+desktop")
    depends_on("patchelf@0.9:", when="+desktop")
    # 2026.09 fetches yaml-cpp itself (CMake FetchContent) and has no option to use a system one
    depends_on("yaml-cpp@:0.6.3", when="@:v2024.12.1_563")  # find_package fails with newest version
    # RStudio's own install-yarn installs classic yarn (1.x)
    depends_on("yarn@1", type="build")
    depends_on("node-js@16:", when="@v2023.03.0_386")  # v16+ supports used vite 'node:' import method
    depends_on("jq", type="build")
    depends_on("pandoc+texlive@2.11.4:", when="+texlive")
    depends_on("pandoc~texlive@2.11.4:", when="~texlive")
    depends_on("icu4c")
    depends_on("soci~static+boost+postgresql+sqlite")
    depends_on("soci cxxstd=11", when="@:v2024.12.1_563")
    depends_on("soci cxxstd=17", when="@v2026.09.0_174:")
    depends_on("java@8:")
    depends_on("java@17:", when="@v2026.09.0_174:")  # GWT build targets Java 17
    depends_on("linux-pam", when="~desktop")

    with when("+notebook"):
        depends_on("r-base64enc")
        depends_on("r-digest")
        depends_on("r-evaluate")
        depends_on("r-glue")
        depends_on("r-highr")
        depends_on("r-htmltools")
        depends_on("r-jsonlite")
        depends_on("r-knitr")
        depends_on("r-magrittr")
        depends_on("r-markdown")
        depends_on("r-mime")
        depends_on("r-rmarkdown")
        depends_on("r-stringi")
        depends_on("r-stringr")
        depends_on("r-tinytex")
        depends_on("r-xfun")
        depends_on("r-yaml")

    patch("seckeyfilefix1.patch", when="@v2022.07.1_554")

    def url_for_version(self, version):
        tag = version.string.replace("_", "+")
        return f"https://github.com/rstudio/rstudio/archive/refs/tags/{tag}.tar.gz"

    def cmake_args(self):
        args = [
            "-DRSTUDIO_PACKAGE_BUILD=Yes",
            "-DRSTUDIO_USE_SYSTEM_YAML_CPP=Yes",
            "-DRSTUDIO_USE_SYSTEM_BOOST=Yes",
            "-DRSTUDIO_USE_SYSTEM_SOCI=Yes",
        ]
        if self.spec.satisfies("+desktop"):
            args.extend(
                [
                    "-DRSTUDIO_TARGET=Desktop",
                    '-DQT_QMAKE_EXECUTABLE="{0}"'.format(self.spec["qt"].prefix.bin.qmake),
                ]
            )
        else:
            args.extend(["-DRSTUDIO_TARGET=Server"])

        if self.spec.satisfies("@v2026.09.0_174:"):
            # find_package(Boost) is called with RStudio's requested version as a minimum
            args.append(f"-DRSTUDIO_BOOST_REQUESTED_VERSION={self.spec['boost'].version}")

        return args

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("RSTUDIO_TOOLS_ROOT", self.prefix.tools)

    def patch(self):
        if self.spec.satisfies("@:v2023.03.0_386"):
            # remove hardcoded soci path to use spack soci
            if self.spec["soci"].satisfies("@:4.0.0"):
                soci_lib = self.spec["soci"].prefix.lib64
            else:
                soci_lib = self.spec["soci"].prefix.lib
            filter_file(
                'set(SOCI_LIBRARY_DIR "/usr/lib")',
                'set(SOCI_LIBRARY_DIR "{0}")'.format(soci_lib),
                "src/cpp/CMakeLists.txt",
                string=True,
            )

            # unbundle icu libraries
            filter_file(
                "${QT_LIBRARY_DIR}/${ICU_LIBRARY}.so",
                join_path(self.spec["icu4c"].prefix.lib, "${ICU_LIBRARY}.so"),
                "src/cpp/desktop/CMakeLists.txt",
                string=True,
            )

    @run_before("cmake")
    def install_deps(self):
        deps = Executable("./dependencies/common/install-dictionaries")
        deps()
        deps = Executable("./dependencies/common/install-mathjax")
        deps()
        deps = Executable("./dependencies/common/install-quarto")
        deps()
        # As node-js 16.14.0 is not available via spack we will install it locally
        # EDIT: for v2023.03.0_386, required node-js version added via spack.
        # It looks as though the script has to be run from within the dependencies/common
        # dir
        if not self.spec.satisfies("@=v2023.03.0_386"):
            with working_dir("dependencies/common"):
                deps = Executable("./install-npm-dependencies")
                deps()
        if self.spec.satisfies("@v2023.03.0_386:"):
            deps = Executable("./dependencies/common/install-panmirror")
            deps()
        if self.spec.satisfies("@v2026.09.0_174:"):
            deps = Executable("./dependencies/common/install-copilot-language-server")
            deps()
            # GWT is no longer bundled; the GWT build looks for it in dependencies/common
            with working_dir("dependencies/common"):
                deps = Executable("./install-gwt")
                deps()

        # two methods for pandoc
        # 1) replace install-pandoc:
        #    - link pandoc into tools/pandoc/$PANDOC_VERSION
        #      (this is what install-pandoc would do)
        #    - cmake then installs pandoc files from there into bin
        # 2) remove install-pandoc and cmake install step + link directly into bin
        # (both only matter if Quarto is disabled: by default RStudio uses Quarto's pandoc)

        # method 1)
        # PANDOC_VERSION moved from src/cpp/session/CMakeLists.txt to cmake/globals.cmake
        filter_file(
            r'set\(PANDOC_VERSION "[^"]*" CACHE INTERNAL "Pandoc version"\)',
            'set(PANDOC_VERSION "{0}" CACHE INTERNAL "Pandoc version")'.format(
                self.spec["pandoc"].version
            ),
            "src/cpp/session/CMakeLists.txt",
            "cmake/globals.cmake",
            ignore_absent=True,
        )

        pandoc_dir = join_path(self.prefix.tools, "pandoc", self.spec["pandoc"].version)
        mkdirp(pandoc_dir)
        with working_dir(pandoc_dir):
            symlink(self.spec["pandoc"].prefix.bin.pandoc, "pandoc")
            symlink(
                os.path.join(self.spec["pandoc"].prefix.bin, "pandoc-citeproc"), "pandoc-citeproc"
            )

    @run_after("install")
    def post_install(self):
        if self.spec.satisfies("+pamenvhelper"):
            pam_helper_script = join_path(self.prefix.bin, "pam-env-helper")
            install(join_path(self.package_dir, "pam-env-helper"), pam_helper_script)
            set_executable(pam_helper_script)
