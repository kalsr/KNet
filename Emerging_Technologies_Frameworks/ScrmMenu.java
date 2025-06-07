
// SUPPLY CHAIN RISK MANAGEMENT(SCRM)FRAMEWORK APPLICATION DEVELOPMENT  
// THIS FRAMEWORK APPLICATION WAS WRITTEN USING OBJECT-ORIENTED PROGRAMMING LANGUUAGE JAVA USING JGRASP (APRIL, 2019)
// SCRM FRAMEWORK APPLICATION WILL PROVIDE ABSTRACTION OF THE FUNCTIONS NEEDED TO DEVELOP A PROTOTYPE OR PROOF OF CONCEPT
// THE APPLICATION WAS WRITTEN BY Mr Randy Singh,FROM TECHNOLOGY INNOVATION TEAM (DISA/BDE5)
// CONTACT PHONE # (301)225-9535  

import java.util.Scanner; 

public class ScrmMenu 

{
public static void main(String[] args) 
{
 
// Declare a variable to hold the 
// user's menu selection. 

int menuSelection;

final int MAX_VALUE = 7;
 
// Declare variables to hold the units 
// of measurement.
 
 String SCT1GS, SCT1A, SCT2GS, SCT2A, SCT3GS, SCT3A;
 String SCTAS, SCTAE, SCTIS, SCTIE, SCTFIS, SCTFIE, SCTSVCS, SCTSVCE, SCTTSS, SCTTSE, SCTIECCS, SCTIECCE;
 String SCTCT1TC, SCTCT1M, SCTCT2TC, SCTCT2M, SCTCT3TC,SCTCT3M;
 String SCVCT1VC, SCVCT1M, SCVCT2VC, SCVCT2M, SCVCT3VC,SCVCT3M;
 String SCCT1AC, SCCT1ICT, SCCT2AC, SCCT2ICT, SCCT3AC, SCCT3ICT;
 String SCVMOT1VT, SCVMOT1MT, SCVMOT2VT, SCVMOT2MT, SCVMOT3VT, SCVMOT3MT;
 String SCPCT1C, SCPCT1E, SCPCT2C, SCPCT2E, SCPCT3C, SCPCT3E;
 
  
// Create a Scanner object for keyboard input. 

Scanner keyboard = new Scanner(System.in); 

// Display the LIST OF BIG DATA Taxonomy Categories 

System.out.println();

System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("WELCOME TO SUPPLY-CHAIN RISK MANAGEMENT FRAMEWORK APPLICATION: ");
System.out.println();
System.out.println   ("HERE ARE THE SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  SCRM STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 7) 
  
{
 
System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID SCRM FRAMEWORK SELECTION CATEGORY");
System.out.println();
System.out.println  ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE IS THE VALID SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println    ("1. SCRM ORGANIZATION & STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


  
 menuSelection = keyboard.nextInt();
  
 } 
 
 while (menuSelection > 0 || menuSelection <= 7)
 
  



 switch(menuSelection)
 
{ 

//************************* SCRM ORGANIZATION & STAKEHOLDERS TIERS ******************************************


 case 1:
 
 int menuSelect;
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED SCRM ORGANIZATION & STAKEHOLDERS TIERS.  ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW SUBCATEGORIES OF SCRM STAKEHOLDERS ");
 System.out.println();

ScrmSetter SCRMOS;

//Following statement creates an object using the AiSetter Class as
// its Blueprint. 

SCRMOS = new ScrmSetter();

//*****************DISPLAY THE COCOMS IOT MENU***************
  
 System.out.println();
 System.out.println("1.  SHOW ENTIRE LIST OF SCRM ORGANIZATION & STAKEHOLDERS TIERS.");
 System.out.println();
 System.out.println("2.  SCRM TIER-1: ORGANIZATION STAKE-HOLDERS.");
 System.out.println();
 System.out.println("3.  SCRM TIER-1: ORGANIZATION ACTIVITIES.");
 System.out.println();
 System.out.println("4.  SCRM TIER-2: MISSION STAKE-HOLDERS.");
 System.out.println();
 System.out.println("5.  SCRM TIER-2: MISSION ACTIVITIES.");
 System.out.println();
 System.out.println("6.  SCRM TIER-3: INFORMATION-SYSTEMS STAKE-HOLDERS.");
 System.out.println();
 System.out.println("7.  SCRM TIER-3: INFORMATION-SYSTEMS ACTIVITIES.");
 System.out.println();
   //System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER SCRM TIERS CATEGORY CHOICE FROM 1 to 7: ");
   
 
  menuSelect = keyboard.nextInt();

System.out.println("************************************************************************************************" );

 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 7)
  

  
{
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("THIS IS INVALID SCRM ORGANIZATION & STAKEHOLDERS TIERS CATEGORY SELECTION"); 
 System.out.println();
 System.out.print(" ENTER YOUR SCRM ORGANIZATION & STAKEHOLDERS TIERS CATEGORY CHOICE FROM 1 to 7:: "); 
 System.out.println();
 
 System.out.println("1.  SHOW ENTIRE LIST OF SCRM ORGANIZATION & STAKEHOLDERS TIERS.");
 System.out.println();
 System.out.println("2.  SCRM TIER-1: ORGANIZATION STAKE-HOLDERS.");
 System.out.println();
 System.out.println("3.  SCRM TIER-1: ORGANIZATION ACTIVITIES.");
 System.out.println();
 System.out.println("4.  SCRM TIER-2: MISSION STAKE-HOLDERS.");
 System.out.println();
 System.out.println("5.  SCRM TIER-2: MISSION ACTIVITIES.");
 System.out.println();
 System.out.println("6.  SCRM TIER-3: INFORMATION-SYSTEMS STAKE-HOLDERS.");
 System.out.println();
 System.out.println("7.  SCRM TIER-3: INFORMATION-SYSTEMS ACTIVITIES.");
 System.out.println();
   //System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER SCRM TIERS CATEGORY CHOICE FROM 1 to 7: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          //System.out.println("************************************************************************************************" );
          System.out.println();
          //System.out.println("PLEASE SEE BELOW THE ENTIRE LIST OF SCRM STAKE HOLDERS & ACTIVITIES: ");
          System.out.println();
          
          SCRMOS.setSCT1GS    ("  Executive Leadership (CEO, CIO, COO, CFO,CISO, CTO, etc.) - Risk executive functions: Tier 1 activities help to ensure that ICT SCRM mitigation strategies are cost-effective, efficient, and consistent with the strategic goals and objectives of the organization. It is critical that, as organizations define and implement organization-wide strategies, policies, and processes in this tier, they include ICT SCRM considerations.  ");

          SCRMOS.setSCT1A     ("  Define corporate strategy, policy, goals and objectives: ICT SCRM activities at this tier include: 1. Establish ICT SCRM policies based on external and organizational requirements and constraints(e.g., applicable laws and regulations). Policies should include the purpose and applicability, as well as investment and funding requirements, of the ICT SCRM program; 2. Based on the ICT SCRM policy, identify: A. Mission/business requirements that will influence ICT SCRM, such as cost, schedule, performance, security, privacy, quality, and safety; B. Information security requirements, including ICT SCRM-specific requirements; and C. Organization-wide mission/business functions and how ICT SCRM will be integrated into their processes; 3. Establish risk tolerance level for ICT supply chain risks; 4. Establish a group of individuals across the organization who will address ICT SCRM throughout the organization, known as the ICT SCRM Team; and 5. Ensure that ICT SCRM is appropriately integrated into the organization risk management policies and activities..");

          SCRMOS.setSCT2GS    ("  Business Management (includes program management [PM], research and development [R&D], Engineering [SDLC oversight],Acquisitions / Procurement, Cost Accounting, and other management related to reliability, safety,security, quality, etc.): Tier2 (Mission/Business Process) addresses risk from a mission/business process perspective and is informed by the risk context, risk decisions, and risk activities at Tier 1.12 In this tier, program requirements are defined and managed – including ICT SCRM as well as cost, schedule, performance, and a variety of critical nonfunctional requirements. These nonfunctional requirements include concepts such as reliability, dependability, safety, security, and quality. Many threats to and through the supply chain are addressed at this level in the management of trust relationships with system integrators, suppliers, and external service providers of ICT products and services. Because ICT SCRM can both directly and indirectly impact mission/business processes, understanding, integrating and coordinating ICT SCRM activities at this tier are critical for ensuring successful mission and business operations. ");
          
          SCRMOS.setSCT2A     ("  ICT SCRM activities at this tier include: 1. Defining the risk response strategy, including ICT SCRM considerations, for critical processes; 2. Establishing ICT SCRM processes to support mission/business processes; 3. Determining the ICT SCRM requirements of the mission/business systems needed to execute the mission/business processes; 4. Incorporating ICT SCRM requirements into the mission/business processes; 5. Integrating ICT SCRM requirements into an enterprise architecture to facilitate the allocation of ICT SCRM controls to organizational information systems and the environments in which those systems operate; and 6. Establishing a mission/business-specific ICT SCRM team that coordinates and collaborates with the organizational ICT SCRM team."); 
                 
          SCRMOS.setSCT3GS    ("  Systems Management (architect, developers, system owner, QA/QC, test, and contracting personnel, approving selection, payment and approach for obtaining, maintenance engineering, disposal personnel, etc.). ");
          
          SCRMOS.setSCT3A     ("  Policy implementation,requirements, constraints, implementations: Tier3 (Information Systems) is where ICT SCRM activities are integrated into the SDLC of organizational information systems and system components. Many threats through the supply chain are addressed at this level with the use of ICT SCRM-related information security requirements. Risk management activities at Tier3 reflect the organization’s risk management strategy defined in Tier 1 (per NIST SP 800-39), as well as cost, schedule, and performance requirements for individual information systems as defined in Tier 2. ICT SCRM activities at this tier include: 1. Applying, monitoring and managing ICT SCRM controls in the development and sustainment of systems supporting mission/business processes; and 2. Applying, monitoring and managing ICT SCRM controls to the SDLC and the environment in which the SDLC is conducted (e.g., ICT supply chain infrastructure) used to develop and integrate mission/business systems. At Tier 3, ICT SCRM significantly intersects with the SDLC, which includes acquisition (both custom and off-the-shelf), requirements, architectural design, development, delivery, installation, integration, maintenance, and disposal/retirement of information systems, including ICT products and services. ");
      

                   
// Display the Centcom IOT taxonomy values stored in the fields

     
      System.out.println               (" TIER-1: ORGANIZATION STAKE-HOLDERS         : " + SCRMOS.getSCT1GS());
      System.out.println();          
      System.out.println               (" TIER-1: ORGANIZATION ACTIVITIES            : " + SCRMOS.getSCT1A());
      System.out.println();
      System.out.println               (" TIER-2: MISSION STAKE-HOLDERS              : " + SCRMOS.getSCT2GS());
      System.out.println();
      System.out.println               (" TIER-2: MISSION ACTIVITIES                 : " + SCRMOS.getSCT2A());
      System.out.println();
      System.out.println               (" TIER-3: INFORMATION-SYSTEMS STAKE-HOLDERS  : " + SCRMOS.getSCT3GS());
      System.out.println();
      System.out.println               (" TIER-3: INFORMATION-SYSTEMS ACTIVITIES     : " + SCRMOS.getSCT3A());
     
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      
      System.out.println( "TO CONTINUE WITH NEXT SCRM STAKE HOLDERS & ACTIVITIES (SCRMOS) SUBCATEGORY PLEASE SELECT AGAIN SCRM FRAMEWORK CATEGORY CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println();
        // System.out.println("PLEASE SEE SUBCATEGORY TIER-1: ORGANIZATION STAKE-HOLDERS: ");
         System.out.println();
  
  // *****************Information Types***************

       SCRMOS.setSCT1GS    (" Executive Leadership (CEO, CIO, COO, CFO,CISO, CTO, etc.) - Risk executive functions: Tier 1 activities help to ensure that ICT SCRM mitigation strategies are cost-effective, efficient, and consistent with the strategic goals and objectives of the organization. It is critical that, as organizations define and implement organization-wide strategies, policies, and processes in this tier, they include ICT SCRM considerations.  ");

      
//**************** Display the USSOCOM IOT INFORMATION TYPES****************

     
      System.out.println               (" TIER-1: ORGANIZATION STAKE-HOLDERS = " + SCRMOS.getSCT1GS());
      System.out.println();
      
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SCRM STAKE HOLDERS & ACTIVITIES (SCRMOS) SUBCATEGORY PLEASE SELECT AGAIN SCRM FRAMEWORK CATEGORY CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
        // System.out.println("PLEASE SEE SUBCATEGORY TIER-1: ORGANIZATION ACTIVITIES: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
        SCRMOS.setSCT1A     (" Define corporate strategy, policy, goals and objectives: ICT SCRM activities at this tier include: 1. Establish ICT SCRM policies based on external and organizational requirements and constraints(e.g., applicable laws and regulations). Policies should include the purpose and applicability, as well as investment and funding requirements, of the ICT SCRM program; 2. Based on the ICT SCRM policy, identify: A. Mission/business requirements that will influence ICT SCRM, such as cost, schedule, performance, security, privacy, quality, and safety; B. Information security requirements, including ICT SCRM-specific requirements; and C. Organization-wide mission/business functions and how ICT SCRM will be integrated into their processes; 3. Establish risk tolerance level for ICT supply chain risks; 4. Establish a group of individuals across the organization who will address ICT SCRM throughout the organization, known as the ICT SCRM Team; and 5. Ensure that ICT SCRM is appropriately integrated into the organization risk management policies and activities..");


 
        
         System.out.println               (" TIER-1: ORGANIZATION ACTIVITIES = " + SCRMOS.getSCT1A());    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SCRM STAKE HOLDERS & ACTIVITIES (SCRMOS) SUBCATEGORY PLEASE SELECT AGAIN SCRM FRAMEWORK CATEGORY CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SEE BELOW SUBCATEGORY TIER-2: MISSION STAKE-HOLDERS: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
     SCRMOS.setSCT2GS    (" Business Management (includes program management [PM], research and development [R&D], Engineering [SDLC oversight],Acquisitions / Procurement, Cost Accounting, and other management related to reliability, safety,security, quality, etc.): Tier2 (Mission/Business Process) addresses risk from a mission/business process perspective and is informed by the risk context, risk decisions, and risk activities at Tier 1.12 In this tier, program requirements are defined and managed – including ICT SCRM as well as cost, schedule, performance, and a variety of critical nonfunctional requirements. These nonfunctional requirements include concepts such as reliability, dependability, safety, security, and quality. Many threats to and through the supply chain are addressed at this level in the management of trust relationships with system integrators, suppliers, and external service providers of ICT products and services. Because ICT SCRM can both directly and indirectly impact mission/business processes, understanding, integrating and coordinating ICT SCRM activities at this tier are critical for ensuring successful mission and business operations. ");
 
          


       

      System.out.println               (" TIER-2: MISSION STAKE-HOLDERS = " + SCRMOS.getSCT2GS());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SCRM STAKE HOLDERS & ACTIVITIES (SCRMOS) SUBCATEGORY PLEASE SELECT AGAIN SCRM FRAMEWORK CATEGORY CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );

      

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         //System.out.println("PLEASE SEE BELOW SUBCATEGORY SCRM TIER-2: MISSION ACTIVITIES:");
 
         System.out.println();
       
       

  // ****************Processor Types*******************
  
  
      SCRMOS.setSCT2A     (" ICT SCRM activities at this tier include: 1. Defining the risk response strategy, including ICT SCRM considerations, for critical processes; 2. Establishing ICT SCRM processes to support mission/business processes; 3. Determining the ICT SCRM requirements of the mission/business systems needed to execute the mission/business processes; 4. Incorporating ICT SCRM requirements into the mission/business processes; 5. Integrating ICT SCRM requirements into an enterprise architecture to facilitate the allocation of ICT SCRM controls to organizational information systems and the environments in which those systems operate; and 6. Establishing a mission/business-specific ICT SCRM team that coordinates and collaborates with the organizational ICT SCRM team."); 
  
      

          System.out.println               (" TIER-2: MISSION ACTIVITIES  = " + SCRMOS.getSCT2A());

         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println( "TO CONTINUE WITH NEXT SCRM STAKE HOLDERS & ACTIVITIES (SCRMOS) SUBCATEGORY PLEASE SELECT AGAIN SCRM FRAMEWORK CATEGORY CHOICE # 1");
         System.out.println();
         System.out.println("************************************************************************************************" );
     
      }
else
   
      if ( menuSelect == 6)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         //System.out.println("PLEASE SEE BELOW SUBCATEGORY TIER-3: INFORMATION-SYSTEMS STAKE-HOLDERS:");
 
         System.out.println();
       
   
  
      SCRMOS.setSCT3GS    (" Systems Management (architect, developers, system owner, QA/QC, test, and contracting personnel, approving selection, payment and approach for obtaining, maintenance engineering, disposal personnel, etc.). ");
  
      

         System.out.println               (" TIER-3: INFORMATION-SYSTEMS STAKE-HOLDERS  = " + SCRMOS.getSCT3GS());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println( "TO CONTINUE WITH NEXT SCRM STAKE HOLDERS & ACTIVITIES (SCRMOS) SUBCATEGORY PLEASE SELECT AGAIN SCRM FRAMEWORK CATEGORY CHOICE # 1");
         System.out.println();
         System.out.println("************************************************************************************************" );
     
      }
else
   
      if ( menuSelect == 7)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         //System.out.println("PLEASE SEE BELOW SUBCATEGORY TIER-3: INFORMATION-SYSTEMS ACTIVITIES :");
 
         System.out.println();
       
       

  
  
    SCRMOS.setSCT3A     (" Policy implementation,requirements, constraints, implementations: Tier3 (Information Systems) is where ICT SCRM activities are integrated into the SDLC of organizational information systems and system components. Many threats through the supply chain are addressed at this level with the use of ICT SCRM-related information security requirements. Risk management activities at Tier3 reflect the organization’s risk management strategy defined in Tier 1 (per NIST SP 800-39), as well as cost, schedule, and performance requirements for individual information systems as defined in Tier 2. ICT SCRM activities at this tier include: 1. Applying, monitoring and managing ICT SCRM controls in the development and sustainment of systems supporting mission/business processes; and 2. Applying, monitoring and managing ICT SCRM controls to the SDLC and the environment in which the SDLC is conducted (e.g., ICT supply chain infrastructure) used to develop and integrate mission/business systems. At Tier 3, ICT SCRM significantly intersects with the SDLC, which includes acquisition (both custom and off-the-shelf), requirements, architectural design, development, delivery, installation, integration, maintenance, and disposal/retirement of information systems, including ICT products and services. ");
   
      

         System.out.println               (" TIER-3: INFORMATION-SYSTEMS ACTIVITIES  = " + SCRMOS.getSCT3A());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println( "TO CONTINUE WITH NEXT SCRM STAKE HOLDERS & ACTIVITIES (SCRMOS) SUBCATEGORY PLEASE SELECT AGAIN SCRM FRAMEWORK CATEGORY CHOICE # 1");
         System.out.println();
         System.out.println("************************************************************************************************" );
     
      }

   
     else
          
   
  
// ******************Display the Main menu************************************

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE THE SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  SCRM STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 7) 
  
{
 
System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID SCRM FRAMEWORK SELECTION CATEGORY");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE IS THE VALID SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println    ("1. SCRM ORGANIZATION & STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");

    
  menuSelection = keyboard.nextInt();


 
 } 

break;


//*************************ICT SUPPLY-CHAIN THREAT AGENTS******************************************



case 2: 

 
 //String SCTAS, SCTAE, SCTIS, SCTIE, SCTFIS, SCTFIE, SCTSVCS, SCTSVCE, SCTTSS, SCTTSE, SCTIECCS, SCTIECCE;
 
 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED SUPPLY-CHAIN THREAT AGENTS CATEGORY ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW SUPPLY-CHAIN THREAT AGENTS SUBCATEGORIES");
 System.out.println();

ScrmSetter SCRMTA;

//  Following statement creates an object using the AiSetter class as
//its Blueprint. Centcom will reference the object.

SCRMTA = new ScrmSetter();

  

