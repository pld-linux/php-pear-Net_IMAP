%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       IMAP
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - an implementation of the IMAP protocol
Summary(pl):	%{_pearname} - implementacja protoko�u IMAP
Name:		php-pear-%{_pearname}
Version:	0.5.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	aeaa1abb15ea16cc6f2357a6c01c9448
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an implementation of the IMAP4Rev1 protocol using PEAR's
Net_Socket and Auth_SASL class.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa dostarcza implementacj� protoko�u IMAP4Rev1 przy u�yciu
PEAR-owych klas Net_Socket oraz Auth_SASL.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
