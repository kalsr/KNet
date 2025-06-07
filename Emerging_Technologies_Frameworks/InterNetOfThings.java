// InterNetOfThings Class 

public class InterNetOfThings
{
// DISA Taxonomy Field Declarations

private String InformationType;
private String DeviceType;
private String PlatformType;
private String ProcessorType;
private String NetworkType;
private String InfrastructureType;
private String OperatingSystemType;
private String InterOperabilityType;
private String UsersType;
private String BehavioursType;


// Mutator Methods

public void setInformation(String Information)
{ 
InformationType = Information;
}
public void setDevice (String Device)
{ 
DeviceType = Device;
}
public void setPlatform (String Platform)
{ 
PlatformType = Platform;
}
public void setProcessor (String Processor)
{
 ProcessorType = Processor;
}
public void setNetwork(String Network)
{
NetworkType = Network;
}
public void setInfrastructure (String Infrastructure)
{
 InfrastructureType = Infrastructure;
}
public void setOperatingSystem(String OperatingSystem)
{
OperatingSystemType = OperatingSystem;
}
public void setInterOperability (String InterOperability)
{ 
InterOperabilityType = InterOperability;
}
public void setUser (String Users)
{
UsersType = Users;
}
public void setBehaviours (String Behaviours)
{
BehavioursType = Behaviours;
}
// Accessor Methods

public String getInformationType()
{ 
return InformationType.toUpperCase();
}

public String getDeviceType()
{ 
return DeviceType.toUpperCase();
}

public String getProcessorType ()
{ 
return ProcessorType.toUpperCase();
}

public String getNetworkType ()
{
 return NetworkType.toUpperCase();
}

public String getInfrastructureType ()
{ 
return InfrastructureType.toUpperCase();
}

public String getOperatingSystemType ()
{
return OperatingSystemType.toUpperCase();
}

public String getInterOperabilityType ()
{
 return InterOperabilityType.toUpperCase();
}

public String getUsersType ()
{ 
return UsersType.toUpperCase();
}

public String getBehavioursType ()
{ 
return BehavioursType.toUpperCase();
}

public String getPlatformType ()
{ 
return PlatformType.toUpperCase();
}

}
