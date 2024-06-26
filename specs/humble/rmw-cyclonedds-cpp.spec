# Meta Package
Name:           ros-humble-rmw-cyclonedds-cpp
Version:        1.3.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rmw_cyclonedds_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rmw_cyclonedds_cpp
Requires:       ros2-humble-rmw_cyclonedds_cpp-devel

Obsoletes: ros-humble-rmw-cyclonedds-cpp < 1.3.4-1

%description
Implement the ROS middleware interface using Eclipse CycloneDDS in
C++.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.4-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.4-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.4-1
- Initial humble build
