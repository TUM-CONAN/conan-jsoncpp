from conans import ConanFile, CMake, tools, AutoToolsBuildEnvironment
from conans.util import files
import os
import shutil

class LibJsoncppConan(ConanFile):
    name = "jsoncpp"
    version = "1.7.1"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    exports = [
        "patches/CMakeProjectWrapper.txt",
        "patches/FindJSONCPP.cmake"
    ]
    url = "https://git.ircad.fr/conan/conan-jsoncpp"
    license="MIT License"
    description = "A C++ library for interacting with JSON. "
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"
    short_paths = True

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        tools.get("https://github.com/open-source-parsers/jsoncpp/archive/{0}.tar.gz".format(self.version))
        os.rename("jsoncpp-" + self.version, self.source_subfolder)

    def build(self):
        shutil.move("patches/CMakeProjectWrapper.txt", "CMakeLists.txt")

        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED"] = self.options.shared
        cmake.definitions["BUILD_STATIC_LIBS"] = "OFF"
        cmake.definitions["LIBRARY_INSTALL_DIR"] = os.path.join(self.package_folder, "lib")
        cmake.definitions["JSONCPP_WITH_TESTS"] = "OFF"
        cmake.definitions["JSONCPP_WITH_POST_BUILD_UNITTEST"] = "OFF"
        if not tools.os_info.is_windows:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = "ON"

        cmake.configure(build_folder=self.build_subfolder)
        cmake.build()
        cmake.install()
    
    def package(self):
        self.copy("FindJSONCPP.cmake", src="patches", dst=".", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
