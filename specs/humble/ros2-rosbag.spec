Name:           ros2-rosbag
Version:        noetic.1.16.0
Release:        1%{?dist}
Summary:        ROS package rosbag

License:        BSD
URL:            http://wiki.ros.org/rosbag

Source0:        https://github.com/ros-gbp/ros_comm-release/archive/release/noetic/rosbag/1.16.0-1.tar.gz#/ros2-noetic-rosbag-1.16.0-source0.tar.gz



# common BRs
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: make
BuildRequires: patch
BuildRequires: python3-devel
BuildRequires: python-unversioned-command
BuildRequires: ros2-ament_package
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

BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  lz4-devel
BuildRequires:  python3-pillow
BuildRequires:  python3-pillow python3-pillow-qt
BuildRequires:  ros2-noetic-ament_package-devel
BuildRequires:  ros2-noetic-catkin-devel
BuildRequires:  ros2-noetic-cpp_common-devel
BuildRequires:  ros2-noetic-rosbag_storage-devel
BuildRequires:  ros2-noetic-rosconsole-devel
BuildRequires:  ros2-noetic-roscpp-devel
BuildRequires:  ros2-noetic-roscpp_serialization-devel
BuildRequires:  ros2-noetic-std_srvs-devel
BuildRequires:  ros2-noetic-topic_tools-devel
BuildRequires:  ros2-noetic-xmlrpcpp-devel

Requires:       python3-gnupg
Requires:       python3-pycryptodomex
Requires:       python3-rospkg
Requires:       ros2-noetic-genmsg
Requires:       ros2-noetic-genpy
Requires:       ros2-noetic-rosbag_storage
Requires:       ros2-noetic-rosconsole
Requires:       ros2-noetic-roscpp
Requires:       ros2-noetic-roslib
Requires:       ros2-noetic-rospy
Requires:       ros2-noetic-std_srvs
Requires:       ros2-noetic-topic_tools
Requires:       ros2-noetic-xmlrpcpp

Provides:  ros2-noetic-rosbag = 1.16.0-1
Obsoletes: ros2-noetic-rosbag < 1.16.0-1



%description
This is a set of tools for recording from and playing back to ROS
topics. It is intended to be high performance and avoids
deserialization and reserialization of the messages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros2-noetic-catkin-devel
Requires:       boost-devel
Requires:       bzip2-devel
Requires:       lz4-devel
Requires:       python3-pillow
Requires:       python3-pillow python3-pillow-qt
Requires:       ros2-noetic-ament_package-devel
Requires:       ros2-noetic-cpp_common-devel
Requires:       ros2-noetic-rosbag_storage-devel
Requires:       ros2-noetic-rosconsole-devel
Requires:       ros2-noetic-roscpp-devel
Requires:       ros2-noetic-roscpp_serialization-devel
Requires:       ros2-noetic-std_srvs-devel
Requires:       ros2-noetic-topic_tools-devel
Requires:       ros2-noetic-xmlrpcpp-devel
Requires:       ros2-noetic-genmsg-devel
Requires:       ros2-noetic-genpy-devel
Requires:       ros2-noetic-roslib-devel
Requires:       ros2-noetic-rospy-devel

Provides: ros2-noetic-rosbag-devel = 1.16.0-1
Obsoletes: ros2-noetic-rosbag-devel < 1.16.0-1


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

CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \

source %{_libdir}/ros2/setup.bash

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
  -DCMAKE_SKIP_INSTALL_RPATH=ON \
  -DBUILD_TESTING=OFF \
  --base-paths . \
  --install-base %{buildroot}/%{_libdir}/ros2/ \
  --packages-select rosbag



# remove wrong buildroot prefixes
find %{buildroot}/%{_libdir}/ros2/ -type f -exec sed -i "s:%{buildroot}::g" {} \;

rm -rf %{buildroot}/%{_libdir}/ros2/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

touch files.list
find %{buildroot}/%{_libdir}/ros2/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
# TODO: is cmake/ necessary? it stems from the yaml vendor
find %{buildroot}/%{_libdir}/ros2/{lib*/pkgconfig,include/,cmake/,rosbag/include/,share/rosbag/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
find %{buildroot}/%{_libdir}/ros2/ -name *__rosidl_generator_py.so -type f -exec patchelf --add-rpath "%{_libdir}/ros2/lib" {} \;

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
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.16.0-1
- update to latest release
