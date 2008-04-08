Summary:	Malayalam dictionary for aspell
Summary(pl.UTF-8):	Słownik malajalam dla aspella
Name:		aspell-ml
Version:	0.03
%define	subv	1
Release:	1
Epoch:		1
License:	GPL v3+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/ml/aspell6-ml-%{version}-%{subv}.tar.bz2
# Source0-md5:	5ac03b3b0d0618b0aa470c9f5ac46866
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Malayalam dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik malajalam (lista słów) dla aspella.

%prep
%setup -q -n aspell6-ml-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
