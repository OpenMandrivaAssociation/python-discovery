Name:		python-discovery
Version:	1.6.2
Release:	1
Summary:	Python interpreter discovery
License:	MIT
Group:		Development/Python
URL:		https://github.com/tox-dev/python-discovery
Source0:	https://files.pythonhosted.org/packages/source/p/python-discovery/python_discovery-%{version}.tar.gz
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildSystem:	python
BuildArch:	noarch

%description
Library for finding Python interpreters installed on the system.

%build -p
# The sdist is not a git checkout. hatch-vcs still accepts this.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%doc README.md
%license LICENSE
%{python_sitelib}/python_discovery
%{python_sitelib}/python_discovery-%{version}.dist-info
