Summary:	GNOME 3D Tetris game
Name:		gno3dtet
Version:	1.2.0
Release:	1
License:	GPL
Group:		X11/Games
Group(pl):	X11/Gry
Vendor:		Seb's Games, Inc
Source0:	ftp://webdat.com/pub/seb/gno3dtet/%{name}-%{version}.tgz
URL:		http://webdat.com/seb/3dtetris.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
gno3dtet is a 3D Tetris-like game for GNOME.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure

make 

%install
rm -f $RPM_BUILD_ROOT

make install \
	DESTDOR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -f $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gno3dtet
%{_prefix}/var/games/gno3dtet.hof
%{_datadir}/pixmaps/gno3dtet.png
%{_applnkdir}/Games/gno3dtet.desktop
