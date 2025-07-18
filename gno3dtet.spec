Summary:	GNOME 3D Tetris game
Summary(pl.UTF-8):	Tetris 3D dla GNOME
Name:		gno3dtet
Version:	1.6.4
Release:	3
License:	GPL
Vendor:		Sebastien Nicoud <snicoud@home.com>
Group:		X11/Applications/Games
Source0:	ftp://webdat.com/pub/seb/gno3dtet/%{name}-%{version}.tgz
# Source0-md5:	62c01388996b648c07fc2fe46fb6bca6
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-desktop.patch
URL:		http://webdat.com/seb/3dtetris.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
Prereq:		fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var

%description
gno3dtet is a 3D Tetris-like game for GNOME.

%description -l pl.UTF-8
gno3dtet to trójwymiarowa gra podobna do Tetrisa dla GNOME.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
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
chown root:games %{_localstatedir}/games/gno3dtet.hof

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gno3dtet
%{_datadir}/sounds/gno3dtet
%{_pixmapsdir}/gno3dtet.png
%{_applnkdir}/Games/gno3dtet.desktop
%attr(664,root,games) %ghost %{_localstatedir}/games/gno3dtet.hof
