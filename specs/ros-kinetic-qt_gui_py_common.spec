Name:           ros-kinetic-qt_gui_py_common
Version:        0.3.8
Release:        1%{?dist}
Summary:        ROS package qt_gui_py_common

License:        BSD
URL:            http://ros.org/wiki/qt_gui_py_common

Source0:        https://github.com/ros-gbp/qt_gui_core-release/archive/release/kinetic/qt_gui_py_common/0.3.8-0.tar.gz#/ros-kinetic-qt_gui_py_common-0.3.8-source0.tar.gz


BuildArch: noarch

BuildRequires:  ros-kinetic-catkin

Requires:       python-rospkg
Requires:       ros-kinetic-python_qt_binding

%description
qt_gui_py_common provides common functionality for GUI plugins written
in Python.


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
  --pkg qt_gui_py_common

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
* Sun Nov 19 2017 Till Hofmann <thofmann@fedoraproject.org> - 0.3.8-1
- Update to latest release
* Fri Aug 25 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.3.4-2
- Remove all Requires: on devel packages
* Wed Aug 16 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.3.4-1
- Update auto-generated Spec file