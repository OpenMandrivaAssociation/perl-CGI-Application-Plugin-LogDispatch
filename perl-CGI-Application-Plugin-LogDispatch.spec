%define upstream_name    CGI-Application-Plugin-LogDispatch
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Add Log::Dispatch support to CGI::Application
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI::Application)
BuildRequires:	perl(Log::Dispatch)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
CGI::Application::Plugin::LogDispatch adds logging support to your the
CGI::Application manpage modules by providing a the Log::Dispatch manpage
dispatcher object that is accessible from anywhere in the application.

If you have the CGI::Application::Plugin::DevPopup manpage installed, a
"Log Entries" report is added to the popup window, containing all of the
entries that were logged during the execution of the runmode. 

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
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.20.0-2mdv2011.0
+ Revision: 653391
- rebuild for updated spec-helper

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 405776
- rebuild using %%perl_convert_version

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2009.1
+ Revision: 307144
- import perl-CGI-Application-Plugin-LogDispatch


* Wed Nov 26 2008 cpan2dist 1.02-1mdv
- initial mdv release, generated with cpan2dist

