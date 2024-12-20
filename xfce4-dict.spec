%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_rebuild_configure 1

Summary: 	A dictionary support for Xfce
Name: 		xfce4-dict
Version:	0.8.8
Release:	1
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/applications/xfce4-dict/
Source0:	http://archive.xfce.org/src/apps/xfce4-dict/%{url_ver}/%{name}-%{version}.tar.bz2
Patch1:		xfce4-dict-0.6.0-gold.patch
Requires:	xfce4-panel >= 4.10
BuildRequires:	xfce4-panel-devel >= 4.10
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-dict-plugin = %{version}
Obsoletes:	xfce4-dict-plugin < 0.4.0
Provides:	xfce4-dict-plugin = %{version}


%description
This Xfce program allows you to search different kinds of dictionary
services for words or phrases and shows you the result.Currently you 
can query a Dict server(RFC 2229), any online dictionary service by 
opening a web browser or search for words using the aspell/ispell 
program.

%prep
%setup -q

%build
%configure \
	--disable-static
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog AUTHORS
%{_bindir}/%{name}
%{_libdir}/xfce4/panel/plugins/*
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/applications/*.desktop
%{_mandir}/man1/%{name}.*
%{_iconsdir}/hicolor/*x*/apps/org.xfce.Dictionary.png
