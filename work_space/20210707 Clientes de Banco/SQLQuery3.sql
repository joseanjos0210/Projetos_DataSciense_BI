/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [IdCliente]
      ,[Customer ID]
      ,[Name]
      ,[Surname]
      ,[Gender]
      ,[Age]
      ,[Date Joined]
      ,[Balance]
  FROM [DS_TRAINNING].[dbo].[RAW_ClientesBanco_20210705]

  select count(*) from [dbo].[RAW_ClientesBanco_20210705]
  
  /****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [IdCliente]
      ,[Customer ID]
      ,[Name]
      ,[Surname]
      ,[Gender]
      ,[Age]
      ,[Date Joined]
      ,[Balance]
  FROM [DS_TRAINNING].[dbo].[RAW_FuncMarketing_20210705]
  
  select count(*) from [dbo].[RAW_FuncMarketing_20210705]




  delete from [dbo].[RAW_ClientesBanco_20210705]

