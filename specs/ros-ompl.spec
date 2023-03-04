Name:           ros-ompl
Version:        noetic.1.6.0
Release:        1%{?dist}
Summary:        ROS package ompl

License:        BSD
URL:            https://ompl.kavrakilab.org

Source0:        https://github.com/ros-gbp/ompl-release/archive/release/noetic/ompl/1.6.0-1.tar.gz#/ros-noetic-ompl-1.6.0-source0.tar.gz



# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  flann-devel
BuildRequires:  ode-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-noetic-catkin-devel


Provides:  ros-noetic-ompl = 1.6.0-1
Obsoletes: ros-noetic-ompl < 1.6.0-1
Obsoletes: ros-kinetic-ompl < 1.6.0-1



%description
OMPL is a free sampling-based motion planning library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
Requires:       boost-devel
Requires:       eigen3-devel
Requires:       flann-devel
Requires:       ode-devel
Requires:       pkgconfig
Requires:       ros-noetic-catkin-devel

Provides: ros-noetic-ompl-devel = 1.6.0-1
Obsoletes: ros-noetic-ompl-devel < 1.6.0-1
Obsoletes: ros-kinetic-ompl-devel < 1.6.0-1


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
  -DCMAKE_INSTALL_LIBDIR=%{_libdir}/ros/lib \
  -DOMPL_REGISTRATION=OFF \
  --source . \
  --install \
  --install-space %{_libdir}/ros/ \
  --pkg ompl




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/ompl/cmake} \
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
* Fri Mar 03 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.6.0-1
- Update to latest release
* Wed Jul 24 2019 Till Hofmann <thofmann@fedoraproject.org> - melodic.1.4.2-1
- Update to latest release
* Thu Nov 08 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.2.3-2
- Add missing BR flann-devel
* Tue May 22 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.2.3-1
- Update to latest release
* Fri Jan 19 2018 Tim Niemueller <tim@niemuelle.de> - 1.2.1-2
- Add flags to fix lib path and disable registration

* Thu Jan 18 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.2.1-1
- Initial package
