// Email Isolation FRAMEWORK - Setter Class TEMPLATE 
// DEVELOPED ON 10-28-2020
public class EmailIsolationSetter
{
// Email Isolation DATA DOMAINS set to be Private for high security

private String components,ERC,Protocols,Formats,SWM;
private String BMF,MIME,MTS,SMT,SMTE,PMT,CAS,POP,IMAP,PMAM,WMA;
private String IR,CRT,ART,UMS,UMR,UMAS,TMD,DCP,PSP,EMB,UBE;
private String CDA,CSC,IEI,SAPP,ESA;
private String PLCY,MIA,MVM,MTM,MIDA;
private String MIRP,MIRDA,MIRC,MIRE,MIRR,MILL;
private String PGP,SMIME,KM,ISSUE;
private String IDP,SMS,MP,SSP,HRR,GISSP,CPMS;
private String UCOS,STOS,CSMO;
private String HMSA,PEFM,BSSS,AMR,SAC,WAC,CSMC;
private String NCAS,NEC,CISN;
private String ICCA,SMC,PI,AWBMS,CSMC;
private String LOG,BMAS,RFSC,STMS,RAMS,CAMS;
private String INTRO,VEU,RUDBA,SPF,DKIM,DMARC,AMDS,RS;
private String INTR,ETS,ECS,SRS;
private String INTO,WARB,TRUE,USRE;
private String INTDN,WCLNT,SCLNT,MBST,SCRM;


// 5G Mutator Methods

public void setDataTraffic(String FivegTraffic)
{ 
DataTraffic = FivegTraffic;
}
public void setNumberOfConnections (String FivegConnections)
{ 
 NumberOfConnections = FivegConnections;
}
public void setInternetOfThings (String FivegIOT)
{ 
 InternetOfThings = FivegIOT;
}
public void setIncreasedEnergyEfficiency (String FivegEfficiency)
{ 
IncreasedEnergyEfficiency = FivegEfficiency;
}
public void setIncreasedOperationalExpenditures (String FivegExpenditures)
{
 IncreasedOperationalExpenditures = FivegExpenditures;
}
public void setNewUsecases(String FivegUseCases)
{
NewUsecases = FivegUseCases;
}
public void setNewApplications (String FivegApplications)
{
 NewApplications = FivegApplications;
}
public void setApplicationDataSegmentation(String ZADS)
{
ApplicationDataSegmentation = ZADS;
}
public void setAdminAuthenticationAuthorization (String ZAAA)
{ 
AdminAuthenticationAuthorization = ZAAA;
}
public void setSecurityPolicyOrchestration (String ZSPO)
{
SecurityPolicyOrchestration = ZSPO;
}
public void setIdentityRequirements (String ZIR)
{
IdentityRequirements = ZIR;
}
public void setHealthComplianceRequirements (String ZHCR)
{
HealthComplianceRequirements = ZHCR;
}
public void setAuthorizationRequirements (String ZAA)
{
AuthorizationRequirements = ZAA;
}
public void setAccountingAuditingRequirements (String ZAAR)
{
AccountingAuditingRequirements = ZAAR;
}
public void setSegmentationRequirements (String ZSR)
{
SegmentationRequirements = ZSR;
}
public void setOrchestrationRequirements (String ZOR)
{
OrchestrationRequirements = ZOR;
}
public void setAdditionalCloudDataTaggingDiscoveryRequirements (String ZACTDR)
{
AdditionalCloudDataTaggingDiscoveryRequirements = ZACTDR;
}
public void setOptionalRequirements (String ZOPR)
{
OptionalRequirements = ZOPR;
}
public void setEffectiveness (String ZEF)
{
Effectiveness = ZEF;
}
public void setSuitability (String ZSY)
{
Suitability = ZSY;
}
public void setPerformance (String ZPF)
{
Performance = ZPF;
}

// 5G Accessor Methods

public String getDataTraffic()
{ 
return DataTraffic.toUpperCase();
}

public String getNumberOfConnections()
{ 
return NumberOfConnections.toUpperCase();
}
public String getInternetOfThings()
{ 
return InternetOfThings.toUpperCase();
}
public String getIncreasedEnergyEfficiency ()
{ 
return IncreasedEnergyEfficiency.toUpperCase();
}

public String getIncreasedOperationalExpenditures ()
{
 return IncreasedOperationalExpenditures.toUpperCase();
}

public String getNewUsecases ()
{ 
return NewUsecases.toUpperCase();
}

public String getNewApplications ()
{
return NewApplications.toUpperCase();
}

public String getApplicationDataSegmentation ()
{
 return ApplicationDataSegmentation.toUpperCase();
}

public String getAdminAuthenticationAuthorization ()
{ 
return AdminAuthenticationAuthorization.toUpperCase();
}

public String getSecurityPolicyOrchestration ()
{ 
return SecurityPolicyOrchestration.toUpperCase();
}

public String getIdentityRequirements ()
{ 
return IdentityRequirements.toUpperCase();
}

public String getHealthComplianceRequirements ()
{ 
return HealthComplianceRequirements.toUpperCase();
}
public String getAuthorizationRequirements ()
{ 
return AuthorizationRequirements.toUpperCase();
}
public String getAccountingAuditingRequirements ()
{ 
return AccountingAuditingRequirements.toUpperCase();
}
public String getSegmentationRequirements ()
{ 
return SegmentationRequirements.toUpperCase();
}
public String getOrchestrationRequirements ()
{ 
return OrchestrationRequirements.toUpperCase();
}
public String getAdditionalCloudDataTaggingDiscoveryRequirements ()
{ 
return AdditionalCloudDataTaggingDiscoveryRequirements.toUpperCase();
}
public String getOptionalRequirements ()
{ 
return OptionalRequirements.toUpperCase();
}
public String getEffectiveness()
{ 
return Effectiveness.toUpperCase();
}
public String getSuitability()
{ 
return Suitability.toUpperCase();
}
public String getPerformance()
{ 
return Performance.toUpperCase();
}
}
