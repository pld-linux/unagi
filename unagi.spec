Summary:	Unagi is a modular compositing manager
Name:		unagi
Version:	0.1
Release:	0.1
License:	GPL v3
Group:		X11/Applications
Source0:	http://projects.mini-dweeb.org/attachments/download/89/%{name}-%{version}.tar.gz
# Source0-md5:	79251ccefaa7346991939de79a8c3bbc
URL:		http://projects.mini-dweeb.org/projects/unagi
# xcb-ewmh doesn't exist yet in PLD
BuildRequires:	xcb-ewmh
BuildRequires:	xcb-proto
BuildRequires:	xcb-util-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unagi is a modular compositing manager which aims to be efficient,
lightweight and responsive.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
