
// ZERO-TRUST FRAMEWORK WAS DEVELOPED BASED ON THE ZTA WORKING GROUP REQUIREMENTS & USE CASES.
// This code was written using Object-Oriented programming in Java JGRASP (APRIL, 2019)
// This code was written by Mr Randy Singh,Computer Scientist,Technology Innovation Team (DISA/BDE5)
// Contact Phone# (301)225-9535  

import java.util.Scanner; 

public class ZtMenu 

{
public static void main(String[] args) 
{
 
// Declare a variable to hold the 
// user's menu selection. 

int menuSelection;

final int MAX_VALUE = 4;
 
// Declare variables to hold the units 
// of measurement.
 
String IdentityAuthentication, HealthCompliance, Authorization, Accounting, Segmentation, Orchestration,EndUserAuthenticationAuthorization, ApplicationDataSegmentation, AdminAuthenticationAuthorization, SecurityPolicyOrchestration,IdentityRequirements, HealthComplianceRequirements,
 AuthorizationRequirements, AccountingAuditingRequirements, SegmentationRequirements, OrchestrationRequirements, AdditionalCloudDataTaggingDiscoveryRequirements, OptionalRequirements, Effectiveness, Suitability, Performance;
 
// Create a Scanner object for keyboard input. 

Scanner keyboard = new Scanner(System.in); 

// Display the LIST OF ZERO-TRUST Categories 

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("WELCOME TO ZERO-TRUST FRAMEWORK APPLICATION.  ");
System.out.println();
System.out.println   ("HERE ARE ZERO-TRUST FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  FUNCTIONAL REQUIREMENTS. "); 
System.out.println();
System.out.println   ("2.  PROPOSED USE CASES."); 
System.out.println();
System.out.println   ("3.  ARCHITECTURAL REQUIREMENTS."); 
System.out.println();
System.out.println   ("4.  EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("PLEASE ENTER ZERO-TRUST CATEGORY CHOICE (1 - 4)FROM THE LIST ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the ZERO-TRUST menu selection. 

 while (menuSelection < 1 || menuSelection > 4) 
  
{
 
System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID CHOICE FOR ZERO-TRUST CATEGORY SELECTION");
System.out.println();
System.out.println("HERE IS THE VALID LIST OF ZERO-TRUST CATEGORIES: ");
System.out.println();
System.out.println ("1.  FUNCTIONAL REQUIREMENTS. "); 
System.out.println();
System.out.println ("2.  PROPOSED USE CASES."); 
System.out.println();
System.out.println ("3.  ARCHITECTURAL REQUIREMENTS."); 
System.out.println();
System.out.println ("4.  EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER ZERO-TRUST CATEGORY CHOICE(1 - 4)FROM THE LIST ABOVE: ");


  
 menuSelection = keyboard.nextInt();
  
 } 
 
 while (menuSelection > 0 || menuSelection <= 4)
 
  



 switch(menuSelection)
 
{ 

//*************************ZERO-TRUST FRAMEWORK BEGINS HERE******************************************


 case 1:
 
 int menuSelect;
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED FUNCTIONAL-REQUIREMENTS CATEGORY OF ZERO-TRUST FRAMEWORK ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW FUNCTIONAL-REQUIREMENTS SUBCATEGORIES");
 System.out.println();

ZTSetter ZTFR;

//Following statement creates an object using the ZTSetter Class as
// its Blueprint. 

ZTFR = new ZTSetter();

//*****************DISPLAY THE ZERO-TRUST MENU***************
  

 System.out.println("1.  SHOW ENTIRE LIST OF FUNCTIONAL-REQUIREMENTS FOR ZERO-TRUST.");
 System.out.println();
 System.out.println("2.  IDENTIFY & AUTHENTICATION REQUIREMENTS.");
 System.out.println();
 System.out.println("3.  HEALTH & COMPLIANCE REQUIREMENTS.");
 System.out.println();
 System.out.println("4.  AUTHENTICATION REQUIREMENTS.");
 System.out.println();
 System.out.println("5.  ACCOUNTING REQUIREMENTS.");
 System.out.println();
 System.out.println("6.  SEGMENTATION REQUIREMENTS.");
 System.out.println();
 System.out.println("7.  ORCHESTRATION REQUIREMENTS.");
 System.out.println();
  //System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR FUNCTIONAL REQUIREMENTS CHOICE FROM 1 to 7: ");
   
 
  menuSelect = keyboard.nextInt();

System.out.println("************************************************************************************************" );

 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 7)
  

  
{
  System.out.println("************************************************************************************************" );
 System.out.println(); 
 System.out.println("THIS IS INVALID CHOICE");
 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR FUNCTIONAL REQUIREMENTS CHOICE FROM 1 to 7: "); 
 System.out.println();
 
  System.out.println("1.  SHOW ENTIRE LIST OF FUNCTIONAL-REQUIREMENTS FOR ZERO-TRUST.");
 System.out.println();
 System.out.println("2.  IDENTIFY & AUTHENTICATION REQUIREMENTS.");
 System.out.println();
 System.out.println("3.  HEALTH & COMPLIANCE REQUIREMENTS.");
 System.out.println();
 System.out.println("4.  AUTHENTICATION REQUIREMENTS.");
 System.out.println();
 System.out.println("5.  ACCOUNTING REQUIREMENTS.");
 System.out.println();
 System.out.println("6.  SEGMENTATION REQUIREMENTS.");
 System.out.println();
 System.out.println("7.  ORCHESTRATION REQUIREMENTS.");
System.out.println();

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          //System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE LIST OF FUNCTIONAL REQUIREMENTS FOR ZERO-TRUST : ");
          System.out.println();
          
          ZTFR.setIdentityAuthentication   ("NEED TO ASSOCIATE IDENTITY TO USER AND DEVICE. ");

          ZTFR.setHealthCompliance         ("NEED TO DETERMINE PATCH LEVEL AND SECURITY POSTURE OF DEVICE PRIOR TO NETWORK AUTHORIZATION. ");

          ZTFR.setAuthorization            ("NEED TO AUTHORIZE USER/DEVICE, BASED ON IDENTITY AND HYGIENE, AT MICRO PARAMETER OR JUST IN TIME (JIT)SOLUTION FOR ADMINISTRATORS (WITH ASSOCIATED ITSM TICKET).");
          
          ZTFR.setAccounting               ("NEED TO IDENTIFY AND DOCUMENT RESOURCES CONSUMED BY USERS AND ADMINISTRATORS FOR COMPLIANCE AND POTENTIAL INCIDENCE RESPONSE. ");        
          
          ZTFR.setSegmentation             ("NEED TO LIMIT COMMUNICATION (DIRECTIONAL PORT/PROTOCOL)BETWEEN ALL NETWORK FLOWS TO INCLUDE APPLICATION TIERS. ");
          
          ZTFR.setOrchestration            ("NEED CAPABILITY TO DYNAMICALLY PROVISION IDENTITY, HYGIENE, AUTHORIZATION AND SEGMENTATION POLICIES. ");
                   
// Display the ZERO-TRUST FUNCTIONAL REQUIREMENTS values stored in the fields

     
      System.out.println               (" IDENTIFY & AUTHENTICATION REQUIREMENT = " + ZTFR.getIdentityAuthentication());
      System.out.println();          
      System.out.println               (" HEALTH & COMPLIANCE REQUIREMENT       = " + ZTFR.getHealthCompliance());
      System.out.println();
      System.out.println               (" AUTHORIZATION REQUIREMENT             = " + ZTFR.getAuthorization());
      System.out.println();
      System.out.println               (" ACCOUNTING REQUIREMENT                = " + ZTFR.getAccounting());
      System.out.println();
      System.out.println               (" SEGMENTATION REQUIREMENT              = " + ZTFR.getSegmentation());
      System.out.println();
      System.out.println               (" ORCHESTRATION REQUIREMENT             = " + ZTFR.getOrchestration());
      System.out.println();
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      
      System.out.println( "TO CONTINUE WITH NEXT ZERO-TRUST CATEGORY PLEASE SELECT AGAIN CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println();
         System.out.println("PLEASE SEE ZERO-TRUST IDENTIFY & AUTHENTICATION REQUIREMENT ONLY: ");
         System.out.println();
  
  // *****************Information Types***************

        ZTFR.setIdentityAuthentication   ("NEED TO ASSOCIATE IDENTITY TO USER AND DEVICE. ");


      
//**************** Display the ZERO-TRUST INFORMATION TYPES****************

     
      System.out.println               (" IDENTITY & AUTHENTICATION REQUIREMENT                = " + ZTFR.getIdentityAuthentication());
      System.out.println();
      
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ZERO-TRUST CATEGORY PLEASE SELECT AGAIN CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
        // System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE ZERO-TRUST HEALTH & COMPLIANCE  REQUIREMENTS ONLY: ");
         System.out.println();
         

  
 // *****************ZERO-TRUST HEALTH COMPLIANCE REQUIREMENTS*****************
 
 
      ZTFR.setHealthCompliance         ("NEED TO DETERMINE PATCH LEVEL AND SECURITY POSTURE OF DEVICE PRIOR TO NETWORK AUTHORIZATION. ");
 
        
      System.out.println               (" HEALTH & COMPLIANCE REQUIREMENT                     = " + ZTFR.getHealthCompliance());
    
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ZERO-TRUST CATEGORY PLEASE SELECT AGAIN CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE ZERO-TRUST AUTHORIZATION REQUIREMENTS ONLY: ");
         System.out.println();
         


  // ********************ZERO-TRUST AUTHORIZATION*********************
  
 
      ZTFR.setAuthorization          ("NEED TO AUTHORIZE USER/DEVICE, BASED ON IDENTITY AND HYGIENE, AT MICRO PARAMETER OR JUST IN TIME (JIT)SOLUTION FOR ADMINISTRATORS (WITH ASSOCIATED ITSM TICKET).");
          


       

       System.out.println               (" AUTHORIZATION REQUIREMENT                             = " + ZTFR.getAuthorization());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ZERO-TRUST CATEGORY PLEASE SELECT AGAIN CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );

      

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         //System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE ZERO-TRUST ACCOUNTING REQUIREMENTS ONLY: ");
 
         System.out.println();
       
       

  // ****************ZERO-TRUST ACCOUNTING REQUIREMENTS*******************
  
  
     ZTFR.setAccounting               ("NEED TO IDENTIFY AND DOCUMENT RESOURCES CONSUMED BY USERS AND ADMINISTRATORS FOR COMPLIANCE AND POTENTIAL INCIDENCE RESPONSE. "); 
      

         System.out.println           (" ACCOUNTING REQUIREMENT        = " + ZTFR.getAccounting());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println( "TO CONTINUE WITH NEXT ZERO-TRUST CATEGORY PLEASE SELECT AGAIN CHOICE # 1");
         System.out.println();
         System.out.println("************************************************************************************************" );
     
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          //System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE ZERO-TRUST SEGMENTATION REQUIREMENTS ONLY: ");
          System.out.println();
         

  // ***************************ZERO-TRUST ORCHESTRATION REQUIREMENTS*************************
 

         ZTFR.setOrchestration            ("NEED CAPABILITY TO DYNAMICALLY PROVISION IDENTITY, HYGIENE, AUTHORIZATION AND SEGMENTATION POLICIES. ");

         System.out.println               (" SEGMENTATION REQUIREMENT     = " + ZTFR.getOrchestration());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println( "TO CONTINUE WITH NEXT ZERO-TRUST CATEGORY PLEASE SELECT AGAIN CHOICE # 1");
         System.out.println();
         System.out.println("************************************************************************************************" );

        

      }

     else
          
    if ( menuSelect == 7)
       
       {
          System.out.println();
          //System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE ZERO-TRUST ORCHESTRATION REQUIREMENTS ONLY: ");
          System.out.println();
         

         ZTFR.setSegmentation             ("NEED TO LIMIT COMMUNICATION (DIRECTIONAL PORT/PROTOCOL)BETWEEN ALL NETWORK FLOWS TO INCLUDE APPLICATION TIERS. ");

         System.out.println               (" ORCHESTRATION REQUIREMENT    = " + ZTFR.getSegmentation());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println( "TO CONTINUE WITH NEXT ZERO-TRUST CATEGORY PLEASE SELECT AGAIN CHOICE # 1");
         System.out.println();
         System.out.println("************************************************************************************************" );
        

      }

     else

  
// ******************Display the ZERO-TRUST Main Menu************************************

System.out.println();
//System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE ZERO-TRUST FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  FUNCTIONAL REQUIREMENTS. "); 
System.out.println();
System.out.println   ("2.  PROPOSED USE CASES."); 
System.out.println();
System.out.println   ("3.  ARCHITECTURAL REQUIREMENTS."); 
System.out.println();
System.out.println   ("4.  EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER ZERO-TRUST CATEGORY CHOICE 1 - 4)FROM THE LIST ABOVE: ");

       
       menuSelection = keyboard.nextInt();
 
// Validate the ZERO-TRUST Menu selection. 

 while (menuSelection < 1 || menuSelection > 4) 
  
{
 
 
System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID CHOICE FOR ZERO-TRUST CATEGORY SELECTION");
System.out.println();
System.out.println("HERE IS THE VALID LIST OF ZERO-TRUST CATEGORIES: ");
System.out.println();
System.out.println  ("1.  FUNCTIONAL REQUIREMENTS. "); 
System.out.println();
System.out.println  ("2.  PROPOSED USE CASES."); 
System.out.println();
System.out.println  ("3.  ARCHITECTURAL REQUIREMENTS."); 
System.out.println();
System.out.println  ("4.  EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("PLEASE ENTER ZERO-TRUST FRAMEWORK CATEGORY CHOICE (1 - 4)FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();


 
 } 

break;


//*************************ZERO-TRUSTUSE-CASES FRAMEWORK BEGINS HERE******************************************

case 2: 
 
 
 System.out.println();
 //System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED USE-CASES CATEGORY-2 OF ZERO-TRUST FRAMEWORK");
 System.out.println();
 System.out.println("PLEASE SEE BELOW USE-CASES CATEGORIES");

 System.out.println();

ZTSetter ZTUC;

//  Following statement creates an object using the ZTSetter TEMPLATE CLASS as
//  its BLUEPRINT. 

ZTUC = new ZTSetter();

  

 //System.out.println("1.  SHOW ENTIRE LIST OF USE-CASES FOR ZERO-TRUST FRAMEWORK.");
 //System.out.println();
 System.out.println("1.  USE-CASE1: END USER AUTHENTICATION & AUTHORIZATION.");
 System.out.println();
 System.out.println("2.  USE-CASE2: APPLICATION & DATA SEGMENTATION.");
 System.out.println();
 System.out.println("3.  USE-CASE3: ADMIN AUTHENTICATION & AUTHORIZATION.");
 System.out.println();
 System.out.println("4.  USE-CASE4: SECURITY POLICY ORCHESTRATION.");
 System.out.println();

 
  System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM USE-CASE 1 to 4: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE ZERO-TRUST MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 4)
  

  
{
  System.out.println("************************************************************************************************" );
  
 System.out.println("THIS IS INVALID USE-CASE CATEGORY CHOICE SELECTION"); 
 System.out.println();
 System.out.println("PLEASE SELECT A VALID CHOICE FROM THE VALID LIST BELOW"); 
 System.out.println();
 System.out.println("1.  USE-CASE1: END USER AUTHENTICATION & AUTHORIZATION.");
 System.out.println();
 System.out.println("2.  USE-CASE2: APPLICATION & DATA SEGMENTATION.");
 System.out.println();
 System.out.println("3.  USE-CASE3: ADMIN AUTHENTICATION & AUTHORIZATION.");
 System.out.println();
 System.out.println("4.  USE-CASE4: SECURITY POLICY ORCHESTRATION.");
 System.out.println(); 
  System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM USE-CASE 1 to 4: ");


 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW USE-CASE 1 -  END USER AUTHENTICATION AND AUTHORIZATION WALKTHROUGH : ");
          System.out.println();
          
          
           System.out.println("1. USER WILL LEVERAGE A MULTI-FACTOR AUTHENTICATION MECHANISM TO ESTABLISH IDENTITY BASED ON CENTRALIZED IDENTITY PROVIDER");
           System.out.println();
           System.out.println("2. DEVICE WILL ESTABLISH IDENTITY BASED ON A CENTRALIZED IDENTITY PROVIDER. THIS WILL LIKELY BE CERTIFICATE BASED.");
           System.out.println();
           System.out.println("3. THE SECURITY STATUS , PATCH STATUS AND TOOL STATUS OF THE DEVICE WILL BE CONFIRMED BY A HEALTH & COMPLIANCE TOOL FOR LOCAL NETWORK ACCESS.");
           System.out.println();
           System.out.println("4. REAL TIME CONTEXTUAL ACCESS CONTROL DETERMINED BY A VALIDATED IDENTITY.");
           System.out.println();
           System.out.println("5. NETWORK AUTHORIZATION WILL BE PROVIDED BASED ON THE CONTEXUAL ACCESS CONTROL.");
           System.out.println();
           System.out.println("6. ALL AUTHENTICATION & AUTHORIZATION ACTIVITIES WILL BE ACCOUNTED FOR THROUGH LOGS SENT TO THE SECURITY INFORMATION & EVENT MANAGEMENT (SIEM) SOLUTION. " );
           System.out.println();
           System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");
                    
     // Display End_User_Authentication_&_Authorization stored in the fields

     
     // System.out.println               ("ZTUC END USER AUTHENTICATION & AUTHORIZATION                    = " + ZTUC.getEnd_User_Authentication_&_Authorization());
     
       System.out.println();
                 
           
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH USE-CASE 2 PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE USE-CASE 2 - APPLICATION AND DATA SEGMENTATION WALKTHROUGH : ");
         System.out.println();
  
  // *****************Application_And_Data_Segmentation USE CASE***************

        //ZTUC.setApplication_And_Data_Segmentation          
         System.out.println("1. THROUGH THE ADOPTION OF SOFTWARE DEFINED NETWORK (SDN), MICROCORE & PERIMETER (MCAP) ARE IMPLEMENTED FOR SEGMENTATION. MCAP WILL PROVIDE SWITCHING/ROUTING CAPABILITIES ALONG WITH FIREWALL PROTECTIONS.");
         System.out.println();
         System.out.println("2. EACH APPLICATION TIER (WEB, APP, DB) WILL HAVE GRANULAR FIREWALL POLICY TO ISOLATE TRAFFIC BASED ON PORT & PROTOCOL. MICRO SEGMENTATION ALLOWS FOR THIS POLICY TO BE ENFORCED EVEN WHEN SYSTEMS ARE ON THE SAME SUBNET.");
         System.out.println();
         System.out.println("3. APPLICATION PROCESSES WILL BE LEARNED & WHITELISTED AS THE CORRECT PROCESS FOR LEVERAGING A PORT & PROTOCOL.");
         System.out.println();
         System.out.println("4. DATA WILL BE TAGGED 7 SPECIFICALLY ASSOCIATED WITH SYSTEMS/APPLICATIONS.");
         System.out.println();
         System.out.println("5. ALL AUTHORIZATIONS ACTIVITIES WILL BE ACCOUNTED FOR THROUGH LOGGING TO THE SIEM.");
         System.out.println();
         System.out.println("6. ALL AUTHENTICATION & AUTHORIZATION ACTIVITIES WILL OCCUR AGAINST THE CENTRALIZED IDENTITY PROVIDER." );
         System.out.println();
         System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");
      
//**************** Display the APPLICATION AND DATA SEGMENTATION USE CASE****************

     
     // System.out.println               ("ZTUC APPLICATION AND DATA SEGMENTATION   = " + ZTUC.getApplication_And_Data_Segmentation());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH USE-CASE 3 PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW USE-CASE 3 - THE ADMIN AUTHENTICATION & AUTHORIZATION WALKTHROUGH : ");
         System.out.println();
         System.out.println("***********************************************************************************" );
        // *****************Admin_Authentication_&_Authorization USE CASE***************

        //ZTUC.setAdmin_Authentication_&_Authorization
               
         System.out.println("1.THE ADMINISTRATOR WILL LEVERAGE A MULTI-FACTOR AUTHENTICATION MECHANISM TO ESTABLISH IDENTITY BASED ON A CENTRALIZED IDENTITY PROVIDER.");
         System.out.println();
         System.out.println("2. AS ACCESS IS NEEDED TO MANAGE SYSTEMS A JUST-IN-TIME (JIT) GATEWAY WILL PROVIDE THE AUTHORIZATION DIRECTLY TO THE SYSTEM. THIS GATEWAY MAY ALSO PROVIDE A PROXY RDP OR SSH SESSION FOR MANAGEMENT.");
         System.out.println();
         System.out.println("3. SYSTEMS WILL EITHER BE MANAGED VIA JIT GATEWAY OR VIA API FROM AN ORCHESTRATION TOOL. MANAGEMENT WILL OCCUR OVER A ISOLATED MANAGEMENT SEGMENT OF THE NETWORK.");
         System.out.println();
         System.out.println("4. ALL AUTHORIZATION ACTIVITIES WILL BE ACCOUNTED FOR THROUGH LOGGING TO THE SIEM.");
         System.out.println();
         System.out.println("5. THE CENTRALIZED IDENTITY PROVIDER WILL BE LEVERAGED FOR ALL IDENTITIES AND AUTHORIZATIONS.");
         System.out.println();
         System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");

         
      
//**************** Display Admin_Authentication_&_Authorization USE CASE REQUIREMENTS****************

     
      //System.out.println               ("ZTUC ADMIN AUTHENTICATION AND AUTHORIZATION   = " + ZTUC.getAdmin_Authentication_&_Authorization());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH USE-CASE 4 PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );
 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         //System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW USE-CASE 4 - SECURITY POLICY ORCHESTRATION WALKTHROUGH : ");
         System.out.println();
  
  // *****************Security_Policy_Orchestration***************

        //ZTUC.setSecurity_Policy_Orchestration 
                        
         System.out.println("1.THE SDE GLOBAL ORCHESTRATOR WILL ENABLE SERVICE DELIVERY AND CYBER OPERATIONS ACROSS THE AGENCY. THIS WILL ASSOCIATERELEVANT SECURITY POLICIES WITH WORKLOAD DEPLOYMENTS .");
         System.out.println();
         System.out.println("2.SERVICE-LEVEL ORCHESTRATORS WILL FURTHER DEPLOY SPECIFIC SYSTEMS AND THEIR ASSOCIATED SECURITY POLICY. SECURITY POLICY WILL BE VERY GRANULAR AND IS BEST IMPLEMENTED VIA API AT DEPLOYMENT TIME ."); 
         System.out.println();       
         System.out.println("3. POLICY ENFORCEMENT ENGINES WILL ACCEPT THE POLICY VIA REST API AND ENFORCE ON THE INFRASTUCTURE.");
         System.out.println();
         System.out.println("4. ALL ORCHESTRATION ACTIVITIES WILL BE ACCOUNTED FOR THROUGH LOGGING TO THE SIEM.");
         System.out.println();
         System.out.println("5. ORCHESTRATED/AUTOMATED POLICIES WILL INCLUDE THE DEPLOYMENT OF IDENTITY AND ROLES ON THE CENTRALIZED IDENTITY PROVIDER.");
         System.out.println();
         System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");


      
//**************** Display the Security_Policy_Orchestration REQUIREMENTS****************

     
     // System.out.println               ("ZTUC SECURITY POLICY ORCHESTRATION   = " + ZTUC.getSecurity_Policy_Orchestration());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH USE-CASE4 PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );
      }

  else
   
               
 
// ******************Display the ZERO-TRUST Main Menu************************************

System.out.println();
//System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE ZERO-TRUST FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  FUNCTIONAL REQUIREMENTS. "); 
System.out.println();
System.out.println   ("2.  PROPOSED USE CASES."); 
System.out.println();
System.out.println   ("3.  ARCHITECTURAL REQUIREMENTS."); 
System.out.println();
System.out.println   ("4.  EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER ZERO-TRUST CATEGORY CHOICE 1 - 4)FROM THE LIST ABOVE: ");
       
       menuSelection = keyboard.nextInt();
 
// Validate the ZERO-TRUST Menu selection. 

 while (menuSelection < 1 || menuSelection > 4) 
  
{
 
 
System.out.println("THIS IS INVALID CHOICE FOR ZERO-TRUST CATEGORY SELECTION");
System.out.println();
System.out.println("HERE IS THE VALID LIST OF ZERO-TRUST CATEGORIES: ");
System.out.println();
System.out.println   ("1.  FUNCTIONAL REQUIREMENTS. "); 
System.out.println();
System.out.println   ("2.  PROPOSED USE CASES."); 
System.out.println();
System.out.println   ("3.  ARCHITECTURAL REQUIREMENTS."); 
System.out.println();
System.out.println   ("4.  EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("PLEASE ENTER ZERO-TRUST CATEGORY CHOICE (1 - 4)FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();

  
 } 


break; 

//*************************ZERO- TRUST FRAMEWORK CATEGORY-3 - ARCHITECTURAL REQUIREMENTS******************************************

case 3:

 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED ARCHITECTURAL REQUIREMENTS CATEGORY OF ZERO-TRUST FRAMEWORK");
 System.out.println();
 System.out.println("PLEASE SEE BELOW ARCHITECTURAL REQUIREMENTS CATEGORIES");
 System.out.println();

ZTSetter ZTAR;

//  Following statement creates an object using the AZTSetter class as
//its Blueprint. ject.

ZTAR = new ZTSetter();

  

 System.out.println("1.  SHOW IDENTITY REQUIREMENTS.");
 System.out.println();
 System.out.println("2.  SHOW HEALTH & COMPLIANCE REQUIREMENTS.");
 System.out.println();
 System.out.println("3.  SHOW AUTHORIZATION REQUIREMENTS.");
 System.out.println();
 System.out.println("4.  SHOW ACCOUNTING & AUDITING REQUIREMENTS.");
 System.out.println();
 System.out.println("5.  SHOW SEGMENTATION REQUIREMENTS.");
 System.out.println();
 System.out.println("6.  SHOW ORCHESTRATION REQUIREMENTS.");
 System.out.println();
 System.out.println("7.  SHOW ADDITIONAL - CLOUD, DTAT TAGGING, DICOVERY REQUIREMENTS.");
 System.out.println();
 System.out.println("8.  SHOW OPTIONAL REQUIREMENTS.");
 System.out.println();
 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR ARCHITECTURAL REQUIREMENTS CHOICE FROM 1 to 8: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE ZERO-TRUST MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 8)
  

  
{
  System.out.println("************************************************************************************************" );
  
 System.out.println    ("THIS IS INVALID SELECTION"); 
 System.out.println();
 System.out.println    ("ENTER YOUR ARCHITECTURAL REQUIREMENTS SELECTION FROM 1 to 8: ");
 System.out.println();
 System.out.println("1.  SHOW IDENTITY REQUIREMENTS.");
 System.out.println();
 System.out.println("2.  SHOW HEALTH & COMPLIANCE REQUIREMENTS.");
 System.out.println();
 System.out.println("3.  SHOW AUTHORIZATION REQUIREMENTS.");
 System.out.println();
 System.out.println("4.  SHOW ACCOUNTING & AUDITING REQUIREMENTS.");
 System.out.println();
 System.out.println("5.  SHOW SEGMENTATION REQUIREMENTS.");
 System.out.println();
 System.out.println("6.  SHOW ORCHESTRATION REQUIREMENTS.");
 System.out.println();
 System.out.println("7.  SHOW ADDITIONAL - CLOUD, DTAT TAGGING, DICOVERY REQUIREMENTS.");
 System.out.println();
 System.out.println("8.  SHOW OPTIONAL REQUIREMENTS.");
 System.out.println();
 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR ARCHITECTURAL REQUIREMENTS CHOICE FROM 1 to 8: ");


 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println();
          //System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IDENTITY REQUIREMENTS : ");
          System.out.println();
          
          //ZTAR.setIdentityRequirements("The system shall not assume trust of the device or user 1.1 The system shall have the capability to identify the user 1.2 The system shall have the capability to identify the device 1.2.1 The system shall be able to identify client and server endpoints 1.2.2 The system shall be able to identify network devices 2 The system shall integrate with an enterprise identity provider 2.1 The system shall be able to integrate with industry standard providers such as Active Directory, Radius, LDAP, OAUTH, OpenID Connect and SAML 3 The system shall support enterprise authentication methods 3.1 The system shall support certificate-based authentication 3.2 The system shall support public key infrastructure 3.3 The system shall support or integrate with multifactor authentication 4 The system shall have the ability to continuously challenge identity 4.1 The system shall support multiple attributes such as geolocation to challenge identity 5 The system shall connect to a centralized identity source 6 The system shall have the capability to redirect or drop unidentified users or machines" );         
          
          
                                                System.out.println("1. The system shall not assume trust of the device or user".toUpperCase());
                                                System.out.println();
                                                System.out.println("1.1 The system shall have the capability to identify the user".toUpperCase());
                                                System.out.println();
                                                System.out.println("1.2 The system shall have the capability to identify the device".toUpperCase());
                                                System.out.println();
                                                System.out.println("1.2.1 The system shall be able to identify client and server endpoints".toUpperCase());
                                                System.out.println();
                                                System.out.println("1.2.2 The system shall be able to identify network devices" .toUpperCase());
                                                System.out.println();
                                                System.out.println("2 The system shall integrate with an enterprise identity provider".toUpperCase());
                                                System.out.println();
                                                System.out.println("2.1 The system shall be able to integrate with industry standard providers such as Active Directory, Radius, LDAP, OAUTH, OpenID Connect and SAML".toUpperCase());
                                                System.out.println();
                                                System.out.println("3 The system shall support enterprise authentication methods".toUpperCase());
                                                System.out.println();
                                                System.out.println("3.1 The system shall support certificate-based authentication".toUpperCase());
                                                System.out.println();
                                                System.out.println("3.2 The system shall support public key infrastructure".toUpperCase());
                                                System.out.println();
                                                System.out.println("3.3 The system shall support or integrate with multifactor authentication" .toUpperCase());
                                                System.out.println();
                                                System.out.println("4 The system shall have the ability to continuously challenge identity".toUpperCase());
                                                System.out.println();
                                                System.out.println("4.1 The system shall support multiple attributes such as geolocation to challenge identity".toUpperCase());
                                                System.out.println();
                                                System.out.println("5 The system shall connect to a centralized identity source".toUpperCase());
                                                System.out.println();
                                                System.out.println("6 The system shall have the capability to redirect or drop unidentified users or machines. ".toUpperCase());
                                                System.out.println();
                                                System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");         
        

         
// Display the IDENTITY REQUIREMENTS stored in the fields

     
     // System.out.println               ("ARCHITECTURAL - IDENTITY REQUIREMENTS     = " + ZTAR.getIdentityRequirements());
      System.out.println();
               
      System.out.println();
     
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ARCHITECTURAL REQUIREMENTS PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 3"); 
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW HEALTH & COMPLIANCE REQUIREMENTS ");
         System.out.println();
  
  // *****************Health Compliance Requirements***************

       // ZTAR.setHealthComplianceRequirements ("1 The system shall determine or integrate with a solution that is able to determine the health & compliance of the endpoint 1.1 The system shall determine or integrate with a solution that is able to determine the security posture of the device such as OS STIG compliance 1.2 The system shall determine or integrate with a solution that is able to determine the patch level of the device 1.3 The system shall determine or integrate with a solution that is able to determine if any tools or agents are missing from the device 1.4 The system shall determine or integrate with a solution that is able to determine if any unauthorized software is on the device 1.5 The system shall determine or integrate with a solution that is able to determine the fully qualified domain name, IP address, MAC address and operating system of the device 2 The system shall be able to place or integrate with a solution that is able to place a machine in remediation for not meeting compliance 3 The system shall determine or integrate with a solution to determine be able to determine health and compliance across multiple device types "); 
        
System.out.println("1 The system shall determine or integrate with a solution that is able to determine the health & compliance of the endpoint".toUpperCase()); 
System.out.println();
System.out.println("1.1 The system shall determine or integrate with a solution that is able to determine the security posture of the device such as OS STIG compliance".toUpperCase());
System.out.println(); 
System.out.println("1.2 The system shall determine or integrate with a solution that is able to determine the patch level of the device".toUpperCase());
System.out.println();
System.out.println("1.3 The system shall determine or integrate with a solution that is able to determine if any tools or agents are missing from the device".toUpperCase());
System.out.println(); 
System.out.println("1.4 The system shall determine or integrate with a solution that is able to determine if any unauthorized software is on the device".toUpperCase());
System.out.println(); 
System.out.println("1.5 The system shall determine or integrate with a solution that is able to determine the fully qualified domain name, IP address, MAC address and operating system of the device".toUpperCase());
System.out.println(); 
System.out.println("2 The system shall be able to place or integrate with a solution that is able to place a machine in remediation for not meeting compliance".toUpperCase());
System.out.println(); 
System.out.println( "3 The system shall determine or integrate with a solution to determine be able to determine health and compliance across multiple device types".toUpperCase());
System.out.println();
System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");

    
//**************** Display the Health Compliance Requirements****************

     
      //System.out.println    ("ARCHITECTURAL - HEALTH & COMPLIANCE REQUIREMENTS = " + ZTAR.getHealthComplianceRequirements());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ARCHITECTURAL REQUIREMENTS PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 3"); 
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         //System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW AUTHORIZATION REQUIREMENTS ");
         System.out.println();
         

  
 // *****************Authorization Requirements*****************
 
 
       //  ZTAR.setAuthorizationRequirements ("1 The system shall control authorization of user and machines 1.1 The system shall be able to assign role based access controls to groups and users 2 The system shall support time limited authorization for administrators 2.1 The system shall provide a portal to request privileged access to systems 3 The system shall associate identity to authorization policy through integration of Zero Trust Architecture tools 3.1 The system shall align network security policy to authorization of users and machines 4 The system shall support dynamic/real-time access decisions 5 The system shall support querying to determine authorization level of user or device ");        
         
System.out.println("1 The system shall control authorization of user and machines".toUpperCase());
System.out.println();
System.out.println("1.1 The system shall be able to assign role based access controls to groups and users".toUpperCase()); 
System.out.println();
System.out.println("2 The system shall support time limited authorization for administrators".toUpperCase());
System.out.println(); 
System.out.println("2.1 The system shall provide a portal to request privileged access to systems".toUpperCase()); 
System.out.println();
System.out.println("3 The system shall associate identity to authorization policy through integration of Zero Trust Architecture tools".toUpperCase());
System.out.println();
System.out.println("3.1 The system shall align network security policy to authorization of users and machines".toUpperCase()); 
System.out.println();
System.out.println("4 The system shall support dynamic/real-time access decisions".toUpperCase());
System.out.println();
System.out.println("5 The system shall support querying to determine authorization level of user or device".toUpperCase());
System.out.println();
System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");
       
        
        // System.out.println   ("ARCHITECTURAL - AUTHORIZATION REQUIREMENTS = " +ZTAR.getAuthorizationRequirements());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ARCHITECTURAL REQUIREMENTS PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 3"); 
      System.out.println();
      System.out.println("************************************************************************************************" );


 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         //System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW ACCOUNTING & AUDITING REQUIREMENTS ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      //ZTAR.setAccountingAuditingRequirements ("1 The system shall provide accounting of all elements with the Zero Trust Architecture/n 1.1 The system shall provide accounting of user and device identity 1.2 The system shall provide accounting each time authorization is provided or changed 1.3 The system shall provide accounting each time segmentation policy is implemented or changed 2 The system shall provide accounting all network flows within the Zero Trust Architecture 2.1 The system shall provide a packet capture capability 2.2 The system shall provide logging and account for transaction of all production data flows 2.3 The system shall should support offloading to enterprise security and event manager tools 3 The system shall provide log data via REST API to log aggregator "); 
    
System.out.println("1 The system shall provide accounting of all elements with the Zero Trust Architecture".toUpperCase());
System.out.println();
System.out.println("1.1 The system shall provide accounting of user and device identity".toUpperCase());
System.out.println();
System.out.println("1.2 The system shall provide accounting each time authorization is provided or changed".toUpperCase()); 
System.out.println();
System.out.println("1.3 The system shall provide accounting each time segmentation policy is implemented or change".toUpperCase());
System.out.println();
System.out.println("2 The system shall provide accounting all network flows within the Zero Trust Architecture".toUpperCase());
System.out.println(); 
System.out.println("2.1 The system shall provide a packet capture capability".toUpperCase());
System.out.println();                                               
System.out.println("2.2 The system shall provide logging and account for transaction of all production data flows".toUpperCase());
System.out.println();
System.out.println("2.3 The system shall should support offloading to enterprise security and event manager tools".toUpperCase()); 
System.out.println();                                              
System.out.println("3 The system shall provide log data via REST API to log aggregator".toUpperCase());
System.out.println();
System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");       

     // System.out.println("ARCHITECTURAL - ACCOUNTING & AUDITING REQUIREMENTS = " + ZTAR.getAccountingAuditingRequirements());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ARCHITECTURAL REQUIREMENTS PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 3"); 
      System.out.println();
      System.out.println("************************************************************************************************" );
      
      }
      else
      
 if ( menuSelect == 5 )
     
        {
         System.out.println();
         //System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW SEGMENTATION REQUIREMENTS ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
        // ZTAR.setSegmentationRequirements("1 The system shall provide network segmentation of application systems (micro-segmentation)/n 1.1 The system shall be able to apply role based rule sets to group and individual systems 1.2 The system shall segment north-south network flows 1.3 The system shall segment east-west network flows 1.4 The system shall segment end-to-end/transport network flows 2 The system shall provide segmentation of both stateless and stateful application flows 3 The system shall segment host-level processes for security policies ");       
         
                                                   System.out.println("1 The system shall provide network segmentation of application systems (micro-segmentation) ".toUpperCase());
                                                   System.out.println();
                                                   System.out.println("1.1 The system shall be able to apply role based rule sets to group and individual systems".toUpperCase());
                                                   System.out.println();
                                                   System.out.println("1.2 The system shall segment north-south network flows ".toUpperCase());
                                                   System.out.println();
                                                   System.out.println("1.3 The system shall segment east-west network flows".toUpperCase());
                                                   System.out.println();
                                                   System.out.println("1.4 The system shall segment end-to-end/transport network flows ".toUpperCase());
                                                   System.out.println();
                                                   System.out.println("2 The system shall provide segmentation of both stateless and stateful application flows ".toUpperCase());
                                                   System.out.println();
                                                   System.out.println("3 The system shall segment host-level processes for security policies".toUpperCase());
                                                   System.out.println();
                                                   System.out.println("5 The system shall support querying to determine authorization level of user or device".toUpperCase());
                                                   System.out.println();
                                                   System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");
 
        
        // System.out.println   ("ARCHITECTURAL - AUTHORIZATION REQUIREMENTS = " + ZTAR.getAuthorizationRequirements());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ARCHITECTURAL REQUIREMENTS PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 3"); 
      System.out.println();
      System.out.println("************************************************************************************************" );


 
   }
   
   else
   
      if ( menuSelect == 6)
      
       {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW ORCHESTRATION REQUIREMENTS ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      //ZTAR.setOrchestrationRequirements("1 The system shall support automation through REST APIs/n 1.1 The system shall accept REST APIs to configuration of infrastructure and tools to include identity, security and accounting policies 2 The system shall support dynamic policy enforcement and changes ");
      
                                              System.out.println("1 The system shall support automation through REST APIs ".toUpperCase());
                                              System.out.println();       
                                              System.out.println("1.1 The system shall accept REST APIs to configuration of infrastructure and tools to include identity, security and accounting policies ".toUpperCase());
                                              System.out.println();
                                              System.out.println("2 The system shall support dynamic policy enforcement and changes".toUpperCase()); 
                                              System.out.println();
                                              System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");
                                              
      //System.out.println("ARCHITECTURAL - ACCOUNTING & AUDITING REQUIREMENTS = " + ZTAR.getAccountingAuditingRequirements());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ARCHITECTURAL REQUIREMENTS PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 3"); 
      System.out.println();
      System.out.println("************************************************************************************************" );
      }

  else
   
    if ( menuSelect == 7)
      
       {
         System.out.println();
         //System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW ADDITIONAL - CLOUD, DATA TAGGING, DISCOVERY REQUIREMENTS ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      //ZTAR.setAdditionalCloudDataTaggingDiscoveryRequirements(" 1 The system shall provide the same protections across cloud hosted environments/ 1.1 The system shall support CSP IaaS offerings 1.2 The system shall support CSP PaaS offerings 1.3 The system shall support CSP SaaS offerings 1.4 The system shall protect/proxy CSP administrative access 2 The system shall support tagging of data 3 The system shall support asset discovery 3.1 The system shall be able to discover assets on the network 3.2 The system shall be able to discover flows between assets on the network"); 
      
                                             System.out.println("1 The system shall provide the same protections across cloud hosted environments ".toUpperCase());
                                             System.out.println();  
                                             System.out.println("1.1 The system shall support CSP IaaS offerings".toUpperCase());
                                             System.out.println(); 
                                             System.out.println("1.2 The system shall support CSP PaaS offerings ".toUpperCase());
                                             System.out.println();     
                                             System.out.println("1.3 The system shall support CSP SaaS offerings".toUpperCase());
                                             System.out.println(); 
                                             System.out.println("1.4 The system shall protect/proxy CSP administrative access ".toUpperCase());
                                             System.out.println();  
                                             System.out.println("2 The system shall support tagging of data ".toUpperCase());
                                             System.out.println(); 
                                             System.out.println("3 The system shall support asset discovery".toUpperCase());
                                             System.out.println();  
                                             System.out.println("3.1 The system shall be able to discover assets on the network".toUpperCase());
                                             System.out.println();  
                                             System.out.println("3.2 The system shall be able to discover flows between assets on the network".toUpperCase());
                                             System.out.println();
                                             System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");
      

     // System.out.println("ARCHITECTURAL - ACCOUNTING & AUDITING REQUIREMENTS = " + ZTAR.getAccountingAuditingRequirements());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ARCHITECTURAL REQUIREMENT PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 3"); 
      System.out.println();
      System.out.println("************************************************************************************************" );
      }
else
                  
    if ( menuSelect == 8)
      
       {
         System.out.println();
         //System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW OPTIONAL REQUIREMENTS ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      //TAR.setOptionalRequirements("1 The system shall replace existing security architecture constructs/n 1.1 The system shall replace existing perimeter security capabilities 2 The system shall integrate with existing security architecture constructs and requirements 2.1 The system shall integrate with web application firewalls 2.2 The system shall integrate with application aware firewalls 2.3 The system shall integrate with database firewalls 2.3 The system shall integrate with intrusion prevention systems (IPS) "); 
      
                                              System.out.println("1 The system shall replace existing security architecture constructs ".toUpperCase());
                                              System.out.println();
                                              System.out.println("1.1 The system shall replace existing perimeter security capabilities".toUpperCase());
                                              System.out.println();
                                              System.out.println("2 The system shall integrate with existing security architecture constructs and requirements ".toUpperCase());
                                              System.out.println();
                                              System.out.println("2.1 The system shall integrate with web application firewalls ".toUpperCase());
                                              System.out.println();
                                              System.out.println("2 The system shall provide accounting all network flows within the Zero Trust Architecture".toUpperCase());
                                              System.out.println(); 
                                              System.out.println("2.2 The system shall integrate with application aware firewalls".toUpperCase());
                                              System.out.println(); 
                                              System.out.println("2.3 The system shall integrate with database firewalls ".toUpperCase());
                                              System.out.println(); 
                                              System.out.println("2.4 The system shall integrate with intrusion prevention systems (IPS)".toUpperCase());
                                              System.out.println();
                                              System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");
                                              


       

      //System.out.println("ARCHITECTURAL - ACCOUNTING & AUDITING REQUIREMENTS = " + ZTAR.getAccountingAuditingRequirements());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ARCHITECTURAL REQUIREMENTS PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 3"); 
      System.out.println();
      System.out.println("************************************************************************************************" );
      }

  else
  

// ******************Display the ZERO-TRUST Main Menu************************************

System.out.println();
//System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE ZERO-TRUST FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  FUNCTIONAL REQUIREMENTS. "); 
System.out.println();
System.out.println   ("2.  PROPOSED USE CASES."); 
System.out.println();
System.out.println   ("3.  ARCHITECTURAL REQUIREMENTS."); 
System.out.println();
System.out.println   ("4.  EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER ZERO-TRUST CATEGORY CHOICE 1 - 4)FROM THE LIST ABOVE: ");
       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 4) 
  
{
 
 
System.out.println("THIS IS INVALID CHOICE FOR ZERO-TRUST CATEGORY SELECTION");
System.out.println();
System.out.println("HERE IS THE VALID LIST OF ZERO-TRUST CATEGORIES: ");
System.out.println();
System.out.println  ("1.  FUNCTIONAL REQUIREMENTS. "); 
System.out.println();
System.out.println  ("2.  PROPOSED USE CASES."); 
System.out.println();
System.out.println  ("3.  ARCHITECTURAL REQUIREMENTS."); 
System.out.println();
System.out.println  ("4.  EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("PLEASE ENTER ZERO-TRUST CATEGORY CHOICE (1 - 4)FROM THE LIST ABOVE: ");

   

  
  menuSelection = keyboard.nextInt();

  
 } 


break;

case 4: 
 
 
 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED EVALUATION-CRITERIA CATEGORY OF ZERO-TRUST FRAMEWORK");
 System.out.println();
 System.out.println("PLEASE SEE BELOW EVALUATION-CRITERIA CATEGORIES");

 System.out.println();

ZTSetter ZTEC;

//  Following statement creates an object using the AiSetter class as
//its Blueprint. Centcom will reference the object.

ZTEC = new ZTSetter();

  

 //System.out.println("1.  SHOW ENTIRE LIST OF USE CASES FOR ZERO-TRUST FRAMEWORK.");
 //System.out.println();
 System.out.println("1.  SHOW ENTIRE LIST OF EVALUATION CRITERIA.");
 System.out.println();
 System.out.println("2.  EVALUATION-CRITERIA FOR EFFECTIVENESS.");
 System.out.println();
 System.out.println("3.  EVALUATION-CRITERIA FOR SUITABILITY.");
 System.out.println();
 System.out.println("4.  EVALUATION-CRITERIA FOR PERFORMANCE.");
 System.out.println();

 
  System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM EVALUATION CRITERIA CATEGORIES 1 to 4: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 4)
  

  
{
  System.out.println("************************************************************************************************" );
  
 System.out.println("THIS IS INVALID CHOICE FOR EVALUATION-CRITERIA SELECTION"); 
 System.out.println();
 System.out.println("PLEASE SELECT A VALID CHOICE FROM THE LIST BELOW"); 
 System.out.println();
 System.out.println("1.  SHOW ENTIRE LIST OF EVALUATION-CRITERIA.");
 System.out.println();
 System.out.println("2.  EVALUATION-CRITERIA FOR EFFECTIVENESS.");
 System.out.println();
 System.out.println("3.  EVALUATION-CRITERIA FOR SUITABILITY.");
 System.out.println();
 System.out.println("4.  EVALUATION-CRITERIA FOR PERFORMANCE.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR EVALUATION-CRITERIA CHOICE FROM USE-CASE 1 to 4: ");


 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println();
          //System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE LIST OF ENTIRE-EVALUATION CRITERIA ");
          System.out.println();
          
          ZTEC.setEffectiveness   (" ABILITY TO ACCOMPLISH MISSION OBJECTIVES & ACHEIVEMENT OF DESIRED RESULTS - ALIGNED TO ZTA REQUIREMENTS. " );
          ZTEC.setSuitability       (" ABILITY OF SOLUTION TO BE SUPPORTED IN THE INTENDED OPERATIONAL ENVIRONMENT WHICH IS ALIGNED TO COMMON OPERATIONAL REQUIREMENTS (AUTOMATION, ARCHITECTURE, SECURITY). " );
          ZTEC.setPerformance     (" MEASURE OF SYSTEMS PERFORMANCE EXPRESSED IN QUATIFIABLE FORM - FOCUSED ON DEPLOYMENT FOOTPRINT & SCALABILITY. " );
          
         
// Display the AC taxonomy values stored in the fields

     
      System.out.println               ("EVALUATION CRITERIA - EFFECTIVENESS      = " + ZTEC.getEffectiveness());
      System.out.println();
      System.out.println               ("EVALUATION CRITERIA - SUITABILITY        = " + ZTEC.getSuitability());
      System.out.println();
      System.out.println               ("EVALUATION CRITERIA - PERFORMANCE        = " + ZTEC.getPerformance());
      System.out.println();
                 
           
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH EVALUATION-CRITERIA PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else 
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE EVALUATION-CRITERIA FOR EFFECTIVENESS ONLY : ");
         System.out.println();
  
  // *****************Information Types***************

       ZTEC.setEffectiveness   (" ABILITY TO ACCOMPLISH MISSION OBJECTIVES & ACHEIVEMENT OF DESIRED RESULTS - ALIGNED TO ZTA REQUIREMENTS. " ); 
            
//**************** Display the USTRANSCOM IOT INFORMATION TYPES****************

     
      System.out.println               ("EVALUATION CRITERIA - EFFECTIVENESS                    = " + ZTEC.getEffectiveness());

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH EVALUATION-CRITERIA PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );

      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         //System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE EVALUATION-CRITERIA FOR SUITABILITY ONLY ");
         System.out.println();
  
  // *****************Information Types***************

         ZTEC.setSuitability(" ABILITY OF SOLUTION TO BE SUPPORTED IN THE INTENDED OPERATIONAL ENVIRONMENT WHICH IS ALIGNED TO COMMON OPERATIONAL REQUIREMENTS (AUTOMATION, ARCHITECTURE, SECURITY). " );
      
//**************** Display the USTRANSCOM IOT INFORMATION TYPES****************

     
      System.out.println               ("EVALUATION CRITERIA - SUITABILITY                      = " + ZTEC.getSuitability());
;
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH EVALUATION-CRITERIA PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );
 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE EVALUATION-CRITERIA FOR PERFORMANCE ONLY ");
         System.out.println();
  
