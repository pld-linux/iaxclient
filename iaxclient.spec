# TODO: optflags
#
# Conditional build:
%bcond_with	examples		# build with example apps
#
Summary:	A portable IAX/IAX2 protocol telephony client library
Summary(pl):	Przeno¶na biblioteka kliencka protoko³u IAX/IAX2
Name:		iaxclient
Version:	20050329
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://duch.mimuw.edu.pl/~hunter/iax/%{name}-snap-%{version}.tar.gz
# Source0-md5:	3a8b5d32f3866e3852a4bff5d868784a
Patch0:		%{name}-nodebug.patch
Patch1:		%{name}-Makefile.patch
URL:		http://iaxclient.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IAXClient is an Open Source library to implement the IAX protocol.

%description -l pl
IAXClient jest bibliotek± Open Source iplementuj±c± protokó³ IAX.

%package devel
Summary:	Header files for IAXClient library
Summary(pl):	Pliki nag³ówkowe biblioteki IAXClient
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for IAXClient library.

%description devel -l pl
Pliki nag³ówkowe biblioteki IAXClient.

%package static
Summary:	Static IAXClient library
Summary(pl):	Statyczna biblioteka IAXClient
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static IAXClient library.

%description static -l pl
Statyczna biblioteka IAXClient.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p0

%build
cd lib
%{__make}
%{__make} shared
cd ..

%if %{with examples}
cd simpleclient
%{__make} -C iax2slin

%{__make} -C testcall

# WX-windows and gtk required!
%{__make} -C iaxcomm

# Tk/Tcl
%{__make} -C tkphone
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_includedir}
install -d $RPM_BUILD_ROOT%{_docdir}

install lib/libiaxclient.{so,a} $RPM_BUILD_ROOT%{_libdir}
install lib/iaxclient.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so

#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
