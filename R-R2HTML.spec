%global packname  R2HTML
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          2.2
Release:          3
Summary:          HTML exportation for R objects
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-boot R-splines R-survival R-stats R-cluster R-nlme R-rpart R-nnet R-utils 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-boot R-splines R-survival R-stats R-cluster R-nlme R-rpart R-nnet R-utils 
%rename R-cran-R2HTML

%description
Includes HTML function and methods to write in an HTML file. Thus, making
HTML reports is easy. Includes a function that allows redirection on the
fly, which appears to be very usefull for teaching purpose, as the student
can keep a copy of the produced output to keep all that he did during the
course. Package comes with a vignette describing how to write HTML reports
for statistical analysis. Finally, a driver for Sweave allows to parse
HTML flat files containing R code and to automatically write the
corresponding outputs (tables and graphs).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/output
%{rlibdir}/%{packname}/samples


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-1
+ Revision: 774986
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 774730
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Fri Dec 25 2009 Jérôme Brenier <incubusss@mandriva.org> 1.59.1-1mdv2010.1
+ Revision: 482255
- new version 1.59.1

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.59-2mdv2010.0
+ Revision: 433083
- rebuild

* Sun Aug 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.59-1mdv2009.0
+ Revision: 270297
- update to new version 1.59

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.58-4mdv2009.0
+ Revision: 260150
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.58-3mdv2009.0
+ Revision: 248236
- rebuild

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.58-1mdv2008.1
+ Revision: 169873
- import R-cran-R2HTML

