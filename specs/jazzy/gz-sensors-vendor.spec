# Meta Package
Name:           ros-jazzy-gz-sensors-vendor
Version:        0.0.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-sensors
Summary:        Meta package for ros2-jazzy-gz_sensors_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gz_sensors_vendor
Requires:       ros2-jazzy-gz_sensors_vendor-devel

Obsoletes: ros-jazzy-gz-sensors-vendor < 0.0.4-1

%description
Vendor package for: gz-sensors8 8.2.0 Gazebo Sensors : Sensor models
for simulation

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.4-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.3-1
- Update to latest release
