# Meta Package
Name:           ros-jazzy-logging-demo
Version:        0.33.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-logging_demo and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-logging_demo
Requires:       ros2-jazzy-logging_demo-devel

Obsoletes: ros-jazzy-logging-demo < 0.33.4-1

%description
Examples for using and configuring loggers.

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
