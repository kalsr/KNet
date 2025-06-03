// BIG DATA Setter Class  
//DEPARTMENT OF DEFENSE BIG DATA STANDARD TAXONOMY - CLASS (SETTER & GETTER METHODS)- Developed On 10-16-2018 BY: - Kalsnet Technologies (KNet))

public class BigDataSetter
{
// DISA Taxonomy Field Declarations



private String EtlDataProcessing;
private String DataCollection;
private String DataHygiene;
private String DataHygieneSoftware;
private String DataWarehouse;
private String DistributedProcessingSoftware;
private String DataArchitectureModeling;
private String BusinessAnalytics;
private String IntelligenceExploitation;
private String DataAnalytics;
private String DataVisualizationSoftware;


// Mutator (Setter) Methods For DoD Big Data

public void setEtlDataProcessing(String EtlProcessing)
{ 
EtlDataProcessing = EtlProcessing;
}

public void setDataCollection (String DCollection)
{ 
DataCollection = DCollection;
}

public void setDataHygiene (String DHygiene)
{ 
DataHygiene = DHygiene;
}

public void setDataHygieneSoftware (String DHSoftware)
{
 DataHygieneSoftware = DHSoftware;
}

public void setDataWarehouse(String DWarehouse)
{
DataWarehouse = DWarehouse;
}

public void setDistributedProcessingSoftware (String DPSoftware)
{
 DistributedProcessingSoftware = DPSoftware;
}

public void setDataArchitectureModeling(String DAModeling)
{
DataArchitectureModeling = DAModeling;
}

public void setBusinessAnalytics (String BAnalytics)
{ 
BusinessAnalytics = BAnalytics;
}

public void setIntelligenceExploitation(String IExploit)
{
IntelligenceExploitation = IExploit;
}

public void setDataAnalytics (String DAnalytics)
{
DataAnalytics = DAnalytics;
}


public void setDataVisualizationSoftware (String DVSoftware)
{
DataVisualizationSoftware = DVSoftware;
}


// Accessor Methods For DoD Big Data

public String getEtlDataProcessing()
{ 
return EtlDataProcessing.toUpperCase();
}

public String getDataCollection()
{ 
return DataCollection.toUpperCase();
}

public String getDataHygiene ()
{ 
return DataHygiene.toUpperCase();
}

public String getDataHygieneSoftware ()
{
 return DataHygieneSoftware.toUpperCase();
}

public String getDataWarehouse()
{ 
return DataWarehouse.toUpperCase();
}

public String getDistributedProcessingSoftware()
{
return DistributedProcessingSoftware.toUpperCase();
}

public String getDataArchitectureModeling()
{
 return DataArchitectureModeling.toUpperCase();
}

public String getBusinessAnalytics()
{ 
return BusinessAnalytics.toUpperCase();
}

public String getIntelligenceExploitation()
{ 
return IntelligenceExploitation.toUpperCase();
}

public String getDataAnalytics()
{ 
return DataAnalytics.toUpperCase();
}

public String getDataVisualizationSoftware()
{ 
return DataVisualizationSoftware.toUpperCase();
}


}
