%define upstream_name    Catalyst-Plugin-Prototype
%define upstream_version 1.33

Name:		perl-%{upstream_name}
Version:	1.330.0
Release:	6

Summary:	Plugin for Prototype
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(HTML::Prototype)
BuildRequires:	perl(Class::Data::Inheritable)
BuildArch:	noarch

%description
Helper to generate Prototype library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.330.0-3mdv2011.0
+ Revision: 654885
- rebuild for updated spec-helper

* Thu Jun 25 2009 Olivier Thauvin <nanardon@mandriva.org> 1.330.0-2mdv2011.0
+ Revision: 388901
- don't use new macros to allow backports

* Sun Jun 21 2009 Olivier Thauvin <nanardon@mandriva.org> 1.330.0-1mdv2010.0
+ Revision: 387708
- Buildrequires
- import perl-Catalyst-Plugin-Prototype


* Sun Jun 21 2009 cpan2dist 1.33-1mdv
- initial mdv release, generated with cpan2dist

