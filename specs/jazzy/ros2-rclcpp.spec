Name:           ros2-jazzy-rclcpp
Version:        28.1.2
Release:        1%{?dist}
Summary:        ROS package rclcpp

License:        Apache License 2.0
URL:            http://www.ros.org/

Source0:        https://github.com/ros2-gbp/rclcpp-release/archive/release/jazzy/rclcpp/28.1.2-1.tar.gz#/ros2-jazzy-rclcpp-28.1.2-source0.tar.gz



# common BRs
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: make
BuildRequires: patch
BuildRequires: python3-devel
BuildRequires: python-unversioned-command
BuildRequires: python3-colcon-common-extensions
BuildRequires: python3-pip
BuildRequires: python3-pydocstyle
BuildRequires: python3-pytest
BuildRequires: python3-pytest-repeat
BuildRequires: python3-pytest-rerunfailures
BuildRequires: python3-rosdep
BuildRequires: python3-setuptools
BuildRequires: python3-vcstool

# BuildRequires:  boost-devel
# BuildRequires:  console-bridge-devel
# BuildRequires:  gtest-devel
# BuildRequires:  log4cxx-devel
# BuildRequires:  python3-devel
# BuildRequires:  python3-colcon-common-extensions
# BuildRequires:  python-unversioned-command

BuildRequires:  python3-devel
BuildRequires:  ros2-jazzy-ament_cmake_gen_version_h-devel
BuildRequires:  ros2-jazzy-ament_cmake_gmock-devel
BuildRequires:  ros2-jazzy-ament_cmake_google_benchmark-devel
BuildRequires:  ros2-jazzy-ament_cmake_gtest-devel
BuildRequires:  ros2-jazzy-ament_cmake_ros-devel
BuildRequires:  ros2-jazzy-ament_index_cpp-devel
BuildRequires:  ros2-jazzy-ament_lint_auto-devel
BuildRequires:  ros2-jazzy-ament_lint_common-devel
BuildRequires:  ros2-jazzy-ament_package-devel
BuildRequires:  ros2-jazzy-builtin_interfaces-devel
BuildRequires:  ros2-jazzy-libstatistics_collector-devel
BuildRequires:  ros2-jazzy-mimick_vendor-devel
BuildRequires:  ros2-jazzy-performance_test_fixture-devel
BuildRequires:  ros2-jazzy-rcl-devel
BuildRequires:  ros2-jazzy-rcl_interfaces-devel
BuildRequires:  ros2-jazzy-rcl_logging_interface-devel
BuildRequires:  ros2-jazzy-rcl_yaml_param_parser-devel
BuildRequires:  ros2-jazzy-rcpputils-devel
BuildRequires:  ros2-jazzy-rcutils-devel
BuildRequires:  ros2-jazzy-rmw-devel
BuildRequires:  ros2-jazzy-rmw_implementation_cmake-devel
BuildRequires:  ros2-jazzy-rosgraph_msgs-devel
BuildRequires:  ros2-jazzy-rosidl_default_generators-devel
BuildRequires:  ros2-jazzy-rosidl_dynamic_typesupport-devel
BuildRequires:  ros2-jazzy-rosidl_runtime_c-devel
BuildRequires:  ros2-jazzy-rosidl_runtime_cpp-devel
BuildRequires:  ros2-jazzy-rosidl_typesupport_c-devel
BuildRequires:  ros2-jazzy-rosidl_typesupport_cpp-devel
BuildRequires:  ros2-jazzy-statistics_msgs-devel
BuildRequires:  ros2-jazzy-test_msgs-devel
BuildRequires:  ros2-jazzy-tracetools-devel

Requires:       ros2-jazzy-libstatistics_collector
Requires:       ros2-jazzy-rcl
Requires:       ros2-jazzy-rcl_logging_interface
Requires:       ros2-jazzy-rcl_yaml_param_parser
Requires:       ros2-jazzy-rcpputils
Requires:       ros2-jazzy-rcutils
Requires:       ros2-jazzy-rmw
Requires:       ros2-jazzy-rosidl_dynamic_typesupport
Requires:       ros2-jazzy-statistics_msgs
Requires:       ros2-jazzy-tracetools

Provides:  ros2-jazzy-rclcpp = 28.1.2-1
Obsoletes: ros2-jazzy-rclcpp < 28.1.2-1



%description
The ROS client library in C++.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-devel
Requires:       ros2-jazzy-ament_cmake_gen_version_h-devel
Requires:       ros2-jazzy-ament_cmake_ros-devel
Requires:       ros2-jazzy-ament_index_cpp-devel
Requires:       ros2-jazzy-builtin_interfaces-devel
Requires:       ros2-jazzy-rcl_interfaces-devel
Requires:       ros2-jazzy-rosgraph_msgs-devel
Requires:       ros2-jazzy-rosidl_runtime_c-devel
Requires:       ros2-jazzy-rosidl_runtime_cpp-devel
Requires:       ros2-jazzy-rosidl_typesupport_c-devel
Requires:       ros2-jazzy-rosidl_typesupport_cpp-devel
Requires:       ros2-jazzy-ament_cmake_gmock-devel
Requires:       ros2-jazzy-ament_cmake_google_benchmark-devel
Requires:       ros2-jazzy-ament_cmake_gtest-devel
Requires:       ros2-jazzy-ament_lint_auto-devel
Requires:       ros2-jazzy-ament_lint_common-devel
Requires:       ros2-jazzy-ament_package-devel
Requires:       ros2-jazzy-libstatistics_collector-devel
Requires:       ros2-jazzy-mimick_vendor-devel
Requires:       ros2-jazzy-performance_test_fixture-devel
Requires:       ros2-jazzy-rcl-devel
Requires:       ros2-jazzy-rcl_logging_interface-devel
Requires:       ros2-jazzy-rcl_yaml_param_parser-devel
Requires:       ros2-jazzy-rcpputils-devel
Requires:       ros2-jazzy-rcutils-devel
Requires:       ros2-jazzy-rmw-devel
Requires:       ros2-jazzy-rmw_implementation_cmake-devel
Requires:       ros2-jazzy-rosidl_default_generators-devel
Requires:       ros2-jazzy-rosidl_dynamic_typesupport-devel
Requires:       ros2-jazzy-statistics_msgs-devel
Requires:       ros2-jazzy-test_msgs-devel
Requires:       ros2-jazzy-tracetools-devel

