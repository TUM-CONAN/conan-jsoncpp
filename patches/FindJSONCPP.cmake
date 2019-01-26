find_path(JsonCpp_INCLUDE_DIR NAMES "json/json.h" PATHS ${CONAN_INCLUDE_DIRS_JSONCPP})
message(STATUS "Look for ${CONAN_LIBS_JSONCPP} in ${CONAN_LIB_DIRS_JSONCPP}")
find_library(JsonCpp_LIBRARY NAMES ${CONAN_LIBS_JSONCPP} PATHS ${CONAN_LIB_DIRS_JSONCPP})

message("** JsonCpp already found by conan!")
SET(JsonCpp_FOUND TRUE)
message(STATUS "** Found JsonCpp:  ${JsonCpp_LIBRARY}")
message(STATUS "** Found JsonCpp include:  ${JsonCpp_INCLUDE_DIR}")

set(JsonCpp_INCLUDE_DIRS ${JsonCpp_INCLUDE_DIR})
set(JsonCpp_LIBRARIES ${JsonCpp_LIBRARY})

mark_as_advanced(JsonCpp_LIBRARY JsonCpp_INCLUDE_DIR)
