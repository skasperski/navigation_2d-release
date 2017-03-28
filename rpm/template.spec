Name:           ros-jade-nav2d-operator
Version:        0.3.2
Release:        0%{?dist}
Summary:        ROS nav2d_operator package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/nav2d_operator
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-costmap-2d
Requires:       ros-jade-message-runtime
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-tf
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-costmap-2d
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf

%description
The operator is a lightweight, purely reactive obstacle-avoidance module for
mobile robots moving in a planar environment. The operator node works by
evaluating a set of predefined motion primitives based on a local costmap and a
desired direction. The best evaluated motion command will be send to the mobile
base.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Mar 28 2017 Sebastian Kasperski <sebastian.kasperski@dfki.de> - 0.3.2-0
- Autogenerated by Bloom

* Fri Feb 17 2017 Sebastian Kasperski <sebastian.kasperski@dfki.de> - 0.3.1-0
- Autogenerated by Bloom

* Tue Apr 19 2016 Sebastian Kasperski <sebastian.kasperski@dfki.de> - 0.3.0-0
- Autogenerated by Bloom

* Sat Jan 23 2016 Sebastian Kasperski <sebastian.kasperski@dfki.de> - 0.1.4-0
- Autogenerated by Bloom

