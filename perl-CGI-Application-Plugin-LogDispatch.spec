
%define realname   CGI-Application-Plugin-LogDispatch
%define version    1.02
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Add Log::Dispatch support to CGI::Application
Source:     http://www.cpan.org/modules/by-module/CGI/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(CGI::Application)
BuildRequires: perl(Log::Dispatch)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

%description
CGI::Application::Plugin::LogDispatch adds logging support to your the
CGI::Application manpage modules by providing a the Log::Dispatch manpage
dispatcher object that is accessible from anywhere in the application.

If you have the CGI::Application::Plugin::DevPopup manpage installed, a
"Log Entries" report is added to the popup window, containing all of the
entries that were logged during the execution of the runmode. 



%prep
%setup -q -n %{realname}-%{version} 

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


