#define snapshot 20210401
#define commit 8a1b4228388d3284e0f112bfb2aa500e196e0f1d

Name:		alligator
Version:	21.06
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	RSS reader for Plasma Mobile
%if 0%{?snapshot}
Source0:	https://invent.kde.org/plasma-mobile/alligator/-/archive/master/alligator-master.tar.bz2
%else
Source0:	https://download.kde.org/stable/plasma-mobile/%{version}/alligator-%{version}.tar.xz
%endif
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
%if 0%{?snapshot}
%autosetup -p1 -n alligator-master
%else
%autosetup -p1
%endif
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/alligator
%{_datadir}/applications/org.kde.alligator.desktop
%{_datadir}/icons/hicolor/scalable/apps/alligator.svg
%{_datadir}/metainfo/org.kde.alligator.appdata.xml
