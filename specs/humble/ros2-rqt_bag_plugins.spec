Name:           ros2-humble-rqt_bag_plugins
Version:        1.1.5
Release:        1%{?dist}
Summary:        ROS package rqt_bag_plugins

License:        BSD
URL:            http://wiki.ros.org/rqt_bag

Source0:        https://github.com/ros2-gbp/rqt_bag-release/archive/release/humble/rqt_bag_plugins/1.1.5-1.tar.gz#/ros2-humble-rqt_bag_plugins-1.1.5-source0.tar.gz


BuildArch: noarch

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

BuildRequires:  ros2-humble-ament_package-devel

Requires:       python3-cairo
Requires:       python3-pillow python3-pillow-qt
Requires:       ros2-humble-geometry_msgs
Requires:       ros2-humble-rclpy
Requires:       ros2-humble-rosbag2
Requires:       ros2-humble-rqt_bag
Requires:       ros2-humble-rqt_gui
Requires:       ros2-humble-rqt_gui_py
Requires:       ros2-humble-rqt_plot
Requires:       ros2-humble-sensor_msgs
Requires:       ros2-humble-std_msgs

Provides:  ros2-humble-rqt_bag_plugins = 1.1.5-1
Obsoletes: ros2-humble-rqt_bag_plugins < 1.1.5-1



%description
rqt_bag provides a GUI plugin for displaying and replaying ROS bag
files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ros2-humble-ament_package-devel
Requires:       ros2-humble-geometry_msgs-devel
Requires:       ros2-humble-rclpy-devel
Requires:       ros2-humble-rosbag2-devel
Requires:       ros2-humble-rqt_bag-devel
Requires:       ros2-humble-rqt_gui-devel
Requires:       ros2-humble-rqt_gui_py-devel
Requires:       ros2-humble-rqt_plot-devel
Requires:       ros2-humble-sensor_msgs-devel
Requires:       ros2-humble-std_msgs-devel

Provides: ros2-humble-rqt_bag_plugins-devel = 1.1.5-1
Obsoletes: ros2-humble-rqt_bag_plugins-devel < 1.1.5-1


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

source %{_libdir}/ros2-humble/setup.bash

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
  --install-base %{buildroot}/%{_libdir}/ros2-humble/ \
  --packages-select rqt_bag_plugins



# remove wrong buildroot prefixes
find %{buildroot}/%{_libdir}/ros2-humble/ -type f -exec sed -i "s:%{buildroot}::g" {} \;

# # Move include directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_bag_plugins/include ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/include/rqt_bag_plugins ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/include/rqt_bag_plugins
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_bag_plugins/include/* %{buildroot}/%{_libdir}/ros2-humble/include/rqt_bag_plugins
# fi
# 
# # Move share directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_bag_plugins/share ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/share ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/share
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_bag_plugins/share %{buildroot}/%{_libdir}/ros2-humble/
#     find %{buildroot}/%{_libdir}/ros2-humble/share -type f -exec sed -i "s:opt/rqt_bag_plugins/::g" {} \;
# fi
# 
# # Move bin directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_bag_plugins/bin ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/bin ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/bin
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_bag_plugins/bin %{buildroot}/%{_libdir}/ros2-humble/
# fi
# 
# # Move extra_cmake directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_bag_plugins/extra_cmake ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/extra_cmake ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/extra_cmake
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_bag_plugins/extra_cmake %{buildroot}/%{_libdir}/ros2-humble/
#     find %{buildroot}/%{_libdir}/ros2-humble/extra_cmake -type f -exec sed -i "s:opt/rqt_bag_plugins/::g" {} \;
# fi
# 
# # Move lib directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_bag_plugins/lib ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/lib ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/lib
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_bag_plugins/lib %{buildroot}/%{_libdir}/ros2-humble/lib
# fi
# 
# # Move lib64 directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_bag_plugins/lib64 ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/lib64 ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/lib64
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_bag_plugins/lib64 %{buildroot}/%{_libdir}/ros2-humble/lib64
# fi

rm -rf %{buildroot}/%{_libdir}/ros2-humble/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# remove __pycache__
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find . -name '*.pyc' -delete

touch files.list
find %{buildroot}/%{_libdir}/ros2-humble/{opt,bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2-humble/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/{lib*/pkgconfig,include/,cmake/,rqt_bag_plugins/include/,share/rqt_bag_plugins/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2-humble/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
# find %{buildroot}/%{_libdir}/ros2-humble/ -name *__rosidl_generator_py.so -type f -exec patchelf --force-rpath --add-rpath "%{_libdir}/ros2/lib" {} \;

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
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.5-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.4-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.4-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.4-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.5.1-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.4-1
- Initial humble build
