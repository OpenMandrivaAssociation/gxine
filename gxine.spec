%define name gxine
%define version 0.5.906
%define release %mkrel 1
%define xinever 1.1.16.3-2mdv
%define fname %name-%version

Summary: GTK+ frontend for the Xine multimedia player
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/xine/%{fname}.tar.bz2
Patch0: gxine-no-gnome-mime-registration.patch
Patch2: gxine-0.5.906-fix-glib-includes.patch
License: GPLv2+
Group: Video
URL: http://xine.sf.net
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: xine-plugins >= %xinever
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires: libxine-devel >= %xinever
BuildRequires: xine-plugins
BuildRequires: libgtk+2.0-devel
BuildRequires: libxaw-devel
BuildRequires: libxext-devel
BuildRequires: liblirc-devel > 0.8.5-0.20090320.1mdv2009.1
BuildRequires: libjs-devel
BuildRequires: libnspr-devel

%description
This is a graphical frontend for Xine based on the GTK+ toolkit.

%package mozilla
Summary: Xine video player plugin for Mozilla
Group: Video
Requires: %name = %version

%description mozilla
This is a video player plugin for Mozilla and compatible web browsers
based on the Xine engine.

%prep
%setup -q -n %fname
%apply_patches

#autoreconf -fi

%build
export LDFLAGS="-L%_prefix/X11R6/lib"
export CPPFLAGS=$(pkg-config --cflags mozilla-nspr)
%configure2_5x --disable-integration-wizard --with-spidermonkey=%_includedir/js
%make JS_LIBS="-lmozjs185 -ldl -lm"

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
rm -f %buildroot/%_libdir/gxine/*a
mkdir -p %buildroot/%_libdir/mozilla/plugins
mv %buildroot/%_libdir/gxine/gxineplugin.so %buildroot/%_libdir/mozilla/plugins
%find_lang %name
%find_lang %name.theme
cat %name.theme.lang >> %name.lang

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_bindir/gxine
%_bindir/gxine_client
%{_datadir}/applications/gxine.desktop
%{_datadir}/pixmaps/*
%{_datadir}/gxine/
%{_mandir}/man1/gxine.*
%{_mandir}/man1/gxine_client.*
%{_datadir}/icons/hicolor/64x64/apps/gxine.png
%lang(de) %{_mandir}/de/man1/gxine*
%lang(es) %{_mandir}/es/man1/gxine*



%files mozilla
%defattr(-,root,root)
%_libdir/mozilla/plugins/gxineplugin.so


