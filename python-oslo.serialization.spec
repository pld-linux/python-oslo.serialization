#
# Conditional build:
%bcond_with	doc	# do build doc (missing deps)
%bcond_with	tests	# do perform "make test" (missing deps)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Oslo Serialization library
Name:		python-oslo.serialization
Version:	2.27.0
Release:	7
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/o/oslo.serialization/oslo.serialization-%{version}.tar.gz
# Source0-md5:	2b8d57696687f69929c1fa41ba490a26
URL:		https://pypi.python.org/pypi/oslo.serialization
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%endif
Requires:	python-msgpack >= 0.4.0
Requires:	python-oslo.utils >= 3.20.0
Requires:	python-pbr >= 2.0.0
Requires:	python-pytz >= 2013.6
Requires:	python-six >= 1.9.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The oslo.serialization library provides support for representing
objects in transmittable and storable formats, such as Base64, JSON
and MessagePack.

%package -n python3-oslo.serialization
Summary:	Oslo Serialization library
Group:		Libraries/Python
Requires:	python3-msgpack >= 0.4.0
Requires:	python3-oslo.utils >= 3.20.0
Requires:	python3-pbr >= 2.0.0
Requires:	python3-pytz >= 2013.6
Requires:	python3-six >= 1.9.0

%description -n python3-oslo.serialization
The oslo.serialization library provides support for representing
objects in transmittable and storable formats, such as Base64, JSON
and MessagePack.

%package apidocs
Summary:	API documentation for Python oslo.serialization module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona oslo.serialization
Group:		Documentation

%description apidocs
API documentation for Pythona oslo.serialization module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona oslo.serialization.

%prep
%setup -q -n oslo.serialization-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/oslo_serialization
%{py_sitescriptdir}/oslo.serialization-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-oslo.serialization
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/oslo_serialization
%{py3_sitescriptdir}/oslo.serialization-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
