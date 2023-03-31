Name:		texlive-arraysort
Version:	31576
Release:	2
Summary:	Sort arrays (or portions of them)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/arraysort
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arraysort.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arraysort.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arraysort.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a mechanism for sorting arrays (or
portions of them); the arrays should have been created using
the arrayjobx package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/arraysort/arraysort.sty
%doc %{_texmfdistdir}/doc/latex/arraysort/Makefile
%doc %{_texmfdistdir}/doc/latex/arraysort/README
%doc %{_texmfdistdir}/doc/latex/arraysort/arraysort.pdf
#- source
%doc %{_texmfdistdir}/source/latex/arraysort/arraysort.dtx
%doc %{_texmfdistdir}/source/latex/arraysort/arraysort.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
