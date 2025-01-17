Name:		shiboken
Version:	1.2.4
Release:	5
License:	GPLv2
Summary:	Creates the PySide bindings source files
Group:		Development/KDE and Qt
URL:		https://www.pyside.org
Source0:	https://github.com/PySide/Shiboken/archive/%{version}.tar.gz
Source100:	shiboken.rpmlintrc
Patch0:		1.2.2-Fix-tests-with-Python-3.patch
Patch1:		python-3.5.patch
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
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

%package -n python2-shiboken

%files -n python2-shiboken
%{_bindir}/%{name}-%py2ver
%py2_platsitedir/%{name}.so

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
%{_libdir}/lib%{name}*cpython*.so.%{libmajor}*

#------------------------------------------------------------------------------

%define libmajor 1
%define libname_py2 %mklibname %{name}_python2.7 %{libmajor}

%package -n %{libname_py2}
Summary:        Shiboken Generator core lib
Group:          System/Libraries

%description -n %{libname_py2}
Shiboken Generator core lib.

%files -n %{libname_py2}
%{_libdir}/lib%{name}*python2*.so.%{libmajor}*

#------------------------------------------------------------------------------

%define oldapiexdev %mklibname apiextractor -d

%package devel
Summary:	Devel stuff for Shiboken Generator
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libname_py2} = %{version}-%{release}
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
%setup -qn Shiboken-%{version}
# Fix inconsistent naming of libshiboken.so and ShibokenConfig.cmake,
# caused by the usage of a different version suffix with python >= 3.2
#sed -i -e "/get_config_var('SOABI')/d" cmake/Modules/FindPython3InterpWithDebug.cmake
%autopatch -p1

cp -a . %{py2dir}

%build

pushd %py2dir
%cmake
%make
popd

%cmake -DUSE_PYTHON3=True
%make

%install
pushd %{py2dir}
%makeinstall_std -C build
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-%{python2_version}
mv %{buildroot}%{_mandir}/man1/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}-%{python2_version}.1
popd
%makeinstall_std -C build



