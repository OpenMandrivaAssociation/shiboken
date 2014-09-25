Name:		shiboken
Version:	1.2.2
Release:	1
License:	GPLv2
Summary:	Creates the PySide bindings source files
Group:		Development/KDE and Qt
URL:		http://www.pyside.org
Source0:	http://download.qt-project.org/official_releases/pyside/%{name}-%{version}.tar.bz2
Source100:	shiboken.rpmlintrc
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	python-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
Obsoletes:	generatorrunner < 0.6.17

%description
The Shiboken Generator (A.K.A. shiboken) is the plugin that creates the
PySide bindings source files from Qt headers and auxiliary files
(typesystems, global.h and glue files).

Since 1.1.1 it's merged with apiextractor and generatorrunner.

%files
%{_bindir}/%{name}
%{py_platsitedir}/%{name}.so
%{_mandir}/man1/*

#------------------------------------------------------------------------------

%define libmajor 1
%define libname %mklibname %{name} %{libmajor}

%define oldapiexlib %mklibname apiextractor 0
%define oldgenlib %mklibname genrunner 0

%package -n %{libname}
Summary:	Shiboken Generator core lib
Group:		System/Libraries
Obsoletes:	%{oldapiexlib} <= 0.10.11
Obsoletes:	%{oldgenlib} <= 0.6.17

%description -n %{libname}
Shiboken Generator core lib.

%files -n %{libname}
%{_libdir}/lib%{name}-python%{py_ver}.so.%{libmajor}*

#------------------------------------------------------------------------------

%define oldapiexdev %mklibname apiextractor -d

%package devel
Summary:	Devel stuff for Shiboken Generator
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{oldapiexdev} < 0.10.11
Obsoletes:	generatorrunner-devel < 0.6.17

%description devel
Devel stuff for Shiboken Generator.

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%__sed 's/-Wno-strict-aliasing/-fno-strict-aliasing/' -i CMakeLists.txt
%cmake
%make

%install
%makeinstall_std -C build
