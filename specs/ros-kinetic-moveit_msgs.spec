Name:           ros-kinetic-moveit_msgs
Version:        0.9.1
Release:        1%{?dist}
Summary:        ROS package moveit_msgs

License:        BSD
URL:            http://moveit.ros.org

Source0:        https://github.com/ros-gbp/moveit_msgs-release/archive/release/kinetic/moveit_msgs/0.9.1-0.tar.gz#/ros-kinetic-moveit_msgs-0.9.1-source0.tar.gz


BuildArch: noarch

# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python2-devel

BuildRequires:  ros-kinetic-actionlib_msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry_msgs
BuildRequires:  ros-kinetic-message_generation
BuildRequires:  ros-kinetic-object_recognition_msgs
BuildRequires:  ros-kinetic-octomap_msgs
BuildRequires:  ros-kinetic-sensor_msgs
BuildRequires:  ros-kinetic-shape_msgs
BuildRequires:  ros-kinetic-std_msgs
BuildRequires:  ros-kinetic-trajectory_msgs

Requires:       ros-kinetic-actionlib_msgs
Requires:       ros-kinetic-geometry_msgs
Requires:       ros-kinetic-message_runtime
Requires:       ros-kinetic-object_recognition_msgs
Requires:       ros-kinetic-octomap_msgs
Requires:       ros-kinetic-sensor_msgs
Requires:       ros-kinetic-shape_msgs
Requires:       ros-kinetic-std_msgs
Requires:       ros-kinetic-trajectory_msgs

%description
Messages, services and actions used by MoveIt


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

DESTDIR=%{buildroot} ; export DESTDIR

catkin_make_isolated \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCATKIN_ENABLE_TESTING=OFF \
  --source . \
  --install \
  --install-space %{_libdir}/ros/ \
  --pkg moveit_msgs

rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,setup*,env.sh}

find %{buildroot}/%{_libdir}/ros/{bin,etc,include,lib*/pkgconfig,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list


find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list

%files -f files.list



%changelog
* Thu Jan 18 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.9.1-1
- Initial package