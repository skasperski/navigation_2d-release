Name:           ros-jade-nav2d-karto
Version:        0.3.1
Release:        0%{?dist}
Summary:        ROS nav2d_karto package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/robot_operator
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-nav-msgs
Requires:       ros-jade-nav2d-localizer
Requires:       ros-jade-nav2d-msgs
Requires:       ros-jade-roscpp
Requires:       ros-jade-tf
Requires:       ros-jade-visualization-msgs
Requires:       suitesparse-devel
Requires:       tbb-devel
BuildRequires:  eigen3-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-nav-msgs
BuildRequires:  ros-jade-nav2d-localizer
BuildRequires:  ros-jade-nav2d-msgs
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-visualization-msgs
BuildRequires:  suitesparse-devel
BuildRequires:  tbb-devel

%description
Graph-based Simultaneous Localization and Mapping module. Includes OpenKarto
GraphSLAM library by &quot;SRI International&quot;.

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
* Fri Feb 17 2017 Sebastian Kasperski <sebastian.kasperski@dfki.de> - 0.3.1-0
- Autogenerated by Bloom

* Tue Apr 19 2016 Sebastian Kasperski <sebastian.kasperski@dfki.de> - 0.3.0-0
- Autogenerated by Bloom

* Sat Jan 23 2016 Sebastian Kasperski <sebastian.kasperski@dfki.de> - 0.1.4-0
- Autogenerated by Bloom

