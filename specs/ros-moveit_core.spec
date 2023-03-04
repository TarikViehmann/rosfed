Name:           ros-moveit_core
Version:        noetic.1.1.11
Release:        1%{?dist}
Summary:        ROS package moveit_core

License:        BSD
URL:            http://moveit.ros.org

Source0:        https://github.com/ros-gbp/moveit-release/archive/release/noetic/moveit_core/1.1.11-1.tar.gz#/ros-noetic-moveit_core-1.1.11-source0.tar.gz



# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  assimp
BuildRequires:  boost-devel
BuildRequires:  bullet-devel
BuildRequires:  console-bridge-devel
BuildRequires:  eigen3-devel
BuildRequires:  fcl-devel
BuildRequires:  libccd-devel
BuildRequires:  octomap-devel
BuildRequires:  orocos-kdl
BuildRequires:  orocos-kdl-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  tinyxml-devel
BuildRequires:  urdfdom-devel
BuildRequires:  urdfdom-headers-devel
BuildRequires:  ros-noetic-angles-devel
BuildRequires:  ros-noetic-catkin-devel
BuildRequires:  ros-noetic-eigen_stl_containers-devel
BuildRequires:  ros-noetic-geometric_shapes-devel
BuildRequires:  ros-noetic-geometry_msgs-devel
BuildRequires:  ros-noetic-kdl_parser-devel
BuildRequires:  ros-noetic-moveit_msgs-devel
BuildRequires:  ros-noetic-moveit_resources_panda_moveit_config-devel
BuildRequires:  ros-noetic-moveit_resources_pr2_description-devel
BuildRequires:  ros-noetic-octomap_msgs-devel
BuildRequires:  ros-noetic-pluginlib-devel
BuildRequires:  ros-noetic-pybind11_catkin-devel
BuildRequires:  ros-noetic-random_numbers-devel
BuildRequires:  ros-noetic-rosconsole-devel
BuildRequires:  ros-noetic-roslib-devel
BuildRequires:  ros-noetic-rostest-devel
BuildRequires:  ros-noetic-rostime-devel
BuildRequires:  ros-noetic-rosunit-devel
BuildRequires:  ros-noetic-ruckig-devel
BuildRequires:  ros-noetic-sensor_msgs-devel
BuildRequires:  ros-noetic-shape_msgs-devel
BuildRequires:  ros-noetic-srdfdom-devel
BuildRequires:  ros-noetic-std_msgs-devel
BuildRequires:  ros-noetic-tf2_eigen-devel
BuildRequires:  ros-noetic-tf2_geometry_msgs-devel
BuildRequires:  ros-noetic-tf2_kdl-devel
BuildRequires:  ros-noetic-trajectory_msgs-devel
BuildRequires:  ros-noetic-urdf-devel
BuildRequires:  ros-noetic-visualization_msgs-devel
BuildRequires:  ros-noetic-xmlrpcpp-devel

Requires:       assimp
Requires:       fcl-devel
Requires:       octomap-devel
Requires:       ros-noetic-eigen_stl_containers
Requires:       ros-noetic-geometric_shapes
Requires:       ros-noetic-geometry_msgs
Requires:       ros-noetic-kdl_parser
Requires:       ros-noetic-moveit_msgs
Requires:       ros-noetic-octomap_msgs
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-pybind11_catkin
Requires:       ros-noetic-random_numbers
Requires:       ros-noetic-rosconsole
Requires:       ros-noetic-roslib
Requires:       ros-noetic-rostime
Requires:       ros-noetic-ruckig
Requires:       ros-noetic-sensor_msgs
Requires:       ros-noetic-shape_msgs
Requires:       ros-noetic-srdfdom
Requires:       ros-noetic-std_msgs
Requires:       ros-noetic-tf2_eigen
Requires:       ros-noetic-tf2_geometry_msgs
Requires:       ros-noetic-trajectory_msgs
Requires:       ros-noetic-urdf
Requires:       ros-noetic-visualization_msgs
Requires:       ros-noetic-xmlrpcpp

Provides:  ros-noetic-moveit_core = 1.1.11-1
Obsoletes: ros-noetic-moveit_core < 1.1.11-1
Obsoletes: ros-kinetic-moveit_core < 1.1.11-1



%description
Core libraries used by MoveIt

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       ros-noetic-catkin-devel
Requires:       assimp
Requires:       boost-devel
Requires:       bullet-devel
Requires:       console-bridge-devel
Requires:       eigen3-devel
Requires:       fcl-devel
Requires:       libccd-devel
Requires:       octomap-devel
Requires:       orocos-kdl
Requires:       orocos-kdl-devel
Requires:       python3-devel
Requires:       tinyxml-devel
Requires:       urdfdom-devel
Requires:       urdfdom-headers-devel
Requires:       ros-noetic-angles-devel
Requires:       ros-noetic-eigen_stl_containers-devel
Requires:       ros-noetic-geometric_shapes-devel
Requires:       ros-noetic-geometry_msgs-devel
Requires:       ros-noetic-kdl_parser-devel
Requires:       ros-noetic-moveit_msgs-devel
Requires:       ros-noetic-moveit_resources_panda_moveit_config-devel
Requires:       ros-noetic-moveit_resources_pr2_description-devel
Requires:       ros-noetic-octomap_msgs-devel
Requires:       ros-noetic-pluginlib-devel
Requires:       ros-noetic-pybind11_catkin-devel
Requires:       ros-noetic-random_numbers-devel
Requires:       ros-noetic-rosconsole-devel
Requires:       ros-noetic-roslib-devel
Requires:       ros-noetic-rostest-devel
Requires:       ros-noetic-rostime-devel
Requires:       ros-noetic-rosunit-devel
Requires:       ros-noetic-ruckig-devel
Requires:       ros-noetic-sensor_msgs-devel
Requires:       ros-noetic-shape_msgs-devel
Requires:       ros-noetic-srdfdom-devel
Requires:       ros-noetic-std_msgs-devel
Requires:       ros-noetic-tf2_eigen-devel
Requires:       ros-noetic-tf2_geometry_msgs-devel
Requires:       ros-noetic-tf2_kdl-devel
Requires:       ros-noetic-trajectory_msgs-devel
Requires:       ros-noetic-urdf-devel
Requires:       ros-noetic-visualization_msgs-devel
Requires:       ros-noetic-xmlrpcpp-devel

Provides: ros-noetic-moveit_core-devel = 1.1.11-1
Obsoletes: ros-noetic-moveit_core-devel < 1.1.11-1
Obsoletes: ros-kinetic-moveit_core-devel < 1.1.11-1


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
  --pkg moveit_core




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/moveit_core/cmake} \
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
* Wed Apr 29 2020 Till Hofmann <thofmann@fedoraproject.org> - melodic.1.0.3-1
- Update to latest release
* Wed Jul 24 2019 Till Hofmann <thofmann@fedoraproject.org> - melodic.1.0.2-1
- Update to latest release
* Wed Nov 07 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.9.15-1
- Update to latest release
* Wed May 30 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.9.12-1
- Update to latest release
* Thu Jan 18 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.9.11-1
- Initial package