 System.out.println("1.  SHOW ENTIRE LIST OF SUPPLY-CHAIN THREAT AGENTS.");
 System.out.println();
 System.out.println("2.  THREAT AGENTS: COUNTERAFEITERS - SCENARIOS.");
 System.out.println();
 System.out.println("3.  THREAT AGENTS: COUNTERAFEITERS - EXAMPLES.");
 System.out.println();
 System.out.println("4.  THREAT AGENTS: INSIDERS - SCENARIOS.");
 System.out.println();
 System.out.println("5.  THREAT AGENTS: INSIDERS - EXAMPLES.");
 System.out.println();
 System.out.println("6.  THREAT AGENTS: FOREIGN-INTELLIGENCE SERVICES - SCENARIOS.");
 System.out.println();
 System.out.println("7.  THREAT AGENTS: FOREIGN-INTELLIGENCE SERVICES - EXAMPLES.");
 System.out.println();
 System.out.println("8.  THREAT AGENTS: TERRORISTS - SCENARIOS.");
 System.out.println();
 System.out.println("9.  THREAT AGENTS: TERRORISTS - EXAMPLES.");
 System.out.println();
 System.out.println("10. THREAT AGENTS: INDUSTRIAL-ESPIONAGE/CYBER-CRIMINALS - SCENARIOS.");
 System.out.println();
 System.out.println("11. THREAT AGENTS: INDUSTRIAL-ESPIONAGE/CYBER-CRIMINALS - EXAMPLES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
   System.out.println("************************************************************************************************" );
  
 System.out.println("THIS IS INVALID THREAT AGENTS SELECTION"); 
 System.out.println();
 System.out.println("1.  SHOW ENTIRE LIST OF SUPPLY-CHAIN THREAT AGENTS.");
 System.out.println();
 System.out.println("2.  THREAT AGENTS: COUNTERAFEITERS - SCENARIOS.");
 System.out.println();
 System.out.println("3.  THREAT AGENTS: COUNTERAFEITERS - EXAMPLES.");
 System.out.println();
 System.out.println("4.  THREAT AGENTS: INSIDERS - SCENARIOS.");
 System.out.println();
 System.out.println("5.  THREAT AGENTS: INSIDERS - EXAMPLES.");
 System.out.println();
 System.out.println("6.  THREAT AGENTS: FOREIGN-INTELLIGENCE SERVICES - SCENARIOS.");
 System.out.println();
 System.out.println("7.  THREAT AGENTS: FOREIGN-INTELLIGENCE SERVICES - EXAMPLES.");
 System.out.println();
 System.out.println("8.  THREAT AGENTS: TERRORISTS - SCENARIOS.");
 System.out.println();
 System.out.println("9.  THREAT AGENTS: TERRORISTS - EXAMPLES.");
 System.out.println();
 System.out.println("10. THREAT AGENTS: INDUSTRIAL-ESPIONAGE/CYBER-CRIMINALS - SCENARIOS.");
 System.out.println();
 System.out.println("11. THREAT AGENTS: INDUSTRIAL-ESPIONAGE/CYBER-CRIMINALS - EXAMPLES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");

 
  menuSelect = keyboard.nextInt();


 }
    //String SCTAS, SCTAE, SCTIS, SCTIE, SCTFIS, SCTFIE, SCTTSS, SCTTSE, SCTIECCS, SCTIECCE;

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SHOW ENTIRE LIST OF SUPPLY-CHAIN THREAT AGENTS: ");
          System.out.println();
          System.out.println("************************************************************************************************" );

