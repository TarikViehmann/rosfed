Name:           ros2-humble-desktop
Version:        0.10.0
Release:        1%{?dist}
Summary:        ROS package desktop

License:        Apache License 2.0
URL:            http://www.ros.org/

Source0:        https://github.com/ros2-gbp/variants-release/archive/release/iron/desktop/0.10.0-3.tar.gz#/ros2-iron-desktop-0.10.0-source0.tar.gz


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

BuildRequires:  ros2-iron-ament_cmake-devel
BuildRequires:  ros2-iron-ament_package-devel

Requires:       ros2-iron-action_tutorials_cpp
Requires:       ros2-iron-action_tutorials_interfaces
Requires:       ros2-iron-action_tutorials_py
Requires:       ros2-iron-angles
Requires:       ros2-iron-composition
Requires:       ros2-iron-demo_nodes_cpp
Requires:       ros2-iron-demo_nodes_cpp_native
Requires:       ros2-iron-demo_nodes_py
Requires:       ros2-iron-depthimage_to_laserscan
Requires:       ros2-iron-dummy_map_server
Requires:       ros2-iron-dummy_robot_bringup
Requires:       ros2-iron-dummy_sensors
Requires:       ros2-iron-examples_rclcpp_minimal_action_client
Requires:       ros2-iron-examples_rclcpp_minimal_action_server
Requires:       ros2-iron-examples_rclcpp_minimal_client
Requires:       ros2-iron-examples_rclcpp_minimal_composition
Requires:       ros2-iron-examples_rclcpp_minimal_publisher
Requires:       ros2-iron-examples_rclcpp_minimal_service
Requires:       ros2-iron-examples_rclcpp_minimal_subscriber
Requires:       ros2-iron-examples_rclcpp_minimal_timer
Requires:       ros2-iron-examples_rclcpp_multithreaded_executor
Requires:       ros2-iron-examples_rclpy_executors
Requires:       ros2-iron-examples_rclpy_minimal_action_client
Requires:       ros2-iron-examples_rclpy_minimal_action_server
Requires:       ros2-iron-examples_rclpy_minimal_client
Requires:       ros2-iron-examples_rclpy_minimal_publisher
Requires:       ros2-iron-examples_rclpy_minimal_service
Requires:       ros2-iron-examples_rclpy_minimal_subscriber
Requires:       ros2-iron-image_tools
Requires:       ros2-iron-intra_process_demo
Requires:       ros2-iron-joy
Requires:       ros2-iron-lifecycle
Requires:       ros2-iron-logging_demo
Requires:       ros2-iron-pcl_conversions
Requires:       ros2-iron-pendulum_control
Requires:       ros2-iron-pendulum_msgs
Requires:       ros2-iron-quality_of_service_demo_cpp
Requires:       ros2-iron-quality_of_service_demo_py
Requires:       ros2-iron-ros_base
Requires:       ros2-iron-rqt_common_plugins
Requires:       ros2-iron-rviz2
Requires:       ros2-iron-rviz_default_plugins
Requires:       ros2-iron-teleop_twist_joy
Requires:       ros2-iron-teleop_twist_keyboard
Requires:       ros2-iron-tlsf
Requires:       ros2-iron-tlsf_cpp
Requires:       ros2-iron-topic_monitor
Requires:       ros2-iron-turtlesim

Provides:  ros2-iron-desktop = 0.10.0-1
Obsoletes: ros2-iron-desktop < 0.10.0-1



