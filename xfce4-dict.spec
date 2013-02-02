%define url_ver %(echo %{version} | cut -c 1-3)

Summary: 	A dictionary support for Xfce
Name: 		xfce4-dict
Version: 	0.6.0
Release:	6
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/xfce4-dict/
Source0:	http://archive.xfce.org/src/apps/xfce4-dict/%{url_ver}/%{name}-%{version}.tar.bz2
Patch1:		xfce4-dict-0.6.0-gold.patch
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel
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


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 0.6.0-5mdv2012.0
+ Revision: 791553
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 0.6.0-4
+ Revision: 790041
- Rebuild

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-3
+ Revision: 633059
- rebuild for new Xfce 4.8.0

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-2mdv2011.0
+ Revision: 615577
- the mass rebuild of 2010.1 packages

* Thu Dec 31 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-1mdv2010.1
+ Revision: 484473
- update to new version 0.6.0

* Sat May 09 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.3-1mdv2010.0
+ Revision: 373808
- update to new version 0.5.3

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.2-2mdv2009.1
+ Revision: 349197
- rebuild whole xfce

* Sat Dec 06 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.2-1mdv2009.1
+ Revision: 310956
- update to new version 0.5.2

* Mon Nov 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-1mdv2009.1
+ Revision: 306370
- update to new version 0.5.1

* Tue Nov 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-1mdv2009.1
+ Revision: 302306
- update to new version 0.5.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-2mdv2009.1
+ Revision: 294945
- rebuild for new Xfce4.6 beta1
- update to new version 0.4.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Mon May 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-1mdv2009.0
+ Revision: 209076
- add source and spec files
- Created package structure for xfce4-dict.

