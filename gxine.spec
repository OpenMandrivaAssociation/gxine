%define name gxine
%define version 0.5.11
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
mkdir -p %buildroot%{_menudir}/
cat > %buildroot%{_menudir}/%{name} <<EOF 
?package(%name):command="%{_bindir}/%name" title="Gxine" longtitle="Xine Video Player" needs="X11" section="Multimedia/Video" icon="video_section.png" mimetypes="video/dv,video/mpeg,video/msvideo,video/quicktime,video/x-anim,video/x-avi,video/x-ms-asf,video/x-ms-wmv,video/x-msvideo,video/x-nsv,video/x-flc,video/x-fli,application/ogg,application/x-ogg,audio/basic,audio/x-mp3,audio/x-mpeg,audio/mpeg,audio/x-wav,audio/x-mpegurl,audio/x-scpls,audio/x-m4a,audio/x-ms-asf,audio/x-ms-asx,audio/x-ms-wax,application/vnd.rn-realmedia,audio/x-real-audio,audio/x-pn-realaudio,application/x-flac,audio/x-flac,misc/ultravox,application/x-matroska" accept_url="true" multiple_files="true" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Video;Player" \
  --add-category="X-MandrivaLinux-Multimedia-Video" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%post
%update_menus
%update_desktop_database

%postun
%clean_menus
%clean_desktop_database

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
%lang(de) %{_mandir}/de/man1/gxine.*
%lang(de) %{_mandir}/de/man1/gxine_client.*
%_menudir/%name

%files mozilla
%defattr(-,root,root)
%_libdir/mozilla/plugins/gxineplugin.so