          SCRMTA.setSCTAS   (" Counterfeits inserted into ICT supply chain. A Threat Scenario is a summary of potential consequence(s) of the successful exploitation of a specific vulnerability or vulnerabilities by a threat agent. Analyzing threat scenarios can help organizations to determine the likelihood and impact a specific event or events would have on an organization and identify appropriate mitigating strategies.Threat scenarios are generally used in two ways: #1. To translate the often disconnected information garnered from a risk assessment, such as described in [NIST SP 800-30 Rev. 1] , into a more narrowly scoped and tangible, story-like situation for further evaluation. These stories can help organizations to discover dependencies and additional vulnerabilities requiring mitigation and used for training; and #2. To determine the impact that the successful exercise of a specific vulnerability would have on the organization and identify the benefits of mitigating strategies.  ");
         
          SCRMTA.setSCTAE   (" Criminal groups seek to acquire and sell counterfeit ICT components for monetary gain. Specifically, organized crime groups seek disposed units, purchase overstock items, and acquire blueprints to obtain ICT components that they can sell through various gray market resellers to acquirers. ");
          
          SCRMTA.setSCTIS   (" Intellectual property loss. ");
          
          SCRMTA.setSCTIE   (" Disgruntled insiders sell or transfer intellectual property to competitors or foreign intelligence agencies for a variety of reasons including monetary gain. Intellectual property includes software code, blueprints, or documentation.");
          
          SCRMTA.setSCTFIS  (" Malicious code insertion - Threats to the system could include: loss of power to the system, loss of functionality, or loss of integrity causing incorrect commands to be processed. Some threat sources could include nature, malicious outsiders, and malicious insiders. The system is equipped with certain safety controls such as backup generator power, redundancy of design, and contingency plans if the system fails. The organization identified the following as potential areas for improvement: 1. Establish and retain identification of supply chain elements, processes, and actors; 2. Control access and configuration changes within the SDLC and require periodic code reviews; 3. Require static code testing; and 4. Incident Response Handling.  ");
          
          SCRMTA.setSCTFIE  (" Foreign intelligence services seek to penetrate ICT supply chain and implant unwanted functionality (by inserting new or modifying existing functionality) to be used when the system is operational to gather information or subvert system or mission operations.  ");
          
          SCRMTA.setSCTTSS  (" Unauthorized access.  ");
          
          SCRMTA.setSCTTSE  (" Terrorists seek to penetrate or disrupt the ICT supply chain and may implant unwanted functionality to obtain information or cause physical disablement and destruction through ICT. ");
          
          SCRMTA.setSCTIECCS (" SCENARIOS: Industrial Espionage/Intellectual Property Loss - MITIGATION STRATEGIES INCLUDE Improve traceability and monitoring capabilities. 1. INFORMATION SYSTEM COMPONENT INVENTORY. 2. IDENTIFICATION AND AUTHENTICATION POLICY AND PROCEDURES. 3. DEVELOPER CONFIGURATION MANAGEMENT. 4. SUPPLY CHAIN PROTECTION TO VALIDATE AS GENUINE AND NOT ALTERED. 5. SUPPLY CHAIN PROTECTION TO IDENTITY AND TRACEABILITY. Increase provenance and information control requirements SUCH AS. #1. COLLABORATION AND INFORMATION SHARING. #2. PROVENANCE POLICY AND PROCEDURES. #3. BASELINING AND TRACKING PROVENANCE. #4. SUPPLY CHAIN PROTECTION BY SUPPLIER REVIEWS");
          
          SCRMTA.setSCTIECCE (" Industrial spies/cyber criminals seek ways to penetrate ICT supply chain to gather information or subvert system or mission operations (e.g., exploitation of an HVAC contractor to steal credit card information). ");
          



          

         
// Display the AC taxonomy values stored in the fields

     
      System.out.println               (" COUNTERAFEITERS SCENARIOS                      : " + SCRMTA.getSCTAS());
      System.out.println();
      System.out.println               (" COUNTERAFEITERS EXAMPLES                       : " + SCRMTA.getSCTAE());
      System.out.println();
      System.out.println               (" INSIDERS THREATS SCENARIOS                     : " + SCRMTA.getSCTIS());
      System.out.println();
      System.out.println               (" INSIDERS THREAT EXAMPLES                       : " + SCRMTA.getSCTIE());
      System.out.println();
      System.out.println               (" FOREIGN INTELLIGENCE SERVICES SCENARIOS        : " + SCRMTA.getSCTFIS());
      System.out.println();
      System.out.println               (" FOREIGN INTELLIGENCE SERVICES EXAMPLES         : " + SCRMTA.getSCTFIE());
      System.out.println();
      System.out.println               (" TERRORISTS THREAT SCENARIOS                    : " + SCRMTA.getSCTTSS());
      System.out.println();
      System.out.println               (" TERRORISTS THREAT EXAMPLES                     : " + SCRMTA.getSCTTSE());
      System.out.println();
      System.out.println               (" INDUSTRIAL ESPIONAGE/CYBER CRIMINALS SCENARIOS : " + SCRMTA.getSCTIECCS());
      System.out.println();
      System.out.println               (" INDUSTRIAL ESPIONAGE/CYBER CRIMINALS EXAMPLES  : " + SCRMTA.getSCTIECCE());
      System.out.println();
     
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT AGENTS CATEGORY # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
        // System.out.println("PLEASE SHOW THREAT AGENTS: COUNTERAFEITERS - SCENARIOS: ");
         System.out.println();
  
  // *****************COUNTRAFEITIERS SCENARIOS **************

         SCRMTA.setSCTAS  ("  Counterfeits inserted into ICT supply chain. A Threat Scenario is a summary of potential consequence(s) of the successful exploitation of a specific vulnerability or vulnerabilities by a threat agent. Analyzing threat scenarios can help organizations to determine the likelihood and impact a specific event or events would have on an organization and identify appropriate mitigating strategies.Threat scenarios are generally used in two ways: #1. To translate the often disconnected information garnered from a risk assessment, such as described in [NIST SP 800-30 Rev. 1] , into a more narrowly scoped and tangible, story-like situation for further evaluation. These stories can help organizations to discover dependencies and additional vulnerabilities requiring mitigation and used for training; and #2. To determine the impact that the successful exercise of a specific vulnerability would have on the organization and identify the benefits of mitigating strategies.  ");
 
      
//**************** Display the COUNTRAFEITIERS SCENARIOS****************

     
      System.out.println               (" COUNTERAFEITERS SCENARIOS = " + SCRMTA.getSCTAS());

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
     System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT AGENTS CATEGORY SELECT CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: COUNTERAFEITERS - EXAMPLES: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         SCRMTA.setSCTAE   (" Criminal groups seek to acquire and sell counterfeit ICT components for monetary gain. Specifically, organized crime groups seek disposed units, purchase overstock items, and acquire blueprints to obtain ICT components that they can sell through various gray market resellers to acquirers. ");
         
         System.out.println       (" COUNTERAFEITERS EXAMPLES = " + SCRMTA.getSCTAE());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT AGENTS CATEGORY SELECT CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - SCENARIOS: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      SCRMTA.setSCTIS   (" Intellectual property loss. ");       

