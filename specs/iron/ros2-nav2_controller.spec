Name:           ros2-iron-nav2_controller
Version:        1.2.9
Release:        1%{?dist}
Summary:        ROS package nav2_controller

License:        Apache-2.0
URL:            http://www.ros.org/

Source0:        https://github.com/SteveMacenski/navigation2-release/archive/release/iron/nav2_controller/1.2.9-1.tar.gz#/ros2-iron-nav2_controller-1.2.9-source0.tar.gz



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

BuildRequires:  ros2-iron-ament_cmake-devel
BuildRequires:  ros2-iron-ament_cmake_gtest-devel
BuildRequires:  ros2-iron-ament_cmake_pytest-devel
BuildRequires:  ros2-iron-ament_lint_auto-devel
BuildRequires:  ros2-iron-ament_lint_common-devel
BuildRequires:  ros2-iron-ament_package-devel
BuildRequires:  ros2-iron-angles-devel
BuildRequires:  ros2-iron-nav2_common-devel
BuildRequires:  ros2-iron-nav2_core-devel
BuildRequires:  ros2-iron-nav2_msgs-devel
BuildRequires:  ros2-iron-nav2_util-devel
BuildRequires:  ros2-iron-nav_2d_msgs-devel
BuildRequires:  ros2-iron-nav_2d_utils-devel
BuildRequires:  ros2-iron-pluginlib-devel
BuildRequires:  ros2-iron-rclcpp-devel
BuildRequires:  ros2-iron-rclcpp_action-devel
BuildRequires:  ros2-iron-std_msgs-devel

Requires:       ros2-iron-angles
Requires:       ros2-iron-nav2_core
Requires:       ros2-iron-nav2_msgs
Requires:       ros2-iron-nav2_util
Requires:       ros2-iron-nav_2d_msgs
Requires:       ros2-iron-nav_2d_utils
Requires:       ros2-iron-pluginlib
Requires:       ros2-iron-rclcpp
Requires:       ros2-iron-rclcpp_action
Requires:       ros2-iron-std_msgs

Provides:  ros2-iron-nav2_controller = 1.2.9-1
Obsoletes: ros2-iron-nav2_controller < 1.2.9-1



%description
Controller action interface

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros2-iron-ament_cmake-devel
Requires:       ros2-iron-ament_cmake_gtest-devel
Requires:       ros2-iron-ament_cmake_pytest-devel
Requires:       ros2-iron-ament_lint_auto-devel
Requires:       ros2-iron-ament_lint_common-devel
Requires:       ros2-iron-ament_package-devel
Requires:       ros2-iron-angles-devel
Requires:       ros2-iron-nav2_common-devel
Requires:       ros2-iron-nav2_core-devel
Requires:       ros2-iron-nav2_msgs-devel
Requires:       ros2-iron-nav2_util-devel
Requires:       ros2-iron-nav_2d_msgs-devel
Requires:       ros2-iron-nav_2d_utils-devel
Requires:       ros2-iron-pluginlib-devel
Requires:       ros2-iron-rclcpp-devel
Requires:       ros2-iron-rclcpp_action-devel
Requires:       ros2-iron-std_msgs-devel

Provides: ros2-iron-nav2_controller-devel = 1.2.9-1
Obsoletes: ros2-iron-nav2_controller-devel < 1.2.9-1


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

source %{_libdir}/ros2-iron/setup.bash

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
  --install-base %{buildroot}/%{_libdir}/ros2-iron/ \
  --packages-select nav2_controller



# remove wrong buildroot prefixes
find %{buildroot}/%{_libdir}/ros2-iron/ -type f -exec sed -i "s:%{buildroot}::g" {} \;

# # Move include directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-iron/opt/nav2_controller/include ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-iron/include/nav2_controller ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-iron/include/nav2_controller
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-iron/opt/nav2_controller/include/* %{buildroot}/%{_libdir}/ros2-iron/include/nav2_controller
# fi
# 
# # Move share directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-iron/opt/nav2_controller/share ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-iron/share ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-iron/share
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-iron/opt/nav2_controller/share %{buildroot}/%{_libdir}/ros2-iron/
#     find %{buildroot}/%{_libdir}/ros2-iron/share -type f -exec sed -i "s:opt/nav2_controller/::g" {} \;
# fi
# 
# # Move bin directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-iron/opt/nav2_controller/bin ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-iron/bin ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-iron/bin
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-iron/opt/nav2_controller/bin %{buildroot}/%{_libdir}/ros2-iron/
# fi
# 
# # Move extra_cmake directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-iron/opt/nav2_controller/extra_cmake ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-iron/extra_cmake ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-iron/extra_cmake
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-iron/opt/nav2_controller/extra_cmake %{buildroot}/%{_libdir}/ros2-iron/
#     find %{buildroot}/%{_libdir}/ros2-iron/extra_cmake -type f -exec sed -i "s:opt/nav2_controller/::g" {} \;
# fi
# 
# # Move lib directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-iron/opt/nav2_controller/lib ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-iron/lib ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-iron/lib
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-iron/opt/nav2_controller/lib %{buildroot}/%{_libdir}/ros2-iron/lib
# fi
# 
# # Move lib64 directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-iron/opt/nav2_controller/lib64 ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-iron/lib64 ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-iron/lib64
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-iron/opt/nav2_controller/lib64 %{buildroot}/%{_libdir}/ros2-iron/lib64
# fi

rm -rf %{buildroot}/%{_libdir}/ros2-iron/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# remove __pycache__
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find . -name '*.pyc' -delete

touch files.list
find %{buildroot}/%{_libdir}/ros2-iron/{opt,bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2-iron/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros2-iron/{lib*/pkgconfig,include/,cmake/,nav2_controller/include/,share/nav2_controller/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2-iron/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
# find %{buildroot}/%{_libdir}/ros2-iron/ -name *__rosidl_generator_py.so -type f -exec patchelf --force-rpath --add-rpath "%{_libdir}/ros2/lib" {} \;

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
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.9-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.8-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release