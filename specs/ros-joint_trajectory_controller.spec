Name:           ros-joint_trajectory_controller
Version:        noetic.0.21.1
Release:        1%{?dist}
Summary:        ROS package joint_trajectory_controller

License:        BSD
URL:            https://github.com/ros-controls/ros_controllers/wiki

Source0:        https://github.com/ros-gbp/ros_controllers-release/archive/release/noetic/joint_trajectory_controller/0.21.1-1.tar.gz#/ros-noetic-joint_trajectory_controller-0.21.1-source0.tar.gz



# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  boost-devel
BuildRequires:  poco-devel
BuildRequires:  tinyxml-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  urdfdom-devel
BuildRequires:  ros-noetic-actionlib-devel
BuildRequires:  ros-noetic-angles-devel
BuildRequires:  ros-noetic-catkin-devel
BuildRequires:  ros-noetic-code_coverage-devel
BuildRequires:  ros-noetic-control_msgs-devel
BuildRequires:  ros-noetic-control_toolbox-devel
BuildRequires:  ros-noetic-controller_interface-devel
BuildRequires:  ros-noetic-controller_manager-devel
BuildRequires:  ros-noetic-hardware_interface-devel
BuildRequires:  ros-noetic-pluginlib-devel
BuildRequires:  ros-noetic-realtime_tools-devel
BuildRequires:  ros-noetic-roscpp-devel
BuildRequires:  ros-noetic-rostest-devel
BuildRequires:  ros-noetic-std_msgs-devel
BuildRequires:  ros-noetic-trajectory_msgs-devel
BuildRequires:  ros-noetic-urdf-devel
BuildRequires:  ros-noetic-xacro-devel

Requires:       ros-noetic-actionlib
Requires:       ros-noetic-control_toolbox
Requires:       ros-noetic-controller_interface
Requires:       ros-noetic-realtime_tools
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-urdf

Provides:  ros-noetic-joint_trajectory_controller = 0.21.1-1
Obsoletes: ros-noetic-joint_trajectory_controller < 0.21.1-1
Obsoletes: ros-kinetic-joint_trajectory_controller < 0.21.1-1



%description
Controller for executing joint-space trajectories on a group of
joints.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros-noetic-angles-devel
Requires:       ros-noetic-catkin-devel
Requires:       ros-noetic-control_msgs-devel
Requires:       ros-noetic-hardware_interface-devel
Requires:       ros-noetic-trajectory_msgs-devel
Requires:       boost-devel
Requires:       poco-devel
Requires:       tinyxml-devel
Requires:       tinyxml2-devel
Requires:       urdfdom-devel
Requires:       ros-noetic-actionlib-devel
Requires:       ros-noetic-code_coverage-devel
Requires:       ros-noetic-control_toolbox-devel
Requires:       ros-noetic-controller_interface-devel
Requires:       ros-noetic-controller_manager-devel
Requires:       ros-noetic-pluginlib-devel
Requires:       ros-noetic-realtime_tools-devel
Requires:       ros-noetic-roscpp-devel
Requires:       ros-noetic-rostest-devel
Requires:       ros-noetic-std_msgs-devel
Requires:       ros-noetic-urdf-devel
Requires:       ros-noetic-xacro-devel

Provides: ros-noetic-joint_trajectory_controller-devel = 0.21.1-1
Obsoletes: ros-noetic-joint_trajectory_controller-devel < 0.21.1-1
Obsoletes: ros-kinetic-joint_trajectory_controller-devel < 0.21.1-1


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
  --pkg joint_trajectory_controller




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/joint_trajectory_controller/cmake} \
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
* Fri Mar 03 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.21.1-1
- Update to latest release
* Fri Jan 19 2018 Tim Niemueller <tim@niemueller.de> - 0.13.2-1
- Initial package
