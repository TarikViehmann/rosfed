# Meta Package
Name:           ros-humble-tf2-msgs
Version:        0.25.7
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/tf2_msgs
Summary:        Meta package for ros2-humble-tf2_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-tf2_msgs
Requires:       ros2-humble-tf2_msgs-devel

Obsoletes: ros-humble-tf2-msgs < 0.25.7-1

%description
tf2_msgs

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.7-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.6-1
- Update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.5-1
- update to latest upstream
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.4-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.3-1
- update to latest upstream release
* Thu Jul 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.3-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.2-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.7.6-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.2-1
- Initial humble build
