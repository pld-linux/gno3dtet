Name: gno3dtet
Version: 1.2.0
Release: 1
Summary: GNOME 3D Tetris game
Copyright: GPL
Vendor: Seb's Games, Inc
Url: http://webdat.com/seb/3dtetris.html
Group: Amusements/Games
Source: ftp://webdat.com/pub/seb/gno3dtet/gno3dtet-1.2.0.tgz
Packager: Sebastien Nicoud <snicoud@rmi.net>

%description
gno3dtet is a 3D Tetris-like game for GNOME

%prep

%setup

%build
configure --prefix=/usr
make 

%install
make install

%files
/usr/bin/gno3dtet
/usr/var/games/gno3dtet.hof
/usr/share/pixmaps/gno3dtet.png
/usr/share/gnome/apps/Games/gno3dtet.desktop
/usr/share/gnome/help/gno3dtet/C/gno3dtet.html
/usr/share/gnome/help/gno3dtet/C/copying.html
/usr/share/gnome/help/gno3dtet/C/topic.dat
