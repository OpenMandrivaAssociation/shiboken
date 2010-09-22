Name: shiboken
Version: 0.5.0
Release: %mkrel 1
License: GPLv2
Summary: Creates the PySide bindings source files
Group: Development/KDE and Qt
URL: http://www.pyside.org
Source0:  http://www.pyside.org/files/%name-%version.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: apiextractor-devel >= 0.8.0
BuildRequires: generatorrunner-devel >= 0.6.1
BuildRequires: python-devel

%description
The Shiboken Generator (A.K.A. shiboken) is the plugin that creates the
PySide bindings source files from Qt headers and auxiliary files
(typesystems, global.h and glue files).

%files 
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_libdir}/generatorrunner/shiboken_generator.so

#------------------------------------------------------------------------------

%define libmajor 0
%define libname %mklibname %name %{libmajor}

%package -n %{libname}
Summary: Shiboken Generator core lib
Group: System/Libraries

%description -n %{libname}
Shiboken Generator core lib.

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib%{name}.so.%{libmajor}*

#------------------------------------------------------------------------------

%package devel
Summary: Devel stuff for Shiboken Generator
Group: Development/KDE and Qt
Requires: %{libname} = %{version}
Requires: %name = %{version}

%description devel
Devel stuff for Shiboken Generator.

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %buildroot

