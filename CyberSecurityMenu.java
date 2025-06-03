veloped by Kalsnet Technologies (KNet)//The CyberSecurity Framework program was developed to help Security Analysts,Security Planners System, Network System's Administrators to understand & 
//Address IOT Security Vulnerabilitiesin within Critical Infrastructure of DISA, DoD & USA. Critical Infrastructure is Interconnected.
//This program addresses the critical infrastructure Security Framework. This Application will help to Identify,Protect, Detect & Respond 
//the Security framework taxonomies and Provide Mitigation Strategies. The Application was written by Kalsnet Technologies (KNet).                  


import java.util.Scanner; 

public class CyberSecurityMenu 

{

public static void main(String[] args) 

{ 

// Declare a variable to hold the 
// user's menu selection. 

 int menuSelection;

// Create a Scanner object for keyboard input. 

Scanner keyboard = new Scanner(System.in);
 
// DISPLAY THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE.

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println(" WELCOME TO CYBER SECURITY FRAMEWORK APPLICATION FOR DoD CRITICAL INFRASTRUCTURE. ");
 System.out.println();
 System.out.println(" HERE IS THE LIST OF CYBER SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

//while (menuSelection < 1 || menuSelection > 21) 

  
  //System.out.println();

 //menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS THE VALID SECURITY FRAMEWORK CHECKLIST FOR DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 //System.out.println();

 menuSelection = keyboard.nextInt(); 
 
 } 
 
 while (menuSelection > 0 || menuSelection <= 21)
 
// Perform the selected operation. 

 switch(menuSelection) 
{ 
 
 case 1:
 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("ASSET MANAGEMENT:");
  System.out.println();
  System.out.println();
  System.out.println("DATA, PERSONNEL, DEVICES, SYSTEMS, & FACILITIES THAT ENABLE  THE  ORGANIZATION TO ACHEIVE BUSINESS PURPOSES ARE IDENTIFIED AND");
  System.out.println(); 
  System.out.println("MANAGED CONSISTENT WITH THEIR RELATIVE IMPORTANCE TO BUSINESS OBJECTIVES & THE ORGANIZATION'S RISK STRATEGY.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println ("BELOW IS THE LIST OF ASSET MANAGEMENT SUBCATEGORIES: ");
  System.out.println();
  System.out.println("1. Physical Devices and Systems within the Organization are Inventoried");
  System.out.println();
  System.out.println("2. Software platforms and applications within the organization are inventoried");
  System.out.println();
  System.out.println("3. Organizational Communication and Data Flows are Mapped");
  System.out.println();
  System.out.println("4. External Information Systems are Catalogued");
  System.out.println();
  System.out.println("5. Resources (e.g., Hardware, Devices, Data, and Software) are Prioritized based on their Classification, Criticality, and Business Value ");
  System.out.println();
  System.out.println("6. Cybersecurity Roles and Responsibilities for the entire Workforce and Third-Party Stakeholders (e.g., Suppliers, Customers, Partners) Are Established" );
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE ASSET MANAGEMENT ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. CCS CSC 1,COBIT 5 BAI09.01, BAI09.02,ISA 62443-2-1:2009 4.2.3.4,ISA 62443-3-3:2013 SR 7.8,ISO/IEC 27001:2013 A.8.1.1, A.8.1.2,NIST SP 800-53 Rev. 4 CM-8");
  System.out.println();
  System.out.println("2. CCS CSC 2,COBIT 5 BAI09.01, BAI09.02, BAI09.05,ISA 62443-2-1:2009 4.2.3.4,ISA 62443-3-3:2013 SR 7.8,ISO/IEC 27001:2013 A.8.1.1, A.8.1.2,NIST SP 800-53 Rev. 4 CM-8");
  System.out.println();
  System.out.println("3. CCS CSC 1,COBIT 5 DSS05.02,ISA 62443-2-1:2009 4.2.3.4,ISO/IEC 27001:2013 A.13.2.1,NIST SP 800-53 Rev. 4 AC-4, CA-3, CA-9, PL-8");
  System.out.println();
  System.out.println("4. COBIT 5 APO02.02,ISO/IEC 27001:2013 A.11.2.6,NIST SP 800-53 Rev. 4 AC-20, SA-9");
  System.out.println();
  System.out.println("5. COBIT 5 APO03.03, APO03.04, BAI09.02,ISA 62443-2-1:2009 4.2.3.6,ISO/IEC 27001:2013 A.8.2.1,NIST SP 800-53 Rev. 4 CP-2, RA-2, SA-14");
  System.out.println();
  System.out.println("6. COBIT 5 APO01.02, DSS06.03,ISA 62443-2-1:2009 4.3.2.3.3,ISO/IEC 27001:2013 A.6.1.1,NIST SP 800-53 Rev. 4 CP-2, PS-7, PM-11");
  System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();



 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 

 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 

 menuSelection = keyboard.nextInt(); 
 
 } 


break;
 
case 2: 

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("BUSINESS ENVIRONMENT:");
  System.out.println();
  System.out.println();
  System.out.println("The Organizations Mission, Objectives, Stakeholders & Activities Are Understood & Prioritized & The Organizations Role In The Supply Chain Is Identified & Communicated."); 
  System.out.println();
  System.out.println("This Information Is Used To Inform Cybersecurity Roles, Responsibilities & Risk Management Decisions.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF BUSINESS ENVIRONMENT SUBCATEGORIES: ");
  System.out.println();
  System.out.println("1. The Organizations Role In The Supply Chain Is Identified & Communicated ");
  System.out.println();
  System.out.println("2. The Organizations Place In Critical Infrastructure & Its Industry Sector Is Identified & Communicated");
  System.out.println();
  System.out.println("3. Priorities For Organizational Mission, Objectives & Activities Are Established & Communicated");
  System.out.println();
  System.out.println("4. Dependencies & Critical Functions For Delivery Of Critical Services Are Established");
  System.out.println();
  System.out.println("5. Resilience requirements to support delivery of critical services are established ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE BUSINESS ENVIRONMENT ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. COBIT 5 APO08.04, APO08.05, APO10.03, APO10.04, APO10.05,ISO/IEC 27001:2013 A.15.1.3, A.15.2.1, A.15.2.2,NIST SP 800-53 Rev. 4 CP-2, SA-12");
  System.out.println();
  System.out.println("2. COBIT 5 APO02.06, APO03.01,NIST SP 800-53 Rev. 4 PM-8");
  System.out.println();
  System.out.println("3. COBIT 5 APO02.01, APO02.06, APO03.01,ISA 62443-2-1:2009 4.2.2.1, 4.2.3.6,NIST SP 800-53 Rev. 4 PM-11, SA-14");
  System.out.println();
  System.out.println("4. ISO/IEC 27001:2013 A.11.2.2, A.11.2.3, A.12.1.3,NIST SP 800-53 Rev. 4 CP-8, PE-9, PE-11, PM-8, SA-14");
  System.out.println();
  System.out.println("5. COBIT 5 DSS04.02,ISO/IEC 27001:2013 A.11.1.4, A.17.1.1, A.17.1.2, A.17.2.1,NIST SP 800-53 Rev. 4 CP-2, CP-11, SA-14");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println(" THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK CHOICE# SELECTION.  ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 

 menuSelection = keyboard.nextInt(); 
 
 } 
 
break; 

case 3:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("GOVERNANCE POLICIES & PROCEDURES:");
  System.out.println();
  System.out.println();
  System.out.println("The Policies, Procedures, & Processes To Manage & Monitor The Organizations Regulatory, Legal, Risk, Environmental & Operational Requirements "); 
  System.out.println();
  System.out.println("Are Understood & Inform The Management Of Cybersecurity Risk.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF GOVERNANCE POLICIES & PROCEDURES SUBCATEGORIES: ");
  System.out.println();
  System.out.println(" 1. Organizational Information Security Policy Is Established");
  System.out.println();
  System.out.println(" 2. Information Security Roles & Responsibilities Are Coordinated And Aligned With Internal Roles & External Partners");
  System.out.println();
  System.out.println(" 3. Legal & Regulatory Requirements Regarding Cybersecurity, Including Privacy And Civil Liberties Obligations, Are Understood & Managed");
  System.out.println();
  System.out.println(" 4. Governance & Risk Management Processes Address Cybersecurity Risks");
  System.out.println();
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE GOVERNANCE POLICIES & PROCEDURES ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. ISA 62443-2-1:2009 4.3.2.6,ISO/IEC 27001:2013 A.5.1.1,NIST SP 800-53 Rev. 4 -1 controls from all families");
  System.out.println();
  System.out.println("2.  COBIT 5 APO13.12,ISA 62443-2-1:2009 4.3.2.3.3,ISO/IEC 27001:2013 A.6.1.1, A.7.2.1, NIST SP 800-53 Rev. 4 PM-1, PS-7, COBIT 5 MEA03.01, MEA03.04");
  System.out.println();
  System.out.println("3. ISA 62443-2-1:2009 4.4.3.7,ISO/IEC 27001:2013 A.18.1,NIST SP 800-53 Rev. 4 -1 controls from all families (except PM-1)" );
  System.out.println();
  System.out.println("4. COBIT 5 DSS04.02,ISA 62443-2-1:2009 4.2.3.1, 4.2.3.3, 4.2.3.8, 4.2.3.9, 4.2.3.11, 4.3.2.4.3, 4.3.2.6.3,NIST SP 800-53 Rev. 4 PM-9, PM-11.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt(); 
 } 

break;

case 4:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("RISK ASSESSMENT:");
  System.out.println();
  System.out.println();
  System.out.println("The Organization Understands The Cybersecurity Risk To Organizational Operations (Including Mission, Functions, Image, Or Reputation), Organizational Assets, & Individuals"); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF RISK ASSESSMENT SUBCATEGORIES: ");
  System.out.println();
  System.out.println(" 1. Asset Vulnerabilities Are Identified & Documented");
  System.out.println();
  System.out.println(" 2. Threat & Vulnerability Information 1s Received From Information Sharing Forums & Sources");
  System.out.println();
  System.out.println(" 3. Threats, Both Internal & External, Are Identified & Documented");
  System.out.println();
  System.out.println(" 4. Potential Business Impacts & Likelihoods Are Identified ");
  System.out.println();
  System.out.println(" 5. Threats, Vulnerabilities, Likelihoods, & Impacts Are Used To Determine Risk ");
  System.out.println();
  System.out.println(" 6. Risk Responses Are Identified & Prioritized ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE RISK ASSESSMENT ARE LISTED BELOW:"); 
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println();
  System.out.println("1. CCS CSC 4, COBIT 5 APO12.01, APO12.02, APO12.03, APO12.04, ISA 62443-2-1:2009 4.2.3, 4.2.3.7, 4.2.3.9, 4.2.3.12,ISO/IEC 27001:2013 A.12.6.1, A.18.2.3,NIST SP 800-53 Rev. 4 CA-2, CA-7, CA-8, RA-3, RA-5, SA-5, SA-11, SI-2, SI-4, SI-5");
  System.out.println();
  System.out.println("2. ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12,ISO/IEC 27001:2013 A.6.1.4,NIST SP 800-53 Rev. 4 PM-15, PM-16, SI-5." );
  System.out.println();
  System.out.println("3. COBIT 5 APO12.01, APO12.02, APO12.03, APO12.04,ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12,NIST SP 800-53 Rev. 4 RA-3, SI-5, PM-12, PM-16");
  System.out.println();
  System.out.println("4. COBIT 5 DSS04.02,ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12,NIST SP 800-53 Rev. 4 RA-2, RA-3, PM-9, PM-11, SA-14" );
  System.out.println();
  System.out.println("5. COBIT 5 APO12.02,ISO/IEC 27001:2013 A.12.6.1,NIST SP 800-53 Rev. 4 RA-2, RA-3, PM-16" );
  System.out.println();
  System.out.println("6. COBIT 5 APO12.05, APO13.02, NIST SP 800-53 Rev. 4 PM-4, PM-9");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt(); 
 } 

break;

case 5:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("RISK MANAGEMENT STRATEGY:");
  System.out.println();
  System.out.println();
  System.out.println("The Organizations Priorities, Constraints, Risk Tolerances, & Assumptions Are Established & Used To Support Operational Risk Decisions"); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF RISK MANAGEMENT STRATEGY SUBCATEGORIES: ");
  System.out.println();
  System.out.println(" 1. Risk Management Processes Are Established, Managed, & Agreed To By Organizational Stakeholders");
  System.out.println();
  System.out.println(" 2. Organizational Risk Tolerance Is Determined & Clearly Expressed");
  System.out.println();
  System.out.println(" 3. The Organizations Determination Of Risk Tolerance Is Informed By Its Role In Critical Infrastructure & Sector Specific Risk Analysis");
  System.out.println();
  System.out.println(" 4. Resilience Requirements To Support Delivery Of Critical Services Are Established ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE RISK MANAGEMENT STRATEGY ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println(" 1. COBIT 5 APO12.04, APO12.05, APO13.02, BAI02.03, BAI04.02,ISA 62443-2-1:2009 4.3.4.2,NIST SP 800-53 Rev. 4 PM-9");
  System.out.println();
  System.out.println(" 2. COBIT 5 APO12.06,ISA 62443-2-1:2009 4.3.2.6.5,NIST SP 800-53 Rev. 4 PM-9" );
  System.out.println();
  System.out.println(" 3. NIST SP 800-53 Rev. 4 PM-8, PM-9, PM-11, SA-14" );
  System.out.println();

  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt(); 
 } 


break;

case 6:

System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print(" ACCESS CONTROL:");
  System.out.println();
  System.out.println();
  System.out.println("Access To Assets & Associated Facilities Is Limited To Authorized Users, Processes, Or Devices, & To Authorized Activities & Transactions"); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF ACCESS CONTROL SUBCATEGORIES: ");
  System.out.println();
  System.out.println(" 1. Identities & Credentials Are Managed For Authorized Devices & Users");
  System.out.println();
  System.out.println(" 2. Physical Access To Assets 1s managed & Protected");
  System.out.println();
  System.out.println(" 3. Remote Access Is Managed");
  System.out.println();
  System.out.println(" 4. Access Permissions Are Managed, Incorporating The Principles Of Least Privilege & Separation Of Duties ");
  System.out.println();
  System.out.println(" 5. Network Integrity Is Protected, Incorporating Network Segregation Where Appropriate ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE ACCESS CONTROL ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. CCS CSC 16,COBIT 5 DSS05.04, DSS06.03,ISA 62443-2-1:2009 4.3.3.5.1,ISA 62443-3-3:2013 SR 1.1, SR 1.2, SR 1.3, SR 1.4, SR 1.5, SR 1.7, SR 1.8, SR 1.9,ISO/IEC 27001:2013 A.9.2.1, A.9.2.2, A.9.2.4, A.9.3.1, A.9.4.2, A.9.4.3,NIST SP 800-53 Rev. 4 AC-2, IA Family");
  System.out.println();
  System.out.println("2. COBIT 5 DSS01.04, DSS05.05,ISA 62443-2-1:2009 4.3.3.3.2, 4.3.3.3.8,ISO/IEC 27001:2013 A.11.1.1, A.11.1.2, A.11.1.4, A.11.1.6, A.11.2.3,NIST SP 800-53 Rev. 4 PE-2, PE-3, PE-4, PE-5, PE-6, PE-9");
  System.out.println();
  System.out.println("3. COBIT 5 APO13.01, DSS01.04, DSS05.03,ISA 62443-2-1:2009 4.3.3.6.6,ISA 62443-3-3:2013 SR 1.13, SR 2.6,ISO/IEC 27001:2013 A.6.2.2, A.13.1.1, A.13.2.1,NIST SP 800-53 Rev. 4 AC?17, AC-19, AC-20");
  System.out.println();
  System.out.println("4. CCS CSC 12, 15,ISA 62443-2-1:2009 4.3.3.7.3,ISA 62443-3-3:2013 SR 2.1,ISO/IEC 27001:2013 A.6.1.2, A.9.1.2, A.9.2.3, A.9.4.1, A.9.4.4,NIST SP 800-53 Rev. 4 AC-2, AC-3, AC-5, AC-6, AC-16");
  System.out.println();
  System.out.println("5. ISA 62443-2-1:2009 4.3.3.4,ISA 62443-3-3:2013 SR 3.1, SR 3.8,ISO/IEC 27001:2013 A.13.1.1, A.13.1.3, A.13.2.1,NIST SP 800-53 Rev. 4 AC-4, SC-7");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");


 menuSelection = keyboard.nextInt(); 
 } 

break;

case 7:
System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("AWARENESS AND TRAINING:");
  System.out.println();
  System.out.println();
  System.out.println("The Organizations Personnel & Partners Are Provided Cybersecurity Awareness Education & Are Adequately Trained"); 
  System.out.println();
  System.out.println("To Perform Their Information Security-Related Duties & Responsibilities Consistent With Related Policies, Procedures, & Agreements..");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF AWARENESS AND TRAINING SUBCATEGORIES: ");
  System.out.println();
  System.out.println(" 1. All Users Are Informed & Trained");
  System.out.println();
  System.out.println(" 2. Privileged Users Understand Roles & Responsibilities");
  System.out.println();
  System.out.println(" 3. Third-Party Stakeholders (e.g., Suppliers, Customers, Partners) Understand Roles & Responsibilities");
  System.out.println();
  System.out.println(" 4. Senior Executives Understand Roles & Responsibilities ");
  System.out.println();
  System.out.println(" 5. Physical & Information Security Personnel Understand Roles & Responsibilities");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE AWARENESS AND TRAINING ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. CCS CSC 9,COBIT 5 APO07.03, BAI05.07,ISA 62443-2-1:2009 4.3.2.4.2,ISO/IEC 27001:2013 A.7.2.2");
  System.out.println();
  System.out.println("2. CCS CSC 9,COBIT 5 APO07.02, DSS06.03,ISA 62443-2-1:2009 4.3.2.4.2, 4.3.2.4.3,ISO/IEC 27001:2013 A.6.1.1, A.7.2.2,NIST SP 800-53 Rev. 4 AT-3, PM-13");
  System.out.println();
  System.out.println("3. CS CSC 9,COBIT 5 APO07.03, APO10.04, APO10.05,ISA 62443-2-1:2009 4.3.2.4.2,ISO/IEC 27001:2013 A.6.1.1, A.7.2.2,NIST SP 800-53 Rev. 4 PS-7, SA-9");
  System.out.println();
  System.out.println("4. CCS CSC 9,COBIT 5 APO07.03,ISA 62443-2-1:2009 4.3.2.4.2,ISO/IEC 27001:2013 A.6.1.1, A.7.2.2,NIST SP 800-53 Rev. 4 AT-3, PM-13");
  System.out.println();
  System.out.println("5. CCS CSC 9,COBIT 5 APO07.03,ISA 62443-2-1:2009 4.3.2.4.2,ISO/IEC 27001:2013 A.6.1.1, A.7.2.2,NIST SP 800-53 Rev. 4 AT-3, PM-13");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt(); 
 } 

