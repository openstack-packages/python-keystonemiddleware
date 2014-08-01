Name:		python-keystonemiddleware
Version:	XXX
Release:	1%{?dist}
Summary:	keystone middleware modules

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz


BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	python-pbr

Requires:	python-setuptools
Requires:	python-argparse
Requires:	python-anyjson
Requires:	python-iso8601
Requires:	python-babel
Requires:	python-netaddr
Requires:	python-oslo-config
Requires:	python-keystoneclient
Requires:	python-six
Requires:	python-webob1.2
Requires:	python-requests

%description
Middleware modules designed to provide authentication and
authorization features to web services other than `Keystone

%prep

%setup -q -n keystonemiddleware-%{upstream_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%{python_sitelib}/keystonemiddleware*

%changelog
* Fri Aug 01 2014 Derek Higgins <derekh@redhat.com> - XXX
- Initial package
