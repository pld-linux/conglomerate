Summary:	Free user-friendly XML editor
Summary(pl.UTF-8):   Wolnodostępny, przyjazny dla użytkownika edytor XML-a
Name:		conglomerate
Version:	0.9.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/conglomerate/%{name}-%{version}.tar.gz
# Source0-md5:	49ad67492e947d6c15e5b875d8360890
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locale-names.patch
URL:		http://www.conglomerate.org/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	enchant-devel >= 0.1.0
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gtksourceview-devel >= 1.2.0
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeprintui-devel >= 2.10.2
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	libxslt-devel >= 1.1.14
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires:	gtk+2 >= 2:2.6.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conglomerate is a free user-friendly XML editor. It attempts to hide
the gory details of XML from the end-user. It can support any XML file
format, but so far we have been concentrating on DocBook support. A
goal of the project is to create a free DocBook editor that Word users
can easily learn.

%description -l pl.UTF-8
Conglomerate to wolnodostępny, przyjazny dla użytkownika edytor XML-a.
Próbuje ukryć mordercze szczegóły XML-a przed końcowym użytkownikiem.
Potrafi obsłużyć każdy format pliku XML, ale jak na razie jego rozwój
jest skoncentrowany na obsłudze dla DocBooka. Celem projektu jest
stworzenie wolnodostępnego edytora DocBooka, łatwego do nauczenia dla
użytkowników Worda.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv po/{no,nb}.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--disable-schemas-install \
	--with-html-dir=%{_gtkdocdir} \
	--enable-printing
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/{application-registry,mime-info}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install conglomerate.schemas
%scrollkeeper_update_post
%update_desktop_database_post

%preun
%gconf_schema_uninstall conglomerate.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_pixmapsdir}/%{name}
%{_omf_dest_dir}/*
%{_gtkdocdir}/%{name}