break;

case 8:

 System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("DATA SECURITY:");
  System.out.println();
  System.out.println();
  System.out.println("Information & Records (Data) Are Managed Consistent With The Organizations Risk Strategy"); 
  System.out.println();
  System.out.println("To Protect The Confidentiality, Integrity, & Availability Of Information.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF DATA SECURITY SUBCATEGORIES: ");
  System.out.println();
  System.out.println("1. Data-At-Rest Is Protected");
  System.out.println();
  System.out.println("2. Data-In-Transit Is Protected");
  System.out.println();
  System.out.println("3. Assets Are Formally Managed Throughout Removal, Transfers, & Disposition");
  System.out.println();
  System.out.println("4. Adequate Capacity To Ensure Availability Is Maintained ");
  System.out.println();
  System.out.println("5. Protections Against Data Leaks Are Implemented");
  System.out.println();
  System.out.println("6. Integrity Checking Mechanisms Are Used To Verify Software, Firmware, & Information Integrity");
  System.out.println();
  System.out.println("7. The Development & Testing Environment(s) Are Separate From The Production Environment");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE DATA SECURITY ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. CCS CSC 17,COBIT 5 APO01.06, BAI02.01, BAI06.01, DSS06.06,ISA 62443-3-3:2013 SR 3.4, SR 4.1,ISO/IEC 27001:2013 A.8.2.3,NIST SP 800-53 Rev. 4 SC-28");
  System.out.println();
  System.out.println("2. CCS CSC 17,COBIT 5 APO01.06, DSS06.06,ISA 62443-3-3:2013 SR 3.1, SR 3.8, SR 4.1, SR 4.2,ISO/IEC 27001:2013 A.8.2.3,A.13.1.1, A.13.2.1, A.13.2.3,A.14.1.2,A.14.1.3,NIST SP 800-53 Rev.4 SC-8");
  System.out.println();
  System.out.println("3. COBIT 5 BAI09.03,ISA 62443-2-1:2009 4. 4.3.3.3.9, 4.3.4.4.1,ISA 62443-3-3:2013 SR 4.2,ISO/IEC 27001:2013 A.8.2.3, A.8.3.1, A.8.3.2, A.8.3.3,A.11.2.7,NIST SP 800-53 Rev. 4 CM-8,MP-6,PE-16");
  System.out.println();
  System.out.println("4. COBIT 5 APO13.01,ISA 62443-3-3:2013 SR 7.1, SR 7.2,ISO/IEC 27001:2013 A.12.3.1,NIST SP 800-53 Rev. 4 AU-4, CP-2, SC-5");
  System.out.println();
  System.out.println("5. CCS CSC 17,COBIT 5 APO01.06,ISA 62443-3-3:2013 SR 5.2,ISO/IEC 27001:2013 A.6.1.2, A.7.1.1, A.7.1.2, A.7.3.1, A.8.2.2, A.8.2.3, A.9.1.1, A.9.1.2, A.9.2.3, A.9.4.1, A.9.4.4, A.9.4.5, A.13.1.3,A.13.2.1, A.13.2.3, A.13.2.4,A.14.1.2,A.14.1.3,NIST SP 800-53 Rev.4 AC-4,AC-5,AC-6,PE-19,PS-3,PS-6,SC-7,SC-8,SC-13,SC-31,SI-4");
  System.out.println();
  System.out.println("6. ISA 62443-3-3:2013 SR 3.1, SR 3.3, SR 3.4, SR 3.8,ISO/IEC 27001:2013 A.12.2.1, A.12.5.1, A.14.1.2, A.14.1.3,NIST SP 800-53 Rev. 4 SI-7");
  System.out.println();
  System.out.println("7. COBIT 5 BAI07.04,ISO/IEC 27001:2013 A.12.1.4,NIST SP 800-53 Rev. 4 CM-2.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt(); 
 } 

