Name:		texlive-crossrefware
Version:	64754
Release:	1
Summary:	Scripts for working with crossref.org
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crossrefware
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossrefware.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossrefware.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle contains the following scripts: bibdoiadd.pl: add
DOI numbers to papers in a given bib file, bibzbladd.pl: add
Zbl numbers to papers in a given bib file, bibmradd.pl: add MR
numbers to papers in a given bib file, bbl2bib.pl: convert
thebibliography environment to a bib file, biburl2doi.pl:
convert urls pointing to doi.org to dois ltx2crossrefxml.pl: a
tool for the creation of XML files for submitting to
crossref.org. The scripts use bibtexperllibs.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/tex/latex/crossrefware
%{_texmfdistdir}/texmf-dist/scripts/crossrefware
%doc %{_texmfdistdir}/texmf-dist/doc/support/crossrefware
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/ltx2crossrefxml.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/ltx2crossrefxml.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/bibzbladd.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/bibzbladd.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/biburl2doi.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/biburl2doi.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/bibmradd.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/bibmradd.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/bibdoiadd.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/bibdoiadd.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/bbl2bib.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/bbl2bib.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