      System.out.println               (" INSIDERS THREAT SCENARIOS = " + SCRMTA.getSCTIS());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT AGENTS CATEGORY SELECT CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - EXAMPLES: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       SCRMTA.setSCTIE      (" Disgruntled insiders sell or transfer intellectual property to competitors or foreign intelligence agencies for a variety of reasons including monetary gain. Intellectual property includes software code, blueprints, or documentation.");
        

      System.out.println    (" INSIDERS THREAT EXAMPLES = " + SCRMTA.getSCTIE());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT AGENTS CATEGORY SELECT CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
 
 else
   
      if ( menuSelect == 6)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
        // System.out.println("PLEASE SHOW THREAT AGENTS: FOREIGN-INTELLIGENCE SERVICES - SCENARIOS: ");
         System.out.println();
         


  // ********************FOREIGN INTELLIGENCE SERVICES SCENARIOS*********************
  
 
      SCRMTA.setSCTFIS                 (" Malicious code insertion - Threats to the system could include: loss of power to the system, loss of functionality, or loss of integrity causing incorrect commands to be processed. Some threat sources could include nature, malicious outsiders, and malicious insiders. The system is equipped with certain safety controls such as backup generator power, redundancy of design, and contingency plans if the system fails. The organization identified the following as potential areas for improvement: 1. Establish and retain identification of supply chain elements, processes, and actors; 2. Control access and configuration changes within the SDLC and require periodic code reviews; 3. Require static code testing; and 4. Incident Response Handling.  ");
 
       

      System.out.println               (" FOREIGN INTELLIGENCE SERVICES SCENARIOS = " + SCRMTA.getSCTFIS());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT AGENTS CATEGORY SELECT CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

    else
   
      if ( menuSelect == 7)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
        // System.out.println("PLEASE SHOW THREAT AGENTS: FOREIGN-INTELLIGENCE SERVICES - EXAMLES: ");
         System.out.println();
         


  // ********************FOREIGN INTELLIGENCE SERVICES EXAMPLES*********************
  
 
      SCRMTA.setSCTFIE  (" Foreign intelligence services seek to penetrate ICT supply chain and implant unwanted functionality (by inserting new or modifying existing functionality) to be used when the system is operational to gather information or subvert system or mission operations.  ");
        

      System.out.println               (" FOREIGN-INTELLIGENCE SERVICES EXAMPLES = " + SCRMTA.getSCTFIE());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT AGENTS CATEGORY SELECT CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
 else
   
      if ( menuSelect == 8)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
        // System.out.println("PLEASE SHOW SUBCATEGORY THREAT AGENTS: TERRORISTS - SCENARIOS: ");
         System.out.println();
         


  // ********************INDUSTRIAL TERORISTS SCENARIOS*********************
  
 
     SCRMTA.setSCTTSS  (" Unauthorized access.  ");       

     System.out.println               (" TERRORISTS SCENARIOS = " + SCRMTA.getSCTTSS());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT AGENTS CATEGORY SELECT CHOICE # 2");

      System.out.println();
      System.out.println("************************************************************************************************" );

      }
else
   
      if ( menuSelect == 9)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW SUBCATEGORY THREAT AGENTS: TERRORISTS - EXAMPLES: ");
         System.out.println();
         


  // ********************INDUSTRIAL TERORISTS EXAMPLES*********************
  
 
      SCRMTA.setSCTTSE  (" Terrorists seek to penetrate or disrupt the ICT supply chain and may implant unwanted functionality to obtain information or cause physical disablement and destruction through ICT. ");
        

      System.out.println               (" TERRORISTS EXAMPLES = " + SCRMTA.getSCTTSE());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT AGENTS CATEGORY SELECT CHOICE # 2");     
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
else
   
      if ( menuSelect == 10)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
        // System.out.println("PLEASE SHOW THREAT AGENTS: INDUSTRIAL-ESPIONAGE/CYBER-CRIMINALS - SCENARIOS: ");
         System.out.println();
         


  // ********************INDUSTRIAL ESPIONAGE SCENARIOS*********************
  
 
     SCRMTA.setSCTIECCS (" Industrial Espionage/Intellectual Property Loss - MITIGATION STRATEGIES INCLUDE Improve traceability and monitoring capabilities. 1. INFORMATION SYSTEM COMPONENT INVENTORY. 2. IDENTIFICATION AND AUTHENTICATION POLICY AND PROCEDURES. 3. DEVELOPER CONFIGURATION MANAGEMENT. 4. SUPPLY CHAIN PROTECTION TO VALIDATE AS GENUINE AND NOT ALTERED. 5. SUPPLY CHAIN PROTECTION TO IDENTITY AND TRACEABILITY. Increase provenance and information control requirements SUCH AS. #1. COLLABORATION AND INFORMATION SHARING. #2. PROVENANCE POLICY AND PROCEDURES. #3. BASELINING AND TRACKING PROVENANCE. #4. SUPPLY CHAIN PROTECTION BY SUPPLIER REVIEWS");

       

      System.out.println               (" INDUSTRIAL-ESPIONAGE/CYBER CRIMINALS SCENARIOS = " + SCRMTA.getSCTIECCS());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT AGENTS CATEGORY SELECT CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
 else
 
 if ( menuSelect == 11)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INDUSTRIAL-ESPIONAGE/CYBER-CRIMINALS - EXAMPLES: ");
         System.out.println();
         


  // ********************INDUSTRIAL ESPIONAGE EXAMPLES*********************
  
 
      SCRMTA.setSCTIECCE               (" Industrial spies/cyber criminals seek ways to penetrate ICT supply chain to gather information or subvert system or mission operations (e.g., exploitation of an HVAC contractor to steal credit card information). ");
       

      System.out.println               (" INDUSTRIAL-ESPIONAGE/CYBER CRIMINALS EXAMPLES = " + SCRMTA.getSCTIECCE());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT AGENTS CATEGORY SELECT CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

     else             
   
  
  
// ******************Display the SCRM Main menu************************************

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE THE SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  SCRM STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 7) 
  
{
 
System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID SCRM FRAMEWORK SELECTION CATEGORY");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE IS THE VALID SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  SCRM ORGANIZATION & STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


  
  menuSelection = keyboard.nextInt();

  
 } 

break;

case 3: 

 
 //String SCTCT1TC, SCTCT1M, SCTCT2TC, SCTCT2M, SCTCT3TC, SCTCT3M;
 
 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED SUPPLY-CHAIN THREAT CO0NSIDERATIONS CATEGORY ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW SUPPLY-CHAIN THREAT CONSIDERATIONS SUBCATEGORIES");
 System.out.println();

ScrmSetter SCRMTC;

//  Following statement creates an object using the AiSetter class as
//its Blueprint. Centcom will reference the object.