%description
A package which extends 'ros_base' and includes high level packages
like vizualization tools and demos.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ros2-iron-ament_cmake-devel
Requires:       ros2-iron-ament_package-devel
Requires:       ros2-iron-action_tutorials_cpp-devel
Requires:       ros2-iron-action_tutorials_interfaces-devel
Requires:       ros2-iron-action_tutorials_py-devel
Requires:       ros2-iron-angles-devel
Requires:       ros2-iron-composition-devel
Requires:       ros2-iron-demo_nodes_cpp-devel
Requires:       ros2-iron-demo_nodes_cpp_native-devel
Requires:       ros2-iron-demo_nodes_py-devel
Requires:       ros2-iron-depthimage_to_laserscan-devel
Requires:       ros2-iron-dummy_map_server-devel
Requires:       ros2-iron-dummy_robot_bringup-devel
Requires:       ros2-iron-dummy_sensors-devel
Requires:       ros2-iron-examples_rclcpp_minimal_action_client-devel
Requires:       ros2-iron-examples_rclcpp_minimal_action_server-devel
Requires:       ros2-iron-examples_rclcpp_minimal_client-devel
Requires:       ros2-iron-examples_rclcpp_minimal_composition-devel
Requires:       ros2-iron-examples_rclcpp_minimal_publisher-devel
Requires:       ros2-iron-examples_rclcpp_minimal_service-devel
Requires:       ros2-iron-examples_rclcpp_minimal_subscriber-devel
Requires:       ros2-iron-examples_rclcpp_minimal_timer-devel
Requires:       ros2-iron-examples_rclcpp_multithreaded_executor-devel
Requires:       ros2-iron-examples_rclpy_executors-devel
Requires:       ros2-iron-examples_rclpy_minimal_action_client-devel
Requires:       ros2-iron-examples_rclpy_minimal_action_server-devel
Requires:       ros2-iron-examples_rclpy_minimal_client-devel
Requires:       ros2-iron-examples_rclpy_minimal_publisher-devel
Requires:       ros2-iron-examples_rclpy_minimal_service-devel
Requires:       ros2-iron-examples_rclpy_minimal_subscriber-devel
Requires:       ros2-iron-image_tools-devel
Requires:       ros2-iron-intra_process_demo-devel
Requires:       ros2-iron-joy-devel
Requires:       ros2-iron-lifecycle-devel
Requires:       ros2-iron-logging_demo-devel
Requires:       ros2-iron-pcl_conversions-devel
Requires:       ros2-iron-pendulum_control-devel
Requires:       ros2-iron-pendulum_msgs-devel
Requires:       ros2-iron-quality_of_service_demo_cpp-devel
Requires:       ros2-iron-quality_of_service_demo_py-devel
Requires:       ros2-iron-ros_base-devel
Requires:       ros2-iron-rqt_common_plugins-devel
Requires:       ros2-iron-rviz2-devel
Requires:       ros2-iron-rviz_default_plugins-devel
Requires:       ros2-iron-teleop_twist_joy-devel
Requires:       ros2-iron-teleop_twist_keyboard-devel
Requires:       ros2-iron-tlsf-devel
Requires:       ros2-iron-tlsf_cpp-devel
Requires:       ros2-iron-topic_monitor-devel
Requires:       ros2-iron-turtlesim-devel

Provides: ros2-iron-desktop-devel = 0.10.0-1
Obsoletes: ros2-iron-desktop-devel < 0.10.0-1


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

source %{_libdir}/ros2-humble/setup.bash

# substitute shebang before install block because we run the local catkin script
%py3_shebang_fix .

# DESTDIR=%{buildroot} ; export DESTDIR


colcon \
  build \
  --merge-install \
  --cmake-args -DPYTHON_EXECUTABLE="/usr/bin/python" \
  -DTHIRDPARTY_Asio=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_CXX_FLAGS="$CXXFLAGS -Wno-error=maybe-uninitialized -Wno-error=null-dereference" \
  -DCMAKE_C_FLAGS="$CFLAGS" \
  -DCMAKE_LD_FLAGS="$LDFLAGS" \
  -DBUILD_TESTING=OFF \
  --base-paths . \
  --install-base %{buildroot}/%{_libdir}/ros2-humble/ \
  --packages-select desktop



# remove wrong buildroot prefixes
find %{buildroot}/%{_libdir}/ros2-humble/ -type f -exec sed -i "s:%{buildroot}::g" {} \;

rm -rf %{buildroot}/%{_libdir}/ros2-humble/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# remove __pycache__
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find . -name '*.pyc' -delete

touch files.list
find %{buildroot}/%{_libdir}/ros2-humble/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2-humble/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
# TODO: is cmake/ necessary? it stems from the yaml vendor
find %{buildroot}/%{_libdir}/ros2-humble/{lib*/pkgconfig,include/,cmake/,desktop/include/,share/desktop/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2-humble/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
# find %{buildroot}/%{_libdir}/ros2-humble/ -name *__rosidl_generator_py.so -type f -exec patchelf --force-rpath --add-rpath "%{_libdir}/ros2/lib" {} \;

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
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.5.0-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- Initial humble build
