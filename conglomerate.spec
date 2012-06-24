Summary:	Free user-friendly XML editor
Name:		conglomerate
Version:	0.5.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sf.net//conglomerate/%{name}-%{version}.tar.gz
# Source0-md5:	ad0d44832c72de13bda376aac3e4c3dc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conglomerate is a free user-friendly XML editor. It attempts to hide
the gory details of XML from the end-user. It can support any XML file
format, but so far we have been concentrating on DocBook support. A
goal of the project is to create a free DocBook editor that Word users
can easily learn.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/conge
%{_datadir}/conge
%{_desktopdir}/conge.desktop
