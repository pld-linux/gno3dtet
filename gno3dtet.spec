Summary:	GNOME 3D Tetris game
Name:		gno3dtet
Version:	1.6.1
Release:	2
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Aplikacje/Spiele
Group(pl):	X11/Aplikacje/Gry
Vendor:		Sebastien Nicoud <snicoud@home.com>
Source0:	ftp://webdat.com/pub/seb/gno3dtet/%{name}-%{version}.tgz
Patch0:		%{name}-DESTDIR.patch
URL:		http://webdat.com/seb/3dtetris.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	libstdc++-devel
Prereq:		fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_localstatedir	/var

%description
gno3dtet is a 3D Tetris-like game for GNOME.

%prep
%setup -q
%patch -p1

%build
aclocal -I macros
autoconf
automake -a -c
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Gamesdir=%{_applnkdir}/Games

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch %{_localstatedir}/games/gno3dtet.hof
chmod 664 %{_localstatedir}/games/gno3dtet.hof
chown games.root %{_localstatedir}/games/gno3dtet.hof

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gno3dtet
%{_datadir}/sounds/gno3dtet
%{_pixmapsdir}/gno3dtet.png
%{_applnkdir}/Games/gno3dtet.desktop
%attr(664,root,games) %ghost %{_localstatedir}/games/gno3dtet.hof
