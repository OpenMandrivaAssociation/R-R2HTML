%global packname  R2HTML
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.2
Release:          1
Summary:          HTML exportation for R objects
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-boot R-splines R-survival R-stats R-cluster R-nlme
Requires:         R-rpart R-nnet R-utils
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-boot R-splines R-survival R-stats R-cluster R-nlme
BuildRequires:    R-rpart R-nnet R-utils
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
