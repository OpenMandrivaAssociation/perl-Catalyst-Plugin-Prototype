%define upstream_name    Catalyst-Plugin-Prototype
%define upstream_version 1.33

Name:       perl-%{upstream_name}
Version:    1.330.0
Release:    %mkrel 3

Summary:    Plugin for Prototype
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(HTML::Prototype)
BuildRequires: perl(Class::Data::Inheritable)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Helper to generate Prototype library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ._Changes Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

