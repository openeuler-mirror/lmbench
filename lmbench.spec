%global debug_package %{nil}

Name:    lmbench
Version: 3
Release: 4
Summary: Tools for Performance Analysis
License: GPLv2
URL:	 http://www.bitmover.com/lmbench/
Source0: http://www.bitmover.com/lmbench/%{name}%{version}.tar.gz

Patch0: lmbench3-fix-llseek-and-remove-bk-in-Makefile.patch
Patch1: lmbench3-add-HOWTO-to-indicate-howto-use-this-package.patch
Patch2: Rpc-code-moved-from-glibc-to-libtirpc.patch 
Patch3: add-stack-protect.patch
Patch4: lib_sched.c-fix-a-bug-when-custom-pin-on-large-syste.patch

BuildRequires: gcc libtirpc-devel

%description
A userspace utility for testing the memory subsystem for faults. It's portable and should compile and work on any 32- or 64-bit Unix-like system. (Yes, even weird, proprietary Unices, and even Mac OS X.) For hardware developers, memtester can be told to test memory starting at a particular physical address as of memtester version 4.1.0.

%prep
%setup -q -n %{name}%{version}/
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

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
* Wed Apr 21 2021 Guodong Xu <guodong.xu@linaro.org> - 3-4
- lib_sched.c fix a bug when custom pin tasks to cpus on large systems

* Fri Mar 19 2021 zhangtao <zhangtao221@huawei.com> - 3-3
- add fstack-protector-strong flags

* Wed Jul 15 2020 wangyue <wangyue92@huawei.com> - 3-2 
- Fix rpc.h error.Rpc code moved from glibc to libtirpc.

* Sun Mar 29 2020 Wei Xiong <myeuler@163.com>
- Package init