break;

case 9:

System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("INFORMATION PROTECTION PROCESSES & PROCEDURES:");
  System.out.println();
  System.out.println();
  System.out.println("Security Policies (That Address Purpose, Scope, Roles, Responsibilities, Management Commitment, & Coordination Among Organizational Entities),"); 
  System.out.println();
  System.out.println("Processes & Procedures Are Maintained & Used To Manage Protection Of Information Systems & Assets.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF INFORMATION PROTECTION PROCESSES & PROCEDURES SUBCATEGORIES: ");
  System.out.println();
  System.out.println("1.  A baseline configuration of information technology/industrial control systems is created and maintained.");
  System.out.println();
  System.out.println("2.  A System Development Life Cycle to manage systems is implemented.");
  System.out.println();
  System.out.println("3.  Configuration change control processes are in place.");
  System.out.println();
  System.out.println("4.  Backups of information are conducted, maintained, and tested periodically. ");
  System.out.println();
  System.out.println("5.  Policy and regulations regarding the physical operating environment for organizational assets are met.");
  System.out.println();
  System.out.println("6.  Data is destroyed according to policy.");
  System.out.println();
  System.out.println("7.  Protection processes are continuously improved.");
  System.out.println();
  System.out.println("8.  Effectiveness of protection technologies is shared with appropriate parties.");
  System.out.println();
  System.out.println("9.  Response plans (Incident Response and Business Continuity) and recovery plans (Incident Recovery and Disaster Recovery) are in place and managed. ");
  System.out.println();
  System.out.println("10. Response and recovery plans are tested.");
  System.out.println();
  System.out.println("11. Cybersecurity is included in human resources practices (e.g., deprovisioning, personnel screening).");
  System.out.println();
  System.out.println("12. A vulnerability management plan is developed and implemented.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE INFORMATION PROTECTION PROCESSES & PROCEDURES ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. CCS CSC 3, 10,COBIT 5 BAI10.01, BAI10.02, BAI10.03,BAI10.05,ISA 62443-2-1:2009 4.3.4.3.2, 4.3.4.3.3,ISA 62443-3-3:2013 SR 7.6,ISO/IEC 27001:2013 A.12.1.2, A.12.5.1, A.12.6.2, A.14.2.2, A.14.2.3, A.14.2.4, NIST SP 800-53 Rev. 4 CM-2, CM-3, CM-4, CM-5, CM-6, CM-7, CM-9, SA-10.");
  System.out.println();
  System.out.println("2. COBIT 5 APO13.01,ISA 62443-2-1:2009 4.3.4.3.3,ISO/IEC 27001:2013 A.6.1.5, A.14.1.1, A.14.2.1, A.14.2.5,NIST SP 800-53 Rev. 4 SA-3, SA-4, SA-8, SA-10, SA-11, SA-12, SA-15, SA-17, PL-8.");
  System.out.println();
  System.out.println("3. COBIT 5 BAI06.01,BAI01.06,ISA 62443-2-1:2009 4.3.4.3.2, 4.3.4.3.3,ISA 62443-3-3:2013 SR 7.6,ISO/IEC 27001:2013 A.12.1.2, A.12.5.1, A.12.6.2, A.14.2.2, A.14.2.3, A.14.2.4,NIST SP 800-53 Rev. 4 CM-3, CM-4, SA-10.");
  System.out.println();
  System.out.println("4. COBIT 5 APO13.0,ISA 62443-2-1:2009 4.3.4.3.9,ISA 62443-3-3:2013 SR 7.3, SR 7.4,ISO/IEC 27001:2013 A.12.3.1, A.17.1.2A.17.1.3, A.18.1.3,NIST SP 800-53 Rev. 4 CP-4, CP-6, CP-9.");
  System.out.println();
  System.out.println("5. COBIT 5 DSS01.04, DSS05.05,ISA 62443-2-1:2009 4.3.3.3.1 4.3.3.3.2, 4.3.3.3.3, 4.3.3.3.5, 4.3.3.3.6,ISO/IEC 27001:2013 A.11.1.4, A.11.2.1, A.11.2.2, A.11.2.3,NIST SP 800-53 Rev. 4 PE-10, PE-12, PE-13, PE-14, PE-15, PE-18.");
  System.out.println();
  System.out.println("6. COBIT 5 BAI09.03,ISA 62443-2-1:2009 4.3.4.4.4,ISA 62443-3-3:2013 SR 4.2,ISO/IEC 27001:2013 A.8.2.3, A.8.3.1, A.8.3.2, A.11.2.7,NIST SP 800-53 Rev. 4 MP-6.");
  System.out.println();
  System.out.println("7. COBIT 5 APO11.06, DSS04.05,ISA 62443-2-1:2009 4.4.3.1, 4.4.3.2, 4.4.3.3, 4.4.3.4, 4.4.3.5, 4.4.3.6, 4.4.3.7, 4.4.3.8,NIST SP 800-53 Rev. 4 CA-2, CA-7, CP-2, IR-8, PL-2, PM-6.");
  System.out.println();
  System.out.println("8. ISO/IEC 27001:2013 A.16.1.6,NIST SP 800-53 Rev. 4 AC-21, CA-7, SI-4");
  System.out.println();
  System.out.println("9. COBIT 5 DSS04.03,ISA 62443-2-1:2009 4.3.2.5.3, 4.3.4.5.1,ISO/IEC 27001:2013 A.16.1.1, A.17.1.1, A.17.1.2,NIST SP 800-53 Rev. 4 CP-2, IR-8.");
  System.out.println();
  System.out.println("10. ISA 62443-2-1:2009 4.3.2.5.7, 4.3.4.5.11,ISA 62443-3-3:2013 SR 3.3,ISO/IEC 27001:2013 A.17.1.3,NIST SP 800-53 Rev.4 CP-4, IR-3, PM-14.");
  System.out.println();
  System.out.println("11. COBIT 5 APO07.01, APO07.02, APO07.03, APO07.04, APO07.05,ISA 62443-2-1:2009 4.3.3.2.1, 4.3.3.2.2, 4.3.3.2.3,ISO/IEC 27001:2013 A.7.1.1, A.7.3.1, A.8.1.4,NIST SP 800-53 Rev. 4 PS Family.");
  System.out.println();
  System.out.println("12. ISO/IEC 27001:2013 A.12.6.1, A.18.2.2,NIST SP 800-53 Rev. 4 RA-3, RA-5, SI-2.");
  System.out.println();

  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");



 menuSelection = keyboard.nextInt(); 
 } 

