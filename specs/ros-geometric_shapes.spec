Name:           ros-geometric_shapes
Version:        noetic.0.7.3
Release:        1%{?dist}
Summary:        ROS package geometric_shapes

License:        BSD
URL:            http://www.ros.org/

Source0:        https://github.com/ros-gbp/geometric_shapes-release/archive/release/noetic/geometric_shapes/0.7.3-1.tar.gz#/ros-noetic-geometric_shapes-0.7.3-source0.tar.gz



# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  assimp-devel
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  eigen3-devel
BuildRequires:  gtest-devel
BuildRequires:  octomap-devel
BuildRequires:  pkgconfig
BuildRequires:  qhull-devel
BuildRequires:  ros-noetic-catkin-devel
BuildRequires:  ros-noetic-eigen_stl_containers-devel
BuildRequires:  ros-noetic-random_numbers-devel
BuildRequires:  ros-noetic-resource_retriever-devel
BuildRequires:  ros-noetic-roscpp_serialization-devel
BuildRequires:  ros-noetic-rosunit-devel
BuildRequires:  ros-noetic-shape_msgs-devel
BuildRequires:  ros-noetic-visualization_msgs-devel

Requires:       assimp
Requires:       octomap-devel
Requires:       ros-noetic-eigen_stl_containers
Requires:       ros-noetic-random_numbers
Requires:       ros-noetic-resource_retriever
Requires:       ros-noetic-shape_msgs
Requires:       ros-noetic-visualization_msgs

Provides:  ros-noetic-geometric_shapes = 0.7.3-1
Obsoletes: ros-noetic-geometric_shapes < 0.7.3-1
Obsoletes: ros-kinetic-geometric_shapes < 0.7.3-1



%description
Generic definitions of geometric shapes and bodies.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros-noetic-catkin-devel
Requires:       assimp-devel
Requires:       boost-devel
Requires:       console-bridge-devel
Requires:       eigen3-devel
Requires:       gtest-devel
Requires:       octomap-devel
Requires:       pkgconfig
Requires:       qhull-devel
Requires:       ros-noetic-eigen_stl_containers-devel
Requires:       ros-noetic-random_numbers-devel
Requires:       ros-noetic-resource_retriever-devel
Requires:       ros-noetic-roscpp_serialization-devel
Requires:       ros-noetic-rosunit-devel
Requires:       ros-noetic-shape_msgs-devel
Requires:       ros-noetic-visualization_msgs-devel

Provides: ros-noetic-geometric_shapes-devel = 0.7.3-1
Obsoletes: ros-noetic-geometric_shapes-devel < 0.7.3-1
Obsoletes: ros-kinetic-geometric_shapes-devel < 0.7.3-1


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
  --pkg geometric_shapes




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/geometric_shapes/cmake} \
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
* Fri Mar 03 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.7.3-1
- Update to latest release
* Wed Jul 24 2019 Till Hofmann <thofmann@fedoraproject.org> - melodic.0.6.1-1
- Update to latest release
* Fri Jul 12 2019 Till Hofmann <thofmann@fedoraproject.org> - 0.5.4-4
- Remove ROS distro from package name
* Tue May 22 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.5.4-3
- devel also requires: the devel package of each run dependency
* Tue May 22 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.5.4-2
- devel also requires: the devel package of each run dependency
* Tue May 15 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.5.4-1
- Also add upstream's exec_depend as Requires:
* Tue Feb 20 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.5.3-4
- Replace Recommends: with Requires: in devel subpackage
* Tue Feb 20 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.5.3-3
- Fix Requires: in devel subpackage
* Mon Feb 19 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.5.3-2
- Add Recommends: for all BRs to the devel subpackage
* Tue Feb 06 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.5.3-1
- Split devel package
* Fri Aug 25 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.5.2-2
- Remove all Requires: on devel packages
* Wed Aug 16 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.5.2-1
- Update auto-generated Spec file
