%define snapshot 20200710
%define commit ae62f708713657e9eb8e614a6b1b95613d34ae11

Name:		alligator
Version:	0.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	RSS reader for Plasma Mobile
Source0:	https://invent.kde.org/plasma-mobile/alligator/-/archive/master/alligator-master.tar.bz2
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Syndication)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	pkgconfig(openssl)

%description
RSS reader for Plasma Mobile

%prep
%autosetup -p1 -n alligator-master
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/alligator
%{_datadir}/applications/org.kde.alligator.desktop
%{_datadir}/icons/hicolor/scalable/apps/alligator.svg
%{_datadir}/metainfo/org.kde.alligator.appdata.xml
