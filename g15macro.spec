Name:                   g15macro
Version:                1.0.3
Release:                %mkrel 5
Summary:                Simple Macro recording/playback app for G15Daemon
License:                GPL
Group:                  System/Configuration/Hardware
URL:                    http://g15daemon.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15daemon/g15macro-%{version}.tar.bz2
BuildRequires:          g15-devel
BuildRequires:          g15daemon_client-devel
BuildRequires:          g15render-devel
BuildRequires:          X11-devel
BuildRequires:          x11-proto-devel
BuildRequires:          libxtst-devel
BuildRoot:              %{_tmppath}/%{name}-%{version}-%{release}-root

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

%build
%{configure2_5x} --enable-xtest
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%defattr(-,root,root,0755)
%{_bindir}/g15macro
%{_datadir}/g15macro
