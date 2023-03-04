Name:           ros-moveit
Version:        noetic.1.1.11
Release:        1%{?dist}
Summary:        ROS package moveit

License:        BSD
URL:            http://moveit.ros.org

Source0:        https://github.com/ros-gbp/moveit-release/archive/release/noetic/moveit/1.1.11-1.tar.gz#/ros-noetic-moveit-1.1.11-source0.tar.gz


BuildArch: noarch

# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  ros-noetic-catkin-devel

Requires:       ros-noetic-moveit_commander
Requires:       ros-noetic-moveit_core
Requires:       ros-noetic-moveit_planners
Requires:       ros-noetic-moveit_plugins
Requires:       ros-noetic-moveit_ros
Requires:       ros-noetic-moveit_setup_assistant

Provides:  ros-noetic-moveit = 1.1.11-1
Obsoletes: ros-noetic-moveit < 1.1.11-1
Obsoletes: ros-kinetic-moveit < 1.1.11-1



%description
Meta package that contains all essential package of MoveIt. Until
Summer 2016 MoveIt had been developed over multiple repositories,
where developers' usability and maintenance effort was non-trivial.
See

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ros-noetic-catkin-devel
Requires:       ros-noetic-moveit_commander-devel
Requires:       ros-noetic-moveit_core-devel
Requires:       ros-noetic-moveit_planners-devel
Requires:       ros-noetic-moveit_plugins-devel
Requires:       ros-noetic-moveit_ros-devel
Requires:       ros-noetic-moveit_setup_assistant-devel

Provides: ros-noetic-moveit-devel = 1.1.11-1
Obsoletes: ros-noetic-moveit-devel < 1.1.11-1
Obsoletes: ros-kinetic-moveit-devel < 1.1.11-1


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
  --pkg moveit




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/moveit/cmake} \
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
