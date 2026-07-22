# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRichClick(PythonPackage):
    """The intention of rich-click is to provide attractive help output
    from click, formatted with rich, with minimal customisation required."""

    homepage = "https://github.com/ewels/rich-click"
    pypi = "rich-click/rich_click-1.8.5.tar.gz"

    license("MIT")

    version("1.9.7", sha256="022997c1e30731995bdbc8ec2f82819340d42543237f033a003c7b1f843fc5dc")
    version("1.9.6", sha256="463bd3dbef54a812282bfa93dde80c471bce359823fc1301be368eab63391cb2")
    version("1.9.5.dev0", sha256="22527eb6138ef88cacf8e2d0acbe2df897e3e7cee9eff6f0f9c45c407e2a8808")
    version("1.9.5", sha256="48120531493f1533828da80e13e839d471979ec8d7d0ca7b35f86a1379cc74b6")
    version("1.9.4", sha256="af73dc68e85f3bebb80ce302a642b9fe3b65f3df0ceb42eb9a27c467c1b678c8")
    version("1.9.3.dev0", sha256="7d8c39a820d7ed17cc14512c6f0e25bd8ab9211c4f7c3265b8246dd85d46a157")
    version("1.9.3", sha256="60839150a935604df1378b159da340d3fff91f912903e935da7cb615b5738c1b")
    version("1.9.2.dev0", sha256="4be77eda1ac4e515838e7b3d4fcc44a596047e917d8bb829b3fff49f77aab0eb")
    version("1.9.2", sha256="1c4212f05561be0cac6a9c1743e1ebcd4fe1fb1e311f9f672abfada3be649db6")
    version("1.9.1", sha256="4f2620589d7287f86265432e6a909de4f281de909fe68d8c835fbba49265d268")
    version("1.9.0.dev6", sha256="abe59fd5b639f96880e3071f2413f7b7baf83fc503d91d471ddf8dc7585f74f2")
    version("1.9.0.dev5", sha256="55d06ceef584f3949ddf6ff0be607c660344c6d3d822b7276b5fd2d058ea8ea7")
    version("1.9.0.dev4", sha256="64c1185cd9c9c5a1acb32aa7d33a0b2ec97324884d9cade91c68aa3fea369769")
    version("1.9.0.dev3", sha256="bb57d156ce954b67ce6e7db5ef5b4be7590a431baf68fa79b9c7021fe631c500")
    version("1.9.0.dev2", sha256="f79704ba37cf599692783bc4feee2309217718c7fd3c02752c6a2dde95f35d5d")
    version("1.9.0.dev1", sha256="64735bcb1387389f4eeb16e808632d011d859dc8dbf36654f9a0a7c3d5cf8610")
    version("1.9.0.dev0", sha256="d65c96c094f1df81acbc7d8784bf8691827c60a8a2eaec0cf4e808c43c406904")
    version("1.9.0", sha256="212a19875b1e485803a5448130a9157b04c0d0befcc2bc29cb64d3577b93b005")
    version("1.8.9", sha256="fd98c0ab9ddc1cf9c0b7463f68daf28b4d0033a74214ceb02f761b3ff2af3136")
    version("1.8.8", sha256="547c618dea916620af05d4a6456da797fbde904c97901f44d2f32f89d85d6c84")
    version("1.8.7.dev0", sha256="df825e43a11983e1a83bd5cd9c59e4829d7be40374ed3402434a6f7a86a99089")
    version("1.8.7", sha256="075aa0140a3f796768e1e650174d4e12828de87f3a0aed49fe48fb897fcaa627")
    version("1.8.6", sha256="8a2448fd80e3d4e16fcb3815bfbc19be9bae75c9bb6aedf637901e45f3555752")
    version("1.8.5", sha256="a3eebe81da1c9da3c32f3810017c79bd687ff1b3fa35bfc9d8a3338797f1d1a1")
    version("1.8.4", sha256="0f49471f04439269d0e66a6f43120f52d11d594869a2a0be600cfb12eb0616b9")
    version("1.8.3", sha256="6d75bdfa7aa9ed2c467789a0688bc6da23fbe3a143e19aa6ad3f8bac113d2ab3")
    version("1.8.2", sha256="8e29bdede858b59aa2859a1ab1c4ccbd39ed7ed5870262dae756fba6b5dc72e8")
    version("1.8.1", sha256="73c2ec88a66d7bf6b8c32783539d1c9c92c7c75847f14186092d27f83b206e8a")
    version("1.8.0.dev7", sha256="29c418be25da0fec88a663b6298eb40de290f15a825799dd6c5715242b40d722")
    version("1.8.0.dev6", sha256="c33d08a0de2c5f24748b377a2a1d8bb8e4cb035e641db2bf07d470199ed6311f")
    version("1.8.0.dev5", sha256="c5d447d8dfb39feb63bea46399ff852d02031162e685a611d1f3b64c2de33cdf")
    version("1.8.0", sha256="f8cad0d67d286d6cd6fc9f69f2d6f25c6c4c2d99fb9d6cb3b8987b593dbe6fa8")
    version("1.7.4", sha256="7ce5de8e4dc0333aec946113529b3eeb349f2e5d2fafee96b9edf8ee36a01395")
    version("1.6.1", sha256="f8ff96693ec6e261d1544e9f7d9a5811c5ef5d74c8adb4978430fc0dac16777e")
    version("1.5.2", sha256="a57ca70242cb8b372a670eaa0b0be48f2440b66656deb4a56e6aadc1bbb79670")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-click@7:", type=("build", "run"))
    depends_on("py-rich@10.7.0:", type=("build", "run"))
    depends_on("py-importlib-metadata", type=("build", "run"), when="^python@:3.7")
    depends_on("py-typing-extensions@4", type=("build", "run"), when="@1.8.0:")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/r/rich-click/{0}-{1}.tar.gz"
        if version >= Version("1.8.0"):
            name = "rich_click"
        else:
            name = "rich-click"
        return url.format(name, version)