break;

case 10:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS:");
  System.out.println();
  System.out.println();
  System.out.println("Maintenance & Repairs Of Industrial Control & Information System Components Is Performed Consistent With Policies & Procedures."); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS SUBCATEGORIES: ");
  System.out.println();
  System.out.println(" 1. Maintenance and repair of organizational assets is performed and logged in a timely manner, with approved and controlled tools.");
  System.out.println();
  System.out.println(" 2. Remote maintenance of organizational assets is approved, logged, and performed in a manner that prevents unauthorized access.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. COBIT 5 BAI09.03,ISA 62443-2-1:2009 4.3.3.3.7,ISO/IEC 27001:2013 A.11.1.2, A.11.2.4, A.11.2.5,NIST SP 800-53 Rev. 4 MA-2, MA-3, MA-5.");
  System.out.println();
  System.out.println("2. COBIT 5 DSS05.04,ISA 62443-2-1:2009 4.3.3.6.5, 4.3.3.6.6, 4.3.3.6.7, 4.4.4.6.8,ISO/IEC 27001:2013 A.11.2.4, A.15.1.1, A.15.2.1,NIST SP 800-53 Rev. 4 MA-4." );
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 

 menuSelection = keyboard.nextInt(); 
 
 } 
 
break; 

case 11:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("PROTECTIVE TECHNOLOGY:");
  System.out.println();
  System.out.println();
  System.out.println("Technical Security Solutions Are Managed To Ensure The Security & Resilience Of Systems & Assets, Consistent With Related Policies, Procedures, & Agreements."); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF PROTECTIVE TECHNOLOGY SUBCATEGORIES: ");
  System.out.println();
  System.out.println(" 1. Audit/log records are determined, documented, implemented, and reviewed in accordance with policy.");
  System.out.println();
  System.out.println(" 2. Removable media is protected and its use restricted according to policy.");
  System.out.println();
  System.out.println(" 3. Access to systems and assets is controlled, incorporating the principle of least functionality.");
  System.out.println();
  System.out.println(" 4. Communications and control networks are protected.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE PROTECTIVE TECHNOLOGY ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION:");
  System.out.println();
  System.out.println("1. CCS CSC 1,COBIT 5 APO11.04,ISA 62443-2-1:2009 4.3.3.3.9, 4.3.3.5.8, 4.3.4.4.7, 4.4.2.1, 4.4.2.2, 4.4.2.4,ISA 62443-3-3:2013 SR 2.8, SR 2.9, SR 2.10, SR 2.11, SR 2.12,ISO/IEC 27001:2013 A.12.4.1, A.12.4.2, A.12.4.3, A.12.4.4, A.12.7.1,NIST SP 800-53 Rev. 4 AU Family.");
  System.out.println();
  System.out.println("2. COBIT5 DSS05.02, APO13.01,ISA 62443-3-3:2013 SR 2.3,ISO/IEC 27001:2013 A.8.2.2, A.8.2.3, A.8.3.1, A.8.3.3, A.11.2.9,NIST SP 800-53 Rev. 4 MP-2, MP-4, MP-5, MP-7.");
  System.out.println();
  System.out.println("3. COBIT5 DSS05.02,ISA 62443-2-1:2009 4.3.3.5.1, 4.3.3.5.2, 4.3.3.5.3, 4.3.3.5.4, 4.3.3.5.5, 4.3.3.5.6, 4.3.3.5.7, 4.3.3.5.8, 4.3.3.6.1, 4.3.3.6.2, 4.3.3.6.3, 4.3.3.6.4, 4.3.3.6.5, 4.3.3.6.6, 4.3.3.6.7, 4.3.3.6.8, 4.3.3.6.9, 4.3.3.7.1, 4.3.3.7.2, 4.3.3.7.3, 4.3.3.7.4,ISA 62443-3-3:2013 SR 1.1, SR 1.2, SR 1.3, SR 1.4, SR 1.5, SR 1.6, SR 1.7, SR 1.8, SR 1.9, SR 1.10, SR 1.11, SR 1.12, SR 1.13, SR 2.1, SR 2.2, SR 2.3, SR 2.4, SR 2.5, SR 2.6, SR 2.7,ISO/IEC 27001:2013 A.9.1.2,NIST SP 800-53 Rev. 4 AC-3, CM-7.");
  System.out.println();
  System.out.println("4. CCS CSC 7,COBIT 5 DSS05.02, APO13.01,ISA 62443-3-3:2013 SR 3.1, SR 3.5, SR 3.8, SR 4.1, SR 4.3, SR 5.1, SR 5.2, SR 5.3, SR 7.1, SR 7.6,ISO/IEC 27001:2013 A.13.1.1, A.13.2.1,NIST SP 800-53 Rev. 4 AC-4, AC-17, AC-18, CP-8, SC-7.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt(); 
 } 

