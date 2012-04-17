%define url_ver %(echo %{version} | cut -c 1-3)

Summary: 	A dictionary support for Xfce
Name: 		xfce4-dict
Version: 	0.6.0
Release: 	%mkrel 5
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/xfce4-dict/
Source0:	http://archive.xfce.org/src/apps/xfce4-dict/%{url_ver}/%{name}-%{version}.tar.bz2
Patch1:		xfce4-dict-0.6.0-gold.patch
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-dict-plugin
Obsoletes:	xfce4-dict-plugin < 0.4.0
Provides:	xfce4-dict-plugin
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
This Xfce program allows you to search different kinds of dictionary
services for words or phrases and shows you the result.Currently you 
can query a Dict server(RFC 2229), any online dictionary service by 
opening a web browser or search for words using the aspell/ispell 
program.

%prep
%setup -q
%patch1 -p0
autoconf

%build
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{name}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS
%{_bindir}/%{name}
%{_libdir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_datadir}/applications/*.desktop
%{_mandir}/man1/%{name}.*
