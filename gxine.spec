Summary:	GTK+ frontend for the Xine multimedia player
Name:		gxine
Version:	0.5.910
Release:	1
License:	GPLv2+
Group:		Video
Url:		https://xine.sf.net
Source0:	http://prdownloads.sourceforge.net/xine/%{name}-%{version}.tar.xz
Patch0:		gxine-no-gnome-mime-registration.patch
BuildRequires:	xine-plugins
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(mozjs185)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xext)
Requires:	xine-plugins
Obsoletes:	gxine-mozilla

%description
This is a graphical frontend for Xine based on the GTK+ toolkit.

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/gxine
%{_bindir}/gxine_client
%{_datadir}/applications/gxine.desktop
%{_datadir}/pixmaps/*
%{_datadir}/gxine/
%{_mandir}/man1/gxine.*
%{_mandir}/man1/gxine_client.*
%{_datadir}/icons/hicolor/64x64/apps/gxine.png
%lang(de) %{_mandir}/de/man1/gxine*
%lang(es) %{_mandir}/es/man1/gxine*

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%configure2_5x \
	--disable-static \
	--disable-integration-wizard \
	--with-spidermonkey=%{_includedir}/js \
        --with-gtk3 \
	--without-browser-plugin
%make JS_LIBS="-lmozjs185 -ldl -lm"

%install
%makeinstall_std

%find_lang %{name} %{name}.theme %{name}.lang

