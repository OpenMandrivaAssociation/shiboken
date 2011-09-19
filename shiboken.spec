Name: shiboken
Version: 1.0.4
Release: 3
License: GPLv2
Summary: Creates the PySide bindings source files
Group: Development/KDE and Qt
URL: http://www.pyside.org
Source0:  http://www.pyside.org/files/%name-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: apiextractor-devel >= 0.10.4
BuildRequires: generatorrunner-devel >= 0.6.11
BuildRequires: python-devel

%description
The Shiboken Generator (A.K.A. shiboken) is the plugin that creates the
PySide bindings source files from Qt headers and auxiliary files
(typesystems, global.h and glue files).

%files 
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_libdir}/generatorrunner/shiboken_generator.so

#------------------------------------------------------------------------------

%define libmajor 1
%define libname %mklibname %name %{libmajor}

%package -n %{libname}
Summary: Shiboken Generator core lib
Group: System/Libraries

%description -n %{libname}
Shiboken Generator core lib.

%files -n %{libname}
%{_libdir}/lib%{name}-python%{py_ver}.so.%{libmajor}*

#------------------------------------------------------------------------------

%package devel
Summary: Devel stuff for Shiboken Generator
Group: Development/KDE and Qt
Requires: %{libname} = %{version}
Requires: %name = %{version}

%description devel
Devel stuff for Shiboken Generator.

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/*

#------------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}

%build
sed 's/-Wno-strict-aliasing/-fno-strict-aliasing/' -i CMakeLists.txt
%cmake
%make

%install
%makeinstall_std -C build
