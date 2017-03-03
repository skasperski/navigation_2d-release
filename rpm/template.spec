Name:           ros-kinetic-nav2d
Version:        0.3.1
Release:        0%{?dist}
Summary:        ROS nav2d package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/navigation_2d
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-nav2d-exploration
Requires:       ros-kinetic-nav2d-karto
Requires:       ros-kinetic-nav2d-localizer
Requires:       ros-kinetic-nav2d-msgs
Requires:       ros-kinetic-nav2d-navigator
Requires:       ros-kinetic-nav2d-operator
Requires:       ros-kinetic-nav2d-remote
Requires:       ros-kinetic-nav2d-tutorials
BuildRequires:  ros-kinetic-catkin

%description
Meta-Package containing modules for 2D-Navigation

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Mar 03 2017 Sebastian Kasperski <sebastian.kasperski@dfki.de> - 0.3.1-0
- Autogenerated by Bloom

