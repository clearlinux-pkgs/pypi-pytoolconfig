#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pytoolconfig
Version  : 1.2.2
Release  : 5
URL      : https://files.pythonhosted.org/packages/9b/20/f6327067e79d7f36c89cb6b52b83befb6918672b3d8eb432d8793b08a967/pytoolconfig-1.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9b/20/f6327067e79d7f36c89cb6b52b83befb6918672b3d8eb432d8793b08a967/pytoolconfig-1.2.2.tar.gz
Summary  : Python tool configuration
Group    : Development/Tools
License  : LGPL-3.0 LGPL-3.0-or-later
Requires: pypi-pytoolconfig-license = %{version}-%{release}
Requires: pypi-pytoolconfig-python = %{version}-%{release}
Requires: pypi-pytoolconfig-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pdm_pep517)

%description
# Pytoolconfig
**Py**thon **Tool** **Config**uration
The goal of this project is to manage configuration for python tools, such as
black and rope and add support for a pyproject.toml configuration file.
[Documentation](https://pytoolconfig.readthedocs.io/en/latest/) This library
only supports python 3.7 to 3.11. 3.12 plus may work, but isn't tested.

%package license
Summary: license components for the pypi-pytoolconfig package.
Group: Default

%description license
license components for the pypi-pytoolconfig package.


%package python
Summary: python components for the pypi-pytoolconfig package.
Group: Default
Requires: pypi-pytoolconfig-python3 = %{version}-%{release}

%description python
python components for the pypi-pytoolconfig package.


%package python3
Summary: python3 components for the pypi-pytoolconfig package.
Group: Default
Requires: python3-core
Provides: pypi(pytoolconfig)
Requires: pypi(packaging)
Requires: pypi(tomli)

%description python3
python3 components for the pypi-pytoolconfig package.


%prep
%setup -q -n pytoolconfig-1.2.2
cd %{_builddir}/pytoolconfig-1.2.2
pushd ..
cp -a pytoolconfig-1.2.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659368342
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytoolconfig
cp %{_builddir}/pytoolconfig-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytoolconfig/a8a12e6867d7ee39c21d9b11a984066099b6fb6b
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pytoolconfig/a8a12e6867d7ee39c21d9b11a984066099b6fb6b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
