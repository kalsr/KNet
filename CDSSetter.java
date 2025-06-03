// CROSS DOMAIN SOLUTION (CDS) FRAMEWORK - Setter Class TEMPLATE 

// DEVELOPED ON 08-06-2020

public class CDSSetter

{

// CDS DATA DOMAINS set to be Private for high security

//***************************CASE1-CDS-ELEMENTS***********************************************
private String DataConfidentiality;
private String DataIntegrity;
private String DataAvailability;
private String Usefulness;

//***************************CASE2-CDS-TYPES**********************************************************
private String AccessSolution;
private String TransferSolution;
private String MultiLevelSolution;

//*****************************case3-CDS SECURITY CONTROLS************************************************************

private String SecureConnections;
private String SecMgmt;
private String AdaptiveSecurity;
private String MultiAccess;
private String MultiSecurity;
private String SingleSignOn;
private String Scalability;
private String Ipv6;
private String InterOperability;
private String TrustedPath;

//*************case4 - CDS-ARCHITECTURE************************

private String Cdes;
private String OrgElements;
private String Trb;
private String XmlGuard;
private String CollaborationGateway;
private String CgFunctions;
private String CollaborationClient;

//*************case5- ACCREDETATION AUTHORIZATION************************

private String SabiTsabi;
private String ConnectionApproval;
private String RiskAssesments;
private String WorkingGroup;
private String DevelopFilters;
private String TechAssesments;
private String ValidatePatches;
private String Stigs;

//*************case6- CDS-FUNCTIONS*************************

private String Interface;
private String SecurityPolicy;
private String Operations;
private String Forensic;

//*************************************Case7- CDS USE-CASES***************************************************************

private String CS;
private String DR;
private String SC;
private String DIS;
private String CA;
private String FFM;
private String TBF;
private String IOD;
private String AIME;
private String AMS;

//*********************************Case8- CDS-IMPLEMENTATIONS*******************************************************************

private String Imp;
private String TN;
private String ECD;
private String IIT;
private String RM;
private String CR;
private String ANCD;
private String DB;
private String AG;
private String SCTZ;
private String SPE;
private String MP;
private String LP;
private String AA;
private String DP;
private String TN1;
private String PB;
private String FC;
private String CDT;

//******************************************************************************************************************************8

// CDS Mutator (SETTER) Methods

//**************************Case-1 CDS Elements-Setters***********************************

public void setDataConfidentiality(String CDSConfidentiality)
{ 
  DataConfidentiality = CDSConfidentiality;
}

public void setDataIntegrity (String CDSIntegrity)
{ 
  DataIntegrity = CDSIntegrity;
}

public void setDataAvailability (String CDSAvailability)
{ 
  DataAvailability = CDSAvailability;
}

public void setUsefulness (String CDSUsefulness)
{ 
  Usefulness = CDSUsefulness;
}

//*************************Case-2 CDS TYPE Setters**************************************************

public void setAccessSolution(String Access)
{
AccessSolution  = Access;
}
public void setTransferSolution (String Transfer)
{
TransferSolution = Transfer;
}
public void setMultiLevelSolution (String MLS)
{
MultiLevelSolution = MLS;
}

//*****************************Case-3 CDS SECURITY CONTROL Setters**************************************************

public void setSecureConnections(String Connections)
{
SecureConnections  = Connections;
}
public void setSecMgmt (String SM)
{
SecMgmt = SM;
}
public void setAdaptiveSecurity (String AS)
{
AdaptiveSecurity = AS;
}
public void setMultiAccess (String MA)
{
MultiAccess = MA;
}
public void setMultiSecurity (String MS)
{
MultiSecurity = MS;
}
public void setSingleSignOn (String SSO)
{
SingleSignOn = SSO;
}
public void setScalability (String SCA)
{
Scalability = SCA;
}
public void setIpv6 (String IPV)
{
Ipv6 = IPV;
}
public void setInterOperability (String IO)
{
InterOperability = IO;
}
public void setTrustedPath (String TP)
{
TrustedPath = TP;
}
//***********************************Case-4 CDS ARCHITECTURE SETTERS******************************************************************************

public void setCdes( String CD)
{ 
 Cdes = CD;
}

public void setOrgElements( String OE)
{ 
 OrgElements = OE; 
}

public void setTrb(String TR)
{ 
 Trb = TR;
}

public void setXmlGuard (String XML)
{ 
 XmlGuard = XML;
}

public void setCollaborationGateway(String CG)
{
 CollaborationGateway = CG;
}

public void setCgFunctions(String CGF)
{ 
CgFunctions = CGF;
}
public void setCollaborationClient(String CC)
{ 
 CollaborationClient = CC;
}

//***********************************Case-5 CDS ACCREDITATION AUTHORIZATION-Setters******************************************************************************

public void setSabiTsabi( String SBTB)
{ 
 SabiTsabi = SBTB;
}

public void setConnectionApproval( String CA)
{ 
 ConnectionApproval = CA;
}

public void setRiskAssesments(String RA)
{ 
 RiskAssesments = RA;
}
public void setWorkingGroup (String WG)
{ 
 WorkingGroup = WG;
}

public void setDevelopFilters(String DF)
{
  DevelopFilters = DF;
}

public void setTechAssesments(String TA)
{ 
TechAssesments= TA;
}
public void setValidatePatches(String VP)
{ 
 ValidatePatches = VP;
}
public void setStigs(String STG)
{ 
Stigs = STG;
}


//***********************************Case-6 CDS FUNCTIONS -Setters******************************************************************************

public void setInterface( String INT)
{ 
Interface = INT;
}

public void setSecurityPolicy( String SCP)
{ 
 SecurityPolicy= SCP;
}

public void setOperations(String OPS)
{ 
 Operations = OPS;
}
public void setForensic(String FR)
{ 
 Forensic = FR;
}

//****************************Case-7 CDS USE-CASES - Setters****************

public void setCS (String USC)
{ 
CS = USC;
}

public void setDR( String DSR)
{ 
 DR = DSR;
}

public void setSC(String SCI)
{ 
 SC = SCI;
}
public void setDIS (String DS)
{ 
DIS = DS;
}

public void setCA(String AC)
{
  CA = AC;
}

public void setFFM(String MFF)
{ 
FFM = MFF;
}
public void setTBF(String FBT)
{ 
TBF = FBT;
}
public void setIOD(String DOI)
{ 
IOD = DOI;
}
public void setAIME(String AI)
{
AIME = AI;
}

public void setAMS(String SMA)
{
AMS = SMA;
}

//****************************Case-8 CDS IMPLEMENTATION -Setters*************************

public void setImp( String IM)
{ 
Imp = IM;
}

public void setTN( String NT)
{ 
 TN = NT;
}

public void setECD(String ED)
{ 
 ECD = ED;
}
public void setIIT (String IT)
{ 
 IIT = IT;
}

public void setRM (String MR)
{
  RM = MR;
}

public void setCR (String RC)
{ 
CR = RC;
}

public void setANCD (String AD)
{ 
ANCD = AD;
}

public void setDB(String BD)
{ 
DB = BD;
}

public void setAG(String GA)
{
AG = GA;
}

public void setSCTZ(String TZ)
{
 SCTZ = TZ;
}

public void setSPE(String PES)
{
SPE = PES;
}

public void setMP (String PM)
{
MP = PM;
}

public void setLP (String PL)
{
LP =PL;
}

public void setAA(String AAA)
{
AA = AAA;
}

public void setDP (String PD)
{
DP = PD;
}

public void setTN1 (String NT)
{
TN1 = NT;
}

public void setPB (String BP)
{
PB = BP;
}

public void setFC (String CF)
{
FC = CF;
}

public void setCDT (String DTC)
{
CDT = DTC;
}

//**********************END CDS SETTER METHODS*********************************************************************


// CDS Accessor Methods

//**************************Case-1 CDS Elements- Accessors***************************************

public String getDataConfidentiality()
{ 
return DataConfidentiality.toUpperCase();
}

public String getDataIntegrity()
{ 
return DataIntegrity.toUpperCase();
}

public String getDataAvailability()
{ 
return DataAvailability.toUpperCase();
}

public String getUsefulness()
{ 
return Usefulness.toUpperCase();
}

//*******************Case-2 CDS TYPE -Accessors*******************************************

public String getAccessSolution()
{ 
return AccessSolution.toUpperCase();
}

public String getTransferSolution()
{ 
return TransferSolution.toUpperCase();
}

public String getMultiLevelSolution()
{ 
return MultiLevelSolution.toUpperCase();
}

//*******************Case-3 CDS SECURITY CONTROL -Accessors******************************************

public String getSecureConnections()
{ 
return SecureConnections.toUpperCase();
}

public String getSecMgmt()
{ 
return SecMgmt.toUpperCase();
}

public String getAdaptiveSecurity()
{ 
return AdaptiveSecurity.toUpperCase();
}

public String getMultiAccess()
{ 
return MultiAccess.toUpperCase();
}

public String getMultiSecurity ()
{ 
return MultiSecurity.toUpperCase();
}

public String getSingleSignOn()
{
 return SingleSignOn.toUpperCase();
}

public String getScalability()
{ 
return Scalability.toUpperCase();
}

public String getIpv6()
{ 
return Ipv6.toUpperCase();
}

public String getInterOperability()
{ 
return InterOperability.toUpperCase();
}

public String getTrustedPath()
{ 
return TrustedPath.toUpperCase();
}

//***************************************Case-4 CDS ARCHITECTURE-Accessors***************************************************************

public String getCdes()
{ 
 return Cdes.toUpperCase();
}

public String getOrgElements()
{ 
 return OrgElements.toUpperCase() ;
}

public String getTrb()
{ 
return Trb.toUpperCase();
}

public String getXmlGuard ()
{ 
 return XmlGuard.toUpperCase() ;
}

public String getCollaborationGateway()
{
  return CollaborationGateway.toUpperCase();
}

public String getCgFunctions()
{ 
return CgFunctions.toUpperCase();
}

public String getCollaborationClient()
{ 
return CollaborationClient.toUpperCase();
}


//******************************************Case-5 CDS ACCREDITATION -Accessors**********************************************************

public String getSabiTsabi()
{ 
return SabiTsabi.toUpperCase();
}

public String getConnectionApproval()
{ 
return ConnectionApproval.toUpperCase();
}

public String getRiskAssesments()
{ 
return RiskAssesments.toUpperCase();
}

public String getWorkingGroup()
{ 
return WorkingGroup.toUpperCase();
}

public String getDevelopFilters()
{
 return DevelopFilters.toUpperCase();
}

public String getTechAssesments()
{ 
return TechAssesments.toUpperCase();
}
public String getValidatePatches()
{ 
return ValidatePatches.toUpperCase();
}

public String getStigs()
{ 
return Stigs.toUpperCase();
}

//******************************************Case-6 CDS FUNCTIONS -Accessors**********************************************************

public String getInterface()
{ 
return Interface.toUpperCase();
}

public String getSecurityPolicy()
{ 
return SecurityPolicy.toUpperCase();
}

public String getOperations()
{ 
return Operations.toUpperCase();
}

public String getForensic()
{ 
return Forensic.toUpperCase();
}


//********************************Case-7 CDS USE-CASES -Accessors**********************************

public String getCS()
{ 
return CS.toUpperCase();
}

public String getDR()
{ 
return DR.toUpperCase();
}

public String getSC()
{ 
return SC.toUpperCase();
}

public String getDIS()
{ 
return DIS.toUpperCase();
}

public String getCA()
{ 
return CA.toUpperCase();
}

public String getFFM()
{ 
return FFM.toUpperCase();
}

public String getTBF()
{ 
return TBF.toUpperCase();
}

public String getIOD()
{
 return IOD.toUpperCase();
}

public String getAIME()
{ 
return AIME.toUpperCase();
}

public String getAMS()
{ 
return AMS.toUpperCase();
}

//********************************************Case-8 CDS IMPLEMENTATIONS -Accessors******************************************************************

public String getImp()
{ 
return Imp.toUpperCase();
}

public String getTN()
{ 
return TN.toUpperCase();
}

public String getECD()
{ 
return ECD.toUpperCase();
}

public String getIIT()
{ 
return IIT.toUpperCase();
}

public String getRM()
{ 
return RM.toUpperCase();
}

public String getCR()
{ 
return CR.toUpperCase();
}

public String getANCD()
{ 
return ANCD.toUpperCase();
}

public String getDB()
{
 return DB.toUpperCase();
}

public String getAG()
{ 
return AG.toUpperCase();
}

public String getSCTZ()
{ 
return SCTZ.toUpperCase();
}

public String getSPE()
{ 
return SPE.toUpperCase();
}

public String getMP()
{
 return MP.toUpperCase();
}

public String getLP()
{
 return LP.toUpperCase();
}

public String getAA()
{ 
return AA.toUpperCase();
}

public String getDP()
{ 
return DP.toUpperCase();
}

public String getTN1()
{ 
return TN1.toUpperCase();
}

public String getPB()
{ 
return PB.toUpperCase();
}

public String getFC()
{ 
return FC.toUpperCase();
}

public String getCDT()
{ 
return CDT.toUpperCase();
}

//***************************END CDS ACCESSOR METHODS***********************************************************************************

 }