SCRMTC = new ScrmSetter();

  

 System.out.println("1.  SHOW ENTIRE LIST OF SUPPLY-CHAIN THREAT CONSIDERATIONS.");
 System.out.println();
 System.out.println("2.  TIER1 THREAT CONSIDERATIONS.");
 System.out.println();
 System.out.println("3.  TIER1 THREAT CONSIDERATIONS METHODS.");
 System.out.println();
 System.out.println("4.  TIER2 THREAT CONSIDERATIONS.");
 System.out.println();
 System.out.println("5.  TIER2 THREAT CONSIDERATIONS METHODS.");
 System.out.println();
 System.out.println("6.  TIER3 THREAT CONSIDERATIONS.");
 System.out.println();
 System.out.println("7.  TIER3 THREAT CONSIDERATIONS METHODS.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 7: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 7)
  

  
{
   System.out.println("************************************************************************************************" );
  
 System.out.println("THIS IS INVALID THREAT CONSIDERATIONS SELECTION"); 
 System.out.println();
 System.out.println("1.  SHOW ENTIRE LIST OF SUPPLY-CHAIN THREAT CONSIDERATIONS.");
 System.out.println();
 System.out.println("2.  TIER1 THREAT CONSIDERATIONS.");
 System.out.println();
 System.out.println("3.  TIER1 THREAT CONSIDERATIONS METHODS.");
 System.out.println();
 System.out.println("4.  TIER2 THREAT CONSIDERATIONS.");
 System.out.println();
 System.out.println("5.  TIER2 THREAT CONSIDERATIONS METHODS.");
 System.out.println();
 System.out.println("6.  TIER3 THREAT CONSIDERATIONS.");
 System.out.println();
 System.out.println("7.  TIER3 THREAT CONSIDERATIONS METHODS.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 7: ");

 
  menuSelect = keyboard.nextInt();


 }
       // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SHOW ENTIRE LIST OF SUPPLY-CHAIN THREAT CONSIDERATIONS: ");
          System.out.println();
          System.out.println("************************************************************************************************" );

          SCRMTC.setSCTCT1TC   (" 1. Organization’s business and mission 2. Strategic supplier relationships 3. Geographical considerations related to the extent of the organization’s ICT supply chain. ");        
          SCRMTC.setSCTCT1M    (" 1. Establish common starting points for identifying ICT supply chain threat 2. Establish procedures for countering organization-wide threats such as insertion of counterfeits into critical systems and components. ");         
          SCRMTC.setSCTCT2TC   (" 1. Mission functions 2. Geographic locations 3. Types of suppliers (COTS, external service providers, or custom, etc.) 4. Technologies used organization-wide  ");
          SCRMTC.setSCTCT2M    (" 1. Identify additional sources of threat information specific to organizational mission functions 2. Identify potential threat sources based on the locations and suppliers identified through examining available agency ICT supply chain information (e.g., from supply chain map.) 3. Scope identified threat sources to the specific mission functions, using the agency the ICT supply chain information 4. Establish mission-specific preparatory procedures for countering threat.  ");                   
          SCRMTC.setSCTCT3TC   (" ICT supply chain vulnerabilities may be found in: 1. The systems/components within the SDLC (i.e., being developed and integrated) 2. The development and operational environment directly impacting the SDLC; and 3. The logistics/delivery environment that transports ICT systems and components (logically or physically). ");
          SCRMTC.setSCTCT3M    (" 1. Base the level of detail with which threats should be considered on the SDLC phase 2. Identify and refine threat sources based on the potential for threat insertion within individual SDLC processes. ");


          

         
// Display the AC taxonomy values stored in the fields

     
      System.out.println               (" TIER1 THREAT CONSIDERATIONS         : " + SCRMTC.getSCTCT1TC());
      System.out.println();
      System.out.println               (" TIER1 THREAT CONSIDERATIONS METHODS : " + SCRMTC.getSCTCT1M());
      System.out.println();
      System.out.println               (" TIER2 THREAT CONSIDERATIONS         : " + SCRMTC.getSCTCT2TC());
      System.out.println();
      System.out.println               (" TIER2 THREAT CONSIDERATIONS METHODS : " + SCRMTC.getSCTCT2M());
      System.out.println();
      System.out.println               (" TIER3 THREAT CONSIDERATIONS         : " + SCRMTC.getSCTCT3TC());
      System.out.println();
      System.out.println               (" TIER3 THREAT CONSIDERATIONS METHODS : " + SCRMTC.getSCTCT3M());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT CONSIDERATIONS CATEGORY SELECT CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
        // System.out.println("PLEASE SHOW THREAT AGENTS: COUNTERAFEITERS - SCENARIOS: ");
         System.out.println();
  
  // *****************COUNTRAFEITIERS SCENARIOS **************

         SCRMTC.setSCTCT1TC   (" 1. Organization’s business and mission 2. Strategic supplier relationships 3. Geographical considerations related to the extent of the organization’s ICT supply chain. ");        
       
//**************** Display the COUNTRAFEITIERS SCENARIOS****************

     
      System.out.println               (" TIER1 THREAT CONSIDERATIONS : " + SCRMTC.getSCTCT1TC());

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT CONSIDERATIONS CATEGORY SELECT CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: COUNTERAFEITERS - EXAMPLES: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         SCRMTC.setSCTCT1M    (" 1. Establish common starting points for identifying ICT supply chain threat 2. Establish procedures for countering organization-wide threats such as insertion of counterfeits into critical systems and components. ");         
       
         System.out.println       (" TIER1 THREAT CONSIDERATINS METHODS  : " + SCRMTC.getSCTCT1M());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT CONSIDERATIONS CATEGORY SELECT CHOICE #3");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - SCENARIOS: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      SCRMTC.setSCTCT2TC   (" 1. Mission functions 2. Geographic locations 3. Types of suppliers (COTS, external service providers, or custom, etc.) 4. Technologies used organization-wide  ");
       

      System.out.println               (" TIER2 THREAT CONSIDERATIONS   : " + SCRMTC.getSCTCT2TC());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT CONSIDERATIONS CATEGORY SELECT CHOICE #3");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - EXAMPLES: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
        SCRMTC.setSCTCT2M    (" 1. Identify additional sources of threat information specific to organizational mission functions 2. Identify potential threat sources based on the locations and suppliers identified through examining available agency ICT supply chain information (e.g., from supply chain map.) 3. Scope identified threat sources to the specific mission functions, using the agency the ICT supply chain information 4. Establish mission-specific preparatory procedures for countering threat.  ");                   
        

      System.out.println               (" TIER2 THREAT CONSIDERATIONS METHODS : " + SCRMTC.getSCTCT2M());

      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT CONSIDERATIONS CATEGORY SELECT CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
      
  else
  
      if ( menuSelect == 6)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - EXAMPLES: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
        SCRMTC.setSCTCT3TC   (" ICT supply chain vulnerabilities may be found in: 1. The systems/components within the SDLC (i.e., being developed and integrated) 2. The development and operational environment directly impacting the SDLC; and 3. The logistics/delivery environment that transports ICT systems and components (logically or physically). ");
        

        System.out.println               (" TIER3 THREAT CONSIDERATIONS    : " + SCRMTC.getSCTCT3TC());

      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT CONSIDERATIONS CATEGORY SELECT CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

else
  
      if ( menuSelect == 7)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - EXAMPLES: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
        SCRMTC.setSCTCT3M    (" 1. Base the level of detail with which threats should be considered on the SDLC phase 2. Identify and refine threat sources based on the potential for threat insertion within individual SDLC processes. ");

       

        System.out.println               (" TIER3 THREAT CONSIDERATIONS METHODS : " + SCRMTC.getSCTCT3M());


      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT CONSIDERATIONS CATEGORY SELECT CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

 
     else             
   
  
  
// ******************Display the SCRM Main menu************************************

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE THE SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  SCRM STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 7) 
  
{
 
System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID SCRM FRAMEWORK SELECTION CATEGORY");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE IS THE VALID SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1. SCRM ORGANIZATION & STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


  
  menuSelection = keyboard.nextInt();

  
 } 

break;

//***************************CHOICE#4 SUPPLY-CHAIN VULNERABILITY CONSIDERATIONS BEGIN HERE******************************************

case 4: 

 

 
 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED SUPPLY-CHAIN VULNERABILITIES CO0NSIDERATIONS CATEGORY ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW SUPPLY-CHAIN VULNERABILITIES SUBCATEGORIES");
 System.out.println();

ScrmSetter SCRMVC;

//  Following statement creates an object using the AiSetter class as
//its Blueprint. Centcom will reference the object.

