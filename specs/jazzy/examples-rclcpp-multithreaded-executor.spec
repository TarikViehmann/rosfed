# Meta Package
Name:           ros-jazzy-examples-rclcpp-multithreaded-executor
Version:        0.19.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-examples_rclcpp_multithreaded_executor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-examples_rclcpp_multithreaded_executor
Requires:       ros2-jazzy-examples_rclcpp_multithreaded_executor-devel

Obsoletes: ros-jazzy-examples-rclcpp-multithreaded-executor < 0.19.4-1

%description
Package containing example of how to implement a multithreaded
executor

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.19.4-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.19.3-1
- Update to latest release
