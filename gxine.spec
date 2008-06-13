%define name gxine
%define version 0.5.903
%define release %mkrel 1
%define xinever 1-0.beta10.1mdk
%define fname %name-%version

Summary: GTK+ frontend for the Xine multimedia player
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/xine/%{fname}.tar.bz2
Patch: gxine-no-gnome-mime-registration.patch
License: GPL
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
BuildRequires: liblirc-devel
BuildRequires: libjs-devel
BuildRequires: libnspr-devel
BuildRequires: desktop-file-utils

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
%patch -p1

%build
export LDFLAGS="-L%_prefix/X11R6/lib"
export CPPFLAGS=$(pkg-config --cflags mozilla-nspr)
%configure2_5x --disable-integration-wizard --with-spidermonkey=%_includedir/js-1.5
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
rm -f %buildroot/%_libdir/gxine/*a
mkdir -p %buildroot/%_libdir/mozilla/plugins
mv %buildroot/%_libdir/gxine/gxineplugin.so %buildroot/%_libdir/mozilla/plugins
%find_lang %name
%find_lang %name.theme
cat %name.theme.lang >> %name.lang
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Video;Player" \
  --add-category="X-MandrivaLinux-Multimedia-Video" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

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


