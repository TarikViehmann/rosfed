# Meta Package
Name:           ros-jazzy-mcap-vendor
Version:        0.26.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-mcap_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-mcap_vendor
Requires:       ros2-jazzy-mcap_vendor-devel

Obsoletes: ros-jazzy-mcap-vendor < 0.26.4-1

%description
mcap vendor package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.4-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.2-1
- Update to latest release