break;

case 12:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("DETECT ANOMOLIES & EVENTS:");
  System.out.println();
  System.out.println();
  System.out.println("Anomalous Activity Is Detected In A Timely Manner & The Potential Impact Of Events Is Understood."); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF DETECT ANOMOLIES & EVENTS SUBCATEGORIES: ");
  System.out.println();
  System.out.println(" 1. A baseline of network operations and expected data flows for users and systems is established and managed.");
  System.out.println();
  System.out.println(" 2. Detected events are analyzed to understand attack targets and methods.");
  System.out.println();
  System.out.println(" 3. Event data are aggregated and correlated from multiple sources and sensors.");
  System.out.println();
  System.out.println(" 4. Impact of events is determined.");
  System.out.println();
  System.out.println(" 5. Incident alert thresholds are established.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE DETECT ANOMOLIES & EVENTS ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION:");
  System.out.println();
  System.out.println("1. COBIT 5 DSS03.01,ISA 62443-2-1:2009 4.4.3.3,NIST SP 800-53 Rev. 4 AC-4, CA-3, CM-2, SI-4.");
  System.out.println();
  System.out.println("2. ISA 62443-2-1:2009 4.3.4.5.6, 4.3.4.5.7, 4.3.4.5.8,ISA 62443-3-3:2013 SR 2.8, SR 2.9, SR 2.10, SR 2.11, SR 2.12, SR 3.9, SR 6.1, SR 6.2,ISO/IEC 27001:2013 A.16.1.1, A.16.1.4,NIST SP 800-53 Rev. 4 AU-6, CA-7, IR-4, SI-4.");
  System.out.println();
  System.out.println("3. ISA 62443-3-3:2013 SR 6.1,NIST SP 800-53 Rev. 4 AU-6, CA-7, IR-4, IR-5, IR-8, SI-4,DE.AE-4: Impact of events is determined, COBIT 5 APO12.06,NIST SP 800-53 Rev. 4 CP-2, IR-4, RA-3, SI -4.");
  System.out.println();
  System.out.println("4. COBIT 5 APO12.06,NIST SP 800-53 Rev. 4 CP-2, IR-4, RA-3, SI -4.");
  System.out.println();
  System.out.println("5. COBIT 5 APO12.06,ISA 62443-2-1:2009 4.2.3.10,NIST SP 800-53 Rev. 4 IR-4, IR-5, IR-8.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt(); 
 } 

