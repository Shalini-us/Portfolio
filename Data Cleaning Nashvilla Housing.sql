
--Cleaning Data in SQl Queries

SELECT *
   FROM [Project Portfolio].[dbo].[NashvilleHousing]

--Standardize the dateformat

SELECT saleDateConverted, CONVERT(Date,SaleDate)
   FROM [Project Portfolio].[dbo].[NashvilleHousing]

UPDATE NashvilleHousing
SET SaleDate = CONVERT(Date,SaleDate)

 --------------------------------------------------------------------------------------------------------------------------

--Standardize the dateformat (2nd method)

AlTER TABLE NashvilleHousing
Add SaleDateConverted Date

Update NashvilleHousing
SET SaleDateConverted = CONVERT(Date,SaleDate)

 --------------------------------------------------------------------------------------------------------------------------

-- Populate Property Address data

SELECT PropertyAddress
   FROM [Project Portfolio].[dbo].[NashvilleHousing]


SELECT *
   FROM [Project Portfolio].[dbo].[NashvilleHousing]
--   Where PropertyAddress is null
order by ParcelID

SELECT a.ParcelID, a.ParcelID ,a.PropertyAddress,b.PropertyAddress, ISNULL (a.PropertyAddress, b.PropertyAddress)
   FROM [Project Portfolio].[dbo].[NashvilleHousing] a
 JOIN [Project Portfolio].[dbo].[NashvilleHousing] b
	on a.ParcelID =b.ParcelID
	AND a.[UniqueID ]<>b.[UniqueID ]
Where a.PropertyAddress is null


update a
SET PropertyAddress= ISNULL(a.PropertyAddress,b.PropertyAddress)
   FROM [Project Portfolio].[dbo].[NashvilleHousing] a
 JOIN [Project Portfolio].[dbo].[NashvilleHousing] b
	on a.ParcelID =b.ParcelID
	AND a.[UniqueID ]<>b.[UniqueID ]
Where a.PropertyAddress is null

--------------------------------------------------------------------------------------------------------------------------

-- Breaking out Address into Individual Columns (Address, City, State)

SELECT PropertyAddress
   FROM [Project Portfolio].[dbo].[NashvilleHousing]
--   Where PropertyAddress is null
-- order by ParcelID

Select 
SUBSTRING (PropertyAddress, 1,CHARINDEX(',',PropertyAddress)-1)as Address,
SUBSTRING (PropertyAddress,CHARINDEX(',',PropertyAddress)+1, LEN(PropertyAddress))as Address

   FROM [Project Portfolio].[dbo].[NashvilleHousing]


AlTER TABLE NashvilleHousing
Add PropertySplitAddress Nvarchar (255);

Update NashvilleHousing
SET PropertySplitAddress = SUBSTRING (PropertyAddress, 1,CHARINDEX(',',PropertyAddress)-1)


AlTER TABLE NashvilleHousing
Add PropertySplitCity  Nvarchar (255);

Update NashvilleHousing
SET  PropertySplitCity = SUBSTRING (PropertyAddress,CHARINDEX(',',PropertyAddress)+1, LEN(PropertyAddress))


SELECT *
   FROM [Project Portfolio].[dbo].[NashvilleHousing]

   Select OwnerAddress
      FROM [Project Portfolio].[dbo].[NashvilleHousing]


Select
PARSENAME(REPLACE (OwnerAddress, ',','.'),3)
,PARSENAME(REPLACE (OwnerAddress, ',','.'),2)
,PARSENAME(REPLACE (OwnerAddress, ',','.'),1)
    FROM [Project Portfolio].[dbo].[NashvilleHousing]


AlTER TABLE NashvilleHousing
Add OwnersplitAddress Nvarchar (255);

Update NashvilleHousing
SET OwnersplitAddress = PARSENAME(REPLACE (OwnerAddress, ',','.'),3)


AlTER TABLE NashvilleHousing
Add OwnersplitCity  Nvarchar (255);

Update NashvilleHousing
SET  OwnersplitCity  = PARSENAME(REPLACE (OwnerAddress, ',','.'),2)


AlTER TABLE NashvilleHousing
Add Ownersplitstate  Nvarchar (255);

Update NashvilleHousing
SET  Ownersplitstate  =PARSENAME(REPLACE (OwnerAddress, ',','.'),1)



SELECT *
   FROM [Project Portfolio].[dbo].[NashvilleHousing]

   --------------------------------------------------------------------------------------------------------------------------


-- Change Y and N to Yes and No in "Sold as Vacant" field

Select Distinct (Soldasvacant), count(Soldasvacant)
From [Project Portfolio].[dbo].[NashvilleHousing]
group by Soldasvacant
Order by 2

Select Soldasvacant
,Case when Soldasvacant = 'Y' Then 'Yes'
	  when Soldasvacant = 'N' Then 'NO'
	  Else Soldasvacant
		END
From [Project Portfolio].[dbo].[NashvilleHousing]



Update NashvilleHousing
SET  Soldasvacant= Case when Soldasvacant = 'Y' Then 'Yes'
	  when Soldasvacant = 'N' Then 'NO'
	  Else Soldasvacant
		END

-----------------------------------------------------------------------------------------------------------------------------------------------------------

-- Remove Duplicates
WITH RownumCTE AS(
Select *,
	ROW_NUMBER() OVER (
	PARTITION BY ParcelID,
	PropertyADDRESS,
	SaleDate,
	SalePrice,
	LegalReference
	ORDER BY
		UniqueID
		)row_num
From [Project Portfolio].[dbo].[NashvilleHousing]
--ORDER BY ParcelID
)
--Delete
Select *
FROM RownumCTE
where row_num >1
--order by PropertyAddress

SELECT *
   FROM [Project Portfolio].[dbo].[NashvilleHousing]
   ORDER BY [UniqueID ]

ALTER TABLE [Project Portfolio].[dbo].[NashvilleHousing]
DROP Column PropertyAddress,SaleDate,ownerAddress,TAXDistrict

SELECT *
   FROM [Project Portfolio].[dbo].[NashvilleHousing]