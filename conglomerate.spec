Summary:	Free user-friendly XML editor
Summary(pl):	Wolnodost�pny, przyjazny dla u�ytkownika edytor XML-a
Name:		conglomerate
Version:	0.7.12
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	8743f9d8f079fc22f6aef70efd838aac
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locale-names.patch
URL:		http://www.conglomerate.org/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	gtk-doc
BuildRequires:	gtksourceview-devel >= 0.6
BuildRequires:	intltool >= 0.28
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeprintui-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libxslt-devel >= 1.0.0
Requires(post):	GConf2
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conglomerate is a free user-friendly XML editor. It attempts to hide
the gory details of XML from the end-user. It can support any XML file
format, but so far we have been concentrating on DocBook support. A
goal of the project is to create a free DocBook editor that Word users
can easily learn.

%description -l pl
Conglomerate to wolnodost�pny, przyjazny dla u�ytkownika edytor XML-a.
Pr�buje ukry� mordercze szczeg�y XML-a przed ko�cowym u�ytkownikiem.
Potrafi obs�u�y� ka�dy format pliku XML, ale jak na razie jego rozw�j
jest skoncentrowany na obs�udze dla DocBooka. Celem projektu jest
stworzenie wolnodost�pnego edytora DocBooka, �atwego do nauczenia dla
u�ytkownik�w Worda.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*.png
%{_omf_dest_dir}/*
##%{_gtkdocdir}/%{name}
%{_datadir}/application-registry/*
%{_datadir}/mime-info/*
