# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Motioncor2(Package):
    """MotionCor2 is a multi-GPU program that corrects beam-induced sample
    motion recorded on dose fractionated movie stacks. It implements a robust
    iterative alignment algorithm that delivers precise measurement and
    correction of both global and non-uniform local motions at
    single pixel level, suitable for both single-particle and
    tomographic images. MotionCor2 is sufficiently fast
    to keep up with automated data collection."""

    homepage = "http://msg.ucsf.edu/em/software"
    manual_download = True

    version("1.6.4", sha256="28bb3e6477abf34fe41a78bcb9da9d77d08e2e89ecd41240fab085a308e6c498",
        url="file:///software/local_software/motioncor2/MotionCor2_1.6.4_Mar31_2023.zip")

    depends_on("cuda@11.7.0", type="run")
    depends_on("libtiff", type="run")

    def install(self, spec, prefix):
        cuda_version = spec["cuda"].version.up_to(2).joined

        mkdirp(prefix.bin)
        # with working_dir("MotionCor2_{0}".format(spec.version)):
        install(
            "MotionCor2_1.6.4_Cuda117_Mar312023",
            join_path(prefix.bin, "MotionCor2"),
        )
