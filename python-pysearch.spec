%define debug_package %{nil}

Name:           python-pysearch
Version:        3.1
Release:        3
Summary:        Python API for the Yahoo Search Webservices API
Group:          Development/Python
License:        GPLv2+
URL:            http://sourceforge.net/projects/pysearch/
Source0:        %{name}-%{version}.tar.gz
Provides:       pYsearch
BuildRequires:  python-devel

%description
pYsearch implements a Python API for the Yahoo Search Webservices API.
 It provides an object orientated abstraction of the web services,
 with emphasis on ease of use and extensibility.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog README NEWS docs
%{py_puresitedir}/yahoo/*
%{py_puresitedir}/pYsearch*
