#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : murrine
Version  : 0.98.2
Release  : 13
URL      : http://ftp.gnome.org/pub/GNOME/sources/murrine/0.98/murrine-0.98.2.tar.xz
Source0  : http://ftp.gnome.org/pub/GNOME/sources/murrine/0.98/murrine-0.98.2.tar.xz
Summary  : Murrine GTK+ Theme Engine
Group    : Development/Tools
License  : LGPL-2.1 LGPL-3.0
Requires: murrine-data = %{version}-%{release}
Requires: murrine-lib = %{version}-%{release}
Requires: murrine-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(pixman-1)

%description
This is Murrine GTK+ engine. This source code provides only the engine, get the themes @ gnomelook.org.

%package data
Summary: data components for the murrine package.
Group: Data

%description data
data components for the murrine package.


%package lib
Summary: lib components for the murrine package.
Group: Libraries
Requires: murrine-data = %{version}-%{release}
Requires: murrine-license = %{version}-%{release}

%description lib
lib components for the murrine package.


%package license
Summary: license components for the murrine package.
Group: Default

%description license
license components for the murrine package.


%prep
%setup -q -n murrine-0.98.2
cd %{_builddir}/murrine-0.98.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1593110437
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1593110437
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/murrine
cp %{_builddir}/murrine-0.98.2/COPYING %{buildroot}/usr/share/package-licenses/murrine/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
cp %{_builddir}/murrine-0.98.2/COPYING.2.1 %{buildroot}/usr/share/package-licenses/murrine/9a1929f4700d2407c70b507b3b2aaf6226a9543c
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/gtk-engines/murrine.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/gtk-2.0/2.10.0/engines/libmurrine.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/murrine/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/murrine/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
