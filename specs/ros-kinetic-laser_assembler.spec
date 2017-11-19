Name:           ros-kinetic-laser_assembler
Version:        1.7.4
Release:        2%{?dist}
Summary:        ROS package laser_assembler

License:        BSD
URL:            http://www.ros.org/

Source0:        https://github.com/ros-gbp/laser_assembler-release/archive/release/kinetic/laser_assembler/1.7.4-0.tar.gz#/ros-kinetic-laser_assembler-1.7.4-source0.tar.gz



BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-filters
BuildRequires:  ros-kinetic-laser_geometry
BuildRequires:  ros-kinetic-message_filters
BuildRequires:  ros-kinetic-message_generation
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-sensor_msgs
BuildRequires:  ros-kinetic-tf

Requires:       ros-kinetic-filters
Requires:       ros-kinetic-laser_geometry
Requires:       ros-kinetic-message_filters
Requires:       ros-kinetic-message_runtime
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor_msgs
Requires:       ros-kinetic-tf

%description
Provides nodes to assemble point clouds from either LaserScan or
PointCloud messages


%prep

%setup -c -T
tar --strip-components=1 -xf %{SOURCE0}

%build
# nothing to do here


%install
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \


source %{_libdir}/ros/setup.bash

DESTDIR=%{buildroot} ; export DESTDIR

catkin_make_isolated \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  --source . \
  --install \
  --install-space %{_libdir}/ros/ \
  --pkg laser_assembler

rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,setup*,env.sh}

find %{buildroot}/%{_libdir}/ros/{bin,etc,include,lib/pkgconfig,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list


find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list

%files -f files.list



%changelog
* Fri Aug 25 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.7.4-2
- Remove all Requires: on devel packages
* Wed Aug 16 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.7.4-1
- Update auto-generated Spec file