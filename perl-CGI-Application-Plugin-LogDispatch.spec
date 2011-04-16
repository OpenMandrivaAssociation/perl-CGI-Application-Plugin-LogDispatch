%define upstream_name    CGI-Application-Plugin-LogDispatch
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Add Log::Dispatch support to CGI::Application
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CGI::Application)
BuildRequires: perl(Log::Dispatch)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