break;

case 13:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("CONTINUOUS SECURITY MONITORING:");
  System.out.println();
  System.out.println();
  System.out.println("The Information System & Assets Are Monitored At Discrete Intervals To Identify Cybersecurity Events & Verify The Effectiveness Of Protective Measures"); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF CONTINUOUS SECURITY MONITORING SUBCATEGORIES: ");
  System.out.println();
  System.out.println("1. The network is monitored to detect potential cybersecurity events.");
  System.out.println();
  System.out.println("2. The physical environment is monitored to detect potential cybersecurity events.");
  System.out.println();
  System.out.println("3. Personnel activity is monitored to detect potential cybersecurity events.");
  System.out.println();
  System.out.println("4. Malicious code is detected.");
  System.out.println();
  System.out.println("5. The network is monitored to detect potential cybersecurity events.");
  System.out.println();
  System.out.println("6. The physical environment is monitored to detect potential cybersecurity events.");
  System.out.println();
  System.out.println("7. Personnel activity is monitored to detect potential cybersecurity events.");
  System.out.println();
  System.out.println("8. Malicious code is detected.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE CONTINUOUS SECURITY MONITORING ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION:");
  System.out.println();
  System.out.println("1. CCS CSC 14, 16,COBIT 5 DSS05.07,ISA 62443-3-3:2013 SR 6.2,NIST SP 800-53 Rev. 4 AC-2, AU-12, CA-7, CM-3, SC-5, SC-7, SI-4.");
  System.out.println();
  System.out.println("2. ISA 62443-2-1:2009 4.3.3.3.8,NIST SP 800-53 Rev. 4 CA-7, PE-3, PE-6, PE-20.");
  System.out.println();
  System.out.println("3. ISA 62443-3-3:2013 SR 6.2,ISO/IEC 27001:2013 A.12.4.1,NIST SP 800-53 Rev. 4 AC-2, AU-12, AU-13, CA-7, CM-10, CM-11.");
  System.out.println();
  System.out.println("4. CCS CSC 5,COBIT 5 DSS05.01,ISA 62443-2-1:2009 4.3.4.3.8,ISA 62443-3-3:2013 SR 3.2,ISO/IEC 27001:2013 A.12.2.1,NIST SP 800-53 Rev. 4 SI-3.");
  System.out.println();
  System.out.println("5. ISA 62443-3-3:2013 SR 2.4,ISO/IEC 27001:2013 A.12.5.1,NIST SP 800-53 Rev. 4 SC-18, SI-4. SC-44.");
  System.out.println();
  System.out.println("6. COBIT 5 APO07.06,ISO/IEC 27001:2013 A.14.2.7, A.15.2.1,NIST SP 800-53 Rev. 4 CA-7, PS-7, SA-4, SA-9, SI-4.");
  System.out.println();
  System.out.println("7. NIST SP 800-53 Rev. 4 AU-12, CA-7, CM-3, CM-8, PE-3, PE-6, PE-20, SI-4." );
  System.out.println();
  System.out.println("8. COBIT 5 BAI03.10,ISA 62443-2-1:2009 4.2.3.1, 4.2.3.7,ISO/IEC 27001:2013 A.12.6.1,NIST SP 800-53 Rev. 4 RA-5.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt(); 
 } 


break;