Provides: ros2-jazzy-rclcpp-devel = 28.1.2-1
Obsoletes: ros2-jazzy-rclcpp-devel < 28.1.2-1


%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.



%prep

%setup -c -T
tar --strip-components=1 -xf %{SOURCE0}

%build
# nothing to do here


%install

PYTHONUNBUFFERED=1 ; export PYTHONUNBUFFERED
GZ_BUILD_FROM_SURCE=1; export GZ_BUILD_FROM_SOURCE

CFLAGS=" -Wno-error ${CFLAGS:-%optflags} -Wno-error -w -Wno-error=int-conversion" ; export CFLAGS ; \
CXXFLAGS=" -Wno-error ${CXXFLAGS:-%optflags} -Wno-error -w -Wno-error=int-conversion" ; export CXXFLAGS ; \
FFLAGS=" -Wno-error ${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -w -Wno-error=int-conversion" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -w -Wno-error=int-conversion" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \

source %{_libdir}/ros2-jazzy/setup.bash

# substitute shebang before install block because we run the local catkin script
%py3_shebang_fix .

# DESTDIR=%{buildroot} ; export DESTDIR


colcon \
  build \
  --merge-install \
  --cmake-args -DPYTHON_EXECUTABLE="/usr/bin/python" \
  -DTHIRDPARTY_Asio=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
  -DCMAKE_C_FLAGS="$CFLAGS" \
  -DCMAKE_LD_FLAGS="$LDFLAGS" \
  -DBUILD_TESTING=OFF \
  --base-paths . \
  --install-base %{buildroot}/%{_libdir}/ros2-jazzy/ \
  --packages-select rclcpp



# remove wrong buildroot prefixes
find %{buildroot}/%{_libdir}/ros2-jazzy/ -type f -exec sed -i "s:%{buildroot}::g" {} \;

# # Move include directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/rclcpp/include ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/include/rclcpp ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/include/rclcpp
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-jazzy/opt/rclcpp/include/* %{buildroot}/%{_libdir}/ros2-jazzy/include/rclcpp
# fi
# 
# # Move share directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/rclcpp/share ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/share ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/share
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-jazzy/opt/rclcpp/share %{buildroot}/%{_libdir}/ros2-jazzy/
#     find %{buildroot}/%{_libdir}/ros2-jazzy/share -type f -exec sed -i "s:opt/rclcpp/::g" {} \;
# fi
# 
# # Move bin directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/rclcpp/bin ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/bin ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/bin
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-jazzy/opt/rclcpp/bin %{buildroot}/%{_libdir}/ros2-jazzy/
# fi
# 
# # Move extra_cmake directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/rclcpp/extra_cmake ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/extra_cmake ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/extra_cmake
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-jazzy/opt/rclcpp/extra_cmake %{buildroot}/%{_libdir}/ros2-jazzy/
#     find %{buildroot}/%{_libdir}/ros2-jazzy/extra_cmake -type f -exec sed -i "s:opt/rclcpp/::g" {} \;
# fi
# 
# # Move lib directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/rclcpp/lib ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/lib ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/lib
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-jazzy/opt/rclcpp/lib %{buildroot}/%{_libdir}/ros2-jazzy/lib
# fi
# 
# # Move lib64 directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/rclcpp/lib64 ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/lib64 ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/lib64
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-jazzy/opt/rclcpp/lib64 %{buildroot}/%{_libdir}/ros2-jazzy/lib64
# fi

rm -rf %{buildroot}/%{_libdir}/ros2-jazzy/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# remove __pycache__
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find . -name '*.pyc' -delete

touch files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/{opt,bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/{lib*/pkgconfig,include/,cmake/,rclcpp/include/,share/rclcpp/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2-jazzy/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
# find %{buildroot}/%{_libdir}/ros2-jazzy/ -name *__rosidl_generator_py.so -type f -exec patchelf --force-rpath --add-rpath "%{_libdir}/ros2/lib" {} \;

# replace cmake python macro in shebang
for file in $(grep -rIl '^#!.*@PYTHON_EXECUTABLE@.*$' %{buildroot}) ; do
  sed -i.orig 's:^#!\s*@PYTHON_EXECUTABLE@\s*:%{__python3}:' $file
  touch -r $file.orig $file
  rm $file.orig
done


echo "This is a package automatically generated with rosfed." >> README_FEDORA
echo "See  https://github.com/morxa/rosfed for more information." >> README_FEDORA
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name} README_FEDORA
echo %{_docdir}/%{name} >> files.list
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name}-devel README_FEDORA
echo %{_docdir}/%{name}-devel >> files_devel.list

%py3_shebang_fix %{buildroot}

# Also fix .py.in files
for pyfile in $(grep -rIl '^#!.*python.*$' %{buildroot}) ; do
  %py3_shebang_fix $pyfile
done


%files -f files.list
%files devel -f files_devel.list


%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.28.1.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.28.1.1-1
- Update to latest release