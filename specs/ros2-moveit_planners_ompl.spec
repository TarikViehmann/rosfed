Name:           ros2-humble-moveit_planners_ompl
Version:        2.5.5
Release:        1%{?dist}
Summary:        ROS package moveit_planners_ompl

License:        BSD
URL:            http://moveit.ros.org

Source0:        https://github.com/ros2-gbp/moveit2-release/archive/release/humble/moveit_planners_ompl/2.5.5-1.tar.gz#/ros2-humble-moveit_planners_ompl-2.5.5-source0.tar.gz



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

BuildRequires:  eigen3-devel
BuildRequires:  fcl-devel
BuildRequires:  libomp-devel
BuildRequires:  poco-devel
BuildRequires:  tinyxml-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  urdfdom-devel
BuildRequires:  ros2-humble-ament_cmake-devel
BuildRequires:  ros2-humble-ament_cmake_gtest-devel
BuildRequires:  ros2-humble-ament_lint_auto-devel
BuildRequires:  ros2-humble-ament_lint_common-devel
BuildRequires:  ros2-humble-ament_package-devel
BuildRequires:  ros2-humble-eigen3_cmake_module-devel
BuildRequires:  ros2-humble-moveit_common-devel
BuildRequires:  ros2-humble-moveit_core-devel
BuildRequires:  ros2-humble-moveit_msgs-devel
BuildRequires:  ros2-humble-moveit_resources_fanuc_moveit_config-devel
BuildRequires:  ros2-humble-moveit_resources_panda_moveit_config-devel
BuildRequires:  ros2-humble-moveit_resources_pr2_description-devel
BuildRequires:  ros2-humble-moveit_ros_planning-devel
BuildRequires:  ros2-humble-ompl-devel
BuildRequires:  ros2-humble-pluginlib-devel
BuildRequires:  ros2-humble-rclcpp-devel
BuildRequires:  ros2-humble-tf2_eigen-devel
BuildRequires:  ros2-humble-tf2_ros-devel

Requires:       ros2-humble-moveit_common
Requires:       ros2-humble-moveit_core
Requires:       ros2-humble-moveit_msgs
Requires:       ros2-humble-moveit_ros_planning
Requires:       ros2-humble-ompl
Requires:       ros2-humble-pluginlib
Requires:       ros2-humble-rclcpp
Requires:       ros2-humble-tf2_eigen
Requires:       ros2-humble-tf2_ros

Provides:  ros2-humble-moveit_planners_ompl = 2.5.5-1
Obsoletes: ros2-humble-moveit_planners_ompl < 2.5.5-1



%description
MoveIt interface to OMPL

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros2-humble-ament_cmake-devel
Requires:       ros2-humble-eigen3_cmake_module-devel
Requires:       eigen3-devel
Requires:       fcl-devel
Requires:       libomp-devel
Requires:       poco-devel
Requires:       tinyxml-devel
Requires:       tinyxml2-devel
Requires:       urdfdom-devel
Requires:       ros2-humble-ament_cmake_gtest-devel
Requires:       ros2-humble-ament_lint_auto-devel
Requires:       ros2-humble-ament_lint_common-devel
Requires:       ros2-humble-ament_package-devel
Requires:       ros2-humble-moveit_common-devel
Requires:       ros2-humble-moveit_core-devel
Requires:       ros2-humble-moveit_msgs-devel
Requires:       ros2-humble-moveit_resources_fanuc_moveit_config-devel
Requires:       ros2-humble-moveit_resources_panda_moveit_config-devel
Requires:       ros2-humble-moveit_resources_pr2_description-devel
Requires:       ros2-humble-moveit_ros_planning-devel
Requires:       ros2-humble-ompl-devel
Requires:       ros2-humble-pluginlib-devel
Requires:       ros2-humble-rclcpp-devel
Requires:       ros2-humble-tf2_eigen-devel
Requires:       ros2-humble-tf2_ros-devel

Provides: ros2-humble-moveit_planners_ompl-devel = 2.5.5-1
Obsoletes: ros2-humble-moveit_planners_ompl-devel < 2.5.5-1


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

CFLAGS=" -Wno-error ${CFLAGS:-%optflags} -Wno-error -w" ; export CFLAGS ; \
CXXFLAGS=" -Wno-error ${CXXFLAGS:-%optflags} -Wno-error -w" ; export CXXFLAGS ; \
FFLAGS=" -Wno-error ${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS ; \
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
  --packages-select moveit_planners_ompl



# remove wrong buildroot prefixes
find %{buildroot}/%{_libdir}/ros2-humble/ -type f -exec sed -i "s:%{buildroot}::g" {} \;

rm -rf %{buildroot}/%{_libdir}/ros2-humble/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# remove __pycache__
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find . -name '*.pyc' -delete

touch files.list
find %{buildroot}/%{_libdir}/ros2-humble/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2-humble/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
# TODO: is cmake/ necessary? it stems from the yaml vendor
find %{buildroot}/%{_libdir}/ros2-humble/{lib*/pkgconfig,include/,cmake/,moveit_planners_ompl/include/,share/moveit_planners_ompl/cmake} \
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
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.5-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.4-1
- Initial humble build
