#
# Conditional build:
%bcond_with	examples		# build with example apps
#
Summary:	a portable IAX/IAX2 protocol telephony client library.
Summary(pl):	przeno¶na biblioteka kliencka protoku³u IAX/IAX2
Name:		iaxclient
Version:	20050329
Release:	0.1
License:	LGPL
Group:		Development/Libraries
Source0:	http://duch.mimuw.edu.pl/~hunter/iax/%{name}-snap-%{version}.tar.gz
# Source0-md5:	3a8b5d32f3866e3852a4bff5d868784a
Patch0:		%{name}-nodebug.patch
URL:		http://iaxclient.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IAXClient is an Open Source library to implement the IAX protocol.

%description -l pl
IAXClient jest bibliotek± Open Source iplementuj±c± protokó³ IAX.

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

%build

cd lib
%{__make}
%{__make} shared
cd ..

%if %{with examples}
cd simpleclient
cd iax2slin
%{__make}
cd ..

cd testcall
%{__make}
cd ..

# WX-windows and gtk required!
cd iaxcomm
%{__make}
cd ..

# WX-windows and gtk required!
cd iaxcomm
%{__make}
cd ..

# Tk/Tcl
cd tkphone
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}

install lib/libiaxclient.{so,a} $RPM_BUILD_ROOT%{_libdir}
install lib/iaxclient.h $RPM_BUILD_ROOT%{_includedir}/

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%attr(755,root,root) %{_libdir}/lib*.so

# initscript and its config
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

%files static
%defattr(644,root,root,755)
#%doc extras/*.gz
%{_libdir}/lib*.a
