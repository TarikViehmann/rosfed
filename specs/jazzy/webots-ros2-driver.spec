# Meta Package
Name:           ros-jazzy-webots-ros2-driver
Version:        2023.1.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Summary:        Meta package for ros2-jazzy-webots_ros2_driver and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-webots_ros2_driver
Requires:       ros2-jazzy-webots_ros2_driver-devel

Obsoletes: ros-jazzy-webots-ros2-driver < 2023.1.3-1

%description
Implementation of the Webots - ROS 2 interface

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2023.1.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2023.1.2-1
- Update to latest release