case 14:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("DETECTION PROCESSES:");
  System.out.println();
  System.out.println();
  System.out.println("Detection Processes & Procedures Are Maintained & Tested To Ensure Timely & Adequate Awareness Of Anomalous Events."); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF DETECTION PROCESSES SUBCATEGORIES: ");
  System.out.println();
  System.out.println("1. Roles and responsibilities for detection are well defined to ensure accountability.");
  System.out.println();
  System.out.println("2. Detection activities comply with all applicable requirements.");
  System.out.println();
  System.out.println("3. Detection processes are tested.");
  System.out.println();
  System.out.println("4. Event detection information is communicated to appropriate parties.");
  System.out.println();
  System.out.println("5. Detection processes are continuously improved.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE DETECTION PROCESSES ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION:");
  System.out.println();
  System.out.println("1. CCS CSC 5,COBIT 5 DSS05.01,ISA 62443-2-1:2009 4.4.3.1,ISO/IEC 27001:2013 A.6.1.1.");
  System.out.println();
  System.out.println("2. ISA 62443-2-1:2009 4.4.3.2,ISO/IEC 27001:2013 A.18.1.4,NIST SP 800-53 Rev. 4 CA-2, CA-7, PM-14, SI-4.");
  System.out.println();
  System.out.println("3. COBIT 5 APO13.02,ISA 62443-2-1:2009 4.4.3.2,ISA 62443-3-3:2013 SR 3.3,ISO/IEC 27001:2013 A.14.2.8,NIST SP 800-53 Rev. 4 CA-2, CA-7, PE-3, PM-14, SI-3, SI-4.");
  System.out.println();
  System.out.println("4.COBIT 5 APO12.06,ISA 62443-2-1:2009 4.3.4.5.9,ISA 62443-3-3:2013 SR 6.1,ISO/IEC 27001:2013 A.16.1.2,NIST SP 800-53 Rev. 4 AU-6, CA-2, CA-7,  RA-5, SI-4.");
  System.out.println();
  System.out.println("5. COBIT 5 APO11.06, DSS04.05,ISA 62443-2-1:2009 4.4.3.4,ISO/IEC 27001:2013 A.16.1.6,NIST SP 800-53 Rev. 4, CA-2, CA-7, PL-2, RA-5, SI-4, PM-14.");
  System.out.println();
    System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");


 menuSelection = keyboard.nextInt(); 
 } 

break;

case 15: 

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("RESPONSE PLANNING:");
  System.out.println();
  System.out.println();
  System.out.println("Response processes and procedures are executed and maintained, to ensure timely response to detected cybersecurity events."); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF RESPONSE PLANNING SUBCATEGORIES: ");
  System.out.println();
  System.out.println("1. Response plan is executed during or after an event.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE RESPONSE PLANNING ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION:");
  System.out.println();
  System.out.println("1. COBIT 5 BAI01.10,CCS CSC 18,ISA 62443-2-1:2009 4.3.4.5.1,ISO/IEC 27001:2013 A.16.1.5, NIST SP 800-53 Rev. 4 CP-2, CP-10, IR-4, IR-8.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: "); 
 
 menuSelection = keyboard.nextInt();
 

   }

 break;

 case 16:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("RESPONSE ANALYSIS:");
  System.out.println();
  System.out.println();
  System.out.println("Analysis Is Conducted To Ensure Adequate Response & Support Recovery Activities."); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF RESPONSE ANALYSIS SUBCATEGORIES: ");
  System.out.println();
  System.out.println("1. Notifications from detection systems are investigated.");
  System.out.println();
  System.out.println("2. The impact of the incident is understood.");
  System.out.println();
  System.out.println("3. Forensics are performed.");
  System.out.println();
  System.out.println("4. Incidents are categorized consistent with response plans.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE RESPONSE ANALYSIS ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. COBIT 5 DSS02.07,ISA 62443-2-1:2009 4.3.4.5.6, 4.3.4.5.7, 4.3.4.5.8,ISA 62443-3-3:2013 SR 6.1,ISO/IEC 27001:2013 A.12.4.1, A.12.4.3, A.16.1.5,NIST SP 800-53 Rev. 4 AU-6, CA-7, IR-4, IR-5, PE-6, SI-4.");
  System.out.println();
  System.out.println("2. ISA 62443-2-1:2009 4.3.4.5.6, 4.3.4.5.7, 4.3.4.5.8,ISO/IEC 27001:2013 A.16.1.6,NIST SP 800-53 Rev. 4 CP-2, IR-4." );
  System.out.println();
  System.out.println("3. ISA 62443-3-3:2013 SR 2.8, SR 2.9, SR 2.10, SR 2.11, SR 2.12, SR 3.9, SR 6.1,ISO/IEC 27001:2013 A.16.1.7,NIST SP 800-53 Rev. 4 AU-7, IR-4." );
  System.out.println();
  System.out.println("4. ISA 62443-2-1:2009 4.3.4.5.6,ISO/IEC 27001:2013 A.16.1.4,NIST SP 800-53 Rev. 4 CP-2, IR-4, IR-5, IR-8.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 
 menuSelection = keyboard.nextInt();

  } 

 break;

 case 17: 

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("MITIGATION ACTIVITIES:");
  System.out.println();
  System.out.println();
  System.out.println("Mitigation Activities Are Performed To Prevent Expansion Of An Event, Mitigate Its Effects & Eradicate The Incident."); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF MITIGATION ACTIVITIES SUBCATEGORIES: ");
  System.out.println();
  System.out.println("1. Incidents are contained.");
  System.out.println();
  System.out.println("2. Incidents are mitigated.");
  System.out.println();
  System.out.println("3. Newly identified vulnerabilities are mitigated or documented as accepted risks.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE MITIGATION ACTIVITIES ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. ISA 62443-2-1:2009 4.3.4.5.6,ISA 62443-3-3:2013 SR 5.1, SR 5.2, SR 5.4,ISO/IEC 27001:2013 A.16.1.5,NIST SP 800-53 Rev. 4 IR-4.");
  System.out.println();
  System.out.println("2. ISA 62443-2-1:2009 4.3.4.5.6, 4.3.4.5.10,ISO/IEC 27001:2013 A.12.2.1, A.16.1.5,NIST SP 800-53 Rev. 4 IR-4." );
  System.out.println();
  System.out.println("3. ISO/IEC 27001:2013 A.12.6.1,NIST SP 800-53 Rev. 4 CA-7, RA-3, RA-5.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 

 menuSelection = keyboard.nextInt(); 
 
 } 
 
break; 

case 18:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("IMPROVING RESPONSE ACTIVITIES:");
  System.out.println();
  System.out.println();
  System.out.println("Organizational Response Activities Are Improved By Incorporating Lessons Learned From Current & Previous Detection/Response Activities."); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF RESPONSE ACTIVITIES SUBCATEGORIES: ");
  System.out.println();
  System.out.println("1. Response Plans Incorporate Lessons Learned.");
  System.out.println();
  System.out.println("2. Response Strategies Are Updated.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE RESPONSE ACTIVITIES ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. COBIT 5 BAI01.13,ISA 62443-2-1:2009 4.3.4.5.10, 4.4.3.4,ISO/IEC 27001:2013 A.16.1.6,NIST SP 800-53 Rev. 4 CP-2, IR-4, IR-8.");
  System.out.println();
  System.out.println("2. NIST SP 800-53 Rev. 4 CP-2, IR-4, IR-8.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt(); 
 } 

