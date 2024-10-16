# Meta Package
Name:           ros-jazzy-joint-limits
Version:        4.16.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/ros-controls/ros2_control/wiki
Summary:        Meta package for ros2-jazzy-joint_limits and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-joint_limits
Requires:       ros2-jazzy-joint_limits-devel

Obsoletes: ros-jazzy-joint-limits < 4.16.1-1

%description
Package with interfaces for handling of joint limits in controllers or
in hardware. The package also implements Saturation Joint Limiter for
position-velocity-acceleration set and other individual interfaces.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.16.1-1
- Update to latest release
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.14.0-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.13.0-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.11.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.8.0-1
- Update to latest release
