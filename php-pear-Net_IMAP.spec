%define		status		stable
%define		pearname	Net_IMAP
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - an implementation of the IMAP protocol
Summary(pl.UTF-8):	%{pearname} - implementacja protokołu IMAP
Name:		php-pear-%{pearname}
Version:	1.1.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	942b549b00bb17c76dcbfba88223534c
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

mv docs/Net_IMAP/docs tests
mv docs/Net_IMAP/* .
mv .%{php_pear_dir}/data/Net_IMAP/composer.json .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE.txt install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/*.php