SCRMVC = new ScrmSetter();

  

 System.out.println("1.  SHOW ENTIRE LIST OF SUPPLY-CHAIN VULNERABILITY CONSIDERATIONS.");
 System.out.println();
 System.out.println("2.  TIER1 VULNERABILITY CONSIDERATIONS.");
 System.out.println();
 System.out.println("3.  TIER1 VULNERABILITY CONSIDERATIONS METHODS.");
 System.out.println();
 System.out.println("4.  TIER2 VULNERABILITY CONSIDERATIONS.");
 System.out.println();
 System.out.println("5.  TIER2 VULNERABILITY CONSIDERATIONS METHODS.");
 System.out.println();
 System.out.println("6.  TIER3 VULNERABILITY CONSIDERATIONS.");
 System.out.println();
 System.out.println("7.  TIER3 VULNERABILITY CONSIDERATIONS METHODS.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 7: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 7)
  

  
{
   System.out.println("************************************************************************************************" );
  
 System.out.println("THIS IS INVALID VULNERABILITY CONSIDERATIONS SELECTION"); 
 System.out.println();
 System.out.println("1.  SHOW ENTIRE LIST OF SUPPLY-CHAIN VULNERABILITY CONSIDERATIONS.");
 System.out.println();
 System.out.println("2.  TIER1 VULNERABILITY CONSIDERATIONS.");
 System.out.println();
 System.out.println("3.  TIER1 VULNERABILITY CONSIDERATIONS METHODS.");
 System.out.println();
 System.out.println("4.  TIER2 VULNERABILITY CONSIDERATIONS.");
 System.out.println();
 System.out.println("5.  TIER2 VULNERABILITY CONSIDERATIONS METHODS.");
 System.out.println();
 System.out.println("6.  TIER3 VULNERABILITY CONSIDERATIONS.");
 System.out.println();
 System.out.println("7.  TIER3 VULNERABILITY CONSIDERATIONS METHODS.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 7: ");


 
  menuSelect = keyboard.nextInt();


 }
       // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SHOW ENTIRE LIST OF SUPPLY-CHAIN VULNERABILITY CONSIDERATIONS: ");
          System.out.println();
          System.out.println("************************************************************************************************" );

          SCRMVC.setSCVCT1VC   (" 1. Organization’s mission/business. 2. Supplier relationships (e.g., system integrators, COTS, external services). 3. Geographical considerations related to the extent of the organization’s ICT supply chain. 4. Enterprise/Security Architecture. 5. Criticality Baseline. ");        
          SCRMVC.setSCVCT1M    (" 1. Examine agency ICT supply chain information including that from supply chain maps to identify especially vulnerable locations or organizations. 2. Analyze agency mission for susceptibility to potential supply chain vulnerabilities. 3. Examine system integrator and supplier relationships for susceptibility to potential supply chain vulnerabilities. 4. Review enterprise architecture and criticality baseline to identify areas of weakness requiring more robust ICT supply chain considerations.  ");         
          SCRMVC.setSCVCT2VC   (" 1. Mission functions. 2. Geographic locations. 3. Types of suppliers (COTS, custom,etc). 4. Technologies used.  ");
          SCRMVC.setSCVCT2M    (" 1. Refine analysis from Tier 1 based on specific mission functions and applicable threat and supply chain information. 2. Consider using the National Vulnerability Database (NVD), including Common Vulnerabilities and Exposures (CVE) and Common Vulnerability Scoring System (CVSS), to characterize, categorize, and score vulnerabilities. 3. Consider using scoring guidance to prioritize vulnerabilities for remediation.  ");                   
          SCRMVC.setSCVCT3VC   (" 1. Individual technologies, solutions, and suppliers should be considered.  ");
          SCRMVC.setSCVCT3M    (" 1. Use CVEs where available to characterize and categorize vulnerabilities. 2. Identify weaknesses.  ");


          

         
// Display the AC taxonomy values stored in the fields

     
      System.out.println               (" TIER1 VULNERABILITY CONSIDERATIONS         : " + SCRMVC.getSCVCT1VC());
      System.out.println();
      System.out.println               (" TIER1 VULNERABILITY CONSIDERATIONS METHODS : " + SCRMVC.getSCVCT1M());
      System.out.println();
      System.out.println               (" TIER2 VULNERABILITY CONSIDERATIONS         : " + SCRMVC.getSCVCT2VC());
      System.out.println();
      System.out.println               (" TIER2 VULNERABILITY CONSIDERATIONS METHODS : " + SCRMVC.getSCVCT2M());
      System.out.println();
      System.out.println               (" TIER3 VULNERABILITY CONSIDERATIONS         : " + SCRMVC.getSCVCT3VC());
      System.out.println();
      System.out.println               (" TIER3 VULNERABILITY CONSIDERATIONS METHODS : " + SCRMVC.getSCVCT3M());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN VULNERABILITY CONSIDERATIONS CATEGORY SELECT CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
        // System.out.println("PLEASE SHOW THREAT AGENTS: COUNTERAFEITERS - SCENARIOS: ");
         System.out.println();
  
  // *****************COUNTRAFEITIERS SCENARIOS **************

          SCRMVC.setSCVCT1VC   (" 1. Organization’s mission/business. 2. Supplier relationships (e.g., system integrators, COTS, external services). 3. Geographical considerations related to the extent of the organization’s ICT supply chain. 4. Enterprise/Security Architecture. 5. Criticality Baseline. ");        
       
//**************** Display the COUNTRAFEITIERS SCENARIOS****************

     
      System.out.println               (" TIER1 VULNERABILITY CONSIDERATIONS : " + SCRMVC.getSCVCT1VC());

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN VULNERABILITY CONSIDERATIONS CATEGORY SELECT CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: COUNTERAFEITERS - EXAMPLES: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         SCRMVC.setSCVCT1M    (" 1. Examine agency ICT supply chain information including that from supply chain maps to identify especially vulnerable locations or organizations. 2. Analyze agency mission for susceptibility to potential supply chain vulnerabilities. 3. Examine system integrator and supplier relationships for susceptibility to potential supply chain vulnerabilities. 4. Review enterprise architecture and criticality baseline to identify areas of weakness requiring more robust ICT supply chain considerations.  ");         
       
         System.out.println       (" TIER1 VULNERABILITY CONSIDERATINS METHODS  : " + SCRMVC.getSCVCT1M());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT CONSIDERATIONS CATEGORY SELECT CHOICE #3");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - SCENARIOS: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      SCRMVC.setSCVCT2VC   (" 1. Mission functions. 2. Geographic locations. 3. Types of suppliers (COTS, custom,etc). 4. Technologies used.  ");
      

      System.out.println               (" TIER2 VULNERABILITY CONSIDERATIONS   : " + SCRMVC.getSCVCT2VC());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN VULNERABILITY CONSIDERATIONS CATEGORY SELECT CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         //System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       SCRMVC.setSCVCT2M    (" 1. Refine analysis from Tier 1 based on specific mission functions and applicable threat and supply chain information. 2. Consider using the National Vulnerability Database (NVD), including Common Vulnerabilities and Exposures (CVE) and Common Vulnerability Scoring System (CVSS), to characterize, categorize, and score vulnerabilities. 3. Consider using scoring guidance to prioritize vulnerabilities for remediation.  ");                   
        

      System.out.println               (" TIER2 VULNERABILITY CONSIDERATIONS METHODS : " + SCRMVC.getSCVCT2M());

      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN VULNERABILITY CONSIDERATIONS CATEGORY SELECT CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
      
  else
  
      if ( menuSelect == 6)
      
       {
         System.out.println();
         //System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println();
         


  // ********************Platform Types*********************
  
 
        SCRMVC.setSCVCT3VC   (" 1. Individual technologies, solutions, and suppliers should be considered.  ");
       

        System.out.println               (" TIER3 VULNERABILITY CONSIDERATIONS    : " + SCRMVC.getSCVCT3VC());

      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN VULNERABILITY CONSIDERATIONS CATEGORY SELECT CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

else
  
      if ( menuSelect == 7)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - EXAMPLES: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
        SCRMVC.setSCVCT3M    (" 1. Use CVEs where available to characterize and categorize vulnerabilities. 2. Identify weaknesses.  ");

       

        System.out.println               (" TIER3 VULNERABILITY CONSIDERATIONS METHODS : " + SCRMVC.getSCVCT3M());


      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN VULNERABILITY CONSIDERATIONS CATEGORY SELECT CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

 
     else             
   
  
  
// ******************Display the SCRM Main menu************************************

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE THE SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  SCRM STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 7) 
  
{
 
System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID SCRM FRAMEWORK SELECTION CATEGORY");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE IS THE VALID SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1. SCRM ORGANIZATION & STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


  
  menuSelection = keyboard.nextInt();

  
 }
 
 // ***********************************CHOICE#5 SUPPLY-CHAIN CONSTRAINTS WILL BEGIN HERE*********************************************
 
 break;

case 5: 

 
  
 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED SUPPLY-CHAIN CONSTRAINTS CATEGORY ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW SUPPLY-CHAIN CONSTRAINTS SUBCATEGORIES");
 System.out.println();

ScrmSetter SCRMCON;

//  Following statement creates an object using the AiSetter class as
//its Blueprint. Centcom will reference the object.

SCRMCON = new ScrmSetter();

  

 System.out.println("1.  SHOW ENTIRE LIST OF SUPPLY-CHAIN CONSTRAINTS.");
 System.out.println();
 System.out.println("2.  TIER1 AGENCY CONSTRAINTS.");
 System.out.println();
 System.out.println("3.  TIER1 ICT SUPPLY-CHAIN CONSTRAINTS.");
 System.out.println();
 System.out.println("4.  TIER2 AGENCY CONSTRAINTS.");
 System.out.println();
 System.out.println("5.  TIER2 ICT SUPPLY-CHAIN CONSTRAINTS.");
 System.out.println();
 System.out.println("6.  TIER3 AGENCY CONSTRAINTS.");
 System.out.println();
 System.out.println("7.  TIER3 ICT SUPPLY-CHAIN CONSTRAINTS.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 7: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 7)
  

  
{
   System.out.println("************************************************************************************************" );
  
 System.out.println("THIS IS INVALID SUPPLY-CHAIN CONSTRAINTS SELECTION"); 
 System.out.println();
 System.out.println("1.  SHOW ENTIRE LIST OF SUPPLY-CHAIN CONSTRAINTS.");
 System.out.println();
 System.out.println("2.  TIER1 AGENCY CONSTRAINTS.");
 System.out.println();
 System.out.println("3.  TIER1 ICT SUPPLY-CHAIN CONSTRAINTS.");
 System.out.println();
 System.out.println("4.  TIER2 AGENCY CONSTRAINTS.");
 System.out.println();
 System.out.println("5.  TIER2 ICT SUPPLY-CHAIN CONSTRAINTS.");
 System.out.println();
 System.out.println("6.  TIER3 AGENCY CONSTRAINTS.");
 System.out.println();
 System.out.println("7.  TIER3 ICT SUPPLY-CHAIN CONSTRAINTS.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 7: ");

 
  menuSelect = keyboard.nextInt();
  
  // String SCCT1AC, SCCT1ICT, SCCT2AC, SCCT2ICT, SCCT3AC, SCCT3ICT;



 }
       // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SHOW ENTIRE LIST OF SUPPLY-CHAIN CONSTRAINTS: ");
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          SCRMCON.setSCCT1AC   (" 1. Organization policies, strategies,governance. 2. Applicable laws and regulations. 3. Mission functions. 4. Organization processes (security,quality, etc.) .  ");        
          SCRMCON.setSCCT1ICT  (" 1. Organization ICT SCRM policy based on the existing agency policies, strategies, and governance; applicable laws and regulations; mission functions; and organization processes.  ");         
          SCRMCON.setSCCT2AC   (" 1. Mission functions. 2. Criticality of functions. 3. Enterprise architecture. 4. Mission-level security policies  ");
          SCRMCON.setSCCT2ICT  (" 1. ICT SCRM Mission/business requirements that are incorporated into mission/business processes and enterprise architecture. ");                   
          SCRMCON.setSCCT3AC   (" 1. Functional requirements. 2. Security requirements  ");
          SCRMCON.setSCCT3ICT  (" 1. System-level ICT SCRM requirements.  ");


          

         
// Display the AC taxonomy values stored in the fields

     
      System.out.println               (" TIER1 AGENCY CONSTRAINTS           : " + SCRMCON.getSCCT1AC());
      System.out.println();
      System.out.println               (" TIER1 ICT SUPPLY-CHAIN CONSTRAINTS : " + SCRMCON.getSCCT1ICT());
      System.out.println();
      System.out.println               (" TIER2 AGENCY CONSTRAINTS           : " + SCRMCON.getSCCT2AC());
      System.out.println();
      System.out.println               (" TIER2 ICT SUPPLY-CHAIN CONSTRAINTS : " + SCRMCON.getSCCT2ICT());
      System.out.println();
      System.out.println               (" TIER3 AGENCY CONSTRAINTS           : " + SCRMCON.getSCCT3AC());
      System.out.println();
      System.out.println               (" TIER3 ICT SUPPLY-CHAIN CONSTRAINTS : " + SCRMCON.getSCCT3ICT());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY-CHAIN CONSTRAINTS CATEGORY SELECT CHOICE # 5");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      
      // String SCCT1AC, SCCT1ICT, SCCT2AC, SCCT2ICT, SCCT3AC, SCCT3ICT;
      
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println();
  
  // *****************COUNTRAFEITIERS SCENARIOS **************

         SCRMCON.setSCCT1AC   (" 1. Organization policies, strategies,governance. 2. Applicable laws and regulations. 3. Mission functions. 4. Organization processes (security,quality, etc.) .  ");        
       
//**************** Display the COUNTRAFEITIERS SCENARIOS****************

     
      System.out.println               (" TIER1 AGENCY CONSTRAINTS : " + SCRMCON.getSCCT1AC());

      
      System.out.println();
      //System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN CONSTRAINTS CATEGORY SELECT CHOICE # 5");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
    
    // String SCCT1AC, SCCT1ICT, SCCT2AC, SCCT2ICT, SCCT3AC, SCCT3ICT;
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
        // System.out.println("************************************************************************************************" );
         System.out.println();
       
         System.out.println();
         

  
       
         SCRMCON.setSCCT1ICT  ("    Organization ICT SCRM policy based on the existing agency policies, strategies, and governance; applicable laws and regulations; mission functions; and organization processes.  ");         
         
         System.out.println    (" TIER1 ICT SUPPLY-CHAIN CONSTRAINTS : " + SCRMCON.getSCCT1ICT());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN CONSTRAINTS CATEGORY SELECT CHOICE # 5");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else 
   
   // String SCCT1AC, SCCT1ICT, SCCT2AC, SCCT2ICT, SCCT3AC, SCCT3ICT;
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println();
         


        SCRMCON.setSCCT2AC   (" 1. Mission functions. 2. Criticality of functions. 3. Enterprise architecture. 4. Mission-level security policies  ");
     

      System.out.println      (" TIER2 AGENCY CONSTRAINTS   : " + SCRMCON.getSCCT2AC());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT CONSIDERATIONS CATEGORY SELECT CHOICE #3");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

else
   
   // String SCCT1AC, SCCT1ICT, SCCT2AC, SCCT2ICT, SCCT3AC, SCCT3ICT;
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println();
         
  
 
     SCRMCON.setSCCT2ICT  (" 1. ICT SCRM Mission/business requirements that are incorporated into mission/business processes and enterprise architecture. ");                   
       

      System.out.println      (" TIER2 ICT SUPPLY-CHAIN CONSTRAINTS : " + SCRMCON.getSCCT2ICT());

      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT CONSIDERATIONS CATEGORY SELECT CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
      
  else
  
  // String SCCT1AC, SCCT1ICT, SCCT2AC, SCCT2ICT, SCCT3AC, SCCT3ICT;
  
  
      if ( menuSelect == 6)
      
       {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println();
         


        SCRMCON.setSCCT3AC   (" 1. Functional requirements. 2. Security requirements  ");
       

        System.out.println               (" TIER3 AGENCY CONSTRAINTS    : " + SCRMCON.getSCCT3AC());

      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN CONSTRAINTS CATEGORY SELECT CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

else
  
  // String SCCT1AC, SCCT1ICT, SCCT2AC, SCCT2ICT, SCCT3AC, SCCT3ICT;
  
      if ( menuSelect == 7)
      
       {
        // System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println();
         
 
        SCRMCON.setSCCT3ICT  (" 1. System-level ICT SCRM requirements.  ");
       

        System.out.println   (" TIER3 ICT SUPPLY-CHAIN CONSTRAINTS : " + SCRMCON.getSCCT3ICT());


      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN CONSTRAINTS CATEGORY SELECT CHOICE # 5");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

 
     else             
   
  
  
// ******************Display the SCRM Main menu************************************

System.out.println();
//System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE THE SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  SCRM STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 7) 
  
{
 
//.System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID SCRM FRAMEWORK SELECTION CATEGORY");
System.out.println();
//System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE IS THE VALID SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1. SCRM ORGANIZATION & STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


  
  menuSelection = keyboard.nextInt();

  
 }
 
 break;

//*************************************START OF CHOICE#6 SUPPLY-CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATION***********************************

case 6: 

 
 //String SCVMOT1VT, SCVMOT1MT, SCVMOT2VT, SCVMOT2MT, SCVMOT3VT, SCVMOT3MT;
 
 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED SUPPLY-CHAIN VULNERABILITY MAPPED TO ORGANIZATION CATEGORY ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW SUPPLY-CHAIN VULNERABILITY MAPPED TO ORGANIZATION SUBCATEGORIES");
 System.out.println();

ScrmSetter SCVMO;

//  Following statement creates an object using the AiSetter class as
//its Blueprint. Centcom will reference the object.

SCVMO = new ScrmSetter();

  

 System.out.println("1.  SHOW ENTIRE LIST OF SUPPLY-CHAIN VULNERABILITY MAPPED TO ORGANIZATION.");
 System.out.println();
 System.out.println("2.  TIER1-ORGANIZATION VULNERABILITY TYPES .");
 System.out.println();
 System.out.println("3.  TIER1-ORGANIZATION MITIGATION TYPES.");
 System.out.println();
 System.out.println("4.  TIER2-MISSION/BUSINESS VULNERABILITY TYPES .");
 System.out.println();
 System.out.println("5.  TIER2-MISSION/BUSINESS MITIGATION TYPES.");
 System.out.println();
 System.out.println("6.  TIER3-OPERATION VULNERABILITY TYPES.");
 System.out.println();
 System.out.println("7.  TIER3-OPERATION MITIGATION TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 7: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 7)
  

  
{
   System.out.println("************************************************************************************************" );
  
 System.out.println("THIS IS INVALID CATEGORY SELECTION FOR SUPPLY-CHAIN VULNERABILITY MAPPED TO ORGANIZTION"); 
 System.out.println();
 System.out.println("1.  SHOW ENTIRE LIST OF SUPPLY-CHAIN VULNERABILITY MAPPED TO ORGANIZATION.");
 System.out.println();
 System.out.println("2.  TIER1-ORGANIZATION VULNERABILITY TYPES .");
 System.out.println();
 System.out.println("3.  TIER1-ORGANIZATION MITIGATION TYPES.");
 System.out.println();
 System.out.println("4.  TIER2-MISSION/BUSINESS VULNERABILITY TYPES .");
 System.out.println();
 System.out.println("5.  TIER2-MISSION/BUSINESS MITIGATION TYPES.");
 System.out.println();
 System.out.println("6.  TIER3-OPERATION VULNERABILITY TYPES.");
 System.out.println();
 System.out.println("7.  TIER3-OPERATION MITIGATION TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 7: ");

 
  menuSelect = keyboard.nextInt();


 }
       //String SCVMOT1VT, SCVMOT1MT, SCVMOT2VT, SCVMOT2MT, SCVMOT3VT, SCVMOT3MT;
         
    if ( menuSelect == 1)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("1.  SHOW ENTIRE LIST OF SUPPLY-CHAIN VULNERABILITIES MAPPED TO ORGANIZATION.");
          System.out.println();
          System.out.println("************************************************************************************************" );

          SCVMO.setSCVMOT1VT   (" 1. Deficiencies or weaknesses in organizational governance structures or processes such as a lack of ICT SCRM Plan.  ");        
          SCVMO.setSCVMOT1MT   (" 1. Provide guidance on how to consider dependencies on external organizations as vulnerabilities. 2. Seek out alternate sources of new technology including building in-house. ");         
          SCVMO.setSCVMOT2VT   (" 1. No operational process is in place for detecting counterfeits. 2. No budget was allocated for the implementation of a technical screening for acceptance testing of ICT components entering the SDLC as replacement parts. 3. Susceptibility to adverse issues from innovative technology supply sources (e.g., technology owned or managed by third parties is buggy). ");
          SCVMO.setSCVMOT2MT   (" 1. Develop a program for detecting counterfeits and allocate appropriate budgets for putting in resources and training. 2. Allocate budget for acceptance testing – technical screening of components entering into SDLC. ");                   
          SCVMO.setSCVMOT3VT   (" 1. Discrepancy in system functions not meeting requirements, resulting in substantial impact to performance,  ");
          SCVMO.setSCVMOT3MT   (" 1. Initiate engineering change. Malicious alteration can happen throughout the system life cycle to an agency system to address functional discrepancy and test correction for performance impact.  ");


          

         
// Display the AC taxonomy values stored in the fields

     
      System.out.println               (" TIER1-ORGANIZATION VULNERABILITY TYPES     : " + SCVMO.getSCVMOT1VT());
      System.out.println();
      System.out.println               (" TIER1-ORGANIZATION MITIGATION TYPES        : " + SCVMO.getSCVMOT1MT());
      System.out.println();
      System.out.println               (" TIER2-MISSION/BUSINESS VULNERABILITY TYPES : " + SCVMO.getSCVMOT2VT());
      System.out.println();
      System.out.println               (" TIER2-MISSION/BUSINESS MITIGATION TYPES    : " + SCVMO.getSCVMOT2MT());
      System.out.println();
      System.out.println               (" TIER3-OPERATION VULNERABILITY TYPES        : " + SCVMO.getSCVMOT3VT());
      System.out.println();
      System.out.println               (" TIER3-OPERATION MITIGATION TYPES           : " + SCVMO.getSCVMOT3MT());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN VULNERABILITY MAPPED TO ORGANIZATION SELECT CHOICE # 6");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
        // System.out.println("PLEASE SHOW THREAT AGENTS: COUNTERAFEITERS - SCENARIOS: ");
         System.out.println();
  
  // *****************COUNTRAFEITIERS SCENARIOS **************

         SCVMO.setSCVMOT1VT   (" 1. Deficiencies or weaknesses in organizational governance structures or processes such as a lack of ICT SCRM Plan.  ");        
        
//**************** Display the COUNTRAFEITIERS SCENARIOS****************

     
      System.out.println     (" TIER1 VULNERABILITY TYPES: " + SCVMO.getSCVMOT1VT());

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN VULNERABILITY MAPPED TO ORGANIZATION SELECT CHOICE # 6");

      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         //System.out.println("************************************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: COUNTERAFEITERS - EXAMPLES: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         SCVMO.setSCVMOT1MT   (" 1. Provide guidance on how to consider dependencies on external organizations as vulnerabilities. 2. Seek out alternate sources of new technology including building in-house. ");         
       
         System.out.println   (" TIER1 MITIGATION TYPES : " + SCVMO.getSCVMOT1MT());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN VULNERABILITY MAPPED TO ORGANIZATION SELECT CHOICE # 6");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - SCENARIOS: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       SCVMO.setSCVMOT2VT   (" 1. No operational process is in place for detecting counterfeits. 2. No budget was allocated for the implementation of a technical screening for acceptance testing of ICT components entering the SDLC as replacement parts. 3. Susceptibility to adverse issues from innovative technology supply sources (e.g., technology owned or managed by third parties is buggy). ");
      

      System.out.println    (" TIER2 VULNERABILITY TYPES : " + SCVMO.getSCVMOT2VT());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN VULNERABILITY MAPPED TO ORGANIZATION SELECT CHOICE # 6");

      System.out.println();
      System.out.println("************************************************************************************************" );

      }

else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - EXAMPLES: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
        SCVMO.setSCVMOT2MT   (" 1. Develop a program for detecting counterfeits and allocate appropriate budgets for putting in resources and training. 2. Allocate budget for acceptance testing – technical screening of components entering into SDLC. ");                   
       

       System.out.println    (" TIER2 MITIGATION TYPES : " + SCVMO.getSCVMOT2MT());      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN VULNERABILITY MAPPED TO ORGANIZATION SELECT CHOICE # 6");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
      
  else
  
      if ( menuSelect == 6)
      
       {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - EXAMPLES: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
         SCVMO.setSCVMOT3VT   (" 1. Discrepancy in system functions not meeting requirements, resulting in substantial impact to performance,  ");
       

        System.out.println   (" TIER3 VULNERABILITY TYPES : " + SCVMO.getSCVMOT3VT());


      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN VULNERABILITY MAPPED TO ORGANIZATION SELECT CHOICE # 6");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

else
  
      if ( menuSelect == 7)
      
       {
         System.out.println();
        // System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - EXAMPLES: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
        SCVMO.setSCVMOT3MT   (" 1. Initiate engineering change. Malicious alteration can happen throughout the system life cycle to an agency system to address functional discrepancy and test correction for performance impact.  ");

       

        System.out.println   (" TIER3 MITIGATION TYPES : " + SCVMO.getSCVMOT3MT());



      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN VULNERABILITY MAPPED TO ORGANIZATION SELECT CHOICE # 6");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

 
     else             
   
  
  
// ******************Display the SCRM Main menu************************************

System.out.println();
//System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE THE SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  SCRM STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 7) 
  
{
 
//System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID SCRM FRAMEWORK SELECTION CATEGORY");
System.out.println();
//System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE IS THE VALID SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1. SCRM ORGANIZATION & STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


  
  menuSelection = keyboard.nextInt();

  
 }
 
 break;

//************************CATEGORY#7 SUPPLY CHAIN PLAN CONTROLS BEGIN HERE*****************************************************

case 7: 

 
 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED SUPPLY-CHAIN PLAN CONTROL CATEGORY ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW SUPPLY-CHAIN PLAN CONTROL SUBCATEGORIES");
 System.out.println();


//String SCPCT1C, SCPCT1E, SCPCT2C, SCPCT2E, SCPCT3C, SCPCT3E;

ScrmSetter SCPC;


SCPC = new ScrmSetter();

  

 System.out.println("1.  SHOW ENTIRE LIST OF ICT SUPPLY-CHAIN PLAN CONTROLS.");
 System.out.println();
 System.out.println("2.  TIER1-ORGANIZATION CONTROLS.");
 System.out.println();
 System.out.println("3.  TIER1-ORGANIZATION CONTROL EXAMPLES.");
 System.out.println();
 System.out.println("4.  TIER2-MISSION/BUSINESS CONTROLS. ");
 System.out.println();
 System.out.println("5.  TIER2-MISSION/BUSINESS CONTOL EXAMPLES. ");
 System.out.println();
 System.out.println("6.  TIER3-OPERATION CONTROLS.");
 System.out.println();
 System.out.println("7.  TIER3-OPERATION CONTROL EXAMPLES .");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 7: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 7)
  

  
{
   
 //System.out.println("************************************************************************************************" );
  
 System.out.println("THIS IS INVALID CHOICE FOR ICT SCRM PLAN CONTROLS SELECTION"); 
 System.out.println();
 System.out.println("2.  TIER1-ORGANIZATION CONTROLS.");
 System.out.println();
 System.out.println("3.  TIER1-ORGANIZATION CONTROL EXAMPLES.");
 System.out.println();
 System.out.println("4.  TIER2-MISSION/BUSINESS CONTROLS. ");
 System.out.println();
 System.out.println("5.  TIER2-MISSION/BUSINESS CONTOL EXAMPLES. ");
 System.out.println();
 System.out.println("6.  TIER3-OPERATION CONTROLS.");
 System.out.println();
 System.out.println("7.  TIER3-OPERATION CONTROL EXAMPLES .");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 7: ");

 
  menuSelect = keyboard.nextInt();


 }
       //String SCPCT1C, SCPCT1E, SCPCT2C, SCPCT2E, SCPCT3C, SCPCT3E;

  
    if ( menuSelect == 1)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println(" PLEASE SHOW ENTIRE LIST OF ICT SUPPLY-CHAIN PLAN CONTROLS: ");
          System.out.println();
          System.out.println("************************************************************************************************" );

          SCPC.setSCPCT1C   (" 1. Provides organization common controls baseline to Tiers 2 and 3. ");        
          SCPC.setSCPCT1E   (" 1. Minimum sets of controls applicable to all ICT suppliers 2. Organization-level controls applied to processing and storing supplier information 3. ICT supply chain training and awareness for acquirer staff at the organization level. ");         
          SCPC.setSCPCT2C   (" 1. Inherits common controls from Tier1. 2. Provides mission functionlevel common controls baseline to Tier3. 3. Provides feedback to Tier1 about what is working and what needs to be changed. ");
          SCPC.setSCPCT2E   (" 1. Minimum sets of controls applicable to ICT suppliers for the specific mission function. 2. Program-level refinement of Identity and Access Management controls to address ICT SCRM concerns. 3. Program-specific ICT supply chain training and awareness. ");                   
          SCPC.setSCPCT3C   (" 1. Inherits common controls from Tiers 1&2. 2. Provides system-specific controls for Tier3. 3. Provides feedback to Tier2 and Tier1 about what is working and what needs to be changed. ");
          SCPC.setSCPCT3E   (" 1. Minimum sets of controls applicable to specific hardware and software for the individual system. 2. Appropriately rigorous acceptance criteria for change management for systems that support ICT supply chain e.g., as testing or integrated development environments. 3 . System-specific ICT supply chain training and awareness. 4. Intersections with the SDLC. ");

            
      System.out.println               (" TIER1-ORGANIZATION CONTROLS              : " + SCPC.getSCPCT1C());
      System.out.println();
      System.out.println               (" TIER1-ORGANIZATION CONTROL EXAMPLES      : " + SCPC.getSCPCT1E());
      System.out.println();
      System.out.println               (" TIER2-MISSION/BUSINESS CONTROLS          : " + SCPC.getSCPCT2C());
      System.out.println();
      System.out.println               (" TIER2-MISSION/BUSINESS CONTROLS EXAMPLES : " + SCPC.getSCPCT2E());
      System.out.println();
      System.out.println               (" TIER3-OPERATION CONTROLS                 : " + SCPC.getSCPCT3C());
      System.out.println();
      System.out.println               (" TIER3-OPERATION CONTROL EXAMPLES         : " + SCPC.getSCPCT3E());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH ICT SCRM PLAN CONTROLS SELECT CHOICE # 7");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
        //System.out.println("***********************************************************************************" );
         System.out.println();
        // System.out.println("PLEASE SHOW THREAT AGENTS: COUNTERAFEITERS - SCENARIOS: ");
         System.out.println();
  
  

         SCPC.setSCPCT1C   (" 1. Provides organization common controls baseline to Tiers 2 and 3. ");        
      

     
       System.out.println   (" TIER1-ORGANIZATION CONTROLS : " + SCPC.getSCPCT1C());


      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUPPLY CHAIN THREAT CONSIDERATIONS CATEGORY SELECT CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: COUNTERAFEITERS - EXAMPLES: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         SCPC.setSCPCT1E   (" 1. Minimum sets of controls applicable to all ICT suppliers 2. Organization-level controls applied to processing and storing supplier information 3. ICT supply chain training and awareness for acquirer staff at the organization level. ");         
       
        System.out.println    (" TIER1-ORGANIZATION CONTROL EXAMPLES : " + SCPC.getSCPCT1E());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH ICT SCRM PLAN CONTROLS SELECT CHOICE # 7");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - SCENARIOS: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
        SCPC.setSCPCT2C   (" 1. Inherits common controls from Tier1. 2. Provides mission functionlevel common controls baseline to Tier3. 4. Provides feedback to Tier1 about what is working and what needs to be changed. ");
       

      System.out.println   (" TIER2-MISSION/BUSINESS CONTROLS : " + SCPC.getSCPCT2C());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH ICT SCRM PLAN CONTROLS SELECT CHOICE # 7");

      System.out.println();
      System.out.println("************************************************************************************************" );

      }

else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         //System.out.println("***********************************************************************************" );
         System.out.println();
         //System.out.println("PLEASE SHOW THREAT AGENTS: INSIDERS - EXAMPLES: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
          SCPC.setSCPCT2E   (" 1. Minimum sets of controls applicable to ICT suppliers for the specific mission function. 2. Program-level refinement of Identity and Access Management controls to address ICT SCRM concerns. 3. Program-specific ICT supply chain training and awareness. ");                   
       

     System.out.println      (" TIER2-MISSION/BUSINESS CONTROLS EXAMPLES : " + SCPC.getSCPCT2E());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
     System.out.println( "TO CONTINUE ICT SCRM PLAN CONTROLS SELECT CHOICE # 7");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
      
  else
  
      if ( menuSelect == 6)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         
         System.out.println();
         


  // ********************Platform Types*********************
  
 
        SCPC.setSCPCT3C   (" 1. Inherits common controls from Tiers 1&2. 2. Provides system-specific controls for Tier3. 3. Provides feedback to Tier2 and Tier1 about what is working and what needs to be changed. ");
        

        System.out.println   (" TIER3-OPERATION CONTROLS : " + SCPC.getSCPCT3C());

      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE ICT SCRM PLAN CONTROLS SELECT CHOICE # 7");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

else
  
      if ( menuSelect == 7)
      
       {
         System.out.println();
         //System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println();
         
 
        SCPC.setSCPCT3E   (" 1. Minimum sets of controls applicable to specific hardware and software for the individual system. 2. Appropriately rigorous acceptance criteria for change management for systems that support ICT supply chain e.g., as testing or integrated development environments. 3 . System-specific ICT supply chain training and awareness. 4. Intersections with the SDLC. ");

       

        System.out.println   (" TIER3-OPERATION CONTROL EXAMPLES : " + SCPC.getSCPCT3E());


      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE ICT SCRM PLAN CONTROLS SELECT CHOICE # 7");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

 
     else             
   
  
  
// ******************Display the SCRM Main menu************************************

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE THE SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  SCRM STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 7) 
  
{
 
System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID SCRM FRAMEWORK SELECTION CATEGORY");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE IS THE VALID SCRM FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1. SCRM ORGANIZATION & STAKEHOLDERS TIERS. "); 
System.out.println();
System.out.println   ("2.  SUPPLY CHAIN THREAT AGENTS. "); 
System.out.println();
System.out.println   ("3.  SUPPLY CHAIN THREAT CONSIDERATIONS."); 
System.out.println();
System.out.println   ("4.  SUPPLY CHAIN VULNERABILITY CONSIDERATIONS. "); 
System.out.println();
System.out.println   ("5.  SUPPLY CHAIN CONSTRAINTS. "); 
System.out.println();
System.out.println   ("6.  SUPPLY CHAIN VULNERABILITIES MAPPED TO THE ORGANIZATIONS."); 
System.out.println();
System.out.println   ("7.  SCRM PLAN CONTROLS AT TIERS 1, 2, & 3. "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM FRAMEWORK CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR SCRM CATEGORY CHOICE (1 - 7) FROM THE LIST ABOVE: ");


  
  menuSelection = keyboard.nextInt();

  
 }
 
break; 

 
    }
  }
}

//*************************************END OF SCRM FRAMEWORK APPLICATION***********************************************