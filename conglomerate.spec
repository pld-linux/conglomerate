Summary:	Free user-friendly XML editor
Summary(pl):	Wolnodostêpny, przyjazny dla u¿ytkownika edytor XML
Name:		conglomerate
Version:	0.7.8
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	22ca1070b17d1438da155fb5e0c2af58
Patch0:		%{name}-desktop.patch
URL:		http://www.conglomerate.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	gtk-doc
BuildRequires:	intltool >= 0.28
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libxslt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conglomerate is a free user-friendly XML editor. It attempts to hide
the gory details of XML from the end-user. It can support any XML file
format, but so far we have been concentrating on DocBook support. A
goal of the project is to create a free DocBook editor that Word users
can easily learn.

%description -l pl
Conglomerate to wolnodostêpny, przyjazny dla u¿ytkownika edytor XML.
Próbuje ukryæ mordercze szczegó³y XML-a przed koñcowym u¿ytkownikiem.
Potrafi obs³u¿yæ ka¿dy format pliku XML, ale jak na razie jego rozwój
jest skoncentrowany na obs³udze dla DocBooka. Celem projektu jest
stworzenie wolnodostêpnego edytora DocBooka, ³atwego do nauczenia dla
u¿ytkowników Worda.

%prep
%setup -q
%patch0 -p1

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*.png
%{_omf_dest_dir}/*
%{_gtkdocdir}/%{name}
%{_datadir}/application-registry/*
%{_datadir}/mime-info/*
