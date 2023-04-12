Name:           ros2-navigation2
Version:        humble.1.1.6
Release:        1%{?dist}
Summary:        ROS package navigation2

License:        Apache-2.0
URL:            http://www.ros.org/

Source0:        https://github.com/SteveMacenski/navigation2-release/archive/release/humble/navigation2/1.1.6-1.tar.gz#/ros2-humble-navigation2-1.1.6-source0.tar.gz



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

BuildRequires:  ros2-humble-ament_cmake-devel
BuildRequires:  ros2-humble-ament_package-devel

Requires:       ros2-humble-nav2_amcl
Requires:       ros2-humble-nav2_behavior_tree
Requires:       ros2-humble-nav2_behaviors
Requires:       ros2-humble-nav2_bt_navigator
Requires:       ros2-humble-nav2_collision_monitor
Requires:       ros2-humble-nav2_constrained_smoother
Requires:       ros2-humble-nav2_controller
Requires:       ros2-humble-nav2_core
Requires:       ros2-humble-nav2_costmap_2d
Requires:       ros2-humble-nav2_dwb_controller
Requires:       ros2-humble-nav2_lifecycle_manager
Requires:       ros2-humble-nav2_map_server
Requires:       ros2-humble-nav2_msgs
Requires:       ros2-humble-nav2_navfn_planner
Requires:       ros2-humble-nav2_planner
Requires:       ros2-humble-nav2_regulated_pure_pursuit_controller
Requires:       ros2-humble-nav2_rotation_shim_controller
Requires:       ros2-humble-nav2_rviz_plugins
Requires:       ros2-humble-nav2_simple_commander
Requires:       ros2-humble-nav2_smac_planner
Requires:       ros2-humble-nav2_smoother
Requires:       ros2-humble-nav2_theta_star_planner
Requires:       ros2-humble-nav2_util
Requires:       ros2-humble-nav2_velocity_smoother
Requires:       ros2-humble-nav2_voxel_grid
Requires:       ros2-humble-nav2_waypoint_follower

Provides:  ros2-humble-navigation2 = 1.1.6-1
Obsoletes: ros2-humble-navigation2 < 1.1.6-1



%description
ROS2 Navigation Stack

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros2-humble-ament_cmake-devel
Requires:       ros2-humble-ament_package-devel
Requires:       ros2-humble-nav2_amcl-devel
Requires:       ros2-humble-nav2_behavior_tree-devel
Requires:       ros2-humble-nav2_behaviors-devel
Requires:       ros2-humble-nav2_bt_navigator-devel
Requires:       ros2-humble-nav2_collision_monitor-devel
Requires:       ros2-humble-nav2_constrained_smoother-devel
Requires:       ros2-humble-nav2_controller-devel
Requires:       ros2-humble-nav2_core-devel
Requires:       ros2-humble-nav2_costmap_2d-devel
Requires:       ros2-humble-nav2_dwb_controller-devel
Requires:       ros2-humble-nav2_lifecycle_manager-devel
Requires:       ros2-humble-nav2_map_server-devel
Requires:       ros2-humble-nav2_msgs-devel
Requires:       ros2-humble-nav2_navfn_planner-devel
Requires:       ros2-humble-nav2_planner-devel
Requires:       ros2-humble-nav2_regulated_pure_pursuit_controller-devel
Requires:       ros2-humble-nav2_rotation_shim_controller-devel
Requires:       ros2-humble-nav2_rviz_plugins-devel
Requires:       ros2-humble-nav2_simple_commander-devel
Requires:       ros2-humble-nav2_smac_planner-devel
Requires:       ros2-humble-nav2_smoother-devel
Requires:       ros2-humble-nav2_theta_star_planner-devel
Requires:       ros2-humble-nav2_util-devel
Requires:       ros2-humble-nav2_velocity_smoother-devel
Requires:       ros2-humble-nav2_voxel_grid-devel
Requires:       ros2-humble-nav2_waypoint_follower-devel

Provides: ros2-humble-navigation2-devel = 1.1.6-1
Obsoletes: ros2-humble-navigation2-devel < 1.1.6-1


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
  -DBUILD_TESTING=OFF \
  --base-paths . \
  --install-base %{buildroot}/%{_libdir}/ros2/ \
  --packages-select navigation2



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
find %{buildroot}/%{_libdir}/ros2/{lib*/pkgconfig,include/,cmake/,navigation2/include/,share/navigation2/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
# find %{buildroot}/%{_libdir}/ros2/ -name *__rosidl_generator_py.so -type f -exec patchelf --force-rpath --add-rpath "%{_libdir}/ros2/lib" {} \;

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
* Mon Apr 10 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.6-1
- update to latest upsteam