  // *****************EVALUATION-CRITERIA FOR PERFORMANCE***************

        ZTEC.setPerformance     (" MEASURE OF SYSTEMS PERFORMANCE EXPRESSED IN QUATIFIABLE FORM - FOCUSED ON DEPLOYMENT FOOTPRINT & SCALABILITY. " ); 
             
//**************** Display the EVALUATION-CRITERIA FOR PERFORMANCE****************

     
      System.out.println               ("EVALUATION CRITERIA - PERFORMANCE   = " + ZTEC.getPerformance());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH EVALUATION-CRITERIA PLEASE SELECT AGAIN ZERO-TRUST CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );
      }

  else
  
  

// ******************Display the Main menu************************************

System.out.println();
//System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE ZERO-TRUST FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  FUNCTIONAL REQUIREMENTS. "); 
System.out.println();
System.out.println   ("2.  PROPOSED USE CASES."); 
System.out.println();
System.out.println   ("3.  ARCHITECTURAL REQUIREMENTS."); 
System.out.println();
System.out.println   ("4.  EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER ZERO-TRUST CATEGORY CHOICE 1 - 4)FROM THE LIST ABOVE: ");
       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 4) 
  
{
 
 
System.out.println("THIS IS INVALID CHOICE FOR ZERO-TRUST CATEGORY SELECTION");
System.out.println();
System.out.println("HERE IS THE VALID LIST OF ZERO-TRUST CATEGORIES: ");
System.out.println();
System.out.println   ("1.  FUNCTIONAL REQUIREMENTS. "); 
System.out.println();
System.out.println  ("2.  PROPOSED USE CASES."); 
System.out.println();
System.out.println  ("3.  ARCHITECTURAL REQUIREMENTS."); 

System.out.println  ("4.  EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("PLEASE ENTER ZERO-TRUST CATEGORY CHOICE (1 - 4)FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();

  
 } 


break; 
 
    }
  }
}

//*************************************END OF IOT TAXONOMY & FRAMEWORK PROGRAM***********************************************