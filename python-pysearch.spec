Name:           python-pysearch
Version:        3.1
Release:        %mkrel 1
Summary:        Python API for the Yahoo Search Webservices API
Group:          Development/Python
License:        GPLv2+
URL:            http://sourceforge.net/projects/pysearch/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:       pYsearch
BuildRequires:  python-devel


%description
pYsearch implements a Python API for the Yahoo Search Webservices API.
 It provides an object orientated abstraction of the web services,
 with emphasis on ease of use and extensibility.

%prep
%setup -q -n %{name}-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog README NEWS docs
%{python_sitelib}/yahoo/*
%{python_sitelib}/pYsearch*



%changelog
* Sun Nov 28 2010 Stéphane Téletchéa <steletch@mandriva.org> 3.1-1mdv2011.0
+ Revision: 602514
- Update RPM group name

  + Tadej Panjtar <tadej@mandriva.org>
    - import python-pysearch


