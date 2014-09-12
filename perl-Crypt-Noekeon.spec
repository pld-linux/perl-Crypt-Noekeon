#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Noekeon
Summary:	Crypt::Noekeon - Crypt::CBC-compliant block cipher
Summary(pl.UTF-8):	Crypt::Noekeon - szyfr blokowy kompatybilny z Crypt::CBC
Name:		perl-Crypt-Noekeon
Version:	1.0.2
Release:	6
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	51fc0d4486e2f98cf433df4cf6c4dc6a
URL:		http://search.cpan.org/dist/Crypt-Noekeon/
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_tests:BuildRequires:	perl-perldoc}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Noekeon is a 128-bit key, 128-bit block cipher designed by Joan
Daemen, Michael Peeters, Vincent Rijmen, and Gilles Van Assche.
Noekeon was submitted as a NESSIE candidate. This module supports
the Crypt::CBC interface.

%description -l pl.UTF-8
Noekeon jest 128-bitowym szyfrem blokowym ze 128-bitowym kluczem,
opracowanym przez Joan Daemen, Michaela Peetersa, Vincenta Rijmena
i Gillesa Van Assche. Noekeon został zgłoszony jako kandydat do
NESSIE. Ten moduł obsługuje interfejs Crypt::CBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

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
