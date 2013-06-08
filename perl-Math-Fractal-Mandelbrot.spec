#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Fractal-Mandelbrot
Summary:	Math::Fractal::Mandelbrot - calculate points in the Mandelbrot fractal
Summary(pl.UTF-8):	Math::Fractal::Mandelbrot - obliczanie punktów we fraktalu Mandelbrota
Name:		perl-Math-Fractal-Mandelbrot
Version:	0.04
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b3658ce83d925e109b678dfcfa21dabf
URL:		http://search.cpan.org/dist/Math-Fractal-Mandelbrot/
BuildRequires:	perl-YAML
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module calculates points, horizontal/vertical stripes or
rectangular areas of the famous Mandelbrot fractal.

%description -l pl.UTF-8
Ten moduł oblicza punkty, poziome lub pionowe pasy lub prostokątne
obszary słynnego fraktala Mandelbrota.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES CREDITS README TODO
%dir %{perl_vendorarch}/Math/Fractal
%{perl_vendorarch}/Math/Fractal/Mandelbrot.pm
%dir %{perl_vendorarch}/auto/Math/Fractal
%dir %{perl_vendorarch}/auto/Math/Fractal/Mandelbrot
%{perl_vendorarch}/auto/Math/Fractal/Mandelbrot/Mandelbrot.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Fractal/Mandelbrot/Mandelbrot.so
%{_mandir}/man3/*
