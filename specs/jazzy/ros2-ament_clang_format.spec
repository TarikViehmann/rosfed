Name:           ros2-jazzy-ament_clang_format
Version:        0.17.1
Release:        1%{?dist}
Summary:        ROS package ament_clang_format

License:        Apache License 2.0
URL:            http://www.ros.org/

Source0:        https://github.com/ros2-gbp/ament_lint-release/archive/release/jazzy/ament_clang_format/0.17.1-1.tar.gz#/ros2-jazzy-ament_clang_format-0.17.1-source0.tar.gz


BuildArch: noarch

# common BRs
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: make
BuildRequires: patch
BuildRequires: python3-devel
BuildRequires: python-unversioned-command
BuildRequires: python3-colcon-common-extensions
BuildRequires: python3-pip
BuildRequires: python3-pydocstyle
BuildRequires: python3-pytest
BuildRequires: python3-pytest-repeat
BuildRequires: python3-pytest-rerunfailures
BuildRequires: python3-rosdep
BuildRequires: python3-setuptools
BuildRequires: python3-vcstool

# BuildRequires:  boost-devel
# BuildRequires:  console-bridge-devel
# BuildRequires:  gtest-devel
# BuildRequires:  log4cxx-devel
# BuildRequires:  python3-devel
# BuildRequires:  python3-colcon-common-extensions
# BuildRequires:  python-unversioned-command

BuildRequires:  python3-pytest
BuildRequires:  ros2-jazzy-ament_copyright-devel
BuildRequires:  ros2-jazzy-ament_flake8-devel
BuildRequires:  ros2-jazzy-ament_package-devel
BuildRequires:  ros2-jazzy-ament_pep257-devel

Requires:       clang-tools-extra git-clang-format
Requires:       python3-pyyaml

Provides:  ros2-jazzy-ament_clang_format = 0.17.1-1
Obsoletes: ros2-jazzy-ament_clang_format < 0.17.1-1



%description
The ability to check code against style conventions using clang-format
and generate xUnit test result files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       python3-pytest
Requires:       ros2-jazzy-ament_copyright-devel
Requires:       ros2-jazzy-ament_flake8-devel
Requires:       ros2-jazzy-ament_package-devel
Requires:       ros2-jazzy-ament_pep257-devel

Provides: ros2-jazzy-ament_clang_format-devel = 0.17.1-1
Obsoletes: ros2-jazzy-ament_clang_format-devel < 0.17.1-1


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
GZ_BUILD_FROM_SURCE=1; export GZ_BUILD_FROM_SOURCE

CFLAGS=" -Wno-error ${CFLAGS:-%optflags} -Wno-error -w -Wno-error=int-conversion" ; export CFLAGS ; \
CXXFLAGS=" -Wno-error ${CXXFLAGS:-%optflags} -Wno-error -w -Wno-error=int-conversion" ; export CXXFLAGS ; \
FFLAGS=" -Wno-error ${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -w -Wno-error=int-conversion" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -w -Wno-error=int-conversion" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \

source %{_libdir}/ros2-jazzy/setup.bash

# substitute shebang before install block because we run the local catkin script
%py3_shebang_fix .

# DESTDIR=%{buildroot} ; export DESTDIR


colcon \
  build \
  --merge-install \
  --cmake-args -DPYTHON_EXECUTABLE="/usr/bin/python" \
  -DTHIRDPARTY_Asio=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
  -DCMAKE_C_FLAGS="$CFLAGS" \
  -DCMAKE_LD_FLAGS="$LDFLAGS" \
  -DBUILD_TESTING=OFF \
  --base-paths . \
  --install-base %{buildroot}/%{_libdir}/ros2-jazzy/ \
  --packages-select ament_clang_format



# remove wrong buildroot prefixes
find %{buildroot}/%{_libdir}/ros2-jazzy/ -type f -exec sed -i "s:%{buildroot}::g" {} \;

# # Move include directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/ament_clang_format/include ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/include/ament_clang_format ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/include/ament_clang_format
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-jazzy/opt/ament_clang_format/include/* %{buildroot}/%{_libdir}/ros2-jazzy/include/ament_clang_format
# fi
# 
# # Move share directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/ament_clang_format/share ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/share ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/share
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-jazzy/opt/ament_clang_format/share %{buildroot}/%{_libdir}/ros2-jazzy/
#     find %{buildroot}/%{_libdir}/ros2-jazzy/share -type f -exec sed -i "s:opt/ament_clang_format/::g" {} \;
# fi
# 
# # Move bin directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/ament_clang_format/bin ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/bin ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/bin
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-jazzy/opt/ament_clang_format/bin %{buildroot}/%{_libdir}/ros2-jazzy/
# fi
# 
# # Move extra_cmake directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/ament_clang_format/extra_cmake ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/extra_cmake ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/extra_cmake
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-jazzy/opt/ament_clang_format/extra_cmake %{buildroot}/%{_libdir}/ros2-jazzy/
#     find %{buildroot}/%{_libdir}/ros2-jazzy/extra_cmake -type f -exec sed -i "s:opt/ament_clang_format/::g" {} \;
# fi
# 
# # Move lib directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/ament_clang_format/lib ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/lib ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/lib
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-jazzy/opt/ament_clang_format/lib %{buildroot}/%{_libdir}/ros2-jazzy/lib
# fi
# 
# # Move lib64 directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/ament_clang_format/lib64 ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/lib64 ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/lib64
#     fi
#     # Move the directory
#     mv -f %{buildroot}/%{_libdir}/ros2-jazzy/opt/ament_clang_format/lib64 %{buildroot}/%{_libdir}/ros2-jazzy/lib64
# fi

rm -rf %{buildroot}/%{_libdir}/ros2-jazzy/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# remove __pycache__
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find . -name '*.pyc' -delete

touch files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/{opt,bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/{lib*/pkgconfig,include/,cmake/,ament_clang_format/include/,share/ament_clang_format/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2-jazzy/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
# find %{buildroot}/%{_libdir}/ros2-jazzy/ -name *__rosidl_generator_py.so -type f -exec patchelf --force-rpath --add-rpath "%{_libdir}/ros2/lib" {} \;

# replace cmake python macro in shebang
for file in $(grep -rIl '^#!.*@PYTHON_EXECUTABLE@.*$' %{buildroot}) ; do
  sed -i.orig 's:^#!\s*@PYTHON_EXECUTABLE@\s*:%{__python3}:' $file
  touch -r $file.orig $file
  rm $file.orig
done


echo "This is a package automatically generated with rosfed." >> README_FEDORA
echo "See  https://github.com/morxa/rosfed for more information." >> README_FEDORA
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
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
