%global debug_package %{nil}

Name:    lmbench
Version: 3
Release: 1
Summary: Tools for Performance Analysis
License: GPLv2
URL:	 http://www.bitmover.com/lmbench/
Source0: http://www.bitmover.com/lmbench/%{name}%{version}.tar.gz

Patch0: lmbench3-fix-llseek-and-remove-bk-in-Makefile.patch
Patch1: lmbench3-add-HOWTO-to-indicate-howto-use-this-package.patch

BuildRequires: 	gcc

%description
A userspace utility for testing the memory subsystem for faults. It's portable and should compile and work on any 32- or 64-bit Unix-like system. (Yes, even weird, proprietary Unices, and even Mac OS X.) For hardware developers, memtester can be told to test memory starting at a particular physical address as of memtester version 4.1.0.

%prep
%setup -q -n %{name}%{version}/
%patch0 -p1
%patch1 -p1

%build
%make_build

%install
mkdir -p %{buildroot}/opt/%{name}/{bin,doc,scripts,results,src}
find bin/ -name *.o | xargs rm -rf
find bin/ -name *.a | xargs rm -rf
cp -r bin/* %{buildroot}/opt/%{name}/bin/

install -m 0644 src/* %{buildroot}/opt/%{name}/src

install -m 0755 scripts/* %{buildroot}/opt/%{name}/scripts/
install -m 0644 scripts/Makefile %{buildroot}/opt/%{name}/scripts/
install -m 0644 scripts/README %{buildroot}/opt/%{name}/scripts/

install -m 0644 doc/* %{buildroot}/opt/%{name}/doc/

install -m 0644 Makefile %{buildroot}/opt/%{name}/

install -m 0644 results/Makefile %{buildroot}/opt/%{name}/results


%pre
%preun
%post
%postun

%check

%files
%license COPYING COPYING-2
%doc README HOWTO
/opt/%{name}/*

%changelog
* Sun Mar 29 2020 Wei Xiong <myeuler@163.com>
- Package init

