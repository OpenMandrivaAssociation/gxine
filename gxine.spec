%define name gxine
%define version 0.5.906
%define release  2
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
Requires: xine-plugins >= %xinever
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires: pkgconfig(libxine) >= %xinever
BuildRequires: xine-plugins
BuildRequires: libgtk+2.0-devel
BuildRequires: pkgconfig(xaw7)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(liblircclient0) > 0.8.5-0.20090320.1mdv2009.1
BuildRequires: libjs-devel
BuildRequires: pkgconfig(nspr)

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




%changelog
* Mon Nov 28 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.906-1mdv2012.0
+ Revision: 734828
- new version
- drop patch 1
- fix build with new glib
- fix build with new js library from libmozjs185

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.905-2mdv2011.0
+ Revision: 611055
- rebuild

* Sat Jan 02 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.905-1mdv2010.1
+ Revision: 485077
- new version
- fix desktop entry again

* Mon May 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.904-1mdv2010.0
+ Revision: 374852
- new version
- bump deps

* Thu Mar 26 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.903-2mdv2009.1
+ Revision: 361255
- update libjs path
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Fri Jun 13 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.903-1mdv2009.0
+ Revision: 218667
- new version

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Apr 18 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.902-1mdv2009.0
+ Revision: 195530
- new version
- drop patch 1

* Wed Mar 12 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.901-1mdv2008.1
+ Revision: 187085
- new version
- rediff patch 0
- fix desktop file generation
- update file list

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.5.11-1mdv2008.1
+ Revision: 148213
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- replace %%{_datadir}/man by %%{_mandir}!
- fix man pages

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Thu Feb 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.11-1mdv2007.0
+ Revision: 115808
- new version

* Mon Jan 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.10-1mdv2007.1
+ Revision: 106086
- new version

* Sun Dec 17 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.9-1mdv2007.1
+ Revision: 98265
- fix buildrequires
- new version
- fix build
- fix buildrequires
- Import gxine

* Mon Oct 09 2006 Götz Waschk <waschk@mandriva.org> 0.5.8-1mdv2007.1
- fix nspr build
- rediff the patch
- New version 0.5.8

* Thu Jul 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.7-1mdv2007.0
- New release 0.5.7

* Tue Jul 04 2006 Götz Waschk <waschk@mandriva.org> 0.5.6-2mdv2007.0
- xdg menu
- fix buildrequires

* Mon May 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.6-1mdk
- New release 0.5.6

* Wed Mar 08 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.5-1mdk
- New release 0.5.5

* Tue Jan 24 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.4-1mdk
- New release 0.5.4

* Sun Dec 25 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.3-1mdk
- New release 0.5.3

* Wed Dec 21 2005 Götz Waschk <waschk@mandriva.org> 0.5.2-1mdk
- drop patch 1
- New release 0.5.2
- use mkrel

* Wed Nov 30 2005 Götz Waschk <waschk@mandriva.org> 0.5.1-2mdk
- fix menu location

* Wed Nov 30 2005 Götz Waschk <waschk@mandriva.org> 0.5.1-1mdk
- update file list
- patch for libjs detection
- drop patch 1
- New release 0.5.1

* Sun Oct 30 2005 Götz Waschk <waschk@mandriva.org> 0.5.0-2mdk
- hmm, link with libjs

* Sun Oct 30 2005 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdk
- update file list
- drop patch 1
- enable js
- New release 0.5.0

* Tue Oct 18 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.9-1mdk
- New release 0.4.9

* Tue Sep 13 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.8-1mdk
- New release 0.4.8

* Sat Aug 27 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.7-1mdk
- New release 0.4.7

* Tue Jul 19 2005 Götz Waschk <waschk@mandriva.org> 0.4.6-1mdk
- update file list
- New release 0.4.6

* Thu May 26 2005 Götz Waschk <waschk@mandriva.org> 0.4.5-2mdk
- move mozilla plugin to a separate package (Austin)

* Thu May 26 2005 Götz Waschk <waschk@mandriva.org> 0.4.5-1mdk
- New release 0.4.5

* Thu Apr 28 2005 Götz Waschk <waschk@mandriva.org> 0.4.4-1mdk
- New release 0.4.4

* Tue Mar 29 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 0.4.3-1mdk
- New release 0.4.3

* Wed Mar 09 2005 Götz Waschk <waschk@linux-mandrake.com> 0.4.2-1mdk
- patch to fix build
- disable the wizard again
- New release 0.4.2

* Fri Dec 17 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4.1-1mdk
- update file list
- source URL
- New release 0.4.1

* Sun Dec 12 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4.0-1mdk
- new version

* Sun Nov 28 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4.0-0.rc2.1mdk
- update file list
- new version

* Fri Nov 19 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4.0-0.rc1.1mdk
- fix file list
- drop patch 1
- new version

* Thu Nov 18 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.3-5mdk
- fix build
- fix mime types in the menu
- security fix for a buffer overflow

* Tue Aug 31 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.3-4mdk
- add more mime types to the menu entry
- disable gnome mime registration wizard (bug #11084)

* Sat May 15 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.3-3mdk
- drop prefix
- fix buildrequires

