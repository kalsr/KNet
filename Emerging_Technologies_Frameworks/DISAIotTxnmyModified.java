
// Most of the times DISA Security Analysts, Systems & Networks Administrators do not know the exact Taxonomy & Framework of IOT Devices within the Directorate they are supporting.
// DISA MODIFIED IOT Application dispalys IOT Taxonomy & Framework for 21 Directorates within DISA.
// Currently we do not have access to real IoT Taxonomy data so the dummy data values are entered for Taxonomy Fields for each DISA Directorate
// Once real IOT Taxonomy values are obtained than the Data used will be updated with real IOT Taxonomy Data values. 
// This code was written using Object-Oriented programming in Java using JGRASP software 
// This code was written by Mr Randy Singh on 08/10/2017 and updated on 08/30/2017 to include 21 directorates from DISA.

import java.util.Scanner; 

public class DISAIotTxnmyModified 

{

public static void main(String[] args)  

{
 
// Declare a variable to hold the 
// user's menu selection. 

 int menuSelection;

final int MAX_VALUE = 21;
 

//Declare variables to hold the IOT units of measurement.

 
 String InformationType, DeviceType, PlatformType, ProcessorType, 
 NetworkType, InfrastructureType, OperatingSystemType, 
 InterOperabilityType, UsersType, BehavioursType;
 
// *********************Create a Scanner object for keyboard input. 

Scanner keyboard = new Scanner(System.in); 

// ******************Display the menu*******************

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");

// ***********************Prompt the user for a selection****************************** 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER FROM THE LIST ABOVE THE DIRECTORATE CHOICE# (1 - 21) YOU WISH TO SEE THE IOT TAXONOMY: ");
 
 
 menuSelection = keyboard.nextInt();
 
// ***********************Validate the menu selection********************************. 

 while (menuSelection < 1 || menuSelection > 21) 
  
{

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("--THIS IS INVALID DIRECTORATE CHOICE--"); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");

// ***********************Prompt the user for a selection****************************** 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER FROM THE LIST ABOVE THE DIRECTORATE CHOICE# (1 - 21) YOU WISH TO SEE THE IOT TAXONOMY: ");

 //System.out.println();
  
 menuSelection = keyboard.nextInt();
  
 } 
 
 while (menuSelection > 0 || menuSelection <= 21)
 
 
 
 // **************Perform the selected operation*************. 

 
switch(menuSelection) 

{ 

 case 1:
 

   int menuSelect;
   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println( "YOU SELECTED ENGINEERING DIRECTORATE: ");
   System.out.println();
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println("************************************************************************************************" );
   System.out.println( "PLEASE SEE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - ENGINEERING DIRECTORATE (EE)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
   System.out.println();     
               
   InterNetOfThings EE;
   EE = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR EE.");
 System.out.println();
 System.out.println("2.  EE INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  EE DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  EE PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  EE PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  EE NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  EE INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  EE OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  EE INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. EE USERS_TYPES.");
 System.out.println();
 System.out.println("11. EE BEHAVIOURS_TYPES.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
    
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID TAXONOMY CHOICE--     "); 
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SEE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - ENGINEERING DIRECTORATE (EE)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
 
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR EE.");
 System.out.println();
 System.out.println("2.  EE INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  EE DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  EE PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  EE PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  EE NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  EE INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  EE OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  EE INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. EE USERS_TYPES.");
 System.out.println();
 System.out.println("11. EE BEHAVIOURS_TYPES.");
 System.out.println();
 
 System.out.println("************************************************************************************************" );
 System.out.println();

 System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (EE) ENGINEERING DIRECTORATE: ");
         System.out.println("************************************************************************************************" );
         System.out.println();
 
          EE.setInformation           ("Classified & unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          EE.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          EE.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          EE.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          EE.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          EE.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         EE.setOperatingSystem        ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         EE.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         EE.setUser                  ("Stakeholders across the enterprise");
         

         EE.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println              ("EE INFORMATION-TYPES      = " + EE.getInformationType().toUpperCase());
      System.out.println();
      System.out.println();

      System.out.println               ("EE DEVICE_TYPES           = " + EE.getDeviceType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("EE PROCESSOR_TYPES        = " + EE.getProcessorType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("EE NETWORK_TYPES          = " + EE.getNetworkType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("EE INFRASTRUCTURE_TYPES   = " + EE.getInfrastructureType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("EE OPERATING_SYSTEM_TYPES = " + EE.getOperatingSystemType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("EE INTEROPERABILITY_TYPES = " + EE.getInterOperabilityType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("EE USER_TYPES             = " + EE.getUsersType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("EE BEHAVIOUR_TYPES        = " + EE.getBehavioursType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("EE PLATFORM_TYPES         = " + EE.getPlatformType().toUpperCase());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENGINEERING DIRECTORATE SELECTION # 1");
      System.out.println();
      System.out.println("***************************************************************************************************************" );

      System.out.println();
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
        
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR ENGINEERING DIRECTORATE OFFICE: ");
         System.out.println("***********************************************************************************" );

         System.out.println();
  
  // *****************Information Types***************

        EE.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the EE IOT INFORMATION TYPES****************

     

      System.out.println    ("EE INFORMATION-TYPES = " + EE.getInformationType().toUpperCase());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENGINEERING DIRECTORATE SELECTION # 1");
      System.out.println();
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR ENGINEERING DIRECTORATE OFFICE: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      EE.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("EE DEVICE-TYPES = " + EE.getDeviceType().toUpperCase());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENGINEERING DIRECTORATE SELECTION # 1");
      System.out.println("***************************************************************************************************************" );

      System.out.println();
 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
        
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR ENGINEERING DIRECTORATE OFFICE: ");
         
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       EE.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("EE PLATFORM-TYPES = " + EE.getPlatformType().toUpperCase());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENGINEERING DIRECTORATE SELECTION # 1");
      System.out.println("***************************************************************************************************************" );



      }

  else
   
      if ( menuSelect == 5)
      
       {
         
         System.out.println();

         System.out.println("************************************************************************************************" );
         
 
        System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR ENGINEERING DIRECTORATE OFFICE:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      EE.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("EE PROCESSOR-TYPES = " + EE.getProcessorType().toUpperCase());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENGINEERING DIRECTORATE SELECTION # 1");
      System.out.println("***************************************************************************************************************" );
      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println();

          System.out.println("************************************************************************************************" );
          
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR ENGINEERING DIRECTORATE OFFICE: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         EE.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("EE NETWORK-TYPES = " + EE.getNetworkType().toUpperCase());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENGINEERING DIRECTORATE SELECTION # 1");
        System.out.println("***************************************************************************************************************" );



      }

     else
   
        if ( menuSelect == 7)
      
           {
              
             System.out.println();

             System.out.println("************************************************************************************************" );


              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR ENGINEERING DIRECTORATE OFFICE: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          EE.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          System.out.println();
          System.out.println ("EE INFRASTRUCTURE-TYPES = " + EE.getInfrastructureType().toUpperCase());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENGINEERING DIRECTORATE SELECTION # 1");
          System.out.println("***************************************************************************************************************" );
         
          }

          else
   
            if (menuSelect == 8)
      
             {
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR ENGINEERING DIRECTORATE OFFICE:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                EE.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, UCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println();
                System.out.println       ("EE OPERATING-SYSTEM TYPE  = " + EE.getOperatingSystemType().toUpperCase());
                System.out.println();                         
                
                System.out.println();
                System.out.println("***************************************************************************************************************" );
                System.out.println();
                System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENGINEERING DIRECTORATE SELECTION # 1");
                System.out.println();
                System.out.println("***************************************************************************************************************" );

      }

else
   
      if ( menuSelect == 9)
      
       {
           System.out.println();

           System.out.println("************************************************************************************************" );
           
           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR ENGINEERING DIRECTORATE OFFICE: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           EE.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("EE INTEROPERABILITY-TYPES = " + EE.getInterOperabilityType().toUpperCase());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENGINEERING DIRECTORATE SELECTION # 1");
          System.out.println("***************************************************************************************************************" );


      }

else
   
      if (menuSelect == 10)
      
       {
          System.out.println();  
          System.out.println("************************************************************************************************" );
          System.out.print("PLEASE SEE BELOW IoT USERS-TYPES FOR ENGINEERING DIRECTORATE OFFICE: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          EE.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("EE USERS-TYPES = " + EE.getUsersType().toUpperCase());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENGINEERING DIRECTORATE SELECTION # 1");
         System.out.println("***************************************************************************************************************" );

         System.out.println();

 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR ENGINEERING DIRECTORATE OFFICE: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          EE.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("EE BEHAVIOURS-TYPES = " + EE.getBehavioursType().toUpperCase());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENGINEERING DIRECTORATE SELECTION # 1");
          System.out.println("***************************************************************************************************************" );
          System.out.println();


          }
          
          else
   
// ******************Display the Main menu************************************
      
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");

// ***********************Prompt the user for a selection****************************** 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER FROM THE LIST ABOVE THE DIRECTORATE CHOICE# (1 - 21) YOU WISH TO SEE THE IOT TAXONOMY: ");  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println(" --THIS IS INVALID DIRECTORATE CHOICE-- "); 
 System.out.println();
 System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");

// ***********************Prompt the user for a selection****************************** 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER FROM THE LIST ABOVE THE DIRECTORATE CHOICE# (1 - 21) YOU WISH TO SEE THE IOT TAXONOMY: "); 
    
 menuSelection = keyboard.nextInt();
  
}

break;


case 2: 

// int menuSelect;
   System.out.println();
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED JITC DIRECTORATE");
  
   System.out.println();
   System.out.println("PLEASE SEE BELOW IOT TAXONOMY FOR - (JITC)JOINT INTEROPERABILITY TEST COMMAND: ");
   
   System.out.println("************************************************************************************************" );
   System.out.println();
   InterNetOfThings JITC;

//  Following statement creates an object using the InterNetOfThings class as
//  its Blueprint. Centcom will reference the object.

    JITC = new InterNetOfThings();

//*********************************************new code**********************

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR JITC.");
 System.out.println();
 System.out.println("2.  JITC INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  JITC DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  JITC PLATFORMS_TYPES."); 
 System.out.println();
 System.out.println("5.  JITC PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  JITC NETWORK_TYPES."); 
 System.out.println();
 System.out.println("7.  JITC INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  JITC OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  JITC INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. JITC USERS_TYPES.");
 System.out.println();
 System.out.println("11. JITC BEHAVIOURS_Type.");
 
 System.out.println();
 
 
 // ****************PROMPT THE USER FOR IOT MENU SELECTION*******************
 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR IOT TAXONOMY CHOICE # FROM 1 to 11: ");
 
 menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{

 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("-- THIS IS INVALID TAXONOMY CHOICE --"); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();

 System.out.println("ENTER YOUR IOT TAXONOMY MENU SELECTION FROM 1 to 11: ");
 System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR JITC.");
 System.out.println();
 System.out.println("2.  JITC INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  JITC DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  JITC PLATFORMS_TYPES."); 
 System.out.println();
 System.out.println("5.  JITC PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  JITC NETWORK_TYPES."); 
 System.out.println();
 System.out.println("7.  JITC INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  JITC OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  JITC INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. JITC USERS_TYPES.");
 System.out.println();
 System.out.println("11. JITC BEHAVIOURS_Type.");
 
 System.out.println();
 
 
 // ****************PROMPT THE USER FOR IOT MENU SELECTION*******************
 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR IOT TAXONOMY CHOICE # FROM 1 to 11: ");


  menuSelect = keyboard.nextInt();


 }

    if ( menuSelect == 1)
      
       {

       System.out.println();

       System.out.println("************************************************************************************************" );
       
       System.out.println("PLEASE SEE BELOW ENTIRE IOT TAXONOMY FOR - (JITC)JOINT INTEROPERABILITY TEST COMMAND ");
       System.out.println("************************************************************************************************" );

       System.out.println();

 
       JITC.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       JITC.setDevice                ("Sensors, actuators, circuits, controllers, processors, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");

       JITC.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");

       JITC.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");

       JITC.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

       JITC.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");


       JITC.setOperatingSystem       ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


      JITC.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

      JITC.setUser                  ("Stakeholders across the enterprise");

      JITC.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");

     // Display the Centcom IOT taxonomy values stored in the fields

     System.out.println               ("JITC Information type      = " + JITC.getInformationType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("JITC Device type           = " + JITC.getDeviceType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("JITC Processor type        = " + JITC.getProcessorType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("JITC Network type          = " + JITC.getNetworkType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("JITC Infrastructure type   = " + JITC.getInfrastructureType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("JITC OperatingSystem type  = " + JITC.getOperatingSystemType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("JITC InterOperability type = " + JITC.getInterOperabilityType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("JITC Users type            = " + JITC.getUsersType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("JITC Behaviours type       = " + JITC.getBehavioursType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("JITC Platform type         = " + JITC.getPlatformType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println();
     System.out.println("***************************************************************************************************************" );
     System.out.println( "TO SELECT ANOTHER JITC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN JOINT INTEROPERABILITY TEST COMMAND # 2");
     System.out.println("***************************************************************************************************************" );
     System.out.println();
     
     }

     
      else

    
      if ( menuSelect == 2)
    
        {
         System.out.println("***************************************************************************************************************" );
         System.out.println("PLEASE SEE IoT INFORMATION TYPES JITC: ");
         System.out.println();
  
  // *****************Information Types***************

        JITC.setInformation   ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

//**************** Display the EE IOT INFORMATION TYPES****************

      System.out.println    ("JITC INFORMATION TYPE = " + JITC.getInformationType().toUpperCase());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println( "TO SELECT ANOTHER JITC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN JOINT INTEROPERABILITY TEST COMMAND # 2");
      System.out.println("***************************************************************************************************************" );
      System.out.println();
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
        
     System.out.println("***************************************************************************************************************" );  
     System.out.println("PLEASE SEE BELOW IoT DEVICES TYPE FOR JITC: ");
     System.out.println();
     
  
 // *****************Device Types*****************
 
 
     JITC.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
     
     System.out.println   ("JITC DEVICE TYPE = " + JITC.getDeviceType().toUpperCase());
     System.out.println();
     System.out.println("***************************************************************************************************************" );
     System.out.println( "TO SELECT ANOTHER JITC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN JOINT INTEROPERABILITY TEST COMMAND # 2");
     System.out.println("***************************************************************************************************************" );
     System.out.println();
     
             }
   
   else
      
      if ( menuSelect == 4)
      
       {
         System.out.println("***************************************************************************************************************" );
         
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS TYPE JITC: ");
         System.out.println();
         
  // ********************Platform Types*********************
  
 
       JITC.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, other custom platforms");

       System.out.println("JITC PLATFORM TYPE = " + JITC.getPlatformType().toUpperCase());
       System.out.println();
       System.out.println("***************************************************************************************************************" );
       System.out.println( "TO SELECT ANOTHER JITC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN JOINT INTEROPERABILITY TEST COMMAND # 2");
       System.out.println("***************************************************************************************************************" );
       System.out.println();
      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println("***************************************************************************************************************" );
 
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR TYPE FOR JITC:");
         System.out.println();
             

  // ****************Processor Types*******************
  
  
       JITC.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
       System.out.println("JITC PROCESSOR TYPE = " + JITC.getProcessorType().toUpperCase());
       System.out.println();
       System.out.println("***************************************************************************************************************" );
       System.out.println( "TO SELECT ANOTHER JITC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN JOINT INTEROPERABILITY TEST COMMAND # 2");
       System.out.println("***************************************************************************************************************" );
       System.out.println();
      }

    else
   
        if ( menuSelect == 6)
       
       {
         System.out.println("***************************************************************************************************************" );
         System.out.println("PLEASE SEE BELOW IoT NETWORK TYPE FOR JITC: ");
         System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

        JITC.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        System.out.println("JITC NETWORK TYPE = " + JITC.getNetworkType().toUpperCase());
        System.out.println();    
        System.out.println("***************************************************************************************************************" );
        System.out.println( "TO SELECT ANOTHER JITC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN JOINT INTEROPERABILITY TEST COMMAND # 2");
        System.out.println("***************************************************************************************************************" );
        System.out.println();


      }

     else
   
        if ( menuSelect == 7)
      
           {
           System.out.println("***************************************************************************************************************" );
           System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE  TYPE FOR COMPONENT ACQUISITION OFFICE OFFICE: ");
           System.out.println();
 // *************************INFRASTRUCTURE Types*******************
 
 
          JITC.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

           System.out.println ("JITC INFRASTRUCTURE TYPE = " + JITC.getInfrastructureType().toUpperCase());
           System.out.println();
           System.out.println("***************************************************************************************************************" );
           System.out.println( "TO SELECT ANOTHER JITC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN JOINT INTEROPERABILITY TEST COMMAND # 2");
           System.out.println("***************************************************************************************************************" );
           System.out.println();

         
          }

          else
   
            if (menuSelect == 8)
      
             {
             
            System.out.println("***************************************************************************************************************" );
            System.out.println("PLEASE SEE BELOW IoT OPERATING SYSTEM TYPE FOR JITC:");
            System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
           JITC.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
           System.out.println        ("JITC OPERATING-SYSTEM TYPE  = " + JITC.getOperatingSystemType().toUpperCase());
  

         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER JITC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN JOINT INTEROPERABILITY TEST COMMAND # 2");
      

 
         

         
      }

else
   
      if ( menuSelect == 9)
      
       {
         System.out.println("***************************************************************************************************************" );
         System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY TYPE FOR JITC: ");
         System.out.println();

    
         JITC.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         System.out.println            ("JITC InterOperability type = " + JITC.getInterOperabilityType().toUpperCase());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER JITC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN JOINT INTEROPERABILITY TEST COMMAND # 2");
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();

      }

else
   
      if (menuSelect == 10)
      
       {
         System.out.println("***************************************************************************************************************" );
         System.out.print("PLEASE SEE BELOW IoT USERS TYPE FOR JITC: ");
         System.out.println();
 

  // *********************USERS Types*************************
  
  
       JITC.setUser                  ("Stakeholders across the enterprise");
      
      System.out.println          ("JITC USERS TYPE = " + JITC.getUsersType().toUpperCase());

     System.out.println();    
     System.out.println("***************************************************************************************************************" );
     System.out.println( "TO SELECT ANOTHER JITC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN JOINT INTEROPERABILITY TEST COMMAND # 2");
     System.out.println("***************************************************************************************************************" );
     System.out.println(); 
 
      }

     else
   
      if ( menuSelect == 11)
      
       {
        
         System.out.println("***************************************************************************************************************" );
         System.out.println("PLEASE SEE BELOW IoT BEHAVOURS TYPE FOR JITC: ");
         System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
        JITC.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
        System.out.println();

        System.out.println          ("JITC BEHAVIOURS TYPE = " + JITC.getBehavioursType().toUpperCase());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println( "TO SELECT ANOTHER JITC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN JOINT INTEROPERABILITY TEST COMMAND # 2");
        System.out.println("***************************************************************************************************************" );
        System.out.println(); 

      }
      
     else
      
// ******************Display the Main menu************************************
  
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");

// ***********************Prompt the user for a selection****************************** 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER FROM THE LIST ABOVE THE DIRECTORATE CHOICE# (1 - 21) YOU WISH TO SEE THE IOT TAXONOMY: ");  
 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println("-- THIS IS INVALID DIRECTORATE CHOICE --"); 
 System.out.println();
 System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");

// ***********************Prompt the user for a selection****************************** 
 System.out.println();
 System.out.println("************************************************************************************************" );
 //System.out.println();
 System.out.print(" ENTER FROM THE LIST ABOVE THE DIRECTORATE CHOICE# (1 - 21) YOU WISH TO SEE THE IOT TAXONOMY: ");
 menuSelection = keyboard.nextInt();
  
}

break; 

case 3:

  System.out.println(); 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.println("PLEASE SEE BELOW THE IOT TAXONOMY FOR - (ID) CYBER DEVELOPMENT DIRECTORATE: ");
  System.out.println();

  InterNetOfThings ID;

 //  Following statement creates an object using the InterNetOfThings class as
 //its Blueprint. Centcom will reference the object.

  ID = new InterNetOfThings();


//*********************************************new code**********************

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR ID DIRECTORATE.");
 System.out.println();
 System.out.println("2.  ID INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  ID DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  ID PLATFORMS_TYPES."); 
 System.out.println();
 System.out.println("5.  ID PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  ID NETWORK_TYPES."); 
 System.out.println();
 System.out.println("7.  ID INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  ID OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  ID INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. ID USERS_TYPES.");
 System.out.println();
 System.out.println("11. ID BEHAVIOURS_TYPES.");
 
 System.out.println(); 
 
 System.out.println("************************************************************************************************" );
 
 
 // ****************PROMPT THE USER FOR IOT MENU SELECTION*******************
 
 
 System.out.print("ENTER YOUR IOT TAXONOMY MENU SELECTION FROM 1 to 11: ");
 
 
 menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
 System.out.println("************************************************************************************************" );
 
 System.out.println("-- THIS IS INVALID TAXONOMY CHOICE -- "); 
 System.out.println();
 System.out.println("ENTER YOUR VALID IOT TAXONONOMY MENU SELECTION# FROM LIST BELOW: ");
 System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR ID DIRECTORATE.");
 System.out.println();
 System.out.println("2.  ID INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  ID DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  ID PLATFORMS_TYPES."); 
 System.out.println();
 System.out.println("5.  ID PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  ID NETWORK_TYPES."); 
 System.out.println();
 System.out.println("7.  ID INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  ID OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  ID INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. ID USERS_TYPES.");
 System.out.println();
 System.out.println("11. ID BEHAVIOURS_TYPES.");
 
 System.out.println(); 
 
 System.out.println("************************************************************************************************" );
 
 
 // ****************PROMPT THE USER FOR IOT MENU SELECTION*******************
 
 
 System.out.print("ENTER YOUR IOT TAXONOMY MENU SELECTION FROM 1 to 11: ");


 
  menuSelect = keyboard.nextInt();
  
  }

  
     if ( menuSelect == 1)
      
        {

        System.out.println("************************************************************************************************" );
        System.out.println();
        System.out.println("PLEASE SEE BELOW ENTIRE IOT TAXONOMY FOR - (ID)CYBER DEVELOPMENT DIRECTORATE. ");
        System.out.println();

 
        ID.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

        ID.setDevice                ("Sensors, actuators, circuits, controllers, processors, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");

        ID.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");

        ID.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");

        ID.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        ID.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");


        ID.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


        ID.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

        ID.setUser                  ("Stakeholders across the enterprise");

        ID.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
     // Display the Centcom IOT taxonomy values stored in the fields

      System.out.println               ("ID INFORMATION_TYPES      = " + ID.getInformationType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("ID DEVICE_TYPES           = " + ID.getDeviceType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("ID PROCESSOR_TYPES        = " + ID.getProcessorType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("ID NETWORK_TYPES          = " + ID.getNetworkType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("ID INFRASTRUCTURE_TYPES   = " + ID.getInfrastructureType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("ID OPERATING_SYSTEM_TYPES = " + ID.getOperatingSystemType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("ID INTEROPERABILITY_TYPES = " + ID.getInterOperabilityType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("ID USER_TYPES             = " + ID.getUsersType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("ID BEHAVIOUR_TYPES        = " + ID.getBehavioursType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("ID PLATFORM_TYPES         = " + ID.getPlatformType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN ID PLEASE SELECT AGAIN ID DIRECTORATE SELECTION: 3");
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();

       }
     
      else

      if ( menuSelect == 2)
    
        {
          System.out.println("************************************************************************************************" );
          System.out.println();

          System.out.println("PLEASE SEE IoT INFORMATION_TYPES FOR ID - CYBER DEVELOPMENT DIRECTORATE: ");
          System.out.println();

  
  // *****************Information Types***************

        ID.setInformation   ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
 //**************** Display the ID IOT INFORMATION TYPES****************

      System.out.println    ("ID INFORMATION_TYPE = " + ID.getInformationType().toUpperCase());
      System.out.println();
     
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN ID PLEASE SELECT AGAIN ID DIRECTORATE SELECTION: 3");
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();

           

       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
             System.out.println("************************************************************************************************" );
             System.out.println();
             System.out.println("PLEASE SEE BELOW IoT DEVICE-TYPES FOR (ID) CYBER DEVELOPMENT DIRECTORATE: ");
             System.out.println();
             System.out.println();

  
      // *****************Device Types*****************
 
 
       ID.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
     
      System.out.println   ("ID DEVICE TYPE = " + ID.getDeviceType().toUpperCase());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN ID PLEASE SELECT AGAIN ID DIRECTORATE SELECTION: 3");
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();



   }
   
   else
   
      if ( menuSelect == 4)
      
       {
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT PLATFORM_TYPES FOR (ID) CYBER DEVELOPMENT DIRECTORATE: ");
          System.out.println();

         
      // ********************Platform Types*********************
  
 
       ID.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, other custom platforms");
     
      System.out.println("ID PLATFORM TYPE = " + ID.getPlatformType().toUpperCase());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN ID PLEASE SELECT AGAIN ID DIRECTORATE SELECTION: 3");
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();


      
     
      }

  else
   
      if ( menuSelect == 5)
      
       {
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT PROCESSOR_TYPES FOR FOR (ID) CYBER DEVELOPMENT DIRECTORATE: ");
          System.out.println();

              

      // ****************Processor Types*******************
  
  
      ID.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      
      System.out.println("ID PROCESSOR TYPE = " + ID.getProcessorType().toUpperCase());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN ID PLEASE SELECT AGAIN ID DIRECTORATE SELECTION: 3");
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();


      
     
      }

    else
   
        if ( menuSelect == 6)
       
       {
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE BELOW IoT NETWORK TYPE FOR FOR (ID) CYBER DEVELOPMENT DIRECTORATE: ");
           System.out.println();

       // ***************************NETWORK TYPES*************************
 

        ID.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

       System.out.println("ID NETWORK TYPE = " + ID.getNetworkType().toUpperCase());
       System.out.println();
       System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN ID PLEASE SELECT AGAIN ID SELECTION: 3");
       System.out.println();
       System.out.println("************************************************************************************************" );
        
      }

     else
   
        if ( menuSelect == 7)
      
           {  
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE  TYPE FOR FOR (ID) CYBER DEVELOPMENT DIRECTORATE: ");
               System.out.println();


  
          // *************************INFRASTRUCTURE Types*******************
 
 
           ID.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

           System.out.println ("ID INFRASTRUCTURE_TYPES = " + ID.getInfrastructureType().toUpperCase());
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN ID PLEASE SELECT AGAIN ID DIRECTORATE SELECTION: 3");
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println();




         
          }

          else
   
          if (menuSelect == 8)
      
             {
                  System.out.println("************************************************************************************************" );
                  
                  System.out.println("PLEASE SEE BELOW IoT OPERATING SYSTEM TYPE FOR FOR (ID) CYBER DEVELOPMENT DIRECTORATE: ");
                  System.out.println();

                
  
               // ******************************OPERATING SYSTEM Types********************************
 
 
                ID.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("ID OperatingSystem type  = " + ID.getOperatingSystemType().toUpperCase());
  

                System.out.println();
                System.out.println("************************************************************************************************" );
                System.out.println();
                System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN ID PLEASE SELECT AGAIN ID DIRECTORATE SELECTION: 3");
                System.out.println();
                System.out.println("************************************************************************************************" );
                System.out.println();



  
               }

               else
   
              if ( menuSelect == 9)
      
              {
                System.out.println("************************************************************************************************" );
                   
                System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY_TYPES FOR FOR (ID) CYBER DEVELOPMENT DIRECTORATE: ");
                System.out.println();

           // ************************INTEROPERABILITY Types***********************
 
  
         ID.setInterOperability("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         System.out.println    ("ID InterOperability type = " + ID.getInterOperabilityType().toUpperCase());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN ID PLEASE SELECT AGAIN ID DIRECTORATE SELECTION: 3");
         System.out.println("************************************************************************************************" );
         System.out.println();



        }

        else
   
        if (menuSelect == 10)
      
       {
         System.out.println("************************************************************************************************" );
         System.out.print("PLEASE SEE BELOW IoT USER_TYPES FOR FOR (ID) CYBER DEVELOPMENT DIRECTORATE: ");
         System.out.println();


      // *********************USERS Types*************************
  
  
         ID.setUser                  ("Stakeholders across the enterprise");
 
         System.out.println          ("ID USER_TYPES = " + ID.getUsersType().toUpperCase());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN ID PLEASE SELECT AGAIN ID DIRECTORATE SELECTION: 3");
         System.out.println("************************************************************************************************" );
         System.out.println();


  
    
      }

      else
   
      if ( menuSelect == 11)
      
       {
         System.out.println("************************************************************************************************" );
         
         System.out.println("PLEASE SEE BELOW IoT BEHAVOURS_TYPE FOR (ID) CYBER DEVELOPMENT DIRECTORATE: ");
         System.out.println();

    
        // *********************************BEHAVIOURS Types*********************************
 
 
      ID.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
      System.out.println          ("ID BEHAVIOURS_TYPE = " + ID.getBehavioursType().toUpperCase());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN ID PLEASE SELECT AGAIN ID DIRECTORATE SELECTION: 3");
      System.out.println("************************************************************************************************" );
      System.out.println();


      
          }
          
          else
            
   
// ******************Display the Main menu************************************

System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");

// ***********************Prompt the user for a selection****************************** 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER FROM THE LIST ABOVE THE DIRECTORATE CHOICE# (1 - 21) YOU WISH TO SEE THE IOT TAXONOMY: ");  

 
 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 21) 
  
{
  
 System.out.println("-- THIS IS INVALID DIRECTORATE CHOICE --"); 
 System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();

System.out.println("************************************************************************************************" );
System.out.println();

// Prompt the user for a selection 


 System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
 menuSelection = keyboard.nextInt();
  
  }


break;


//************************SERVICE DEVELOPMENT DIRECTORATE*************************************************


case 4:


  System.out.println();
  System.out.println();
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.println("PLEASE SEE BELOW IOT TAXONOMY FOR - (SD)SERVICE DEVELOPMENT DIRECTORATE");
  System.out.println();
  System.out.println("************************************************************************************************" );

  System.out.println();

 InterNetOfThings SD;

 //  Following statement creates an object using the InterNetOfThings class as
 //its Blueprint. Centcom will reference the object.

 SD = new InterNetOfThings();

 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR SD DIRECTORATE.");
 System.out.println();
 System.out.println("2.  SD INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  SD DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  SD PLATFORMS_TYPES.");
 System.out.println(); 
 System.out.println("5.  SD PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  SD NETWORK_TYPES."); 
 System.out.println();
 System.out.println("7.  SD INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  SD OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  SD INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. SD USERS_TYPES.");
 System.out.println();
 System.out.println("11. SD BEHAVIOURS_TYPES.");
 System.out.println();
 
 System.out.println("************************************************************************************************" );
 System.out.println();
 
 // ****************PROMPT THE USER FOR IOT MENU SELECTION*******************
 
 
 System.out.print("ENTER YOUR SD TAXONOMY MENU SELECTION FROM 1 to 11: ");
 
 
 menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("-- THIS IS INVALID SELECTION --");
 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("ENTER VALID SD MENU SELECTION FROM 1 to 10: ");
 System.out.println();
 System.out.println("1. SHOW ENTIRE IOT TAXONOMY FOR ID DIRECTORATE.");
 System.out.println(); 
 System.out.println("2.  SD INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  SD DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  SD PLATFORMS_TYPES."); 
 System.out.println();
 System.out.println("5.  SD PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  SD NETWORK_TYPES."); 
 System.out.println();
 System.out.println("7.  SD INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  SD OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  SD INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. SD USERS_TYPES.");
 System.out.println();
 System.out.println("11. SD BEHAVIOURS_TYPES.");
 System.out.println();
 
 System.out.println("************************************************************************************************" );
System.out.println();
 System.out.print("ENTER YOUR SD MENU SELECTION FROM 1 to 11: ");

 
  menuSelect = keyboard.nextInt();
  
  }

  
     if ( menuSelect == 1)
      
        {
        System.out.println();
        System.out.println("************************************************************************************************" );
        System.out.println();
        System.out.println("PLEASE SEE BELOW ENTIRE IOT TAXONOMY FOR - (SD) SERVICE DEVELOPMENT DIRECTORATE. ");
        System.out.println();
        System.out.println("************************************************************************************************" );
        

        System.out.println();

 
        SD.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

        SD.setDevice                ("Sensors, actuators, circuits, controllers, processors, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");

        SD.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");

        SD.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");

        SD.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        SD.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");


       SD.setOperatingSystem       ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


       SD.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

       SD.setUser                  ("Stakeholders across the enterprise");

       SD.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");

       System.out.println();
      
     // Display the Centcom IOT taxonomy values stored in the fields

     System.out.println               ("SD INFORMATION_TYPES       = " + SD.getInformationType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("SD DEVICE_TYPES            = " + SD.getDeviceType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("SD PROCESSOR_TYPES         = " + SD.getProcessorType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("SD NETWORK_TYPES           = " + SD.getNetworkType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("SD INFRASTRUCTURE_TYPES    = " + SD.getInfrastructureType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("SD OPERATINGSYSTEM_TYPES   = " + SD.getOperatingSystemType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("SD INTEROPERABILITY_TYPES  = " + SD.getInterOperabilityType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("SD USER_TYPES              = " + SD.getUsersType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("SD BEHAVIOUR_TYPES         = " + SD.getBehavioursType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println               ("SD PLATFORM_TYPES          = " + SD.getPlatformType().toUpperCase());
     System.out.println();
     System.out.println();
     System.out.println();
     System.out.println("************************************************************************************************" );
     System.out.println();
     System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN SD PLEASE SELECT AGAIN SD DIRECTORATE SELECTION: 4");
     System.out.println();
     System.out.println("************************************************************************************************" );
      

       }
     
      else

      if ( menuSelect == 2)
    
        {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW SD INFORMATION_TYPES. ");
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();

  
  // *****************Information Types***************

        SD.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, ontologies, Metadata; Big Data, Ambient Data, Analytics for Decision Support, Visualization Algorithms, Distribution Contexts; Lost data from business failure");

       
 //**************** Display the ID IOT INFORMATION TYPES****************

      System.out.println    ("SD INFORMATION_TYPE = " + SD.getInformationType().toUpperCase());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();

      System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN SD PLEASE SELECT AGAIN SD DIRECTORATE SELECTION: 4");
      System.out.println();
      System.out.println("************************************************************************************************" );

       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
             System.out.println();

             System.out.println("************************************************************************************************" );
             System.out.println();

             System.out.println("PLEASE SEE BELOW SD DEVICE_TYPES. ");
             System.out.println();
             System.out.println("************************************************************************************************" );
  
      // *****************Device Types*****************
 
 
       SD.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
     
      System.out.println   ("SD DEVICE_TYPES = " + SD.getDeviceType().toUpperCase());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN SD PLEASE SELECT AGAIN SD DIRECTORATE SELECTION: 4");
      System.out.println();
      System.out.println("************************************************************************************************" );
      

   }
   
   else
   
      if ( menuSelect == 4)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW SD PLATFORM_TYPES. ");
          System.out.println();
          System.out.println("************************************************************************************************" );

          System.out.println();

         
      // ********************Platform Types*********************
  
 
       SD.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, other custom platforms");

       
      System.out.println("SD PLATFORM_TYPES = " + SD.getPlatformType().toUpperCase());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN SD PLEASE SELECT AGAIN SD DIRECTORATE SELECTION: 4");
      System.out.println();
      System.out.println("************************************************************************************************" );

     
      }

  else
   
      if ( menuSelect == 5)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();

          System.out.println("PLEASE SEE BELOW SD PROCESSOR_TYPES. ");
          System.out.println();
          System.out.println("************************************************************************************************" );
              

      // ****************Processor Types*******************
  
  
      SD.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
     
      System.out.println("SD PROCESSOR_TYPES = " + SD.getProcessorType().toUpperCase());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN SD PLEASE SELECT AGAIN SD DIRECTORATE SELECTION: 4");
      System.out.println();
      System.out.println("************************************************************************************************" );
     
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();

          System.out.println("PLEASE SEE BELOW SD NETWORK_TYPES. ");
          System.out.println();
          System.out.println("********************************************************************************************************************************************************************************************************************************************************************************************************************************************************" );

       // ***************************NETWORK TYPES*************************
 

        SD.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        System.out.println("SD NETWORK_TYPES = " + SD.getNetworkType().toUpperCase());
        System.out.println();
        System.out.println("***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN SD PLEASE SELECT AGAIN SD DIRECTORATE SELECTION: 4");
        System.out.println();
        System.out.println("************************************************************************************************" );
      }

     else
   
        if ( menuSelect == 7)
      
           {  
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();

               System.out.println("PLEASE SEE BELOW SD INFRASTRUCTURE_TYPES. ");
               System.out.println();
               System.out.println("************************************************************************************************" );


  
          // *************************INFRASTRUCTURE Types*******************
 
 
           SD.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

           System.out.println ("SD INFRASTRUCTURE_TYPES = " + SD.getInfrastructureType().toUpperCase());
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN SD PLEASE SELECT AGAIN SD DIRECTORATE SELECTION: 4");
           System.out.println();
           System.out.println("************************************************************************************************" );
         
          }

          else
   
          if (menuSelect == 8)
      
             {
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();

                  System.out.println("PLEASE SEE BELOW OPERATING_SYSTEM_TYPES. ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                
  
               // ******************************OPERATING SYSTEM Types********************************
 
 
                SD.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("SD OperatingSystem type  = " + SD.getOperatingSystemType().toUpperCase());
                System.out.println();
                System.out.println("************************************************************************************************" );
                System.out.println();
                System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN SD PLEASE SELECT AGAIN SD DIRECTORATE SELECTION: 4");
  
               }

               else
   
              if ( menuSelect == 9)
      
              {
                System.out.println();
                System.out.println("************************************************************************************************" );
                System.out.println();
                System.out.println("PLEASE SEE BELOW SD INTEROPERABILITY_TYPES. ");
                System.out.println();
                System.out.println("************************************************************************************************" );


           // ************************INTEROPERABILITY Types***********************
 
  
         SD.setInterOperability("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         System.out.println    ("SD INTEROPERABILITY_TYPES = " + SD.getInterOperabilityType().toUpperCase());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN SD PLEASE SELECT AGAIN SD DIRECTORATE SELECTION: 4");
         System.out.println();
         System.out.println("************************************************************************************************" );
        }

        else
   
        if (menuSelect == 10)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         
         System.out.println("PLEASE SEE BELOW SD USER_TYPES. ");
         System.out.println();
        System.out.println("************************************************************************************************" );

      // *********************USERS Types*************************
  
  
         SD.setUser                  ("Stakeholders Across The Enterprise");
 
         System.out.println          ("SD USER_TYPES = " + SD.getUsersType().toUpperCase());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN SD PLEASE SELECT AGAIN SD DIRECTORATE SELECTION: 4");
         System.out.println();
         System.out.println("************************************************************************************************" );    
      }

      else
   
      if ( menuSelect == 11)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW SD BEHAVIOURS_TYPE. ");
         System.out.println();
         System.out.println("************************************************************************************************" );
    
        // *********************************BEHAVIOURS Types*********************************
 
 
      SD.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
      System.out.println          ("SD BEHAVIOURS_TYPE = " + SD.getBehavioursType().toUpperCase());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT TAXONOMY ITEM IN SD PLEASE SELECT AGAIN SD DIRECTORATE SELECTION: 4");
      System.out.println();
      System.out.println("************************************************************************************************" );
         }
          
          else
            
   
// ******************Display the Main menu************************************

System.out.println();
System.out.println("************************************************************************************************" );

System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");

System.out.println();
System.out.println("************************************************************************************************" );

// Prompt the user for a selection 


 System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 

 
 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 21) 
  
{
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println(); 
System.out.println("------------ THIS IS INVALID SELECTION---------- --");
System.out.println(); 
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");

System.out.println("************************************************************************************************" );

// Prompt the user for a selection 


 System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
 menuSelection = keyboard.nextInt();
  
  }

break;



//***********************************FINANCIAL MANAGEMENT TAXONOMY********************************************************************

case 5:

   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println( "YOU SELECTED FINANCIAL MANAGEMENT DIVISION: ");
   System.out.println();
   System.out.println( "PLEASE SEE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - FINANCIAL MANAGEMENT DIVISION (BDF)");
   System.out.println();
   System.out.println("************************************************************************************************"); 
   System.out.println();
InterNetOfThings BDF;

//  Following statement creates an object using the InterNetOfThings class as
//its Blueprint. Centcom will reference the object.

BDF = new InterNetOfThings();

//*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR BDF.");
 System.out.println();
 System.out.println("2.  BDF INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  BDF DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  BDF PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  BDF PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  BDF NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  BDF INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  BDF OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  BDF INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. BDF USERS_TYPES.");
 System.out.println();
 System.out.println("11. BDF BEHAVIOURS_TYPES.");
 System.out.println();
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR TAXONOMY CHOICE # FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     "); 
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SEE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - FINANCIAL MANAGEMENT DIVISION (BDF)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR BDF.");
  System.out.println();
  System.out.println("2.  BDF INFORMATION_TYPES.");
  System.out.println();
  System.out.println("3.  BDF DEVICE_TYPES.");
  System.out.println();
  System.out.println("4.  BDF PLATFORMS_TYPES.");
  System.out.println();
  System.out.println("5.  BDF PROCESSORS_TYPES.");
  System.out.println();
  System.out.println("6.  BDF NETWORK_TYPES.");
  System.out.println();
  System.out.println("7.  BDF INFRASTRUCTURE_TYPES.");
  System.out.println();
  System.out.println("8.  BDF OPERATING_SYSTEM_TYPES.");
  System.out.println();
  System.out.println("9.  BDF INTEROPERABILITY_TYPES.");
  System.out.println();
  System.out.println("10. BDF USERS_TYPES.");
  System.out.println();
  System.out.println("11. BDF BEHAVIOURS_TYPES.");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (BDF) FINANCIAL MANAGEMENT DIVISION: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          BDF.setInformation           ("Classified and Unclassified; Standardized With Wommon Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for Decision Support, Visualization Algorithms, Distribution Contexts; Lost Data from Business Failure");
         
          BDF.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          BDF.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          BDF.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          BDF.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          BDF.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


          BDF.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


          BDF.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

          BDF.setUser                  ("Stakeholders across the enterprise");
         

          BDF.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("BDF INFORMATION-TYPES      = " + BDF.getInformationType().toUpperCase());
      System.out.println();
      System.out.println();

      System.out.println               ("BDF DEVICE_TYPES           = " + BDF.getDeviceType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("BDF PROCESSOR_TYPES        = " + BDF.getProcessorType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("BDF NETWORK_TYPES          = " + BDF.getNetworkType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("BDF INFRASTRUCTURE_TYPES   = " + BDF.getInfrastructureType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("BDF OPERATING_SYSTEM_TYPES = " + BDF.getOperatingSystemType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("BDF INTEROPERABILITY_TYPES = " + BDF.getInterOperabilityType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("BDF USER_TYPES             = " + BDF.getUsersType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("BDF BEHAVIOUR_TYPES        = " + BDF.getBehavioursType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println               ("BDF PLATFORM_TYPES         = " + BDF.getPlatformType().toUpperCase());
      System.out.println();
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDF TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN FINANCIAL MANAGEMENT DIVISION CHOICE # 5");
      System.out.println();
      System.out.println("***************************************************************************************************************" );
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
        
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR FINANCIAL MANAGEMENT DIVISION: ");
         System.out.println();
  
  // *****************Information Types***************

        BDF.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the BDF IOT INFORMATION TYPES****************

     

      System.out.println    ("BDF INFORMATION-TYPES = " + BDF.getInformationType().toUpperCase());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDF TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN FINANCIAL MANAGEMENT DIVISION CHOICE# 5");
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR FINANCIAL MANAGEMENT DIVISION: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      BDF.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("BDF DEVICE-TYPES = " + BDF.getDeviceType().toUpperCase());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDF TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN FINANCIAL MANAGEMENT DIVISION CHOICE # 5");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR FINANCIAL MANAGEMENT DIVISION: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       BDF.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("BDF PLATFORM-TYPES = " + BDF.getPlatformType().toUpperCase());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDF TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN FINANCIAL MANAGEMENT DIVISION CHOICE # 5");
      System.out.println();
      System.out.println("***************************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
        
         System.out.println(); 
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR FINANCIAL MANAGEMENT DIVISION:");
         System.out.println();
             

  // ****************Processor Types*******************
  
  
      BDF.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("BDF PROCESSOR-TYPES = " + BDF.getProcessorType().toUpperCase());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDF TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN FINANCIAL MANAGEMENT DIVISION CHOICE # 5");
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR FINANCIAL MANAGEMENT DIVISION: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         BDF.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("BDF NETWORK-TYPES = " + BDF.getNetworkType().toUpperCase());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER BDF TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN FINANCIAL MANAGEMENT DIVISION CHOICE # 5");
        System.out.println();
        System.out.println("***************************************************************************************************************" );

      }

     else
   
        if ( menuSelect == 7)
      
           {
              
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR FINANCIAL MANAGEMENT DIVISION: ");
               System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          BDF.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("BDF INFRASTRUCTURE-TYPES = " + BDF.getInfrastructureType().toUpperCase());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDF TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN FINANCIAL MANAGEMENT DIVISION CHOICE # 5");
          System.out.println();
          System.out.println("***************************************************************************************************************" );
         
          }

          else
   
            if (menuSelect == 8)
      
             {
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR FINANCIAL MANAGEMENT DIVISION:");
               System.out.println();
               System.out.println("************************************************************************************************" );
  
 // ******************************OPERATING SYSTEM Types********************************
 
 
               BDF.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
               
               System.out.println       ("BDF OperatingSystem type  = " + BDF.getOperatingSystemType().toUpperCase());
  
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER BDF TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN FINANCIAL MANAGEMENT DIVISION CHOICE # 5");
               System.out.println();
               System.out.println("***************************************************************************************************************" );

      }

else
   
      if ( menuSelect == 9)
      
       {
           System.out.println();
           System.out.println("************************************************************************************************" );
           
           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR FINANCIAL MANAGEMENT DIVISION: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           BDF.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("BDF INTEROPERABILITY-TYPES = " + BDF.getInterOperabilityType().toUpperCase());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDF TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN FINANCIAL MANAGEMENT DIVISION CHOICE # 5");
          System.out.println();
          System.out.println("***************************************************************************************************************" );


      }

else
   
      if (menuSelect == 10)
      
       {
      System.out.println();    
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDF TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN FINANCIAL MANAGEMENT DIVISION CHOICE # 5");
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
 

  // *********************USERS Types*************************
  
  
          BDF.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("BDF USERS-TYPES = " + BDF.getUsersType().toUpperCase());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER BDF TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN FINANCIAL MANAGEMENT DIVISION CHOICE # 5");
         System.out.println();
         System.out.println("***************************************************************************************************************" );



 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println(); 
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR FINANCIAL MANAGEMENT DIVISION: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          BDF.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("BDF BEHAVIOURS-TYPES = " + BDF.getBehavioursType().toUpperCase());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDF TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN FINANCIAL MANAGEMENT DIVISION CHOICE # 5");
          System.out.println();
         System.out.println("***************************************************************************************************************" );


          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

    
System.out.println("************************************************************************************************" );
System.out.println();     
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
      System.out.println("************************************************************************************************" );

      // Prompt the user for a selection 


       System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println(" --THIS IS INVALID SELECTION-- "); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("HERE IS THE LIST OF DISA DIRECTORATES WITH IOT TAXONOMY RELATED DEVICES: ");
 System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();
  
 } 


break;

case 6:

   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println( "YOU SELECTED LOGISTICS AND CONTRACT MANAGEMENT DIVISION: ");
   System.out.println();
   System.out.println( "PLEASE SEE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - LOGISTICS AND CONTRACT MANAGEMENT DIVISION (BDL)");
   System.out.println("************************************************************************************************"); 
   
InterNetOfThings BDL;

//  Following statement creates an object using the InterNetOfThings class as
//its Blueprint. Centcom will reference the object.

BDL = new InterNetOfThings();

//*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR BDL.");
 System.out.println();
 System.out.println("2.  BDL INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  BDL DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  BDL PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  BDL PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  BDL NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  BDL INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  BDL OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  BDL INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. BDL USERS_TYPES.");
 System.out.println();
 System.out.println("11. BDL BEHAVIOURS_TYPES.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR TAXONOMY CHOICE # FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     "); 
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SEE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - LOGISTICS AND CONTRACT MANAGEMENT DIVISION (BDL)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR BDL.");
 System.out.println();
 System.out.println("2.  BDL INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  BDL DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  BDL PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  BDL PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  BDL NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  BDL INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  BDL OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  BDL INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. BDL USERS_TYPES.");
 System.out.println();
 System.out.println("11. BDL BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("***************************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          BDL.setInformation           ("Classified and Unclassified; Standardized With Wommon Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for Decision Support, Visualization Algorithms, Distribution Contexts; Lost Data from Business Failure");
         
          BDL.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          BDL.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          BDL.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          BDL.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          BDL.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         BDL.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         BDL.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         BDL.setUser                  ("Stakeholders across the enterprise");
         

         BDL.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("BDL INFORMATION-TYPES      = " + BDL.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("BDL DEVICE_TYPES           = " + BDL.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDL PROCESSOR_TYPES        = " + BDL.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDL NETWORK_TYPES          = " + BDL.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDL INFRASTRUCTURE_TYPES   = " + BDL.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDL OPERATING_SYSTEM_TYPES = " + BDL.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDL INTEROPERABILITY_TYPES = " + BDL.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDL USER_TYPES             = " + BDL.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDL BEHAVIOUR_TYPES        = " + BDL.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDL PLATFORM_TYPES         = " + BDL.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN LOGISTICS AND CONTRACT MANAGEMENT DIVISION CHOICE #6");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR LOGISTICS AND CONTRACT MANAGEMENT DIVISION: ");
         System.out.println();
  
  // *****************Information Types***************

        BDL.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the BDL IOT INFORMATION TYPES****************

     

      System.out.println    ("BDL INFORMATION-TYPES = " + BDL.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDL TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN LOGISTICS AND CONTRACT MANAGEMENT DIVISION CHOICE# 6");
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR LOGISTICS AND CONTRACT MANAGEMENT DIVISION: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      BDL.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("BDL DEVICE-TYPES = " + BDL.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDL TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN LOGISTICS AND LOGICONTRACT MANAGEMENT DIVISION CHOICE #6");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR LOGISTICS AND CONTRACT MANAGEMENT DIVISION: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       BDL.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("BDL PLATFORM-TYPES = " + BDL.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN LOGISTICS AND LOGICONTRACT MANAGEMENT DIVISION CHOICE # 6");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
        System.out.println("************************************************************************************************" );
        System.out.println();
        System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR LOGISTICS AND CONTRACT MANAGEMENT DIVISION:");
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      BDL.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("BDL PROCESSOR-TYPES = " + BDL.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDL TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN LOGISTICS AND LOGICONTRACT MANAGEMENT DIVISION CHOICE #6");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR LOGISTICS AND CONTRACT MANAGEMENT DIVISION: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         BDL.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("BDL NETWORK-TYPES = " + BDL.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN LOGISTICS AND LOGICONTRACT MANAGEMENT DIVISION CHOICE #6");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println("************************************************************************************************" );

              System.out.println();
              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR LOGISTICS AND CONTRACT MANAGEMENT DIVISION: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          BDL.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("BDL INFRASTRUCTURE-TYPES = " + BDL.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN LOGISTICS AND LOGICONTRACT MANAGEMENT DIVISION CHOICE #6");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR LOGISTICS AND CONTRACT MANAGEMENT DIVISION:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                //BDL.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
               //System.out.println       ("BDL OperatingSystem type  = " + EE.getOperatingSystemType());
  
               // System.out.println("************************************************** ");
               System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENIENCE");
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER BDL TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN LOGISTICS AND LOGICONTRACT MANAGEMENT DIVISION CHOICE #6");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR LOGISTICS AND CONTRACT MANAGEMENT DIVISION: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           BDL.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("BDL INTEROPERABILITY-TYPES = " + BDL.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDL TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN LOGISTICS AND LOGICONTRACT MANAGEMENT DIVISION CHOICE #6");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SEE BELOW IoT USERS-TYPES FOR LOGISTICS AND CONTRACT MANAGEMENT DIVISION: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          BDL.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("BDL USERS-TYPES = " + BDL.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER EE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN LOGISTICS AND LOGICONTRACT MANAGEMENT DIVISION CHOICE #6");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR LOGISTICS AND CONTRACT MANAGEMENT DIVISION: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          BDL.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("BDL BEHAVIOURS-TYPES = " + BDL.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDL TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN LOGISTICS AND CONTRACT MANAGEMENT DIVISION CHICE # 5");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

      
System.out.println("************************************************************************************************" );
System.out.println();     
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");

System.out.println("************************************************************************************************" );
System.out.println();

      // Prompt the user for a selection 


       System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println(" --THIS IS INVALID SELECTION-- ");
 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();
  
 } 


break;

case 7:

   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED WORKFORCE MANAGEMENT DIVISION: ");
   System.out.println();
   System.out.println( "PLEASE SBDW BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - WORKFORCE MANAGEMENT DIVISION (BDW)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
        
               
   InterNetOfThings BDW;
   BDW = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR BDW.");
 System.out.println();
 System.out.println("2.  BDW INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  BDW DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  BDW PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  BDW PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  BDW NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  BDW INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  BDW OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  BDW INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. BDW USERS_TYPES.");
 System.out.println();
 System.out.println("11. BDW BEHAVIOURS_TYPES.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
    //System.out.println()
  System.out.println("    --THIS IS INVALID SELECTION--     "); 
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SBDW BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - WORKFORCE MANAGEMENT DIVISION (BDW)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR BDW.");
  System.out.println();
  System.out.println("2.  BDW INFORMATION_TYPES.");
  System.out.println();
  System.out.println("3.  BDW DEVICE_TYPES.");
  System.out.println();
  System.out.println("4.  BDW PLATFORMS_TYPES.");
  System.out.println();
  System.out.println("5.  BDW PROCESSORS_TYPES.");
  System.out.println();
  System.out.println("6.  BDW NETWORK_TYPES.");
  System.out.println();
  System.out.println("7.  BDW INFRASTRUCTURE_TYPES.");
  System.out.println();
  System.out.println("8.  BDW OPERATING_SYSTEM_TYPES.");
  System.out.println();
  System.out.println("9.  BDW INTEROPERABILITY_TYPES.");
  System.out.println();
  System.out.println("10. BDW USERS_TYPES.");
  System.out.println("11. BDW BEHAVIOURS_TYPES.");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SBDW BELOW THE ENTIRE-IOT-TAXONOMY FOR - (BDW) WORKFORCE MANAGEMENT DIVISION: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          BDW.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          BDW.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          BDW.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          BDW.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          BDW.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          BDW.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         BDW.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         BDW.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         BDW.setUser                  ("Stakeholders across the enterprise");
         

         BDW.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("BDW INFORMATION-TYPES      = " + BDW.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("BDW DEVICE_TYPES           = " + BDW.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDW PROCESSOR_TYPES        = " + BDW.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDW NETWORK_TYPES          = " + BDW.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDW INFRASTRUCTURE_TYPES   = " + BDW.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDW OPERATING_SYSTEM_TYPES = " + BDW.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDW INTEROPERABILITY_TYPES = " + BDW.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDW USER_TYPES             = " + BDW.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDW BEHAVIOUR_TYPES        = " + BDW.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDW PLATFORM_TYPES         = " + BDW.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDW TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORKFORCE MANAGEMENT DIVISION CHOICE # 7");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SBDW IoT INFORMATION-TYPES FOR WORKFORCE MANAGEMENT DIVISION OFFICE: ");
         System.out.println();
  
  // *****************Information Types***************

        BDW.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the BDW IOT INFORMATION TYPES****************

     

      System.out.println    ("BDW INFORMATION-TYPES = " + BDW.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDW TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORKFORCE MANAGEMENT DIVISION CHOICE # 7");
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SBDW BELOW IoT DEVICES-TYPES FOR WORKFORCE MANAGEMENT DIVISION OFFICE: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      BDW.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("BDW DEVICE-TYPES = " + BDW.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDW TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORKFORCE MANAGEMENT DIVISION CHOICE # 7");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SBDW BELOW IoT PLATFORMS-TYPES FOR WORKFORCE MANAGEMENT DIVISION OFFICE: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       BDW.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("BDW PLATFORM-TYPES = " + BDW.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDW TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORKFORCE MANAGEMENT DIVISION CHOICE # 7");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
        System.out.println("************************************************************************************************" );
        System.out.println();
 
        System.out.println("PLEASE SBDW BELOW IoT PROCESSOR-TYPES FOR WORKFORCE MANAGEMENT DIVISION OFFICE:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      BDW.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("BDW PROCESSOR-TYPES = " + BDW.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDW TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORKFORCE MANAGEMENT DIVISION CHOICE # 7");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SBDW BELOW IoT NETWORK-TYPES FOR WORKFORCE MANAGEMENT DIVISION OFFICE: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         BDW.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("BDW NETWORK-TYPES = " + BDW.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER BDW TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORKFORCE MANAGEMENT DIVISION CHOICE # 7");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
               System.out.println("************************************************************************************************" );

               System.out.println();
              System.out.println("PLEASE SBDW BELOW IoT INFRASTRUCTURE-TYPES FOR WORKFORCE MANAGEMENT DIVISION OFFICE: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          BDW.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("BDW INFRASTRUCTURE-TYPES = " + BDW.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDW TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORKFORCE MANAGEMENT DIVISION CHOICE # 7");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SBDW BELOW IoT OPERATING-SYSTEM-TYPES FOR WORKFORCE MANAGEMENT DIVISION OFFICE:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                BDW.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("BDW OperatingSystem type  = " + BDW.getOperatingSystemType());
  
               // System.out.println("************************************************** ");
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER BDW TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORKFORCE MANAGEMENT DIVISION CHOICE # 7");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SBDW BELOW IoT INTEROPERABILITY-TYPES FOR WORKFORCE MANAGEMENT DIVISION OFFICE: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           BDW.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("BDW INTEROPERABILITY-TYPES = " + BDW.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDW TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORKFORCE MANAGEMENT DIVISION CHOICE # 7");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SBDW BELOW IoT USERS-TYPES FOR WORKFORCE MANAGEMENT DIVISION OFFICE: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          BDW.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("BDW USERS-TYPES = " + BDW.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER BDW TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORKFORCE MANAGEMENT DIVISION CHOICE # 7");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println("PLEASE SBDW BELOW IoT BEHAVIOURS-TYPES FOR WORKFORCE MANAGEMENT DIVISION OFFICE: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          BDW.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("BDW BEHAVIOURS-TYPES = " + BDW.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDW TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORKFORCE MANAGEMENT DIVISION CHOICE # 7");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

      
System.out.println("************************************************************************************************" );
System.out.println();     
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();

System.out.println("************************************************************************************************" );
System.out.println();
      // Prompt the user for a selection 

 System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println(" --THIS IS INVALID SELECTION-- "); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("HERE IS THE LIST OF DISA DIRECTORATES WITH IOT TAXONOMY RELATED DEVICES: ");
 System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();
  
 } 



break;


case 8:

   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED STRATEGIC COMMAND OFFICE: ");
   System.out.println();
   System.out.println( "PLEASE SBDC BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - STRATEGIC COMMAND OFFICE (BDC)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
        
               
   InterNetOfThings BDC;
   BDC = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR BDC.");
 System.out.println();
 System.out.println("2.  BDC INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  BDC DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  BDC PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  BDC PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  BDC NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  BDC INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  BDC OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  BDC INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. BDC USERS_TYPES.");
 System.out.println();
 System.out.println("11. BDC BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     "); 
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SBDC BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - STRATEGIC COMMAND OFFICE (BDC)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR BDC.");
  System.out.println();
 System.out.println("2.  BDC INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  BDC DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  BDC PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  BDC PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  BDC NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  BDC INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  BDC OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  BDC INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. BDC USERS_TYPES.");
 System.out.println();
 System.out.println("11. BDC BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("***************************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SBDC BELOW THE ENTIRE-IOT-TAXONOMY FOR - (BDC) STRATEGIC COMMAND OFFICE: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          BDC.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          BDC.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          BDC.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          BDC.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          BDC.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          BDC.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


          BDC.setOperatingSystem        ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         BDC.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         BDC.setUser                  ("Stakeholders across the enterprise");
         

         BDC.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("BDC INFORMATION-TYPES      = " + BDC.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("BDC DEVICE_TYPES           = " + BDC.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDC PROCESSOR_TYPES        = " + BDC.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDC NETWORK_TYPES          = " + BDC.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDC INFRASTRUCTURE_TYPES   = " + BDC.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDC OPERATING_SYSTEM_TYPES = " + BDC.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDC INTEROPERABILITY_TYPES = " + BDC.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDC USER_TYPES             = " + BDC.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDC BEHAVIOUR_TYPES        = " + BDC.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDC PLATFORM_TYPES         = " + BDC.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN STRATEGIC COMMAND OFFICE CHOICE # 8");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SBDC IoT INFORMATION-TYPES FOR STRATEGIC COMMAND OFFICE OFFICE: ");
         System.out.println();
  
  // *****************Information Types***************

        BDC.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the BDC IOT INFORMATION TYPES****************

     

      System.out.println    ("BDC INFORMATION-TYPES = " + BDC.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN STRATEGIC COMMAND OFFICE CHOICE # 8");;
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SBDC BELOW IoT DEVICES-TYPES FOR STRATEGIC COMMAND OFFICE OFFICE: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      BDC.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("BDC DEVICE-TYPES = " + BDC.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN STRATEGIC COMMAND OFFICE CHOICE # 8");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SBDC BELOW IoT PLATFORMS-TYPES FOR STRATEGIC COMMAND OFFICE OFFICE: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       BDC.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("BDC PLATFORM-TYPES = " + BDC.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN STRATEGIC COMMAND OFFICE CHOICE # 8");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
         System.out.println("************************************************************************************************" );
         
        System.out.println();
        System.out.println("PLEASE SBDC BELOW IoT PROCESSOR-TYPES FOR STRATEGIC COMMAND OFFICE OFFICE:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      BDC.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("BDC PROCESSOR-TYPES = " + BDC.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN STRATEGIC COMMAND OFFICE CHOICE # 8");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SBDC BELOW IoT NETWORK-TYPES FOR STRATEGIC COMMAND OFFICE OFFICE: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         BDC.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("BDC NETWORK-TYPES = " + BDC.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER BDC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN STRATEGIC COMMAND OFFICE CHOICE # 8");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
               System.out.println("************************************************************************************************" );

              System.out.println();
              System.out.println("PLEASE SBDC BELOW IoT INFRASTRUCTURE-TYPES FOR STRATEGIC COMMAND OFFICE OFFICE: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          BDC.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("BDC INFRASTRUCTURE-TYPES = " + BDC.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN STRATEGIC COMMAND OFFICE CHOICE # 8");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SBDC BELOW IoT OPERATING-SYSTEM-TYPES FOR STRATEGIC COMMAND OFFICE OFFICE:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
               BDC.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
               System.out.println       ("BDC OperatingSystemtype  = " + BDC.getOperatingSystemType());
  
               
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println( "TO SELECT ANOTHER BDC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN STRATEGIC COMMAND OFFICE CHOICE # 8");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SBDC BELOW IoT INTEROPERABILITY-TYPES FOR STRATEGIC COMMAND OFFICE OFFICE: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           BDC.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("BDC INTEROPERABILITY-TYPES = " + BDC.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN STRATEGIC COMMAND OFFICE CHOICE # 8");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SBDC BELOW IoT USERS-TYPES FOR STRATEGIC COMMAND OFFICE OFFICE: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          BDC.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("BDC USERS-TYPES = " + BDC.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER BDC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN STRATEGIC COMMAND OFFICE CHOICE # 8");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SBDC BELOW IoT BEHAVIOURS-TYPES FOR STRATEGIC COMMAND OFFICE OFFICE: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          BDC.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("BDC BEHAVIOURS-TYPES = " + BDC.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN STRATEGIC COMMAND OFFICE CHOICE # 8");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

      
System.out.println("************************************************************************************************" );
System.out.println();    
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();

System.out.println("************************************************************************************************" );
System.out.println();
      // Prompt the user for a selection 


System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println();
 System.out.println(" --THIS IS INVALID SELECTION-- "); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
 System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();
  
 } 



break;


case 9:

   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED MISSION ENGAGEMENT OFFICE: ");
   System.out.println();
   System.out.println( "PLEASE SBDM BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - MISSION PARTNER ENGAGEMENT OFFICE (BDM)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
        
               
   InterNetOfThings BDM;
   BDM = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR BDM.");
 System.out.println();
 System.out.println("2.  BDM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  BDM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  BDM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  BDM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  BDM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  BDM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  BDM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  BDM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. BDM USERS_TYPES.");
 System.out.println();
 System.out.println("11. BDM BEHAVIOURS_TYPES.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     "); 
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SBDM BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - MISSION PARTNER ENGAGEMENT OFFICE (BDM)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR BDM.");
 System.out.println();
 System.out.println("2.  BDM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  BDM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  BDM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  BDM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  BDM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  BDM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  BDM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  BDM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. BDM USERS_TYPES.");
 System.out.println();
 System.out.println("11. BDM BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("***************************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SBDM BELOW THE ENTIRE-IOT-TAXONOMY FOR - (BDM) MISSION ENGAGEMENT OFFICE: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          BDM.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          BDM.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          BDM.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          BDM.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          BDM.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          BDM.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         BDM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         BDM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         BDM.setUser                  ("Stakeholders across the enterprise");
         

         BDM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("BDM INFORMATION-TYPES      = " + BDM.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("BDM DEVICE_TYPES           = " + BDM.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDM PROCESSOR_TYPES        = " + BDM.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDM NETWORK_TYPES          = " + BDM.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDM INFRASTRUCTURE_TYPES   = " + BDM.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDM OPERATING_SYSTEM_TYPES = " + BDM.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDM INTEROPERABILITY_TYPES = " + BDM.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDM USER_TYPES             = " + BDM.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDM BEHAVIOUR_TYPES        = " + BDM.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDM PLATFORM_TYPES         = " + BDM.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDM TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN MISSION PARTNER ENGAGEMENT OFFICE CHOICE # 9");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SBDM IoT INFORMATION-TYPES FOR ENGINBDMRING DIRECTORATE OFFICE: ");
         System.out.println();
  
  // *****************Information Types***************

        BDM.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the BDM IOT INFORMATION TYPES****************

     

      System.out.println    ("BDM INFORMATION-TYPES = " + BDM.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDM TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN MISSION PARTNER ENGAGEMENT OFFICE CHOICE # 9");
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SBDM BELOW IoT DEVICES-TYPES FOR MISSION ENGAGEMENT OFFICE: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      BDM.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("BDM DEVICE-TYPES = " + BDM.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDM TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN MISSION PARTNER ENGAGEMENT OFFICE CHOICE # 9");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SBDM BELOW IoT PLATFORMS-TYPES FOR MISSION ENGAGEMENT OFFICE: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       BDM.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("BDM PLATFORM-TYPES = " + BDM.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDM TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN MISSION PARTNER ENGAGEMENT OFFICE CHOICE # 9");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
 
        System.out.println("PLEASE SBDM BELOW IoT PROCESSOR-TYPES FOR MISSION ENGAGEMENT OFFICE:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      BDM.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("BDM PROCESSOR-TYPES = " + BDM.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDM TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN MISSION PARTNER ENGAGEMENT OFFICE  CHOICE # 9");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SBDM BELOW IoT NETWORK-TYPES FOR MISSION ENGAGEMENT OFFICE: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         BDM.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("BDM NETWORK-TYPES = " + BDM.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER BDM TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN MISSION PARTNER ENGAGEMENT OFFICE CHOICE # 9");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SBDM BELOW IoT INFRASTRUCTURE-TYPES FOR MISSION ENGAGEMENT OFFICE: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          BDM.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("BDM INFRASTRUCTURE-TYPES = " + BDM.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDM TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENGINBDMRING DIRECTORATE  CHOICE # 9");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SBDM BELOW IoT OPERATING-SYSTEM-TYPES FOR MISSION ENGAGEMENT OFFICE:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                BDM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("BDM OperatingSystem type  = " + BDM.getOperatingSystemType());
  
               
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER BDM TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN MISSION PARTNER ENGAGEMENT OFFICE CHOICE # 9");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SBDM BELOW IoT INTEROPERABILITY-TYPES FOR MISSION ENGAGEMENT OFFICE: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           BDM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("BDM INTEROPERABILITY-TYPES = " + BDM.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDM TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN MISSION PARTNER ENGAGEMENT OFFICE  CHOICE # 9");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SBDM BELOW IoT USERS-TYPES FOR MISSION ENGAGEMENT OFFICE: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          BDM.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("BDM USERS-TYPES = " + BDM.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER BDM TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN MISSION PARTNER ENGAGEMENT OFFICE CHOICE # 9");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SBDM BELOW IoT BEHAVIOURS-TYPES FOR MISSION ENGAGEMENT OFFICE: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          BDM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("BDM BEHAVIOURS-TYPES = " + BDM.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDM TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN MISSION PARTNER ENGAGEMENT OFFICE  CHOICE # 9");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

      
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
      System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();

System.out.println("************************************************************************************************" );
System.out.println();

      // Prompt the user for a selection 


System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println(" --THIS IS INVALID SELECTION-- ");
 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
 System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();
   
 } 


 case 10:
 
 System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED REQUIREMENTS AND ANALYSIS OFFICE: ");
   System.out.println();
   System.out.println();
   System.out.println( "PLEASE SEE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - REQUIREMENTS AND ANALYSIS OFFICE(BDA)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
        
               
   InterNetOfThings BDA;
   BDA = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR BDA.");
 System.out.println();
 System.out.println("2.  BDA INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  BDA DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  BDA PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  BDA PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  BDA NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  BDA INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  BDA OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  BDA INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. BDA USERS_TYPES.");
 System.out.println();
 System.out.println("11. BDA BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     "); 
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SEE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - REQUIREMENTS AND ANALYSIS OFFICE (BDA)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR BDA.");
  System.out.println();
  System.out.println("2.  IOT INFORMATION_TYPES.");
  System.out.println();
  System.out.println("3.  IOT DEVICE_TYPES.");
  System.out.println();
  System.out.println("4.  IOT PLATFORMS_TYPES.");
  System.out.println();
  System.out.println("5.  IOT PROCESSORS_TYPES.");
  System.out.println();
  System.out.println("6.  IOT NETWORK_TYPES.");
  System.out.println();
  System.out.println("7.  IOT INFRASTRUCTURE_TYPES.");
  System.out.println();
  System.out.println("8.  IOT OPERATING_SYSTEM_TYPES.");
  System.out.println();
  System.out.println("9.  IOT INTEROPERABILITY_TYPES.");
  System.out.println();
  System.out.println("10. IOT USERS_TYPES.");
  System.out.println();
  System.out.println("11. IOT BEHAVIOURS_TYPES.");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (BDA) REQUIREMENTS AND ANALYSIS OFFICE: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          BDA.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          BDA.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          BDA.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          BDA.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          BDA.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          BDA.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         BDA.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         BDA.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         BDA.setUser                  ("Stakeholders across the enterprise");
         

         BDA.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("BDA INFORMATION-TYPES      = " + BDA.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("BDA DEVICE_TYPES           = " + BDA.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDA PROCESSOR_TYPES        = " + BDA.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDA NETWORK_TYPES          = " + BDA.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDA INFRASTRUCTURE_TYPES   = " + BDA.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDA OPERATING_SYSTEM_TYPES = " + BDA.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDA INTEROPERABILITY_TYPES = " + BDA.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDA USER_TYPES             = " + BDA.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDA BEHAVIOUR_TYPES        = " + BDA.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("BDA PLATFORM_TYPES         = " + BDA.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN REQUIREMENTS AND ANALYSIS OFFICE CHOICE # 10");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR REQUIREMENTS AND ANALYSIS OFFICE: ");
         System.out.println();
  
  // *****************Information Types***************

        BDA.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the BDA IOT INFORMATION TYPES****************

     

      System.out.println    ("BDA INFORMATION-TYPES = " + BDA.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN REQUIREMENTS AND ANALYSIS OFFICE CHOICE # 10");;
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR REQUIREMENTS AND ANALYSIS OFFICE: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      BDA.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("BDA DEVICE-TYPES = " + BDA.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN REQUIREMENTS AND ANALYSIS OFFICE CHOICE # 10");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR REQUIREMENTS AND ANALYSIS OFFICE: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       BDA.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("BDA PLATFORM-TYPES = " + BDA.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN REQUIREMENTS AND ANALYSIS OFFICE CHOICE # 10");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
 
        System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR REQUIREMENTS AND ANALYSIS OFFICE:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      BDA.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("BDA PROCESSOR-TYPES = " + BDA.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER BDA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN REQUIREMENTS AND ANALYSIS OFFICE CHOICE # 10");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR REQUIREMENTS AND ANALYSIS OFFICE OFFICE: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         BDA.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("BDA NETWORK-TYPES = " + BDA.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER BDA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN REQUIREMENTS AND ANALYSIS OFFICE CHOICE # 10");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR REQUIREMENTS AND ANALYSIS OFFICE: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          BDA.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("BDA INFRASTRUCTURE-TYPES = " + BDA.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN REQUIREMENTS AND ANALYSIS OFFICE CHOICE # 10");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR REQUIREMENTS AND ANALYSIS OFFICE:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                BDA.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("BDA OperatingSystem type  = " + BDA.getOperatingSystemType());
  
               
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER BDA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN REQUIREMENTS AND ANALYSIS OFFICE CHOICE # 10");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR REQUIREMENTS AND ANALYSIS OFFICE: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           BDA.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("BDA INTEROPERABILITY-TYPES = " + BDA.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN REQUIREMENTS AND ANALYSIS OFFICE CHOICE # 10");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SEE BELOW IoT USERS-TYPES FOR REQUIREMENTS AND ANALYSIS OFFICE: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          BDA.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("BDA USERS-TYPES = " + BDA.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER BDA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN REQUIREMENTS AND ANALYSIS OFFICE CHOICE # 10");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR REQUIREMENTS AND ANALYSIS OFFICE: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          BDA.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("BDA BEHAVIOURS-TYPES = " + BDA.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER BDA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN REQUIREMENTS AND ANALYSIS OFFICE CHOICE # 10");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

System.out.println("************************************************************************************************" );
System.out.println();     
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");


      System.out.println("************************************************************************************************" );

      // Prompt the user for a selection 


       System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println(" --THIS IS INVALID SELECTION-- "); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
 System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");

System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();
  
 } 

break;

 

case 11: 
 
   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED COMPONENT ACQUISITION OFFICE: ");
   System.out.println();
   System.out.println( "PLEASE SEE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - COMPONENT ACQUISITION OFFICE (CAE)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
   System.out.println();    
               
   InterNetOfThings CAE;
   CAE = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR CAE.");
 System.out.println();
 System.out.println("2.  CAE INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  CAE DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  CAE PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  CAE PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  CAE NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  CAE INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  CAE OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  CAE INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. CAE USERS_TYPES.");
 System.out.println();
 System.out.println("11. CAE BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     ");
  System.out.println(); 
 
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SEE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - COMPONENT ACQUISITION OFFICE (CAE)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR CAE.");
 System.out.println();
 System.out.println("2.  CAE INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  CAE DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  CAE PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  CAE PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  CAE NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  CAE INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  CAE OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  CAE INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. CAE USERS_TYPES.");
 System.out.println();
 System.out.println("11. CAE BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("***************************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (CAE) COMPONENT ACQUISITION OFFICE: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          CAE.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          CAE.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          CAE.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          CAE.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          CAE.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          CAE.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         CAE.setOperatingSystem        ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         CAE.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         CAE.setUser                  ("Stakeholders across the enterprise");
         

         CAE.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("CAE INFORMATION-TYPES      = " + CAE.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("CAE DEVICE_TYPES           = " + CAE.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("CAE PROCESSOR_TYPES        = " + CAE.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("CAE NETWORK_TYPES          = " + CAE.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("CAE INFRASTRUCTURE_TYPES   = " + CAE.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("CAE OPERATING_SYSTEM_TYPES = " + CAE.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("CAE INTEROPERABILITY_TYPES = " + CAE.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("CAE USER_TYPES             = " + CAE.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("CAE BEHAVIOUR_TYPES        = " + CAE.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("CAE PLATFORM_TYPES         = " + CAE.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER CAE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN COMPONENT ACQUISITION OFFICE CHOICE # 11");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR COMPONENT ACQUISITION OFFICE: ");
         System.out.println();
  
  // *****************Information Types***************

        CAE.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the CAE IOT INFORMATION TYPES****************

     

      System.out.println    ("CAE INFORMATION-TYPES = " + CAE.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER CAE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN COMPONENT ACQUISITION OFFICE CHOICE # 11");
            
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR COMPONENT ACQUISITION OFFICE: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      CAE.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("CAE DEVICE-TYPES = " + CAE.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER CAE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN COMPONENT ACQUISITION OFFICE CHOICE # 11");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR COMPONENT ACQUISITION OFFICE: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       CAE.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("CAE PLATFORM-TYPES = " + CAE.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER CAE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN COMPONENT ACQUISITION OFFICE CHOICE # 11");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
        System.out.println("************************************************************************************************" );
        System.out.println();
 
        System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR COMPONENT ACQUISITION OFFICE:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      CAE.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("CAE PROCESSOR-TYPES = " + CAE.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER CAE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN COMPONENT ACQUISITION OFFICE CHOICE # 11");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR COMPONENT ACQUISITION OFFICE: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         CAE.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("CAE NETWORK-TYPES = " + CAE.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER CAE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN COMPONENT ACQUISITION OFFICE CHOICE # 11");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR COMPONENT ACQUISITION OFFICE: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          CAE.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("CAE INFRASTRUCTURE-TYPES = " + CAE.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER CAE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN COMPONENT ACQUISITION OFFICE CHOICE # 11");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR COMPONENT ACQUISITION OFFICE CHOICE # 11");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                CAE.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("CAE OperatingSystem type  = " + CAE.getOperatingSystemType());
  
               // System.out.println("************************************************** ");
               // System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENIENCE");
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER CAE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN COMPONENT ACQUISITION OFFICE CHOICE # 11");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR COMPONENT ACQUISITION OFFICE: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           CAE.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("CAE INTEROPERABILITY-TYPES = " + CAE.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println( "TO SELECT ANOTHER CAE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN COMPONENT ACQUISITION OFFICE CHOICE # 11");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SEE BELOW IoT USERS-TYPES FOR COMPONENT ACQUISITION OFFICE: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          CAE.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("CAE USERS-TYPES = " + CAE.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER CAE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN COMPONENT ACQUISITION OFFICE CHOICE # 11");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR COMPONENT ACQUISITION OFFICE: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          CAE.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("CAE BEHAVIOURS-TYPES = " + CAE.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER CAE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN COMPONENT ACQUISITION OFFICE CHOICE # 11");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

      
System.out.println("************************************************************************************************" );
System.out.println();    
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();

System.out.println("************************************************************************************************" );
System.out.println();
      // Prompt the user for a selection 


System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println(" --THIS IS INVALID SELECTION-- "); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
 System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();
   
 } 


break; 

//************************************CHIEF TECHNOLOGY OFFICE (CTO)****************************************


case 12:

   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED CHIEF TECHNOLOGY OFFICE: ");
   System.out.println();
   System.out.println( "PLEASE SEE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - CHIEF TECHNOLOGY OFFICE (CTO)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
   System.out.println();     
               
   InterNetOfThings CTO;
   CTO = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR CTO.");
 System.out.println();
 System.out.println("2.  CTO INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  CTO DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  CTO PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  CTO PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  CTO NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  CTO INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  CTO OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  CTO INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. CTO USERS_TYPES.");
 System.out.println();
 System.out.println("11. CTO BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     "); 
  System.out.println();
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SEE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - CHIEF TECHNOLOGY OFFICE(CTO)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR CTO.");
  System.out.println();
  System.out.println("2.  CTO INFORMATION_TYPES.");
  System.out.println();
  System.out.println("3.  CTO DEVICE_TYPES.");
  System.out.println();
  System.out.println("4.  CTO PLATFORMS_TYPES.");
  System.out.println();
  System.out.println("5.  CTO PROCESSORS_TYPES.");
  System.out.println();
  System.out.println("6.  CTO NETWORK_TYPES.");
  System.out.println();
  System.out.println("7.  CTO INFRASTRUCTURE_TYPES.");
  System.out.println();
  System.out.println("8.  CTO OPERATING_SYSTEM_TYPES.");
  System.out.println();
  System.out.println("9.  CTO INTEROPERABILITY_TYPES.");
  System.out.println();
  System.out.println("10. CTO USERS_TYPES.");
  System.out.println();
  System.out.println("11. CTO BEHAVIOURS_TYPES.");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (CTO) CHIEF TECHNOLOGY OFFICE: ");
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
 
          CTO.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          CTO.setDevice                ("Blackberries,Smart Phones, Sensors, Actuators, Circuits, Controllers, Processors, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          
          CTO.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          
          CTO.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          
          CTO.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          
          CTO.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          
         CTO.setOperatingSystem        ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");

         CTO.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         
         CTO.setUser                  ("Stakeholders across the enterprise");
       
         CTO.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
       System.out.println             ("CTO INFORMATION-TYPES      = " + CTO.getInformationType());
       System.out.println();
       System.out.println();

       System.out.println               ("CTO DEVICE_TYPES           = " + CTO.getDeviceType());
       System.out.println();
       System.out.println();
       System.out.println               ("CTO PROCESSOR_TYPES        = " + CTO.getProcessorType());
       System.out.println();
       System.out.println();
       System.out.println               ("CTO NETWORK_TYPES          = " + CTO.getNetworkType());
       System.out.println();
       System.out.println();
       System.out.println               ("CTO INFRASTRUCTURE_TYPES   = " + CTO.getInfrastructureType());
       System.out.println();
       System.out.println();
       System.out.println               ("CTO OPERATING_SYSTEM_TYPES = " + CTO.getOperatingSystemType());
       System.out.println();
       System.out.println();
       System.out.println               ("CTO INTEROPERABILITY_TYPES = " + CTO.getInterOperabilityType());
       System.out.println();
       System.out.println();
       System.out.println               ("CTO USER_TYPES             = " + CTO.getUsersType());
       System.out.println();
       System.out.println();
       System.out.println               ("CTO BEHAVIOUR_TYPES        = " + CTO.getBehavioursType());
       System.out.println();
       System.out.println();
       System.out.println               ("CTO PLATFORM_TYPES         = " + CTO.getPlatformType());
       System.out.println();
       System.out.println("***************************************************************************************************************" );
       System.out.println();
      System.out.println( "TO SELECT ANOTHER CTO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN CHIEF TECHNOLOGY OFFICE CHOICE # 12");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR CHIEF TECHNOLOGY OFFICE: ");
         System.out.println();
  
  // *****************Information Types***************

        CTO.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the CTO IOT INFORMATION TYPES****************

     

      System.out.println    ("CTO INFORMATION-TYPES = " + CTO.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println( "TO SELECT ANOTHER CTO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN CHIEF TECHNOLOGY OFFICE CHOICE # 12");
      System.out.println();
      System.out.println("************************************************************************************************" );     
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR CHIEF TECHNOLOGY OFFICE: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      CTO.setDevice        ("BLACKBERRIES, SMART PHONES, SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS,  COMPUTERS, TABLETS, WEARABLES, ROUTERS, DRONES, THERMOSTATS, REFRIGERATORS, LIGHT-BULBS, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("CTO DEVICE-TYPES = " + CTO.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER CTO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN CHIEF TECHNOLOGY OFFICE CHOICE # 12");
      System.out.println();
      System.out.println("***************************************************************************************************************" );
 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR CHIEF TECHNOLOGY OFFICE: ");
         System.out.println();
         System.out.println("***********************************************************************************" );


  // ********************Platform Types*********************
  
 
       CTO.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("CTO PLATFORM-TYPES = " + CTO.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER CTO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN CHIEF TECHNOLOGY OFFICE CHOICE # 12");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR CHIEF TECHNOLOGY OFFICE:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      CTO.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("CTO PROCESSOR-TYPES = " + CTO.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER CTO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN CHIEF TECHNOLOGY OFFICE CHOICE # 12");
      System.out.println();
      System.out.println("***********************************************************************************" );
      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR CHIEF TECHNOLOGY OFFICE: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         CTO.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("CTO NETWORK-TYPES = " + CTO.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER CTO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN CHIEF TECHNOLOGY OFFICE CHOICE # 12");
        System.out.println();
         System.out.println("***********************************************************************************" );

      }

     else
   
        if ( menuSelect == 7)
      
           {
              System.out.println();
              System.out.println("************************************************************************************************" );
              System.out.println();
              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR CHIEF TECHNOLOGY OFFICE: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          CTO.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("CTO INFRASTRUCTURE-TYPES = " + CTO.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println( "TO SELECT ANOTHER CTO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN CHIEF TECHNOLOGY OFFICE CHOICE # 12");
          System.out.println();
         System.out.println("***********************************************************************************" );
         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR CHIEF TECHNOLOGY OFFICE CHOICE # 12");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
               CTO.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
               System.out.println        ("CTO OPERATING-SYSTEM TYPE  = " + CTO.getOperatingSystemType());
  
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER CTO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN CHIEF TECHNOLOGY OFFICE CHOICE # 12");
               System.out.println();
               System.out.println("***********************************************************************************" );

      }

else
   
      if ( menuSelect == 9)
      
       {
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR CHIEF TECHNOLOGY OFFICE: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           CTO.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("CTO INTEROPERABILITY-TYPES = " + CTO.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER CTO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN CHIEF TECHNOLOGY OFFICE CHOICE # 12");
          System.out.println();
          System.out.println("***********************************************************************************" );

      }

else
   
      if (menuSelect == 10)
      
       {
          System.out.println(); 
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SEE BELOW IoT USERS-TYPES FOR CHIEF TECHNOLOGY OFFICE: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          CTO.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("CTO USERS-TYPES = " + CTO.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER CTO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN CHIEF TECHNOLOGY OFFICE CHOICE # 12");
         System.out.println();
         System.out.println("***********************************************************************************" );

 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR CHIEF TECHNOLOGY OFFICE: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          CTO.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("CTO BEHAVIOURS-TYPES = " + CTO.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER CTO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN CHIEF TECHNOLOGY OFFICE CHOICE # 12");
          System.out.println();
          System.out.println("***********************************************************************************" );
          System.out.println();

          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

      
System.out.println("************************************************************************************************" );
System.out.println();      
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES WITH IOT TAXONOMY RELATED DEVICES: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

      // Prompt the user for a selection 

System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println(" --THIS IS INVALID SELECTION-- ");
 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
 System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();  
 } 


break;

case 13:

   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED DEFENSE SPECTRUM ORGANIZATION: ");
   System.out.println();
   System.out.println( "PLEASE SEE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - DEFENSE SPECTRUM ORGANIZATION (DSO)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
        
               
   InterNetOfThings DSO;
   DSO = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR DSO.");
 System.out.println();
 System.out.println("2.  DSO INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  DSO DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  DSO PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  DSO PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  DSO NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  DSO INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  DSO OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  DSO INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. DSO USERS_TYPES.");
 System.out.println();
 System.out.println("11. DSO BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     "); 
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SEE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - DEFENSE SPECTRUM ORGANIZATION (DSO)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR DSO.");
 System.out.println();
 System.out.println("2.  DSO INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  DSO DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  DSO PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  DSO PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  DSO NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  DSO INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  DSO OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  DSO INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. DSO USERS_TYPES.");
 System.out.println();
 System.out.println("11. DSO BEHAVIOURS_TYPES.");
 System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (DSO) DEFENSE SPECTRUM ORGANIZATION: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          DSO.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          DSO.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          DSO.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          DSO.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          DSO.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          DSO.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         DSO.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         DSO.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         DSO.setUser                  ("Stakeholders across the enterprise");
         

         DSO.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("DSO INFORMATION-TYPES      = " + DSO.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("DSO DEVICE_TYPES           = " + DSO.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("DSO PROCESSOR_TYPES        = " + DSO.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("DSO NETWORK_TYPES          = " + DSO.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("DSO INFRASTRUCTURE_TYPES   = " + DSO.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("DSO OPERATING_SYSTEM_TYPES = " + DSO.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("DSO INTEROPERABILITY_TYPES = " + DSO.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("DSO USER_TYPES             = " + DSO.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("DSO BEHAVIOUR_TYPES        = " + DSO.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("DSO PLATFORM_TYPES         = " + DSO.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER DSO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE SPECTRUM ORGANIZATION CHOICE # 13");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR DEFENSE SPECTRUM ORGANIZATION: ");
         System.out.println();
  
  // *****************Information Types***************

        DSO.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the DSO IOT INFORMATION TYPES****************

     

      System.out.println    ("DSO INFORMATION-TYPES = " + DSO.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER DSO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE SPECTRUM ORGANIZATION CHOICE # 13");
            
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR DEFENSE SPECTRUM ORGANIZATION: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      DSO.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("DSO DEVICE-TYPES = " + DSO.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER DSO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE SPECTRUM ORGANIZATION CHOICE # 13");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR DEFENSE SPECTRUM ORGANIZATION: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       DSO.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("DSO PLATFORM-TYPES = " + DSO.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER DSO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE SPECTRUM ORGANIZATION CHOICE # 13");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
 
        System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR DEFENSE SPECTRUM ORGANIZATION:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      DSO.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("DSO PROCESSOR-TYPES = " + DSO.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER DSO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE SPECTRUM ORGANIZATION CHOICE # 13");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR DEFENSE SPECTRUM ORGANIZATION: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         DSO.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("DSO NETWORK-TYPES = " + DSO.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER DSO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE SPECTRUM ORGANIZATION CHOICE # 13");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR DEFENSE SPECTRUM ORGANIZATION: ");
               System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          DSO.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("DSO INFRASTRUCTURE-TYPES = " + DSO.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER DSO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE SPECTRUM ORGANIZATION CHOICE # 13");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR DEFENSE SPECTRUM ORGANIZATION CHOICE # 13");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                DSO.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("DSO OperatingSystem type  = " + DSO.getOperatingSystemType());
  
               // System.out.println("************************************************** ");
               //System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENIENCE");
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER DSO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE SPECTRUM ORGANIZATION CHOICE # 13");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR DEFENSE SPECTRUM ORGANIZATION: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           DSO.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("DSO INTEROPERABILITY-TYPES = " + DSO.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER DSO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE SPECTRUM ORGANIZATION CHOICE # 13");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SEE BELOW IoT USERS-TYPES FOR DEFENSE SPECTRUM ORGANIZATION: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          DSO.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("DSO USERS-TYPES = " + DSO.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER DSO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE SPECTRUM ORGANIZATION CHOICE # 13");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR DEFENSE SPECTRUM ORGANIZATION: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          DSO.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("DSO BEHAVIOURS-TYPES = " + DSO.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER DSO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE SPECTRUM ORGANIZATION CHOICE # 13");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

      
System.out.println("************************************************************************************************" );
System.out.println();      
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES WITH IOT TAXONOMY RELATED DEVICES: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
      // Prompt the user for a selection 


       System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println(" --THIS IS INVALID SELECTION-- "); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
 System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();  
 } 


break;


case 14:

   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED WHITE HOUSE COMMUNICATIONS AGENCY: ");
   System.out.println();
   System.out.println( "PLEASE SEE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - WHITE HOUSE COMMUNICATIONS AGENCY (WHCA)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
   System.out.println();    
               
   InterNetOfThings WHCA;
   WHCA = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR WHCA.");
 System.out.println();
 System.out.println("2.  WHCA INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  WHCA DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  WHCA PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  WHCA PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  WHCA NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  WHCA INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  WHCA OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  WHCA INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. WHCA USERS_TYPES.");
 System.out.println();
 System.out.println("11. WHCA BEHAVIOURS_TYPES.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     "); 
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SEE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - WHITE HOUSE COMMUNICATIONS AGENCY(WHCA)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR WHCA.");
 System.out.println();
 System.out.println("2.  WHCA INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  WHCA DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  WHCA PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  WHCA PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  WHCA NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  WHCA INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  WHCA OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  WHCA INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. WHCA USERS_TYPES.");
 System.out.println();
 System.out.println("11. WHCA BEHAVIOURS_TYPES.");
 System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (WHCA) WHITE HOUSE COMMUNICATIONS AGENCY: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          WHCA.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          WHCA.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          WHCA.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          WHCA.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          WHCA.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          WHCA.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         WHCA.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         WHCA.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         WHCA.setUser                  ("Stakeholders across the enterprise");
         

         WHCA.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("WHCA INFORMATION-TYPES      = " + WHCA.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("WHCA DEVICE_TYPES           = " + WHCA.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("WHCA PROCESSOR_TYPES        = " + WHCA.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("WHCA NETWORK_TYPES          = " + WHCA.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("WHCA INFRASTRUCTURE_TYPES   = " + WHCA.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("WHCA OPERATING_SYSTEM_TYPES = " + WHCA.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("WHCA INTEROPERABILITY_TYPES = " + WHCA.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("WHCA USER_TYPES             = " + WHCA.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("WHCA BEHAVIOUR_TYPES        = " + WHCA.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("WHCA PLATFORM_TYPES         = " + WHCA.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER WHCA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WHITE HOUSE COMMUNICATIONS AGENCY CHOICE # 14");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR WHITE HOUSE COMMUNICATIONS AGENCY: ");
         System.out.println();
  
  // *****************Information Types***************

        WHCA.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the WHCA IOT INFORMATION TYPES****************

     

      System.out.println    ("WHCA INFORMATION-TYPES = " + WHCA.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER WHCA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WHITE HOUSE COMMUNICATIONS AGENCY CHOICE # 14");
            
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR WHITE HOUSE COMMUNICATIONS AGENCY: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      WHCA.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("WHCA DEVICE-TYPES = " + WHCA.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER WHCA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WHITE HOUSE COMMUNICATIONS AGENCY CHOICE # 14");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR WHITE HOUSE COMMUNICATIONS AGENCY: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       WHCA.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("WHCA PLATFORM-TYPES = " + WHCA.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER WHCA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WHITE HOUSE COMMUNICATIONS AGENCY CHOICE # 14");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
        System.out.println("************************************************************************************************" );
        System.out.println();
 
        System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR WHITE HOUSE COMMUNICATIONS AGENCY:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      WHCA.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("WHCA PROCESSOR-TYPES = " + WHCA.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER WHCA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WHITE HOUSE COMMUNICATIONS AGENCY CHOICE # 14");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR WHITE HOUSE COMMUNICATIONS AGENCY: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         WHCA.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("WHCA NETWORK-TYPES = " + WHCA.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER WHCA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WHITE HOUSE COMMUNICATIONS AGENCY CHOICE # 14");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println("************************************************************************************************" );

              System.out.println();
              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR WHITE HOUSE COMMUNICATIONS AGENCY: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          WHCA.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("WHCA INFRASTRUCTURE-TYPES = " + WHCA.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER WHCA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WHITE HOUSE COMMUNICATIONS AGENCY CHOICE # 14");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR WHITE HOUSE COMMUNICATIONS AGENCY CHOICE # 14");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                WHCA.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("WHCA OperatingSystem type  = " + WHCA.getOperatingSystemType());
  
               // System.out.println("************************************************** ");
               //System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENIENCE");
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER WHCA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WHITE HOUSE COMMUNICATIONS AGENCY CHOICE # 14");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR WHITE HOUSE COMMUNICATIONS AGENCY: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           WHCA.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("WHCA INTEROPERABILITY-TYPES = " + WHCA.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER WHCA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WHITE HOUSE COMMUNICATIONS AGENCY CHOICE # 14");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SEE BELOW IoT USERS-TYPES FOR WHITE HOUSE COMMUNICATIONS AGENCY: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          WHCA.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("WHCA USERS-TYPES = " + WHCA.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER WHCA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WHITE HOUSE COMMUNICATIONS AGENCY CHOICE # 14");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR WHITE HOUSE COMMUNICATIONS AGENCY: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          WHCA.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("WHCA BEHAVIOURS-TYPES = " + WHCA.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER WHCA TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WHITE HOUSE COMMUNICATIONS AGENCY CHOICE # 14");
            


          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

System.out.println();     
System.out.println("************************************************************************************************" );
System.out.println();    
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES WITH IOT TAXONOMY RELATED DEVICES: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

      // Prompt the user for a selection 


System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println(" --THIS IS INVALID SELECTION-- ");
 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
 System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");

System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt(); 
  
 } 


break;

case 15:

   System.out.println();
   System.out.println();
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED ENTERPRISE ENGINEE1RING DIRECTORATE: ");
   System.out.println();
   System.out.println();
   System.out.println( "PLEASE SEE1 BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - ENTERPRISE ENGINEE1RING DIRECTORATE (EE1)");
   System.out.println();
   System.out.println("************************************************************************************************" );
   System.out.println();                      
        
               
   InterNetOfThings EE1;
   EE1 = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR EE1.");
 System.out.println();
 System.out.println("2.  EE1 INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  EE1 DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  EE1 PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  EE1 PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  EE1 NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  EE1 INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  EE1 OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  EE1 INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. EE1 USERS_TYPES.");
 System.out.println();
 System.out.println("11. EE1 BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR TAXONOMY CHOICE # FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
 System.out.println();
 System.out.println("    --THIS IS INVALID SELECTION--     "); 
 System.out.println();
 System.out.println("***************************************************************************************************************" );
 System.out.println();
 System.out.println(" PLEASE SEE1 BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - ENTERPRISE ENGINEE1RING DIRECTORATE(EE1)");
 System.out.println();
 System.out.println("***************************************************************************************************************" );
 System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR EE1.");
 System.out.println();
 System.out.println("2.  EE1 INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  EE1 DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  EE1 PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  EE1 PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  EE1 NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  EE1 INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  EE1 OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  EE1 INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. EE1 USERS_TYPES.");
 System.out.println();
 System.out.println("11. EE1 BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("***************************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE1 BELOW THE ENTIRE-IOT-TAXONOMY FOR - (EE1) ENTERPRISE ENGINEE1RING DIRECTORATE: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          EE1.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          EE1.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          EE1.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          EE1.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          EE1.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          EE1.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         EE1.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         EE1.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         EE1.setUser                  ("Stakeholders across the enterprise");
         

         EE1.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("EE1 INFORMATION-TYPES      = " + EE1.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("EE1 DEVICE_TYPES           = " + EE1.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("EE1 PROCESSOR_TYPES        = " + EE1.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("EE1 NETWORK_TYPES          = " + EE1.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("EE1 INFRASTRUCTURE_TYPES   = " + EE1.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("EE1 OPERATING_SYSTEM_TYPES = " + EE1.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("EE1 INTEROPERABILITY_TYPES = " + EE1.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("EE1 USER_TYPES             = " + EE1.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("EE1 BEHAVIOUR_TYPES        = " + EE1.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("EE1 PLATFORM_TYPES         = " + EE1.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER EE1 TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENTERPRISE ENGINEE1RING DIRECTORATE CHOICE # 15");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE1 IoT INFORMATION-TYPES FOR ENTERPRISE ENGINEE1RING DIRECTORATE: ");
         System.out.println();
  
  // *****************Information Types***************

        EE1.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the EE1 IOT INFORMATION TYPES****************

     

      System.out.println    ("EE1 INFORMATION-TYPES = " + EE1.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER EE1 TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENTERPRISE ENGINEE1RING DIRECTORATE CHOICE # 15");
            
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE1 BELOW IoT DEVICES-TYPES FOR ENTERPRISE ENGINEE1RING DIRECTORATE: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      EE1.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("EE1 DEVICE-TYPES = " + EE1.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER EE1 TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENTERPRISE ENGINEE1RING DIRECTORATE CHOICE # 15");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE1 BELOW IoT PLATFORMS-TYPES FOR ENTERPRISE ENGINEE1RING DIRECTORATE: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       EE1.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("EE1 PLATFORM-TYPES = " + EE1.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER EE1 TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENTERPRISE ENGINEE1RING DIRECTORATE CHOICE # 15");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE1 BELOW IoT PROCESSOR-TYPES FOR ENTERPRISE ENGINEE1RING DIRECTORATE:");
 
         System.out.println();
             

  // ****************Processor Types*******************
  
  
      EE1.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("EE1 PROCESSOR-TYPES = " + EE1.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER EE1 TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENTERPRISE ENGINEE1RING DIRECTORATE CHOICE # 15");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE1 BELOW IoT NETWORK-TYPES FOR ENTERPRISE ENGINEE1RING DIRECTORATE: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         EE1.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("EE1 NETWORK-TYPES = " + EE1.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER EE1 TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENTERPRISE ENGINEE1RING DIRECTORATE CHOICE # 15");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println("************************************************************************************************" );
              System.out.println();
              System.out.println("PLEASE SEE1 BELOW IoT INFRASTRUCTURE-TYPES FOR ENTERPRISE ENGINEE1RING DIRECTORATE: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          EE1.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("EE1 INFRASTRUCTURE-TYPES = " + EE1.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER EE1 TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENTERPRISE ENGINEE1RING DIRECTORATE CHOICE # 15");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE1 BELOW IoT OPERATING-SYSTEM-TYPES FOR ENTERPRISE ENGINEE1RING DIRECTORATE CHOICE # 15");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                EE1.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("EE1 OperatingSystem type  = " + EE1.getOperatingSystemType());
  
               // System.out.println("************************************************** ");
               //System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENIENCE");
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER EE1 TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENTERPRISE ENGINEE1RING DIRECTORATE CHOICE # 15");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE1 BELOW IoT INTEROPERABILITY-TYPES FOR ENTERPRISE ENGINEE1RING DIRECTORATE: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           EE1.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("EE1 INTEROPERABILITY-TYPES = " + EE1.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER EE1 TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENTERPRISE ENGINEE1RING DIRECTORATE CHOICE # 15");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SEE1 BELOW IoT USERS-TYPES FOR ENTERPRISE ENGINEE1RING DIRECTORATE: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          EE1.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("EE1 USERS-TYPES = " + EE1.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER EE1 TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENTERPRISE ENGINEE1RING DIRECTORATE CHOICE # 15");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE1 BELOW IoT BEHAVIOURS-TYPES FOR ENTERPRISE ENGINEE1RING DIRECTORATE: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          EE1.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("EE1 BEHAVIOURS-TYPES = " + EE1.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER EE1 TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN ENTERPRISE ENGINEE1RING DIRECTORATE CHOICE # 15");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

      
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES WITH IOT TAXONOMY RELATED DEVICES: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

      // Prompt the user for a selection 


System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
System.out.println();
System.out.println(" --THIS IS INVALID SELECTION-- ");
System.out.println(); 
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt(); 
   
 } 


break;

case 16:

   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED INFRASTRUCTURE DIRECTORATE: ");
   System.out.println();
   System.out.println( "PLEASE SIE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - INFRASTRUCTURE DIRECTORATE (IE)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
   System.out.println();    
               
   InterNetOfThings IE;
   IE = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR IE.");
 System.out.println();
 System.out.println("2.  IE INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  IE DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  IE PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  IE PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  IE NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  IE INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  IE OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  IE INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. IE USERS_TYPES.");
 System.out.println();
 System.out.println("11. IE BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR TAXONOMY CHOICE # FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
 System.out.println();
 System.out.println("    --THIS IS INVALID SELECTION--     ");
 System.out.println(); 
 System.out.println("***************************************************************************************************************" );
 System.out.println();
 System.out.println(" PLEASE SIE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORIES FOR - INFRASTRUCTURE DIRECTORATE(IE)");
 System.out.println();
 System.out.println("***************************************************************************************************************" );
 System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR IE.");
 System.out.println();
 System.out.println("2.  IE INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  IE DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  IE PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  IE PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  IE NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  IE INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  IE OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  IE INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. IE USERS_TYPES.");
 System.out.println();
 System.out.println("11. IE BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("***************************************************************************************************************" );
 System.out.println();
  System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SIE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (IE) INFRASTRUCTURE DIRECTORATE: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          IE.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          IE.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          IE.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          IE.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          IE.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          IE.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         IE.setOperatingSystem       ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         IE.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         IE.setUser                  ("Stakeholders across the enterprise");
         

         IE.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("IE INFORMATION-TYPES      = " + IE.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("IE DEVICE_TYPES           = " + IE.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("IE PROCESSOR_TYPES        = " + IE.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("IE NETWORK_TYPES          = " + IE.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("IE INFRASTRUCTURE_TYPES   = " + IE.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("IE OPERATING_SYSTEM_TYPES = " + IE.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("IE INTEROPERABILITY_TYPES = " + IE.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("IE USER_TYPES             = " + IE.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("IE BEHAVIOUR_TYPES        = " + IE.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("IE PLATFORM_TYPES         = " + IE.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER IE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN INFRASTRUCTURE DIRECTORATE CHOICE # 16");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SIE IoT INFORMATION-TYPES FOR INFRASTRUCTURE DIRECTORATE: ");
         System.out.println();
  
  // *****************Information Types***************

        IE.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the IE IOT INFORMATION TYPES****************

     

      System.out.println    ("IE INFORMATION-TYPES = " + IE.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER IE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN INFRASTRUCTURE DIRECTORATE CHOICE # 16");
            
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SIE BELOW IoT DEVICES-TYPES FOR INFRASTRUCTURE DIRECTORATE: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      IE.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("IE DEVICE-TYPES = " + IE.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER IE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN INFRASTRUCTURE DIRECTORATE CHOICE # 16");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SIE BELOW IoT PLATFORMS-TYPES FOR INFRASTRUCTURE DIRECTORATE: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       IE.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("IE PLATFORM-TYPES = " + IE.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER IE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN INFRASTRUCTURE DIRECTORATE CHOICE # 16");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SIE BELOW IoT PROCESSOR-TYPES FOR INFRASTRUCTURE DIRECTORATE:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      IE.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("IE PROCESSOR-TYPES = " + IE.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER IE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN INFRASTRUCTURE DIRECTORATE CHOICE # 16");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SIE BELOW IoT NETWORK-TYPES FOR INFRASTRUCTURE DIRECTORATE: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         IE.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("IE NETWORK-TYPES = " + IE.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER IE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN INFRASTRUCTURE DIRECTORATE CHOICE # 16");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SIE BELOW IoT INFRASTRUCTURE-TYPES FOR INFRASTRUCTURE DIRECTORATE: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          IE.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("IE INFRASTRUCTURE-TYPES = " + IE.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER IE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN INFRASTRUCTURE DIRECTORATE CHOICE # 16");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SIE BELOW IoT OPERATING-SYSTEM-TYPES FOR INFRASTRUCTURE DIRECTORATE CHOICE # 16");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                IE.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("IE OperatingSystem type  = " + IE.getOperatingSystemType());
  
               // System.out.println("************************************************** ");
               //System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENIENCE");
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER IE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN INFRASTRUCTURE DIRECTORATE CHOICE # 16");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SIE BELOW IoT INTEROPERABILITY-TYPES FOR INFRASTRUCTURE DIRECTORATE: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           IE.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("IE INTEROPERABILITY-TYPES = " + IE.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER IE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN INFRASTRUCTURE DIRECTORATE CHOICE # 16");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SIE BELOW IoT USERS-TYPES FOR INFRASTRUCTURE DIRECTORATE: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          IE.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("IE USERS-TYPES = " + IE.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER IE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN INFRASTRUCTURE DIRECTORATE CHOICE # 16");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SIE BELOW IoT BEHAVIOURS-TYPES FOR INFRASTRUCTURE DIRECTORATE: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          IE.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("IE BEHAVIOURS-TYPES = " + IE.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER IE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN INFRASTRUCTURE DIRECTORATE CHOICE # 16");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

System.out.println();     
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES WITH IOT TAXONOMY RELATED DEVICES: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );

      // Prompt the user for a selection 


       System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
System.out.println();
System.out.println(" --THIS IS INVALID SELECTION-- "); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();
  
 } 



break;


case 17:

   System.out.println();
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED SERVICES DIRECTORATE: ");
   System.out.println();
   System.out.println( "PLEASE SEE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORSES FOR - SERVICES DIRECTORATE (SE)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
   System.out.println();    
               
   InterNetOfThings SE;
   SE = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR SE.");
 System.out.println();
 System.out.println("2.  SE INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  SE DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  SE PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  SE PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  SE NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  SE INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  SE OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  SE INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. SE USERS_TYPES.");
 System.out.println();
 System.out.println("11. SE BEHAVIOURS_TYPES.");
 System.out.println();
 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     "); 
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SEE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORSES FOR - SERVICES DIRECTORATE(SE)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR SE.");
  System.out.println();
  System.out.println("2.  SE INFORMATION_TYPES.");
  System.out.println();
  System.out.println("3.  SE DEVICE_TYPES.");
  System.out.println();
  System.out.println("4.  SE PLATFORMS_TYPES.");
  System.out.println();
  System.out.println("5.  SE PROCESSORS_TYPES.");
  System.out.println();
  System.out.println("6.  SE NETWORK_TYPES.");
  System.out.println();
  System.out.println("7.  SE INFRASTRUCTURE_TYPES.");
  System.out.println();
  System.out.println("8.  SE OPERATING_SYSTEM_TYPES.");
  System.out.println();
  System.out.println("9.  SE INTEROPERABILITY_TYPES.");
  System.out.println();
  System.out.println("10. SE USERS_TYPES.");
  System.out.println();
  System.out.println("11. SE BEHAVIOURS_TYPES.");
  System.out.println();
 
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (SE) SERVICES DIRECTORATE: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          SE.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          SE.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          SE.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          SE.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          SE.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          SE.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         SE.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         SE.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         SE.setUser                  ("Stakeholders across the enterprise");
         

         SE.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("SE INFORMATION-TYPES      = " + SE.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("SE DEVICE_TYPES           = " + SE.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("SE PROCESSOR_TYPES        = " + SE.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("SE NETWORK_TYPES          = " + SE.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("SE INFRASTRUCTURE_TYPES   = " + SE.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("SE OPERATING_SYSTEM_TYPES = " + SE.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("SE INTEROPERABILITY_TYPES = " + SE.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("SE USER_TYPES             = " + SE.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("SE BEHAVIOUR_TYPES        = " + SE.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("SE PLATFORM_TYPES         = " + SE.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER SE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN SERVICES DIRECTORATE CHOICE # 17");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR SERVICES DIRECTORATE: ");
         System.out.println();
  
  // *****************Information Types***************

        SE.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the SE IOT INFORMATION TYPES****************

     

      System.out.println    ("SE INFORMATION-TYPES = " + SE.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER SE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN SERVICES DIRECTORATE CHOICE # 17");
            
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR SERVICES DIRECTORATE: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      SE.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("SE DEVICE-TYPES = " + SE.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER SE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN SERVICES DIRECTORATE CHOICE # 17");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR SERVICES DIRECTORATE: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       SE.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("SE PLATFORM-TYPES = " + SE.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER SE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN SERVICES DIRECTORATE CHOICE # 17");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
         System.out.println("************************************************************************************************" );
         
 
        System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR SERVICES DIRECTORATE:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      SE.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("SE PROCESSOR-TYPES = " + SE.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER SE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN SERVICES DIRECTORATE CHOICE # 17");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR SERVICES DIRECTORATE: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         SE.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("SE NETWORK-TYPES = " + SE.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER SE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN SERVICES DIRECTORATE CHOICE # 17");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println("************************************************************************************************" );

              System.out.println();
              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR SERVICES DIRECTORATE: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          SE.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("SE INFRASTRUCTURE-TYPES = " + SE.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER SE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN SERVICES DIRECTORATE CHOICE # 17");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR SERVICES DIRECTORATE CHOICE # 17");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                SE.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("SE OperatingSystem type  = " + SE.getOperatingSystemType());
  
               // System.out.println("************************************************** ");
               //System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENSENCE");
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER SE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN SERVICES DIRECTORATE CHOICE # 17");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR SERVICES DIRECTORATE: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           SE.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("SE INTEROPERABILITY-TYPES = " + SE.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER SE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN SERVICES DIRECTORATE CHOICE # 17");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SEE BELOW IoT USERS-TYPES FOR SERVICES DIRECTORATE: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          SE.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("SE USERS-TYPES = " + SE.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER SE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN SERVICES DIRECTORATE CHOICE # 17");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR SERVICES DIRECTORATE: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          SE.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("SE BEHAVIOURS-TYPES = " + SE.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER SE TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN SERVICES DIRECTORATE CHOICE # 17");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

      
System.out.println("************************************************************************************************" );
System.out.println();     
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES WITH IOT TAXONOMY RELATED DEVICES: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
      // Prompt the user for a selection 


       System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println(" --THIS IS INVALID SELECTION-- ");
 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
 System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();
  
 } 



break;

case 18:

   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED OPERATIONS DIRECTORATE: ");
   System.out.println();
   System.out.println( "PLEASE SEE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGOROPS FOR - OPERATIONS DIRECTORATE (OP)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
   System.out.println();     
               
   InterNetOfThings OP;
   OP = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR OP.");
 System.out.println();
 System.out.println("2.  OP INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  OP DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  OP PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  OP PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  OP NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  OP INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  OP OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  OP INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. OP USERS_TYPES.");
 System.out.println();
 System.out.println("11. OP BEHAVIOURS_TYPES.");
 System.out.println();
 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     "); 
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SEE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGOROPS FOR - OPERATIONS DIRECTORATE(OP)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR OP.");
  System.out.println();
  System.out.println("2.  OP INFORMATION_TYPES.");
  System.out.println();
  System.out.println("3.  OP DEVICE_TYPES.");
  System.out.println();
  System.out.println("4.  OP PLATFORMS_TYPES.");
  System.out.println();
  System.out.println("5.  OP PROCESSORS_TYPES.");
  System.out.println();
  System.out.println("6.  OP NETWORK_TYPES.");
  System.out.println();
  System.out.println("7.  OP INFRASTRUCTURE_TYPES.");
  System.out.println();
  System.out.println("8.  OP OPERATING_SYSTEM_TYPES.");
  System.out.println();
  System.out.println("9.  OP INTEROPERABILITY_TYPES.");
  System.out.println();
  System.out.println("10. OP USERS_TYPES.");
  System.out.println();
  System.out.println("11. OP BEHAVIOURS_TYPES.");
  
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (OP) OPERATIONS DIRECTORATE: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          OP.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          OP.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          OP.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          OP.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          OP.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          OP.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


          OP.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         OP.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         OP.setUser                  ("Stakeholders across the enterprise");
         

         OP.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("OP INFORMATION-TYPES      = " + OP.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("OP DEVICE_TYPES           = " + OP.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("OP PROCESSOR_TYPES        = " + OP.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("OP NETWORK_TYPES          = " + OP.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("OP INFRASTRUCTURE_TYPES   = " + OP.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("OP OPERATING_SYSTEM_TYPES = " + OP.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("OP INTEROPERABILITY_TYPES = " + OP.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("OP USER_TYPES             = " + OP.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("OP BEHAVIOUR_TYPES        = " + OP.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("OP PLATFORM_TYPES         = " + OP.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER OP TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN OPERATIONS DIRECTORATE CHOICE # 18");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR OPERATIONS DIRECTORATE: ");
         System.out.println();
  
  // *****************Information Types***************

        OP.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the OP IOT INFORMATION TYPES****************

     

      System.out.println    ("OP INFORMATION-TYPES = " + OP.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER OP TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN OPERATIONS DIRECTORATE CHOICE # 18");
            
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR OPERATIONS DIRECTORATE: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      OP.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("OP DEVICE-TYPES = " + OP.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER OP TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN OPERATIONS DIRECTORATE CHOICE # 18");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR OPERATIONS DIRECTORATE: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       OP.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("OP PLATFORM-TYPES = " + OP.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER OP TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN OPERATIONS DIRECTORATE CHOICE # 18");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR OPERATIONS DIRECTORATE:");
 
         System.out.println();
             

  // ****************Processor Types*******************
  
  
      OP.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("OP PROCESSOR-TYPES = " + OP.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER OP TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN OPERATIONS DIRECTORATE CHOICE # 18");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR OPERATIONS DIRECTORATE: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         OP.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("OP NETWORK-TYPES = " + OP.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER OP TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN OPERATIONS DIRECTORATE CHOICE # 18");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
                System.out.println("************************************************************************************************" );
                System.out.println();

                System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR OPERATIONS DIRECTORATE: ");
                System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          OP.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("OP INFRASTRUCTURE-TYPES = " + OP.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER OP TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN OPERATIONS DIRECTORATE CHOICE # 18");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR OPERATIONS DIRECTORATE CHOICE # 18");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                OP.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("OP OperatingSystem type  = " + OP.getOperatingSystemType());
  
               // System.out.println("************************************************** ");
               //System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENOPNCE");
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER OP TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN OPERATIONS DIRECTORATE CHOICE # 18");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR OPERATIONS DIRECTORATE: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           OP.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("OP INTEROPERABILITY-TYPES = " + OP.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER OP TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN OPERATIONS DIRECTORATE CHOICE # 18");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SEE BELOW IoT USERS-TYPES FOR OPERATIONS DIRECTORATE: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          OP.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("OP USERS-TYPES = " + OP.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER OP TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN OPERATIONS DIRECTORATE CHOICE # 18");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR OPERATIONS DIRECTORATE: ");
              
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          OP.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("OP BEHAVIOURS-TYPES = " + OP.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER OP TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN OPERATIONS DIRECTORATE CHOICE # 18");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

      
System.out.println("************************************************************************************************" );
System.out.println();     
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES WITH IOT TAXONOMY RELATED DEVICES: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

      // Prompt the user for a selection 

System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
System.out.println();
System.out.println(" --THIS IS INVALID SELECTION-- ");
System.out.println(); 
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();
  
 } 
 
 break;
 
 case 19:
 
   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED DEFENSE ENTERPRISE COMPUTING CENTERS: ");
   System.out.println();
   System.out.println( "PLEASE SEE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORDECCS FOR - DEFENSE ENTERPRISE COMPUTING CENTERS (DECC)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
   System.out.println();    
               
   InterNetOfThings DECC;
   DECC = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR DECC.");
 System.out.println();
 System.out.println("2.  DECC INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  DECC DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  DECC PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  DECC PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  DECC NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  DECC INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  DECC OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  DECC INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. DECC USERS_TYPES.");
 System.out.println();
 System.out.println("11. DECC BEHAVIOURS_TYPES.");
 System.out.println();
 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     "); 
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SEE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORDECCS FOR - DEFENSE ENTERPRISE COMPUTING CENTERS(DECC)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR DECC.");
  System.out.println();
  System.out.println("2.  DECC INFORMATION_TYPES.");
  System.out.println();
  System.out.println("3.  DECC DEVICE_TYPES.");
  System.out.println();
  System.out.println("4.  DECC PLATFORMS_TYPES.");
  System.out.println();
  System.out.println("5.  DECC PROCESSORS_TYPES.");
  System.out.println();
  System.out.println("6.  DECC NETWORK_TYPES.");
  System.out.println();
  System.out.println("7.  DECC INFRASTRUCTURE_TYPES.");
  System.out.println();
  System.out.println("8.  DECC OPERATING_SYSTEM_TYPES.");
  System.out.println();
  System.out.println("9.  DECC INTEROPERABILITY_TYPES.");
  System.out.println();
  System.out.println("10. DECC USERS_TYPES.");
  System.out.println();
  System.out.println("11. DECC BEHAVIOURS_TYPES.");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (DECC) DEFENSE ENTERPRISE COMPUTING CENTERS: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          DECC.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          DECC.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          DECC.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          DECC.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          DECC.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          DECC.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         DECC.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         DECC.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         DECC.setUser                  ("Stakeholders across the enterprise");
         

         DECC.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("DECC INFORMATION-TYPES      = " + DECC.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("DECC DEVICE_TYPES           = " + DECC.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("DECC PROCESSOR_TYPES        = " + DECC.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("DECC NETWORK_TYPES          = " + DECC.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("DECC INFRASTRUCTURE_TYPES   = " + DECC.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("DECC OPERATING_SYSTEM_TYPES = " + DECC.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("DECC INTEROPERABILITY_TYPES = " + DECC.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("DECC USER_TYPES             = " + DECC.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("DECC BEHAVIOUR_TYPES        = " + DECC.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("DECC PLATFORM_TYPES         = " + DECC.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER DECC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE ENTERPRISE COMPUTING CENTERS CHOICE # 19");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR DEFENSE ENTERPRISE COMPUTING CENTERS: ");
         System.out.println();
  
  // *****************Information Types***************

        DECC.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the DECC IOT INFORMATION TYPES****************

     

      System.out.println    ("DECC INFORMATION-TYPES = " + DECC.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER DECC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE ENTERPRISE COMPUTING CENTERS CHOICE # 19");
            
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR DEFENSE ENTERPRISE COMPUTING CENTERS: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      DECC.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("DECC DEVICE-TYPES = " + DECC.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER DECC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE ENTERPRISE COMPUTING CENTERS CHOICE # 19");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR DEFENSE ENTERPRISE COMPUTING CENTERS: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       DECC.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("DECC PLATFORM-TYPES = " + DECC.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER DECC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE ENTERPRISE COMPUTING CENTERS CHOICE # 19");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
        System.out.println("************************************************************************************************" );
         
        System.out.println();
        System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR DEFENSE ENTERPRISE COMPUTING CENTERS:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      DECC.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("DECC PROCESSOR-TYPES = " + DECC.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER DECC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE ENTERPRISE COMPUTING CENTERS CHOICE # 19");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR DEFENSE ENTERPRISE COMPUTING CENTERS: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         DECC.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("DECC NETWORK-TYPES = " + DECC.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER DECC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE ENTERPRISE COMPUTING CENTERS CHOICE # 19");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println("************************************************************************************************" );

              System.out.println();
              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR DEFENSE ENTERPRISE COMPUTING CENTERS: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          DECC.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("DECC INFRASTRUCTURE-TYPES = " + DECC.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER DECC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE ENTERPRISE COMPUTING CENTERS CHOICE # 19");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR DEFENSE ENTERPRISE COMPUTING CENTERS CHOICE # 19");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                DECC.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("DECC OperatingSystem type  = " + DECC.getOperatingSystemType());
  
               // System.out.println("************************************************** ");
              // System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENDECCNCE");
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER DECC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE ENTERPRISE COMPUTING CENTERS CHOICE # 19");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR DEFENSE ENTERPRISE COMPUTING CENTERS: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           DECC.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("DECC INTEROPERABILITY-TYPES = " + DECC.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER DECC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE ENTERPRISE COMPUTING CENTERS CHOICE # 19");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SEE BELOW IoT USERS-TYPES FOR DEFENSE ENTERPRISE COMPUTING CENTERS: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          DECC.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("DECC USERS-TYPES = " + DECC.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER DECC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE ENTERPRISE COMPUTING CENTERS CHOICE # 19");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR DEFENSE ENTERPRISE COMPUTING CENTERS: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          DECC.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("DECC BEHAVIOURS-TYPES = " + DECC.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER DECC TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN DEFENSE ENTERPRISE COMPUTING CENTERS CHOICE # 19");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

      
System.out.println("************************************************************************************************" );
System.out.println();     
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES WITH IOT TAXONOMY RELATED DEVICES: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
      // Prompt the user for a selection 


       System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
 System.out.println();
 System.out.println(" --THIS IS INVALID SELECTION-- ");
 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
 System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();
  
 } 

break;

 

case 20: 
 
   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println();
   System.out.println( "YOU SELECTED GLOBAL SERVICE DESK MANAGEMENT OFFICE: ");
   System.out.println();
   System.out.println( "PLEASE SEE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORGSDMOS FOR - GLOBAL SERVICE DESK MANAGEMENT OFFICE (GSDMO)");
   System.out.println();
   System.out.println("************************************************************************************************" );                      
   System.out.println();    
               
   InterNetOfThings GSDMO;
   GSDMO = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR GSDMO.");
 System.out.println();
 System.out.println("2.  GSDMO INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  GSDMO DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  GSDMO PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  GSDMO PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  GSDMO NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  GSDMO INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  GSDMO OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  GSDMO INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. GSDMO USERS_TYPES.");
 System.out.println();
 System.out.println("11. GSDMO BEHAVIOURS_TYPES.");
 System.out.println();
 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR TAXONOMY CHOICE# FROM 1 to 11: ");
  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     ");
  System.out.println(); 
  
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SEE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORGSDMOS FOR - GLOBAL SERVICE DESK MANAGEMENT OFFICE(GSDMO)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR GSDMO.");
 System.out.println();
 System.out.println("2.  GSDMO INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  GSDMO DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  GSDMO PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  GSDMO PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  GSDMO NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  GSDMO INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  GSDMO OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  GSDMO INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. GSDMO USERS_TYPES.");
 System.out.println();
 System.out.println("11. GSDMO BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("***************************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (GSDMO) GLOBAL SERVICE DESK MANAGEMENT OFFICE: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          GSDMO.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          GSDMO.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          GSDMO.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          GSDMO.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          GSDMO.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          GSDMO.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         GSDMO.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         GSDMO.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         GSDMO.setUser                  ("Stakeholders across the enterprise");
         

         GSDMO.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("GSDMO INFORMATION-TYPES      = " + GSDMO.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("GSDMO DEVICE_TYPES           = " + GSDMO.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("GSDMO PROCESSOR_TYPES        = " + GSDMO.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("GSDMO NETWORK_TYPES          = " + GSDMO.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("GSDMO INFRASTRUCTURE_TYPES   = " + GSDMO.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("GSDMO OPERATING_SYSTEM_TYPES = " + GSDMO.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("GSDMO INTEROPERABILITY_TYPES = " + GSDMO.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("GSDMO USER_TYPES             = " + GSDMO.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("GSDMO BEHAVIOUR_TYPES        = " + GSDMO.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("GSDMO PLATFORM_TYPES         = " + GSDMO.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER GSDMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN GLOBAL SERVICE DESK MANAGEMENT OFFICE CHOICE # 20");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR GLOBAL SERVICE DESK MANAGEMENT OFFICE: ");
         System.out.println();
  
  // *****************Information Types***************

        GSDMO.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the GSDMO IOT INFORMATION TYPES****************

     

      System.out.println    ("GSDMO INFORMATION-TYPES = " + GSDMO.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER GSDMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN GLOBAL SERVICE DESK MANAGEMENT OFFICE CHOICE # 20");
            
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR GLOBAL SERVICE DESK MANAGEMENT OFFICE: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      GSDMO.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("GSDMO DEVICE-TYPES = " + GSDMO.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER GSDMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN GLOBAL SERVICE DESK MANAGEMENT OFFICE CHOICE # 20");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR GLOBAL SERVICE DESK MANAGEMENT OFFICE: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       GSDMO.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("GSDMO PLATFORM-TYPES = " + GSDMO.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER GSDMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN GLOBAL SERVICE DESK MANAGEMENT OFFICE CHOICE # 20");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
        System.out.println("************************************************************************************************" );
         
        System.out.println();
        System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR GLOBAL SERVICE DESK MANAGEMENT OFFICE:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      GSDMO.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("GSDMO PROCESSOR-TYPES = " + GSDMO.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println( "TO SELECT ANOTHER GSDMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN GLOBAL SERVICE DESK MANAGEMENT OFFICE CHOICE # 20");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR GLOBAL SERVICE DESK MANAGEMENT OFFICE: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         GSDMO.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("GSDMO NETWORK-TYPES = " + GSDMO.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER GSDMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN GLOBAL SERVICE DESK MANAGEMENT OFFICE CHOICE # 20");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println("************************************************************************************************" );

              System.out.println();
              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR GLOBAL SERVICE DESK MANAGEMENT OFFICE: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          GSDMO.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("GSDMO INFRASTRUCTURE-TYPES = " + GSDMO.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER GSDMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN GLOBAL SERVICE DESK MANAGEMENT OFFICE CHOICE # 20");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR GLOBAL SERVICE DESK MANAGEMENT OFFICE CHOICE # 20");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                GSDMO.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("GSDMO OperatingSystem type  = " + GSDMO.getOperatingSystemType());
  
               // System.out.println("************************************************** ");
               //System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENGSDMONCE");
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER GSDMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN GLOBAL SERVICE DESK MANAGEMENT OFFICE CHOICE # 20");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR GLOBAL SERVICE DESK MANAGEMENT OFFICE: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           GSDMO.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("GSDMO INTEROPERABILITY-TYPES = " + GSDMO.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER GSDMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN GLOBAL SERVICE DESK MANAGEMENT OFFICE CHOICE # 20");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.print("PLEASE SEE BELOW IoT USERS-TYPES FOR GLOBAL SERVICE DESK MANAGEMENT OFFICE: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          GSDMO.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("GSDMO USERS-TYPES = " + GSDMO.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER GSDMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN GLOBAL SERVICE DESK MANAGEMENT OFFICE CHOICE # 20");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR GLOBAL SERVICE DESK MANAGEMENT OFFICE: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          GSDMO.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("GSDMO BEHAVIOURS-TYPES = " + GSDMO.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER GSDMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN GLOBAL SERVICE DESK MANAGEMENT OFFICE CHOICE # 20");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

      
System.out.println("************************************************************************************************" );
System.out.println();     
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES WITH IOT TAXONOMY RELATED DEVICES: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
      // Prompt the user for a selection 


       System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
System.out.println();
System.out.println(" --THIS IS INVALID SELECTION-- "); 
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();

System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();
  
 } 


break; 

case 21:

   System.out.println();
   
   System.out.println("************************************************************************************************" );
   System.out.println( "YOU SELECTED WORK FORCE MANAGEMENT OFFICE: ");
   System.out.println();
   System.out.println( "PLEASE SEE BELOW (1 - 11) IOT TAXONOMY RELATED CATEGORWFMOS FOR - WORK FORCE MANAGEMENT OFFICE (WFMO)");
   System.out.println("************************************************************************************************" );                      
        
               
   InterNetOfThings WFMO;
   WFMO = new InterNetOfThings();
 
 
  //*****************DISPLAY THE IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR WFMO.");
 System.out.println();
 System.out.println("2.  WFMO INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  WFMO DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  WFMO PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  WFMO PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  WFMO NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  WFMO INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  WFMO OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  WFMO INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. WFMO USERS_TYPES.");
 System.out.println();
 System.out.println("11. WFMO BEHAVIOURS_TYPES.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR TAXONOMY CHOICE # FROM 1 to 11: ");  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println();
  System.out.println("    --THIS IS INVALID SELECTION--     "); 
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println(" PLEASE SEE BELOW VALID LIST OF (1 - 11) IOT TAXONOMY RELATED CATEGORWFMOS FOR - WORK FORCE MANAGEMENT OFFICE(WFMO)");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR WFMO.");
  System.out.println();
  System.out.println("2.  WFMO INFORMATION_TYPES.");
  System.out.println();
  System.out.println("3.  WFMO DEVICE_TYPES.");
  System.out.println();
  System.out.println("4.  WFMO PLATFORMS_TYPES.");
  System.out.println();
  System.out.println("5.  WFMO PROCESSORS_TYPES.");
  System.out.println();
  System.out.println("6.  WFMO NETWORK_TYPES.");
  System.out.println();
  System.out.println("7.  WFMO INFRASTRUCTURE_TYPES.");
  System.out.println();
  System.out.println("8.  WFMO OPERATING_SYSTEM_TYPES.");
  System.out.println();
  System.out.println("9.  WFMO INTEROPERABILITY_TYPES.");
  System.out.println();
  System.out.println("10. WFMO USERS_TYPES.");
  System.out.println();
  System.out.println("11. WFMO BEHAVIOURS_TYPES.");
  System.out.println();
  System.out.println("***************************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR VALID TAXONOMY CHOICE# FROM 1 to 11: ");
   
  menuSelect = keyboard.nextInt();


 }

// while (menuSelect > 0 || menuSelect <= 10)

   
   
  // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - (WFMO) WORK FORCE MANAGEMENT OFFICE: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
 
          WFMO.setInformation           ("Classified and unclassified; standardized with common taxonomies, ontologies, metadata; Big Data, ambient data, analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");
          WFMO.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");
          

          WFMO.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");
          

          WFMO.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
          

          WFMO.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");
          

          WFMO.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");
          


         WFMO.setOperatingSystem        ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         WFMO.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");
         

         WFMO.setUser                  ("Stakeholders across the enterprise");
         

         WFMO.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
        
      
      System.out.println               ("WFMO INFORMATION-TYPES      = " + WFMO.getInformationType());
      System.out.println();
      System.out.println();

      System.out.println               ("WFMO DEVICE_TYPES           = " + WFMO.getDeviceType());
      System.out.println();
      System.out.println();
      System.out.println               ("WFMO PROCESSOR_TYPES        = " + WFMO.getProcessorType());
      System.out.println();
      System.out.println();
      System.out.println               ("WFMO NETWORK_TYPES          = " + WFMO.getNetworkType());
      System.out.println();
      System.out.println();
      System.out.println               ("WFMO INFRASTRUCTURE_TYPES   = " + WFMO.getInfrastructureType());
      System.out.println();
      System.out.println();
      System.out.println               ("WFMO OPERATING_SYSTEM_TYPES = " + WFMO.getOperatingSystemType());
      System.out.println();
      System.out.println();
      System.out.println               ("WFMO INTEROPERABILITY_TYPES = " + WFMO.getInterOperabilityType());
      System.out.println();
      System.out.println();
      System.out.println               ("WFMO USER_TYPES             = " + WFMO.getUsersType());
      System.out.println();
      System.out.println();
      System.out.println               ("WFMO BEHAVIOUR_TYPES        = " + WFMO.getBehavioursType());
      System.out.println();
      System.out.println();
      System.out.println               ("WFMO PLATFORM_TYPES         = " + WFMO.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER WFMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORK FORCE MANAGEMENT OFFICE CHOICE # 21");
            }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println("***********************************************************************************" );
        
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR WORK FORCE MANAGEMENT OFFICE: ");
         System.out.println();
  
  // *****************Information Types***************

        WFMO.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

       
//**************** Display the WFMO IOT INFORMATION TYPES****************

     

      System.out.println    ("WFMO INFORMATION-TYPES = " + WFMO.getInformationType());
      
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER WFMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORK FORCE MANAGEMENT OFFICE CHOICE # 21");
            
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR WORK FORCE MANAGEMENT OFFICE: ");
         System.out.println();
         
  
 // *****************Device Types*****************
 
 
      WFMO.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        

      System.out.println   ("WFMO DEVICE-TYPES = " + WFMO.getDeviceType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER WFMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORK FORCE MANAGEMENT OFFICE CHOICE # 21");

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR WORK FORCE MANAGEMENT OFFICE: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
       WFMO.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

      System.out.println("WFMO PLATFORM-TYPES = " + WFMO.getPlatformType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER WFMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORK FORCE MANAGEMENT OFFICE CHOICE # 21");


      }

  else
   
      if ( menuSelect == 5)
      
       {
         
        System.out.println("************************************************************************************************" );
         
        System.out.println();
        System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR WORK FORCE MANAGEMENT OFFICE:");
 
        System.out.println();
             

  // ****************Processor Types*******************
  
  
      WFMO.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      System.out.println("WFMO PROCESSOR-TYPES = " + WFMO.getProcessorType());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( "TO SELECT ANOTHER WFMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORK FORCE MANAGEMENT OFFICE CHOICE # 21");

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR WORK FORCE MANAGEMENT OFFICE: ");
          System.out.println();
         
  // ***************************NETWORK TYPES*************************
 

         WFMO.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("WFMO NETWORK-TYPES = " + WFMO.getNetworkType());
        System.out.println();
        System.out.println("***************************************************************************************************************" );
        System.out.println();
        System.out.println( "TO SELECT ANOTHER WFMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORK FORCE MANAGEMENT OFFICE CHOICE # 21");


      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println("************************************************************************************************" );

              System.out.println();
              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR WORK FORCE MANAGEMENT OFFICE: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          WFMO.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          System.out.println ("WFMO INFRASTRUCTURE-TYPES = " + WFMO.getInfrastructureType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER WFMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORK FORCE MANAGEMENT OFFICE CHOICE # 21");

         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR WORK FORCE MANAGEMENT OFFICE CHOICE # 21");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
                WFMO.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
                System.out.println       ("WFMO OperatingSystem type  = " + WFMO.getOperatingSystemType());
  
               // System.out.println("************************************************** ");
               //System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENWFMONCE");
               System.out.println();
               System.out.println("***************************************************************************************************************" );
               System.out.println();
               System.out.println( "TO SELECT ANOTHER WFMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORK FORCE MANAGEMENT OFFICE CHOICE # 21");


      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR WORK FORCE MANAGEMENT OFFICE: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
           WFMO.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          System.out.println ("WFMO INTEROPERABILITY-TYPES = " + WFMO.getInterOperabilityType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER WFMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORK FORCE MANAGEMENT OFFICE CHOICE # 21");


      }

else
   
      if (menuSelect == 10)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.print("PLEASE SEE BELOW IoT USERS-TYPES FOR WORK FORCE MANAGEMENT OFFICE: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          WFMO.setUser                  ("Stakeholders Across the Enterprise");
 
         
         System.out.println          ("WFMO USERS-TYPES = " + WFMO.getUsersType());
         System.out.println();
         System.out.println("***************************************************************************************************************" );
         System.out.println();
         System.out.println( "TO SELECT ANOTHER WFMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORK FORCE MANAGEMENT OFFICE CHOICE # 21");


 
      }

else
   
      if ( menuSelect == 11)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR WORK FORCE MANAGEMENT OFFICE: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          WFMO.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("WFMO BEHAVIOURS-TYPES = " + WFMO.getBehavioursType());
          System.out.println();
          System.out.println("***************************************************************************************************************" );
          System.out.println();
          System.out.println( "TO SELECT ANOTHER WFMO TAXONOMY CATEGORY (1 - 11) PLEASE SELECT AGAIN WORK FORCE MANAGEMENT OFFICE CHOICE # 21");



          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

      
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println("HERE IS THE LIST OF DISA DIRECTORATES WITH IOT TAXONOMY RELATED DEVICES: ");
      System.out.println();
      System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
      System.out.println();
      System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND.");
      System.out.println(); 
      System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
      System.out.println();
      System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE.");
      System.out.println(); 
      System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION.");
      System.out.println(); 
      System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
      System.out.println();
      System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION.");
      System.out.println(); 
      System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE.");
      System.out.println(); 
      System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
      System.out.println();
      System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
      System.out.println();
      System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
      System.out.println();
      System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
      System.out.println();
      System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
      System.out.println();
      System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
      System.out.println();
      System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
      System.out.println();
      System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
      System.out.println();
      System.out.println("17. (SE)  SERVICES DIRECTORATE.");
      System.out.println();
      System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
      System.out.println();
      System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
      System.out.println();
      System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
      System.out.println();
      System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      // Prompt the user for a selection 


       System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
  
       
       menuSelection = keyboard.nextInt();
 
     // Validate the menu selection. 

     while (menuSelection < 1 || menuSelection > 21) 
  
{
 
System.out.println();
System.out.println(" --THIS IS INVALID SELECTION-- ");
System.out.println(); 
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DISA DIRECTORATES USING IoT TAXONOMY: ");
System.out.println();
System.out.println("1.  (EE)  ENGINEERING DIRECTORAT OFFICE."); 
System.out.println();
System.out.println("2.  (JITC)JOINT INTEOPERABILITY TEST COMMAND."); 
System.out.println();
System.out.println("3.  (ID)  CYBER DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("4.  (SD)  SERVICE DEVELOPMENT DIRECTORATE."); 
System.out.println();
System.out.println("5.  (BDF) FINANCIAL MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("6.  (BDL) LOGISTICS AND CONTRACT MANAGEMENT DIVISION.");
System.out.println();
System.out.println("7.  (BDW) WORKFORCE MANAGEMENT DIVISION."); 
System.out.println();
System.out.println("8.  (BDC) STRATEGIC COMMAND OFFICE."); 
System.out.println();
System.out.println("9.  (BDM) MISSION PARTNER ENGAGEMENT OFFICE.");
System.out.println();
System.out.println("10. (BDA) REQUIREMENTS AND ANALYSIS OFFICE.");
System.out.println();
System.out.println("11. (CAE) COMPONENT ACQUISITION OFFICE.");
System.out.println();
System.out.println("12. (CTO) CHIEF TECHNOLOGY OFFICE.");
System.out.println();
System.out.println("13. (DSO) DEFENSE SPECTRUM ORGANIZATION.");
System.out.println();
System.out.println("14. (WHCA)WHITE HOUSE COMMUNICATIONS AGENCY.");
System.out.println();
System.out.println("15. (EE)  ENTERPRISE ENIGINEERING DIRECTORATE.");
System.out.println();
System.out.println("16. (IE)  INFRASTRUCTURE DIRECTORATE.");
System.out.println();
System.out.println("17. (SE)  SERVICES DIRECTORATE.");
System.out.println();
System.out.println("18. (OP)  OPERATIONS DIRECTORATE.");
System.out.println();
System.out.println("19. (DECC)DEFENSE ENTERPRISE COMPUTING CENTERS.");
System.out.println();
System.out.println("20. GLOBAL SERVICE DESK MANAGEMENT OFFICE.");
System.out.println();
System.out.println("21. WORK FORCE MANAGEMENT OFFICE.");

System.out.println("************************************************************************************************" );
System.out.println();
System.out.print("ENTER FROM THE LIST ABOVE THE ASSOCIATED DIRECTORATE NUMBER YOU WISH TO SEE THE IOT TAXONOMY: ");
 
    
 menuSelection = keyboard.nextInt();
   
 } 

break;

   
   }
  }
  
}
 

//***********************************END OF PROGRAM CODE****************************************
