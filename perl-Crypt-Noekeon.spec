#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	Noekeon
Summary:	Crypt::Noekeon - Crypt::CBC-compliant block cipher
Summary(pl):	Crypt::Noekeon - szyfr blokowy kompatybilny z Crypt::CBC
Name:		perl-Crypt-Noekeon
Version:	1.0.1
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	411f60628c548c6ce946cf62b671e5f1
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Noekeon is a 128-bit key, 128-bit block cipher designed by Joan
Daemen, Michael Peeters, Vincent Rijmen, and Gilles Van Assche.
Noekeon was submitted as a NESSIE candidate. This module supports
the Crypt::CBC interface.

%description -l pl
Noekeon jest 128-bitowym szyfrem blokowym ze 128-bitowym kluczem,
opracowanym przez Joan Daemen, Michaela Peetersa, Vincenta Rijmena
i Gillesa Van Assche. Noekeon zosta³ zg³oszony jako kandydat do
NESSIE. Ten modu³ obs³uguje interfejs Crypt::CBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd examples
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
for f in * ; do
	sed -e "s@#!/usr/local/bin/perl@#!/usr/bin/perl@" $f \
		> $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/Noekeon.pm
%dir %{perl_vendorarch}/auto/Crypt/Noekeon
%{perl_vendorarch}/auto/Crypt/Noekeon/Noekeon.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Noekeon/Noekeon.so
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
