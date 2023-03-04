Name:           ros-pilz_industrial_motion_planner
Version:        noetic.1.1.11
Release:        1%{?dist}
Summary:        ROS package pilz_industrial_motion_planner

License:        BSD
URL:            http://moveit.ros.org

Source0:        https://github.com/ros-gbp/moveit-release/archive/release/noetic/pilz_industrial_motion_planner/1.1.11-1.tar.gz#/ros-noetic-pilz_industrial_motion_planner-1.1.11-source0.tar.gz



# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  orocos-kdl
BuildRequires:  orocos-kdl-devel
BuildRequires:  ros-noetic-catkin-devel
BuildRequires:  ros-noetic-cmake_modules-devel
BuildRequires:  ros-noetic-code_coverage-devel
BuildRequires:  ros-noetic-joint_limits_interface-devel
BuildRequires:  ros-noetic-moveit_core-devel
BuildRequires:  ros-noetic-moveit_msgs-devel
BuildRequires:  ros-noetic-moveit_resources_panda_moveit_config-devel
BuildRequires:  ros-noetic-moveit_resources_prbt_moveit_config-devel
BuildRequires:  ros-noetic-moveit_resources_prbt_pg70_support-devel
BuildRequires:  ros-noetic-moveit_resources_prbt_support-devel
BuildRequires:  ros-noetic-moveit_ros_move_group-devel
BuildRequires:  ros-noetic-moveit_ros_planning-devel
BuildRequires:  ros-noetic-moveit_ros_planning_interface-devel
BuildRequires:  ros-noetic-pilz_industrial_motion_planner_testutils-devel
BuildRequires:  ros-noetic-pluginlib-devel
BuildRequires:  ros-noetic-roscpp-devel
BuildRequires:  ros-noetic-rostest-devel
BuildRequires:  ros-noetic-rosunit-devel
BuildRequires:  ros-noetic-tf2-devel
BuildRequires:  ros-noetic-tf2_eigen-devel
BuildRequires:  ros-noetic-tf2_geometry_msgs-devel
BuildRequires:  ros-noetic-tf2_kdl-devel
BuildRequires:  ros-noetic-tf2_ros-devel

Requires:       orocos-kdl
Requires:       ros-noetic-joint_limits_interface
Requires:       ros-noetic-moveit_core
Requires:       ros-noetic-moveit_msgs
Requires:       ros-noetic-moveit_ros_move_group
Requires:       ros-noetic-moveit_ros_planning
Requires:       ros-noetic-moveit_ros_planning_interface
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-tf2
Requires:       ros-noetic-tf2_eigen
Requires:       ros-noetic-tf2_geometry_msgs
Requires:       ros-noetic-tf2_kdl
Requires:       ros-noetic-tf2_ros

Provides:  ros-noetic-pilz_industrial_motion_planner = 1.1.11-1
Obsoletes: ros-noetic-pilz_industrial_motion_planner < 1.1.11-1
Obsoletes: ros-kinetic-pilz_industrial_motion_planner < 1.1.11-1



%description
MoveIt plugin to generate industrial trajectories PTP, LIN, CIRC and
sequences thereof.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros-noetic-catkin-devel
Requires:       orocos-kdl
Requires:       orocos-kdl-devel
Requires:       ros-noetic-cmake_modules-devel
Requires:       ros-noetic-code_coverage-devel
Requires:       ros-noetic-joint_limits_interface-devel
Requires:       ros-noetic-moveit_core-devel
Requires:       ros-noetic-moveit_msgs-devel
Requires:       ros-noetic-moveit_resources_panda_moveit_config-devel
Requires:       ros-noetic-moveit_resources_prbt_moveit_config-devel
Requires:       ros-noetic-moveit_resources_prbt_pg70_support-devel
Requires:       ros-noetic-moveit_resources_prbt_support-devel
Requires:       ros-noetic-moveit_ros_move_group-devel
Requires:       ros-noetic-moveit_ros_planning-devel
Requires:       ros-noetic-moveit_ros_planning_interface-devel
Requires:       ros-noetic-pilz_industrial_motion_planner_testutils-devel
Requires:       ros-noetic-pluginlib-devel
Requires:       ros-noetic-roscpp-devel
Requires:       ros-noetic-rostest-devel
Requires:       ros-noetic-rosunit-devel
Requires:       ros-noetic-tf2-devel
Requires:       ros-noetic-tf2_eigen-devel
Requires:       ros-noetic-tf2_geometry_msgs-devel
Requires:       ros-noetic-tf2_kdl-devel
Requires:       ros-noetic-tf2_ros-devel

Provides: ros-noetic-pilz_industrial_motion_planner-devel = 1.1.11-1
Obsoletes: ros-noetic-pilz_industrial_motion_planner-devel < 1.1.11-1
Obsoletes: ros-kinetic-pilz_industrial_motion_planner-devel < 1.1.11-1


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

source %{_libdir}/ros/setup.bash

# substitute shebang before install block because we run the local catkin script
%py3_shebang_fix .

DESTDIR=%{buildroot} ; export DESTDIR


catkin_make_isolated \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCATKIN_ENABLE_TESTING=OFF \
  -DPYTHON_VERSION=%{python3_version} \
  -DPYTHON_VERSION_NODOTS=%{python3_version_nodots} \
  --source . \
  --install \
  --install-space %{_libdir}/ros/ \
  --pkg pilz_industrial_motion_planner




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/pilz_industrial_motion_planner/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



# replace cmake python macro in shebang
for file in $(grep -rIl '^#!.*@PYTHON_EXECUTABLE@.*$' %{buildroot}) ; do
  sed -i.orig 's:^#!\s*@PYTHON_EXECUTABLE@\s*:%{__python3}:' $file
  touch -r $file.orig $file
  rm $file.orig
done


echo "This is a package automatically generated with rosfed." >> README_FEDORA
echo "See https://pagure.io/ros for more information." >> README_FEDORA
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
* Fri Mar 03 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.1.11-1
- Update to latest release
