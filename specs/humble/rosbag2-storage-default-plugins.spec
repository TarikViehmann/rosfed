# Meta Package
Name:           ros-humble-rosbag2-storage-default-plugins
Version:        0.15.11
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rosbag2_storage_default_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rosbag2_storage_default_plugins
Requires:       ros2-humble-rosbag2_storage_default_plugins-devel

Obsoletes: ros-humble-rosbag2-storage-default-plugins < 0.15.11-1

%description
ROSBag2 SQLite3 storage plugin

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.11-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.9-1
- Update to latest release
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.8-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.7-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.7-1
- update to latest upstream release
* Tue Aug 08 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.7-1
- update to latest upstream
* Thu Jun 29 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.6-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.4-1
- Initial humble build