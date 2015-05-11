Name:           ros-indigo-nav2d-remote
Version:        0.1.4
Release:        0%{?dist}
Summary:        ROS nav2d_remote package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/remote_controller
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-nav2d-navigator
Requires:       ros-indigo-nav2d-operator
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-nav2d-navigator
BuildRequires:  ros-indigo-nav2d-operator
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
This package is used to manually control a robot that uses the operator and
navigator node from navigation_2d. Currently there is one node to control one
robot with a joystick and one to control multiple robots in simulation. It can
send commands directly to the operator or start and stop navigator actions.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon May 11 2015 Sebastian Kasperski <sebastian.kasperski@dfki.de> - 0.1.4-0
- Autogenerated by Bloom

