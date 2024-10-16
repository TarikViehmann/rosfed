# Meta Package
Name:           ros-jazzy-topic-monitor
Version:        0.33.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-topic_monitor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-topic_monitor
Requires:       ros2-jazzy-topic_monitor-devel

Obsoletes: ros-jazzy-topic-monitor < 0.33.4-1

%description
Package containing tools for monitoring ROS 2 topics.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.4-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.2-1
- Update to latest release
