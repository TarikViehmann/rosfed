Name:           ros-kinetic-collada_parser
Version:        1.12.10
Release:        2%{?dist}
Summary:        ROS package collada_parser

License:        BSD
URL:            http://ros.org/wiki/collada_parser

Source0:        https://github.com/ros-gbp/collada_urdf-release/archive/release/kinetic/collada_parser/1.12.10-0.tar.gz#/ros-kinetic-collada_parser-1.12.10-source0.tar.gz



BuildRequires:  collada-dom-devel
BuildRequires:  urdfdom-headers-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-class_loader
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-urdf
BuildRequires:  ros-kinetic-urdf_parser_plugin

Requires:       ros-kinetic-class_loader
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-urdf_parser_plugin

%description
This package contains a C++ parser for the Collada robot description
format. The parser reads a Collada XML robot description, and creates
a C++ URDF model. Although it is possible to directly use this parser
when working with Collada robot descriptions, the preferred user API
is found in the urdf package.


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
  --pkg collada_parser

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
* Fri Aug 25 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.12.10-2
- Remove all Requires: on devel packages
* Wed Aug 16 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.12.10-1
- Update auto-generated Spec file