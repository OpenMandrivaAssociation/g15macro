Name:                   g15macro
Version:                1.0.3
Release:                9
Summary:                Simple Macro recording/playback app for G15Daemon
License:                GPLv2+
Group:                  System/Configuration/Hardware
URL:                    http://g15daemon.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15daemon/g15macro-%{version}.tar.bz2
Patch0:                 g15macro-1.0.3-rosa-linkage.patch
BuildRequires:          g15-devel
BuildRequires:          g15daemon_client-devel
BuildRequires:          g15render-devel
BuildRequires:          pkgconfig(x11)
BuildRequires:          pkgconfig(xtst)

%description
A simple Macro recording/playback app for G15Daemon.

Requires X11, libg15render, and the XTEST extension headers to compile, and
XTEST extension in order to function.

Features:
- records both keyboard and mouse activity, playback via 'G' hotkey
- up to 56 macros can be created (using the 'M' keys to select a palette).
- Each macro can have up to 128 steps

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure2_5x --enable-xtest
%make

%install
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_docdir}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%defattr(-,root,root,0755)
%{_bindir}/g15macro
%{_datadir}/g15macro


%changelog
* Thu Feb 03 2011 Funda Wang <fwang@mandriva.org> 1.0.3-7mdv2011.0
+ Revision: 635471
- tighten BR

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-6mdv2011.0
+ Revision: 618387
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0.3-5mdv2010.0
+ Revision: 428982
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-4mdv2009.0
+ Revision: 245589
- rebuild

* Mon Feb 11 2008 David Walluck <walluck@mandriva.org> 1.0.3-2mdv2008.1
+ Revision: 165002
- enable xtest

* Fri Feb 08 2008 David Walluck <walluck@mandriva.org> 1.0.3-1mdv2008.1
+ Revision: 163935
- fix file list
- import g15macro


