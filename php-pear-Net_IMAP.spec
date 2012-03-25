%define		status		stable
%define		pearname	Net_IMAP
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - an implementation of the IMAP protocol
Summary(pl.UTF-8):	%{pearname} - implementacja protokołu IMAP
Name:		php-pear-%{pearname}
Version:	1.1.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	79ea05dfc3af6ae2fa276831b4cceb8a
URL:		http://pear.php.net/package/Net_IMAP/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-Net_Socket >= 1.0.8
Suggests:	php-pear-Auth_SASL
Obsoletes:	php-pear-Net_IMAP-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Auth/SASL.*)

%description
Provides an implementation of the IMAP4Rev1 protocol using PEAR's
Net_Socket and Auth_SASL class.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Klasa dostarcza implementację protokołu IMAP4Rev1 przy użyciu
PEAR-owych klas Net_Socket oraz Auth_SASL.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Net_IMAP/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/*.php