break;

case 19:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("RECOVERY PLANNING:");
  System.out.println();
  System.out.println();
  System.out.println("Recovery Processes & Procedures Are Executed & Maintained To Ensure Timely Restoration Of Systems Or Assets Affected By Cybersecurity Events."); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF RECOVERY PLANNING SUBCATEGORIES: ");
  System.out.println();
  System.out.println(" 1. Recovery Plan Is Executed During Or After An Event.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE RECOVERY PLANNING ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. CCS CSC 8,COBIT 5 DSS02.05, DSS03.04,ISO/IEC 27001:2013 A.16.1.5,NIST SP 800-53 Rev. 4 CP-10, IR-4, IR-8.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt(); 
 } 

break;

case 20:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("RECOVERY PLANNING IMPROVEMENTS:");
  System.out.println();
  System.out.println();
  System.out.println("Recovery Planning & Processes Are Improved By Incorporating Lessons Learned Into Future Activities."); 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF RECOVERY PLANNING IMPROVEMENTS SUBCATEGORIES:");
  System.out.println();
  System.out.println(" 1. Recovery Plans Incorporate Lessons Learned.");
  System.out.println();
  System.out.println(" 2. Recovery Strategies Are Updated");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE RECOVERY PLANNING IMPROVEMENTS ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. COBIT 5 BAI05.07,ISA 62443-2-1 4.4.3.4,NIST SP 800-53 Rev. 4 CP-2, IR-4, IR-8");
  System.out.println();
  System.out.println("2. COBIT 5 BAI07.08,NIST SP 800-53 Rev. 4 CP-2, IR-4, IR-8." );
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt(); 
 
 } 

break;

case 21:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("RESTORATION ACTIVITIES COMMUNICATIONS:");
  System.out.println();
  System.out.println();
  System.out.println("Restoration Activities Are Coordinated With Internal & External Parties, Such As Coordinating Centers, ."); 
  System.out.println();
  System.out.println("Service Providers, Owners Of Attacking Systems, Victims, Other CSIRTs, & Vendors.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BELOW IS THE LIST OF RESTORATION ACTIVITIES COMMUNICATIONS SUBCATEGORIES: ");
  System.out.println();
  System.out.println("1. Public Relations Are Managed.");
  System.out.println();
  System.out.println("2. Reputation After An Event Is Repaired.");
  System.out.println();
  System.out.println("3. Recovery Activities Are Communicated To Internal Stakeholders & Executive & Management Teams.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("IMPORTANT REFERENCE DOCUMENTS TO ACHEIVE RESTORATION ACTIVITIES COMMUNICATIONS ARE LISTED BELOW:");
  System.out.println();
  System.out.println("LINKS TO REFERENCE DOCUMENTS LISTED BELOW ARE UNDER CONSTRUCTION: ");
  System.out.println();
  System.out.println("1. COBIT 5 EDM03.02.");
  System.out.println();
  System.out.println("2. COBIT 5 MEA03.02." );
  System.out.println();
  System.out.println("3. NIST SP 800-53 Rev. 4 CP-2, IR-4." );
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" HERE IS THE LIST OF SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
  System.out.println();
  System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
  System.out.println();
  System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
  System.out.println();
  System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
  System.out.println();
  System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
  System.out.println();
  System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
  System.out.println();
  System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
  System.out.println();
  System.out.println("8.  PROTECTION BY DATA SECURITY."); 
  System.out.println();
  System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
  System.out.println();
  System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
  System.out.println();
  System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
  System.out.println();
  System.out.println("12. DETECT ANOMOLIES & EVENTS.");
  System.out.println();
  System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
  System.out.println();
  System.out.println("14. DETECTION PROCESSES.");
  System.out.println();
  System.out.println("15. RESPONSE PLANNING.");
  System.out.println();
  System.out.println("16. RESPONSE ANALYSIS.");
  System.out.println();
  System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
  System.out.println();
  System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
  System.out.println();
  System.out.println("19. RECOVERY PLANNING.");
  System.out.println();
  System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
  System.out.println();
  System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
  System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE CRITICAL INFRASTRUCTURE SECURITY FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");
 
 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 21) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("********** THAT IS  AN INVALID CRITICAL INFRASTRUCTURE FRAMEWORK # SELECTION ********** ");
 System.out.println();
 System.out.println(" HERE IS VALID SECURITY FRAMEWORK CHECKLIST FOR IMPROVING DISA & DoD CRITICAL INFRASTRUCTURE: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1.  IDENTIFY ASSET MANAGEMENT ITEMS."); 
 System.out.println();
 System.out.println("2.  IDENTIFY BUSINESS ENVIRONMENT."); 
 System.out.println();
 System.out.println("3.  IDENTIFY GOVERNANCE POLICIES & PROCEDURES."); 
 System.out.println();
 System.out.println("4.  IDENTIFY RISK ASSESSMENT."); 
 System.out.println();
 System.out.println("5.  IDENTIFY RISK MANAGEMENT STRATEGY."); 
 System.out.println();
 System.out.println("6.  PROTECTION BY ACCESS CONTROL.");
 System.out.println();
 System.out.println("7.  PROTECTION BY AWARENESS AND TRAINING."); 
 System.out.println();
 System.out.println("8.  PROTECTION BY DATA SECURITY."); 
 System.out.println();
 System.out.println("9.  PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES.");
 System.out.println();
 System.out.println("10. PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS.");
 System.out.println();
 System.out.println("11. PROTECTION BY USING PROTECTIVE TECHNOLOGY.");
 System.out.println();
 System.out.println("12. DETECT ANOMOLIES & EVENTS.");
 System.out.println();
 System.out.println("13. DETECTION BY CONTINUOUS SECURITY MONITORING.");
 System.out.println();
 System.out.println("14. DETECTION PROCESSES.");
 System.out.println();
 System.out.println("15. RESPONSE PLANNING.");
 System.out.println();
 System.out.println("16. RESPONSE ANALYSIS.");
 System.out.println();
 System.out.println("17. RESPOND BY MITIGATION ACTIVITIES.");
 System.out.println();
 System.out.println("18  IMPROVING RRESPONSE ACTIVITIES.");
 System.out.println();
 System.out.println("19. RECOVERY PLANNING.");
 System.out.println();
 System.out.println("20. RECOVERY PLANNING IMPROVEMENTS.");
 System.out.println();
 System.out.println("21. RESTORATION ACTIVITIES COMMUNICATIONS.");
 System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER FROM THE FRAMEWORK CHECKLIST # YOU NEED TO KNOW THE DETAILS: ");

  
 menuSelection = keyboard.nextInt(); 
 
 } 

break;

    }
 }
}
//}
