%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
#define commit 8a1b4228388d3284e0f112bfb2aa600e196e0f1d

Name:		plasma6-alligator
Version:	24.05.0
Release:	%{?git:0.%{git}.}1
Summary:	RSS reader for Plasma Mobile
%if 0%{?git}
Source0:	https://invent.kde.org/plasma-mobile/alligator/-/archive/%{gitbranch}/alligator-%{gitbranchd}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/alligator-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KF6Syndication)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(openssl)

%description
RSS reader for Plasma Mobile

%prep
%if 0%{?git}
%autosetup -p1 -n alligator-%{gitbranchd}
%else
%autosetup -p1 -n alligator-%{?git:%{gitbranchd}}%{!?git:%{version}}
%endif
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang alligator

%files -f alligator.lang
%{_bindir}/alligator
%{_datadir}/applications/org.kde.alligator.desktop
%{_datadir}/icons/hicolor/scalable/apps/alligator.svg
%{_datadir}/metainfo/org.kde.alligator.appdata.xml
