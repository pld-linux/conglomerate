Summary:	Free user-friendly XML editor
Summary(pl):	Wolnodostêpny, przyjazny dla u¿ytkownika edytor XML-a
Name:		conglomerate
Version:	0.7.16
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	75e35bd95e6a781d1346083b097f0c71
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locale-names.patch
Patch2:		%{name}-missing_files.patch
URL:		http://www.conglomerate.org/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	enchant-devel >= 0.1.0
BuildRequires:	gtk+2-devel >= 2:2.4.3
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gtksourceview-devel >= 0.6
BuildRequires:	intltool >= 0.30
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeprintui-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libxslt-devel >= 1.0.0
Requires(post):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	gtk+2 >= 2:2.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conglomerate is a free user-friendly XML editor. It attempts to hide
the gory details of XML from the end-user. It can support any XML file
format, but so far we have been concentrating on DocBook support. A
goal of the project is to create a free DocBook editor that Word users
can easily learn.

%description -l pl
Conglomerate to wolnodostêpny, przyjazny dla u¿ytkownika edytor XML-a.
Próbuje ukryæ mordercze szczegó³y XML-a przed koñcowym u¿ytkownikiem.
Potrafi obs³u¿yæ ka¿dy format pliku XML, ale jak na razie jego rozwój
jest skoncentrowany na obs³udze dla DocBooka. Celem projektu jest
stworzenie wolnodostêpnego edytora DocBooka, ³atwego do nauczenia dla
u¿ytkowników Worda.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv po/{no,nb}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
/usr/bin/scrollkeeper-update
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*.png
%{_pixmapsdir}/%{name}
%{_omf_dest_dir}/*
%{_gtkdocdir}/%{name}
%{_datadir}/application-registry/*
%{_datadir}/mime-info/*
