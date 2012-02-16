%define modulename R2HTML
%define realver 1.59-1
%define r_library %{_libdir}/R/library

Summary:	HTML exportation for R objects
Name:		R-cran-%{modulename}
Version:	%(echo %{realver} | tr '-' '.')
Release:	%mkrel 1
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Includes HTML function and methods to write in an HTML file.
Thus, making HTML reports is easy. Includes a function that allows 
redirection on the fly, which appears to be very usefull for teaching 
purpose, as the student can keep a copy of the produced output to keep 
all that he did during the course. Package comes with a vignette 
describing how to write HTML reports for statistical analysis.
Finally, a driver for Sweave allows to parse HTML flat files 
containing R code and to automatically write the corresponding 
outputs (tables and graphs).

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
