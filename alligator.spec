%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
#define commit 8a1b4228388d3284e0f112bfb2aa600e196e0f1d

Name:		alligator
Version:	25.12.1
Release:	%{?git:0.%{git}.}1
Summary:	RSS reader for Plasma Mobile
%if 0%{?git}
Source0:	https://invent.kde.org/plasma-mobile/alligator/-/archive/%{gitbranch}/alligator-%{gitbranchd}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/alligator-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6ColorScheme)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KF6Syndication)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(openssl)

%rename plasma6-alligator

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
RSS reader for Plasma Mobile

%files -f %{name}.lang
%{_bindir}/alligator
%{_datadir}/applications/org.kde.alligator.desktop
%{_datadir}/icons/hicolor/scalable/apps/alligator.svg
%{_datadir}/metainfo/org.kde.alligator.appdata.xml
%{_datadir}/qlogging-categories6/alligator.categories
