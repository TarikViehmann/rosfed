# Meta Package
Name:           ros-jazzy-rosbag2-storage-default-plugins
Version:        0.26.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosbag2_storage_default_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosbag2_storage_default_plugins
Requires:       ros2-jazzy-rosbag2_storage_default_plugins-devel

Obsoletes: ros-jazzy-rosbag2-storage-default-plugins < 0.26.3-1

%description
Intermediate metapackage to point at default storage plugin(s) for
rosbag2

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.2-1
- Update to latest release