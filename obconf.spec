Summary:	Tool for configuring the Openbox window manager
Name:		obconf
Version:	2.0.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://icculus.org/openbox/obconf/%{name}-%{version}.tar.gz
# Source0-md5:	9271c5d2dc366d61f73665a5e8bceabc
URL:		http://openbox.org/obconf/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-autopoint
BuildRequires:	libglade-devel
BuildRequires:	libtool
BuildRequires:	openbox-devel
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ObConf allows you to configure Openbox in real-time. You can change
options such as the theme, desktop names, and focus settings.

%prep
%setup -q

%{__sed} -i 's|no|nb|' po/LINGUAS
%{__mv} po/{no,nb}.po
%{__rm} po/stamp-po

%build
%{__autopoint}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_mime_database

%postun
%update_desktop_database_postun
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/obconf.glade
%{_datadir}/%{name}/*.png
%{_datadir}/mime/packages/obconf.xml
%{_desktopdir}/obconf.desktop
%{_pixmapsdir}/obconf.png

