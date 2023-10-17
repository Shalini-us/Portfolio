Select * 
From [Project Portfolio]..['Covid Deaths$']
Where continent is not null
order by 3,4

Select Distinct(location)
From [Project Portfolio]..['Covid Deaths$']


Select * 
From [Project Portfolio]..['Covid Vaccinations$']
order by 3,4
--Select Data that we are going to be using

Select Location,date, total_cases, new_cases, total_deaths, population
From [Project Portfolio]..['Covid Deaths$']
order by 1,2

--looking at Total Cases vs Total Deaths

Select Location, date, total_cases,total_deaths, (CONVERT(float,total_deaths)/NUllIF(CONVERT(float,total_cases),0))*100 as DeathPercentage
From [Project Portfolio]..['Covid Deaths$']
order by 1,2;
--shows likelihood of dying if you contract covid in your country
Select Location, date, total_cases,total_deaths, (CONVERT(float,total_deaths)/NUllIF(CONVERT(float,total_cases),0))*100 as DeathPercentage
From [Project Portfolio]..['Covid Deaths$']
Where location like '%India%'
order by 1,2;

--Looking at Total cases vs Population
--shows what percentage of population got covid

Select Location, date,population, total_cases, (CONVERT(float,total_cases)/NUllIF(CONVERT(float,population),0))*100 as populationPercentage
From [Project Portfolio]..['Covid Deaths$']
order by 1,2;

--looking at countries with highest infection rate compared to population(tableau table3)
Select Location, population, MAX(total_cases) as highestinfectioncount, Max((CONVERT(float,total_cases)/NUllIF(CONVERT(float,population),0)))*100 as percentpopulationinfected
From [Project Portfolio]..['Covid Deaths$']
Group By Location, population
order by percentpopulationinfected desc

--looking at countries with highest infection rate compared to population(tableau table4 along with date column)
Select Location, population,date, MAX(total_cases) as highestinfectioncount, Max((CONVERT(float,total_cases)/NUllIF(CONVERT(float,population),0)))*100 as percentpopulationinfected
From [Project Portfolio]..['Covid Deaths$']
Group By Location, population,date
order by percentpopulationinfected desc

--showing countries with highest death count per population
Select Location , Max(cast(total_deaths as int))as deathcount
From [Project Portfolio]..['Covid Deaths$']
Where continent is not null
Group By Location
order by deathcount desc


-- Let's Break Things Down by continent
--Showing continent with highest death count
Select continent, Max(cast(total_deaths as int))as Totaldeathcount
From [Project Portfolio]..['Covid Deaths$']
Where continent is not null
Group By continent
order by Totaldeathcount desc

--Global Numbers
Select date, SUM(new_cases)as total_cases, SUM(cast(new_deaths as int))as total_deaths, SUM(cast(new_deaths as int))/NUllIF(SUM(new_cases),0)*100 as DeathPercentage 
From [Project Portfolio]..['Covid Deaths$']
Where continent is not null
Group By date
order by 1,2;


Select SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/SUM(New_Cases)*100 as DeathPercentage
From [Project Portfolio]..['Covid Deaths$']
--Where location like '%states%'
where continent is not null 
--Group By date
order by 1,2

--Covid vacinations
Select * 
From [Project Portfolio]..['Covid Vaccinations$']

--joins looking at Total population Vs vaccinations
Select ['Covid Deaths$'].continent,['Covid Deaths$'].location,['Covid Deaths$'].date,['Covid Deaths$'].population,  ['Covid Vaccinations$'].new_vaccinations
From [Project Portfolio]..['Covid Deaths$']
join [Project Portfolio]..['Covid Vaccinations$']
	On ['Covid Deaths$'].location =['Covid Vaccinations$'].location
	and ['Covid Deaths$'].date= ['Covid Vaccinations$'].date
Where ['Covid Deaths$'].continent is not null
order by 1,2

-- 
Select ['Covid Deaths$'].continent,['Covid Deaths$'].location,['Covid Deaths$'].date,['Covid Deaths$'].population,['Covid Vaccinations$'].new_vaccinations,
SUM(CONVERT(int,['Covid Vaccinations$'].new_vaccinations)) OVER (Partition by ['Covid Deaths$'].location Order by ['Covid Deaths$'].Location, ['Covid Deaths$'].date) as rolling
From [Project Portfolio]..['Covid Deaths$']
join [Project Portfolio]..['Covid Vaccinations$']
	On ['Covid Deaths$'].location =['Covid Vaccinations$'].location
	and ['Covid Deaths$'].date= ['Covid Vaccinations$'].date
Where ['Covid Deaths$'].continent is not null
order by 1,2

--fix (Arithmetic overflow error converting expression to data type int.)
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CAST(vac.new_vaccinations AS bigint)) OVER (Partition by dea.Location Order by dea.location, dea.Date) as RollingPeopleVaccinated
From [Project Portfolio]..['Covid Deaths$'] dea
Join [Project Portfolio]..['Covid Vaccinations$'] vac
	On dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null 
order by 2,3

-- Shows Percentage of Population that has recieved at least one Covid Vaccine
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CAST(vac.new_vaccinations AS bigint)) OVER (Partition by dea.Location Order by dea.location, dea.Date) as RollingPeopleVaccinated
From [Project Portfolio]..['Covid Deaths$'] dea
Join [Project Portfolio]..['Covid Vaccinations$'] vac
	On dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null 
order by 2,3


With PopvsVac (continent,Location, Date, Population, New_vaccinations,Rollingpeoplevaccinated)
as
(
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CAST(vac.new_vaccinations AS bigint)) OVER (Partition by dea.Location Order by dea.location, dea.Date) as RollingPeopleVaccinated
From [Project Portfolio]..['Covid Deaths$'] dea
Join [Project Portfolio]..['Covid Vaccinations$'] vac
	On dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null 
--order by 2,3
)
Select *,(Rollingpeoplevaccinated/Population)*100
From popvsVac


--TEMP Table
Drop Table if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated
(
continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
 )
 Insert into #PercentPopulationVaccinated
 Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CAST(vac.new_vaccinations AS bigint)) OVER (Partition by dea.Location Order by dea.location, dea.Date) as RollingPeopleVaccinated
From [Project Portfolio]..['Covid Deaths$'] dea
Join [Project Portfolio]..['Covid Vaccinations$'] vac
	On dea.location = vac.location
	and dea.date = vac.date
--where dea.continent is not null 
--order by 2,3

Select *,(Rollingpeoplevaccinated/Population)*100
From #PercentPopulationVaccinated


--creating view to store data for later visualization
Create view PercentPopulationVaccinated as
 Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CAST(vac.new_vaccinations AS bigint)) OVER (Partition by dea.Location Order by dea.location, dea.Date) as RollingPeopleVaccinated
From [Project Portfolio]..['Covid Deaths$'] dea
Join [Project Portfolio]..['Covid Vaccinations$'] vac
	On dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null 
--order by 2,3


Select*
From PercentPopulationVaccinated


--table2

Select Location , SUM(cast(new_deaths as int))as Totaldeathcount
From [Project Portfolio]..['Covid Deaths$']
Where continent is null 
and location not in ('world','European Union','International','High income','Upper middle income','Lower middle income','Low income')
Group By Location
order by Totaldeathcount desc

--table3
