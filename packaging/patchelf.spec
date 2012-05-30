#
# Please submit bugfixes or comments via http://bugs.meego.com/
#

Summary:        A utility for patching ELF binaries

Name:           patchelf
Version:        0.5.svn20809
Release:        1
License:        GPLv3
Url:            http://nixos.org/patchelf.html
Group:          Development/Tools
Source0:        %{name}.tar.bz2
Source1001: packaging/patchelf.manifest 
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Prefix: /usr

%description

PatchELF is a simple utility for modifing existing ELF executables and
libraries.  It can change the dynamic loader ("ELF interpreter") of
executables and change the RPATH of executables and libraries.

%prep
%setup -q -n %{name}

%build
cp %{SOURCE1001} .
./bootstrap.sh
./configure --prefix=%{_prefix}
make

%ifnarch %arm
# fixme: x86 specific parts in checks
make check
%endif

%install
%make_install
strip %{buildroot}/%{_bindir}/* || true

%files
%manifest patchelf.manifest
%{_bindir}/patchelf
%{_datadir}/doc/patchelf/README
