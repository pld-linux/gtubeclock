# TODO
#	- pl Comment in desktop file
#	- pl summary and description
#
Summary:	A nixie tube clock for GNOME
#Summary(pl):
Name:		gtubeclock
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.bonnyswan.com/gtubeclock/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	94dffc6431e29cc25ae68f4318c33e05
Patch0:		%{name}-desktop.patch
URL:		http://www.bonnyswan.com/gtubeclock/
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtubeclock is a simple digital clock for GNOME/GTK+. The default
appearance resambles nixie tubes, those old digital displays that
pre-date LEDs. It also has support for other artwork.

#%description -l pl
# TODO

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
