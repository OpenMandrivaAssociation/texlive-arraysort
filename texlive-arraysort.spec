%global tl_name arraysort
%global tl_revision 31576

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Sort arrays (or portions of them)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/arraysort
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arraysort.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arraysort.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arraysort.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a mechanism for sorting arrays (or portions of
them); the arrays should have been created using the arrayjobx package.

