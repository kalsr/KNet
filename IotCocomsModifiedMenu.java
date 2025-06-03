
// IOT COCOMS TAXONOMY & FRAMEWORK Code dispalys IOT TAXONOMY For each of the 9-COCOMS
// Currently the test data values are USED FOR Each Taxonomy Field. 
// However when the actual values are obtained the Taxonomy fiields will be updated accordingly. 
// This code was written using Object-Oriented programming in Java JGRASP (August, 2017)
// This code was written by Mr Randy Singh,Computer Scientist,Technology Innovation Team (DISA/BDE5)
// Contact Phone# (301)225-9535  

import java.util.Scanner; 

public class IotCocomsModifiedMenu 

{
public static void main(String[] args) 
{
 
// Declare a variable to hold the 
// user's menu selection. 

int menuSelection;

final int MAX_VALUE = 10;
 
// Declare variables to hold the units 
// of measurement.
 
 String InformationType, DeviceType, PlatformType, ProcessorType, 
 NetworkType, InfrastructureType, OperatingSystemType, 
 InterOperabilityType, UsersType, BehavioursType;
 
// Create a Scanner object for keyboard input. 

Scanner keyboard = new Scanner(System.in); 

// Display the LIST OF COCOM'S.

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 10) 
  
{
 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");


  
 menuSelection = keyboard.nextInt();
  
 } 
 
 while (menuSelection > 0 || menuSelection <= 10)
 
  



 switch(menuSelection)
 
{ 

//*************************USSOCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************


 case 1:
 
 int menuSelect;
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED USSOCOM IOT Taxonomy");
 System.out.println();
 System.out.println("PLEASE SEE BELOW USSOCOM IOT Taxonomy");
 System.out.println();

InterNetOfThings USSOCOM;

//Following statement creates an object using the InterNetOfThings class as
// its Blueprint. Centcom will reference the object.

USSOCOM = new InterNetOfThings();

//*****************DISPLAY THE COCOMS IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USSOCOM.");
 System.out.println();
 System.out.println("2.  USSOCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USSOCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USSOCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USSOCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USSOCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USSOCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USSOCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USSOCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USSOCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USSOCOM BEHAVIOURS_TYPES.");
 System.out.println();
 //System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");
   
 
  menuSelect = keyboard.nextInt();

System.out.println("************************************************************************************************" );

 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println("************************************************************************************************" );
  
  System.out.println("THIS IS INVALID SELECTION"); 
 
  System.out.println("ENTER YOUR IOT MENU SELECTION FROM 1 to 11: ");
 
  System.out.println();
 
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USSOCOM.");
 System.out.println();
 System.out.println("2.  USSOCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USSOCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USSOCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USSOCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USSOCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USSOCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USSOCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USSOCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USSOCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USSOCOM BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          //System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - USSOCOM: ");
          System.out.println();
          
          USSOCOM.setInformation           ("Classified and Unclassified; Standardized with common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for Decision Support, Visualization Algorithms, Distribution Contexts; lost data from business failure");

          USSOCOM.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");

          USSOCOM.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");

          USSOCOM.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");

          USSOCOM.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

          USSOCOM.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");


         USSOCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         USSOCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

         USSOCOM.setUser                  ("Stakeholders across the enterprise");
   
         USSOCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
         
// Display the Centcom IOT taxonomy values stored in the fields

     
      System.out.println               ("USSOCOM INFORMATION-TYPES      = " + USSOCOM.getInformationType());
      System.out.println();
      System.out.println               ("USSOCOM DEVICE_TYPES           = " + USSOCOM.getDeviceType());
      System.out.println();
      System.out.println               ("USSOCOM PROCESSOR_TYPES        = " + USSOCOM.getProcessorType());
      System.out.println();
      System.out.println               ("USSOCOM NETWORK_TYPES          = " + USSOCOM.getNetworkType());
      System.out.println();
      System.out.println               ("USSOCOM INFRASTRUCTURE_TYPES   = " + USSOCOM.getInfrastructureType());
      System.out.println();
      System.out.println               ("USSOCOM OPERATING_SYSTEM_TYPES = " + USSOCOM.getOperatingSystemType());
      System.out.println();
      System.out.println               ("USSOCOM INTEROPERABILITY_TYPES = " + USSOCOM.getInterOperabilityType());
      System.out.println();
      System.out.println               ("USSOCOM USER_TYPES             = " + USSOCOM.getUsersType());
      System.out.println();
      System.out.println               ("USSOCOM BEHAVIOUR_TYPES        = " + USSOCOM.getBehavioursType());
      System.out.println();
      System.out.println               ("USSOCOM PLATFORM_TYPES         = " + USSOCOM.getPlatformType());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      
      System.out.println( "TO CONTINUE WITH NEXT USSOCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOCOM CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR USSOCOM: ");
         System.out.println();
  
  // *****************Information Types***************

        USSOCOM.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

      
//**************** Display the USSOCOM IOT INFORMATION TYPES****************

     
      System.out.println    ("USSOCOM INFORMATION-TYPES = " + USSOCOM.getInformationType());
      System.out.println();
      
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSOCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOCOM CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR USSOCOM: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         USSOCOM.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        
         System.out.println   ("USSOCOM DEVICE-TYPES = " + USSOCOM.getDeviceType());
    

         
         System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSOCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOCOM CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR USSOCOM: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      USSOCOM.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

       

      System.out.println("USSOCOM PLATFORM-TYPES = " + USSOCOM.getPlatformType());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSOCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOCOM CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );

      

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR USSOCOM:");
 
         System.out.println();
       
       

  // ****************Processor Types*******************
  
  
     USSOCOM.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      

         System.out.println("USSOCOM PROCESSOR-TYPES = " + USSOCOM.getProcessorType());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println( "TO CONTINUE WITH NEXT USSOCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOCOM CHOICE # 1");
         System.out.println();
         System.out.println("************************************************************************************************" );
     
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR USSOCOM: ");
          System.out.println();
         

  // ***************************NETWORK TYPES*************************
 

        USSOCOM.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
         System.out.println("USSOCOM NETWORK-TYPES = " + USSOCOM.getNetworkType());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println( "TO CONTINUE WITH NEXT USSOCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOCOM CHOICE # 1");
         System.out.println();
         System.out.println("************************************************************************************************" );

        

      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println();
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR USSOCOM: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE Types*******************
 
 
          USSOCOM.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          
          System.out.println ("USSOCOM INFRASTRUCTURE-TYPES = " + USSOCOM.getInfrastructureType());
          
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSOCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOCOM CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );

          
         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR USSOCOM:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
              USSOCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
              
             System.out.println            ("USSOCOM OperatingSystem type  = " + USSOCOM.getOperatingSystemType());
  
              
                          

      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSOCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOCOM CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );

         

      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println();

           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR USSOCOM: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
          USSOCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          
          System.out.println ("USSOCOM INTEROPERABILITY-TYPES = " + USSOCOM.getInterOperabilityType());
         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSOCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOCOM CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );

          


      }

else
   
      if (menuSelect == 10)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT USERS-TYPES FOR USSOCOM: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          USSOCOM.setUser       ("Stakeholders Across the Enterprise");
 
         
         System.out.println     ("USSOCOM USERS-TYPES = " + USSOCOM.getUsersType());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println( "TO CONTINUE WITH NEXT USSOCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOCOM CHOICE # 1");
         System.out.println();      
         System.out.println("************************************************************************************************" );
          

 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR USSOCOM: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          USSOCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("USSOCOM BEHAVIOURS-TYPES = " + USSOCOM.getBehavioursType());
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println( "TO CONTINUE WITH NEXT USSOCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOCOM CHOICE # 1");
          System.out.println();
          System.out.println("************************************************************************************************" );
          


          }
          else
            
   
  
  
// ******************Display the Main menu************************************

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");

       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 10) 
  
{
 
 
System.out.println();
System.out.println("THIS IS INVALID COCOM'S CHOICE# "); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();


 
 } 

break;


//*************************USTRANSCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************

case 2: 
 
 
 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED USTRANSCOM IOT Taxonomy");
 System.out.println();
 System.out.println("PLEASE SEE BELOW USTRANSCOM IOT Taxonomy");
 System.out.println();

InterNetOfThings USTRANSCOM;

//  Following statement creates an object using the InterNetOfThings class as
//its Blueprint. Centcom will reference the object.

USTRANSCOM = new InterNetOfThings();

  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USTRANSCOM.");
 System.out.println();
 System.out.println("2.  USTRANSCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USTRANSCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USTRANSCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USTRANSCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USTRANSCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USTRANSCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USTRANSCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USTRANSCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USTRANSCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USTRANSCOM BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID SELECTION"); 
System.out.println();
System.out.println("ENTER YOUR IOT MENU SELECTION FROM 1 to 11: ");
System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USTRANSCOM.");
 System.out.println();
 System.out.println("2.  USTRANSCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USTRANSCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USTRANSCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USTRANSCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USTRANSCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USTRANSCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USTRANSCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USTRANSCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USTRANSCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USTRANSCOM BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - USTRANSCOM: ");
          System.out.println();
          
          USTRANSCOM.setInformation           ("Classified and Unclassified; Standardized with common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for Decision Support, Visualization Algorithms, Distribution Contexts; lost data from business failure");

          USTRANSCOM.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");

          USTRANSCOM.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");

          USTRANSCOM.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");

          USTRANSCOM.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

          USTRANSCOM.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");


         //USTRANSCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         USTRANSCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

         USTRANSCOM.setUser                  ("Stakeholders across the enterprise");
   
         USTRANSCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
       


// Display the Centcom IOT taxonomy values stored in the fields

     
      System.out.println               ("USTRANSCOM INFORMATION-TYPES      = " + USTRANSCOM.getInformationType());
      System.out.println();
      System.out.println               ("USTRANSCOM DEVICE_TYPES           = " + USTRANSCOM.getDeviceType());
      System.out.println();
      System.out.println               ("USTRANSCOM PROCESSOR_TYPES        = " + USTRANSCOM.getProcessorType());
      System.out.println();
      System.out.println               ("USTRANSCOM NETWORK_TYPES          = " + USTRANSCOM.getNetworkType());
      System.out.println();
      System.out.println               ("USTRANSCOM INFRASTRUCTURE_TYPES   = " + USTRANSCOM.getInfrastructureType());
      System.out.println();
      System.out.println               ("USTRANSCOM OPERATING_SYSTEM_TYPES = " + USTRANSCOM.getOperatingSystemType());
      System.out.println();
      System.out.println               ("USTRANSCOM INTEROPERABILITY_TYPES = " + USTRANSCOM.getInterOperabilityType());
      System.out.println();
      System.out.println               ("USTRANSCOM USER_TYPES             = " + USTRANSCOM.getUsersType());
      System.out.println();
      System.out.println               ("USTRANSCOM BEHAVIOUR_TYPES        = " + USTRANSCOM.getBehavioursType());
      System.out.println();
      System.out.println               ("USTRANSCOM PLATFORM_TYPES         = " + USTRANSCOM.getPlatformType());
     
      System.out.println();
     
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USTRANSCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USTRANSCOM CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR USTRANSCOM: ");
         System.out.println();
  
  // *****************Information Types***************

        USTRANSCOM.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

      
//**************** Display the USTRANSCOM IOT INFORMATION TYPES****************

     
      System.out.println    ("USTRANSCOM INFORMATION-TYPES = " + USTRANSCOM.getInformationType());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USTRANSCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USTRANSCOM CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR USTRANSCOM: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         USTRANSCOM.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        
         System.out.println   ("USTRANSCOM DEVICE-TYPES = " + USTRANSCOM.getDeviceType());
    

         
         System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USTRANSCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USTRANSCOM CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR USTRANSCOM: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      USTRANSCOM.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

       

      System.out.println("USTRANSCOM PLATFORM-TYPES = " + USTRANSCOM.getPlatformType());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USTRANSCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USTRANSCOM CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR USTRANSCOM:");
 
         System.out.println();
       
       

  // ****************Processor Types*******************
  
  
     USTRANSCOM.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      

      System.out.println("USTRANSCOM PROCESSOR-TYPES = " + USTRANSCOM.getProcessorType());
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USTRANSCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USTRANSCOM CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR USTRANSCOM: ");
          System.out.println();
         

  // ***************************NETWORK TYPES*************************
 

        USTRANSCOM.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("USTRANSCOM NETWORK-TYPES = " + USTRANSCOM.getNetworkType());
               
        System.out.println();
        System.out.println("************************************************************************************************" );
        System.out.println();
        System.out.println( "TO CONTINUE WITH NEXT USTRANSCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USTRANSCOM CHOICE # 2");
        System.out.println();
        System.out.println("************************************************************************************************" );
        

      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println();
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR USTRANSCOM: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE TYPES*******************
 
 
          USTRANSCOM.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          
          System.out.println ("USTRANSCOM INFRASTRUCTURE-TYPES = " + USTRANSCOM.getInfrastructureType());
          
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USTRANSCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USTRANSCOM CHOICE # 2");
          System.out.println();
          System.out.println("************************************************************************************************" );
         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR USTRANSCOM:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
           USTRANSCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
           System.out.println       ("USTRANSCOM OperatingSystem type  = " + USTRANSCOM.getOperatingSystemType());
  
              
               
              

               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println( "TO CONTINUE WITH NEXT USTRANSCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USTRANSCOM CHOICE # 2");
               System.out.println();
               System.out.println("************************************************************************************************" );

         

      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println();

           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR USTRANSCOM: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
          USTRANSCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          
          System.out.println ("USTRANSCOM INTEROPERABILITY-TYPES = " + USTRANSCOM.getInterOperabilityType());
         
          System.out.println();
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USTRANSCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USTRANSCOM CHOICE # 2");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


      }

else
   
      if (menuSelect == 10)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT USERS-TYPES FOR USTRANSCOM: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          USTRANSCOM.setUser       ("Stakeholders Across the Enterprise");
 
         
         System.out.println     ("USTRANSCOM USERS-TYPES = " + USTRANSCOM.getUsersType());
         System.out.println();
         
            
       System.out.println();
       System.out.println("************************************************************************************************" );
       System.out.println();
       System.out.println( "TO CONTINUE WITH NEXT USTRANSCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USTRANSCOM CHOICE # 2");
       System.out.println();
       System.out.println("************************************************************************************************" );

          

 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR USTRANSCOM: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          USTRANSCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("USTRANSCOM BEHAVIOURS-TYPES = " + USTRANSCOM.getBehavioursType());
          System.out.println();
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USTRANSCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USTRANSCOM CHOICE # 2");
          System.out.println();
          System.out.println("************************************************************************************************" );

          }
                    
          else
            
   
  
  
// ******************Display the Main menu************************************

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");

       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 10) 
  
{
 
 
 System.out.println();
 System.out.println("THIS IS INVALID COCOM'S CHOICE# "); 
 System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();

  
 } 


break; 

//*************************USSTRATCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************

case 3:

 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED USSTRATCOM IOT TAXONOMY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW USSTRATCOM IOT TAXONOMY");
 System.out.println();

InterNetOfThings USSTRATCOM;

//  Following statement creates an object using the InterNetOfThings class as
//its Blueprint. Centcom will reference the object.

USSTRATCOM = new InterNetOfThings();

//*****************DISPLAY THE COCOMS IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USSTRATCOM.");
 System.out.println();
 System.out.println("2.  USSTRATCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USSTRATCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USSTRATCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USSTRATCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USSTRATCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USSTRATCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USSTRATCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USSTRATCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USSTRATCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USSTRATCOM BEHAVIOURS_TYPES.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println("************************************************************************************************" );
  
 System.out.println("THIS IS INVALID SELECTION"); 
 System.out.println();
 System.out.println("ENTER YOUR IOT MENU SELECTION FROM 1 to 11: ");
 System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USSTRATCOM.");
 System.out.println();
 System.out.println("2.  USSTRATCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USSTRATCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USSTRATCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USSTRATCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USSTRATCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USSTRATCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USSTRATCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USSTRATCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USSTRATCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USSTRATCOM BEHAVIOURS_TYPES.");


  System.out.println();
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print("ENTER YOUR CHOICE FROM 1 to 11: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - USSTRATCOM: ");
          System.out.println();
          
          USSTRATCOM.setInformation           ("Classified and Unclassified; Standardized with common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for Decision Support, Visualization Algorithms, Distribution Contexts; lost data from business failure");

          USSTRATCOM.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");

          USSTRATCOM.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");

          USSTRATCOM.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");

          USSTRATCOM.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

          USSTRATCOM.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");


         USSTRATCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         USSTRATCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

         USSTRATCOM.setUser                  ("Stakeholders across the enterprise");
   
         USSTRATCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
       


// Display the Centcom IOT taxonomy values stored in the fields

     
      System.out.println               ("USSTRATCOM INFORMATION-TYPES      = " + USSTRATCOM.getInformationType());
      System.out.println();
      System.out.println               ("USSTRATCOM DEVICE_TYPES           = " + USSTRATCOM.getDeviceType());
      System.out.println();
      System.out.println               ("USSTRATCOM PROCESSOR_TYPES        = " + USSTRATCOM.getProcessorType());
      System.out.println();
      System.out.println               ("USSTRATCOM NETWORK_TYPES          = " + USSTRATCOM.getNetworkType());
      System.out.println();
      System.out.println               ("USSTRATCOM INFRASTRUCTURE_TYPES   = " + USSTRATCOM.getInfrastructureType());
      System.out.println();
      System.out.println               ("USSTRATCOM OPERATING_SYSTEM_TYPES = " + USSTRATCOM.getOperatingSystemType());
      System.out.println();
      System.out.println               ("USSTRATCOM INTEROPERABILITY_TYPES = " + USSTRATCOM.getInterOperabilityType());
      System.out.println();
      System.out.println               ("USSTRATCOM USER_TYPES             = " + USSTRATCOM.getUsersType());
      System.out.println();
      System.out.println               ("USSTRATCOM BEHAVIOUR_TYPES        = " + USSTRATCOM.getBehavioursType());
      System.out.println();
      System.out.println               ("USSTRATCOM PLATFORM_TYPES         = " + USSTRATCOM.getPlatformType());
      System.out.println();
      System.out.println();
      
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSTRATCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSTRATCOM CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR USSTRATCOM: ");
         
         System.out.println();
  
  // *****************Information Types***************

        USSTRATCOM.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

      
//**************** Display the USTRANSCOM IOT INFORMATION TYPES****************

     
      System.out.println    ("USSTRATCOM INFORMATION-TYPES = " + USSTRATCOM.getInformationType());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSTRATCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSTRATCOM CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR USSTRATCOM: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         USSTRATCOM.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        
         System.out.println   ("USSTRATCOM DEVICE-TYPES = " + USSTRATCOM.getDeviceType());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSTRATCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSTRATCOM CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR USSTRATCOM: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      USSTRATCOM.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

       

      System.out.println("USSTRATCOM PLATFORM-TYPES = " + USSTRATCOM.getPlatformType());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSTRATCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSTRATCOM CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR USSTRATCOM:");
 
         System.out.println();
       
       

  // ****************Processor Types*******************
  
  
     USSTRATCOM.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      

      System.out.println("USSTRATCOM PROCESSOR-TYPES = " + USSTRATCOM.getProcessorType());
      System.out.println();
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSTRATCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSTRATCOM CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR USSTRATCOM: ");
          System.out.println();
         

  // ***************************NETWORK TYPES*************************
 

       USSTRATCOM.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("USSTRATCOM NETWORK-TYPES = " + USSTRATCOM.getNetworkType());
        System.out.println();
       
        System.out.println();
        System.out.println("************************************************************************************************" );
        System.out.println();
        System.out.println( "TO CONTINUE WITH NEXT USSTRATCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSTRATCOM CHOICE # 3");
        System.out.println();
        System.out.println("************************************************************************************************" );
        

      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println();
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR USSTRATCOM: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE TYPES*******************
 
  
          USSTRATCOM.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          
          System.out.println ("USSTRATCOM INFRASTRUCTURE-TYPES = " + USSTRATCOM.getInfrastructureType());
          
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USSTRATCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSTRATCOM CHOICE # 3");
          System.out.println();
          System.out.println("************************************************************************************************" );
         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR USSTRATCOM:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
               USSTRATCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
               System.out.println       ("USSTRATCOM OperatingSystem type  = " + USSTRATCOM.getOperatingSystemType());
  
              
               System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENIENCE");
              

               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println( "TO CONTINUE WITH NEXT USSTRATCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSTRATCOM CHOICE # 3");
               System.out.println();
               System.out.println("************************************************************************************************" );

         

      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println();

           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR USSTRATCOM: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
          USSTRATCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          
          System.out.println ("USSTRATCOM INTEROPERABILITY-TYPES = " + USSTRATCOM.getInterOperabilityType());
         
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USSTRATCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSTRATCOM CHOICE # 3");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


      }

else
   
      if (menuSelect == 10)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT USERS-TYPES FOR USSTRATCOM: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          USSTRATCOM.setUser       ("Stakeholders Across the Enterprise");
 
         
         System.out.println     ("USSTRATCOM USERS-TYPES = " + USSTRATCOM.getUsersType());
         System.out.println();
         
            
      System.out.println();
     
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSTRATCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSTRATCOM CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

     

 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR USSTRATCOM: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          USSTRATCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("USSTRATCOM BEHAVIOURS-TYPES = " + USSTRATCOM.getBehavioursType());
          System.out.println();
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USSTRATCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSTRATCOM CHOICE # 3");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


          }
          else
            
   
  
  
// ******************Display the Main menu************************************

      System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");
       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 10) 
  
{
 
 
System.out.println();
System.out.println("THIS IS INVALID COCOM'S CHOICE# "); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();


 } 


break;

//*************************USAFRICOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************


case 4:

 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED USAFRICOM IOT TAXONOMY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW USAFRICOM IOT TAXONOMY");
 System.out.println();

InterNetOfThings USAFRICOM;

//  Following statement creates an object using the InterNetOfThings class as
//its Blueprint. Centcom will reference the object.

USAFRICOM = new InterNetOfThings();

//*****************DISPLAY THE COCOMS IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USAFRICOM.");
 System.out.println();
 System.out.println("2.  USAFRICOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USAFRICOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USAFRICOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USAFRICOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USAFRICOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USAFRICOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USAFRICOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USAFRICOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USAFRICOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USAFRICOM BEHAVIOURS_TYPES.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("THIS IS INVALID SELECTION"); 
 System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USAFRICOM.");
 System.out.println();
 System.out.println("2.  USAFRICOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USAFRICOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USAFRICOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USAFRICOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USAFRICOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USAFRICOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USAFRICOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USAFRICOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USAFRICOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USAFRICOM BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print("ENTER YOUR CHOICE FROM 1 to 11: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - USAFRICOM: ");
          System.out.println();
          
          USAFRICOM.setInformation           ("Classified and Unclassified; Standardized with common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for Decision Support, Visualization Algorithms, Distribution Contexts; lost data from business failure");

          USAFRICOM.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");

          USAFRICOM.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");

          USAFRICOM.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");

          USAFRICOM.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

          USAFRICOM.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");


          USAFRICOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         USAFRICOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

         USAFRICOM.setUser                  ("Stakeholders across the enterprise");
   
         USAFRICOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
       


// Display the Centcom IOT taxonomy values stored in the fields

     
      System.out.println               ("USAFRICOM INFORMATION-TYPES      = " + USAFRICOM.getInformationType());
      System.out.println();
      System.out.println               ("USAFRICOM DEVICE_TYPES           = " + USAFRICOM.getDeviceType());
      System.out.println();
      System.out.println               ("USAFRICOM PROCESSOR_TYPES        = " + USAFRICOM.getProcessorType());
      System.out.println();
      System.out.println               ("USAFRICOM NETWORK_TYPES          = " + USAFRICOM.getNetworkType());
      System.out.println();
      System.out.println               ("USAFRICOM INFRASTRUCTURE_TYPES   = " + USAFRICOM.getInfrastructureType());
      System.out.println();
      System.out.println               ("USAFRICOM OPERATING_SYSTEM_TYPES = " + USAFRICOM.getOperatingSystemType());
      System.out.println();
      System.out.println               ("USAFRICOM INTEROPERABILITY_TYPES = " + USAFRICOM.getInterOperabilityType());
      System.out.println();
      System.out.println               ("USAFRICOM USER_TYPES             = " + USAFRICOM.getUsersType());
      System.out.println();
      System.out.println               ("USAFRICOM BEHAVIOUR_TYPES        = " + USAFRICOM.getBehavioursType());
      System.out.println();
      System.out.println               ("USAFRICOM PLATFORM_TYPES         = " + USAFRICOM.getPlatformType());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USAFRICOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USAFRICOM CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR USAFRICOM: ");
         System.out.println();
  
  // *****************Information Types***************

        USAFRICOM.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

      
//**************** Display the USAFRICOM IOT INFORMATION TYPES****************

     
      System.out.println    ("USAFRICOM INFORMATION-TYPES = " + USAFRICOM.getInformationType());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USAFRICOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USAFRICOM CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         //System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR USAFRICOM: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         USAFRICOM.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        
         System.out.println   ("USAFRICOM DEVICE-TYPES = " + USAFRICOM.getDeviceType());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USAFRICOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USAFRICOM CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR USAFRICOM: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      USAFRICOM.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

       

      System.out.println("USAFRICOM PLATFORM-TYPES = " + USAFRICOM.getPlatformType());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USAFRICOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USAFRICOM CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR USAFRICOM:");
 
         System.out.println();
       
       

  // ****************Processor Types*******************
  
  
     USAFRICOM.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      

      System.out.println("USAFRICOM PROCESSOR-TYPES = " + USAFRICOM.getProcessorType());
      System.out.println();
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USAFRICOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USAFRICOM CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR USAFRICOM: ");
          System.out.println();
         

  // ***************************NETWORK TYPES*************************
 

       USAFRICOM.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("USAFRICOM NETWORK-TYPES = " + USAFRICOM.getNetworkType());
        System.out.println();
       
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USAFRICOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USAFRICOM CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );
        

      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println();
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR USAFRICOM: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE TYPES*******************
 
  
          USAFRICOM.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          
          System.out.println ("USAFRICOM INFRASTRUCTURE-TYPES = " + USAFRICOM.getInfrastructureType());
          
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USAFRICOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USAFRICOM CHOICE # 4");
          System.out.println();
          System.out.println("************************************************************************************************" );
         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR USAFRICOM:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
            USAFRICOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
            System.out.println       ("USAFRICOM OperatingSystem type  = " + USAFRICOM.getOperatingSystemType());
  
              
               System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENIENCE");
              

               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println( "TO CONTINUE WITH NEXT USAFRICOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USAFRICOM CHOICE # 4");
               System.out.println();
               System.out.println("************************************************************************************************" );

         

      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println();
           
           System.out.println("************************************************************************************************" );
           System.out.println();

           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR USAFRICOM: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
          USAFRICOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          
          System.out.println ("USAFRICOM INTEROPERABILITY-TYPES = " + USAFRICOM.getInterOperabilityType());
         
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USAFRICOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USAFRICOM CHOICE # 4");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


      }

else
   
      if (menuSelect == 10)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT USERS-TYPES FOR USAFRICOM: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          USAFRICOM.setUser       ("Stakeholders Across the Enterprise");
 
         
         System.out.println     ("USAFRICOM USERS-TYPES = " + USAFRICOM.getUsersType());
         System.out.println();
         
            
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USAFRICOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USAFRICOM CHOICE # 4");
      System.out.println();
      System.out.println("************************************************************************************************" );

          

 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR USAFRICOM: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
        USAFRICOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("USAFRICOM BEHAVIOURS-TYPES = " + USAFRICOM.getBehavioursType());
          System.out.println();
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USAFRICOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USAFRICOM CHOICE # 4");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


          }
          else
            
   
  
  
// ******************Display the Main menu************************************

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");

       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 10) 
  
{
 
 
System.out.println();
System.out.println("THIS IS INVALID COCOM'S CHOICE# "); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");
    
  menuSelection = keyboard.nextInt();
 
 } 


break;

//*************************USCENTCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************


case 5:

 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED USCENTCOM IOT TAXONOMY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW USCENTCOM IOT TAXONOMY");
 System.out.println();

InterNetOfThings USCENTCOM;

//  Following statement creates an object using the InterNetOfThings class as
//its Blueprint. Centcom will reference the object.

USCENTCOM = new InterNetOfThings();

//*****************DISPLAY THE COCOMS IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USCENTCOM.");
 System.out.println();
 System.out.println("2.  USCENTCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USCENTCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USCENTCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USCENTCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USCENTCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USCENTCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USCENTCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USCENTCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USCENTCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USCENTCOM BEHAVIOURS_TYPES.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("THIS IS INVALID SELECTION"); 
 System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USCENTCOM.");
 System.out.println();
 System.out.println("2.  USCENTCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USCENTCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USCENTCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USCENTCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USCENTCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USCENTCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USCENTCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USCENTCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USCENTCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USCENTCOM BEHAVIOURS_TYPES.");


 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print("ENTER YOUR CHOICE FROM 1 to 11: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - USCENTCOM: ");
          System.out.println();
          
          USCENTCOM.setInformation           ("Classified and Unclassified; Standardized with common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for Decision Support, Visualization Algorithms, Distribution Contexts; lost data from business failure");

          USCENTCOM.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");

          USCENTCOM.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");

          USCENTCOM.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");

          USCENTCOM.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

          USCENTCOM.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");


         USCENTCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         USCENTCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

         USCENTCOM.setUser                  ("Stakeholders across the enterprise");
   
         USCENTCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
       


// Display the Centcom IOT taxonomy values stored in the fields

     
      System.out.println               ("USCENTCOM INFORMATION-TYPES      = " + USCENTCOM.getInformationType());
      System.out.println();
      System.out.println               ("USCENTCOM DEVICE_TYPES           = " + USCENTCOM.getDeviceType());
      System.out.println();
      System.out.println               ("USCENTCOM PROCESSOR_TYPES        = " + USCENTCOM.getProcessorType());
      System.out.println();
      System.out.println               ("USCENTCOM NETWORK_TYPES          = " + USCENTCOM.getNetworkType());
      System.out.println();
      System.out.println               ("USCENTCOM INFRASTRUCTURE_TYPES   = " + USCENTCOM.getInfrastructureType());
      System.out.println();
      System.out.println               ("USCENTCOM OPERATING_SYSTEM_TYPES = " + USCENTCOM.getOperatingSystemType());
      System.out.println();
      System.out.println               ("USCENTCOM INTEROPERABILITY_TYPES = " + USCENTCOM.getInterOperabilityType());
      System.out.println();
      System.out.println               ("USCENTCOM USER_TYPES             = " + USCENTCOM.getUsersType());
      System.out.println();
      System.out.println               ("USCENTCOM BEHAVIOUR_TYPES        = " + USCENTCOM.getBehavioursType());
      System.out.println();
      System.out.println               ("USCENTCOM PLATFORM_TYPES         = " + USCENTCOM.getPlatformType());
      System.out.println();
      System.out.println();
     
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USCENTCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCENTCOM CHOICE # 5");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR USCENTCOM: ");
         System.out.println();
  
  // *****************Information Types***************

        USCENTCOM.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

      
//**************** Display the USAFRICOM IOT INFORMATION TYPES****************

     
      System.out.println    ("USCENTCOM INFORMATION-TYPES = " + USCENTCOM.getInformationType());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USCENTCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCENTCOM CHOICE # 5");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR USCENTCOM: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         USCENTCOM.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        
         System.out.println   ("USCENTCOM DEVICE-TYPES = " + USCENTCOM.getDeviceType());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USCENTCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCENTCOM CHOICE # 5");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR USCENTCOM: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      USCENTCOM.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

       

      System.out.println("USCENTCOM PLATFORM-TYPES = " + USCENTCOM.getPlatformType());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USCENTCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCENTCOM CHOICE # 5");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR USCENTCOM:");
 
         System.out.println();
       
       

  // ****************Processor Types*******************
  
  
     USCENTCOM.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      

      System.out.println("USCENTCOM PROCESSOR-TYPES = " + USCENTCOM.getProcessorType());
      System.out.println();
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USCENTCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCENTCOM CHOICE # 5");
      System.out.println();
      System.out.println("************************************************************************************************" );

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR USCENTCOM: ");
          System.out.println();
         

  // ***************************NETWORK TYPES*************************
 

       USCENTCOM.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
      System.out.println("USCENTCOM NETWORK-TYPES = " + USCENTCOM.getNetworkType());
             
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USCENTCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCENTCOM CHOICE # 5");
      System.out.println();
      System.out.println("************************************************************************************************" );
        

      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println();
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR USCENTCOM: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE TYPES*******************
 
  
          USCENTCOM.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          
          System.out.println ("USCENTCOM INFRASTRUCTURE-TYPES = " + USCENTCOM.getInfrastructureType());
          
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USCENTCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCENTCOM CHOICE # 5");
          System.out.println();
          System.out.println("************************************************************************************************" );
         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR USCENTCOM:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
               USCENTCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
               System.out.println       ("USCENTCOM OperatingSystem type  = " + USCENTCOM.getOperatingSystemType());
  
              
               System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENIENCE");
              

               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println( "TO CONTINUE WITH NEXT USCENTCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCENTCOM CHOICE # 5");
               System.out.println();
               System.out.println("************************************************************************************************" );

         

      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println();

           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR USCENTCOM: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
          USCENTCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          
          System.out.println ("USCENTCOM INTEROPERABILITY-TYPES = " + USCENTCOM.getInterOperabilityType());
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USCENTCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCENTCOM CHOICE # 5");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


      }

else
   
      if (menuSelect == 10)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT USERS-TYPES FOR USAFRICOM: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          USCENTCOM.setUser       ("Stakeholders Across the Enterprise");
 
         
         System.out.println     ("USCENTCOM USERS-TYPES = " + USCENTCOM.getUsersType());
         System.out.println();
         
            
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USCENTCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCENTCOM CHOICE # 5");
      System.out.println();
      System.out.println("************************************************************************************************" );

          

 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR USCENTCOM: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
        USCENTCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("USCENTCOM BEHAVIOURS-TYPES = " + USCENTCOM.getBehavioursType());
          System.out.println();
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USCENTCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCENTCOM CHOICE # 5");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


          }
          else
            
   
  
  
// ******************Display the Main menu************************************

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");
       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 10) 
  
{
 
 
System.out.println();
System.out.println("THIS IS INVALID COCOM'S CHOICE# "); 
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");

   

  
  menuSelection = keyboard.nextInt();
 } 


break;

//*************************USEUCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************


case 6:

 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED USEUCOM IOT TAXONOMY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW USEUCOM IOT TAXONOMY");
 System.out.println();

InterNetOfThings USEUCOM;

//  Following statement creates an object using the InterNetOfThings class as
//its Blueprint. Centcom will reference the object.

USEUCOM = new InterNetOfThings();

//*****************DISPLAY THE COCOMS IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USEUCOM.");
 System.out.println();
 System.out.println("2.  USEUCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USEUCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USEUCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USEUCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USEUCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USEUCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USEUCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USEUCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USEUCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USEUCOM BEHAVIOURS_TYPES.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("THIS IS INVALID SELECTION"); 
 System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USEUCOM.");
 System.out.println();
 System.out.println("2.  USEUCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USEUCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USEUCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USEUCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USEUCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USEUCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USEUCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USEUCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USEUCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USEUCOM BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print("ENTER YOUR CHOICE FROM 1 to 11: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - USEUCOM: ");
          System.out.println();
          
          USEUCOM.setInformation           ("Classified and Unclassified; Standardized with common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for Decision Support, Visualization Algorithms, Distribution Contexts; lost data from business failure");

          USEUCOM.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");

          USEUCOM.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");

          USEUCOM.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");

          USEUCOM.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

          USEUCOM.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");


         USEUCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         USEUCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

         USEUCOM.setUser                  ("Stakeholders across the enterprise");
   
         USEUCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
       


// Display the Centcom IOT taxonomy values stored in the fields

     
      System.out.println               ("USEUCOM INFORMATION-TYPES      = " + USEUCOM.getInformationType());
      System.out.println();
      System.out.println               ("USEUCOM DEVICE_TYPES           = " + USEUCOM.getDeviceType());
      System.out.println();
      System.out.println               ("USEUCOM PROCESSOR_TYPES        = " + USEUCOM.getProcessorType());
      System.out.println();
      System.out.println               ("USCENTCOM NETWORK_TYPES        = " + USEUCOM.getNetworkType());
      System.out.println();
      System.out.println               ("USEUCOM INFRASTRUCTURE_TYPES   = " + USEUCOM.getInfrastructureType());
      System.out.println();
      System.out.println               ("USEUCOM OPERATING_SYSTEM_TYPES = " + USEUCOM.getOperatingSystemType());
      System.out.println();
      System.out.println               ("USEUCOM INTEROPERABILITY_TYPES = " + USEUCOM.getInterOperabilityType());
      System.out.println();
      System.out.println               ("USEUCOM USER_TYPES             = " + USEUCOM.getUsersType());
      System.out.println();
      System.out.println               ("USEUCOM BEHAVIOUR_TYPES        = " + USEUCOM.getBehavioursType());
      System.out.println();
      System.out.println               ("USEUCOM PLATFORM_TYPES         = " + USEUCOM.getPlatformType());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USEUCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USEUCOM CHOICE # 6");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR USEUCOM: ");
         System.out.println();
  
  // *****************Information Types***************

        USEUCOM.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

      
//**************** Display the USAFRICOM IOT INFORMATION TYPES****************

     
      System.out.println    ("USEUCOM INFORMATION-TYPES = " + USEUCOM.getInformationType());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USEUCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USEUCOM CHOICE # 6");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR USEUCOM: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         USEUCOM.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        
         System.out.println   ("USEUCOM DEVICE-TYPES = " + USEUCOM.getDeviceType());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USEUCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USEUCOM CHOICE # 6");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR USEUCOM: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      USEUCOM.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

       

      System.out.println("USEUCOM PLATFORM-TYPES = " + USEUCOM.getPlatformType());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USEUCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USEUCOM CHOICE # 6");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR USEUCOM:");
 
         System.out.println();
       
       

  // ****************Processor Types*******************
  
  
     USEUCOM.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      

      System.out.println("USEUCOM PROCESSOR-TYPES = " + USEUCOM.getProcessorType());
      System.out.println();
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USEUCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USEUCOM CHOICE # 6");
      System.out.println();
      System.out.println("************************************************************************************************" );

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR USEUCOM: ");
          System.out.println();
         

  // ***************************NETWORK TYPES*************************
 

       USEUCOM.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
      System.out.println("USEUCOM NETWORK-TYPES = " + USEUCOM.getNetworkType());
      System.out.println();
       
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USEUCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USEUCOM CHOICE # 6");
      System.out.println();
      System.out.println("************************************************************************************************" );
        

      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println();
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR USEUCOM: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE TYPES*******************
 
  
          USEUCOM.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          
          System.out.println ("USEUCOM INFRASTRUCTURE-TYPES = " + USEUCOM.getInfrastructureType());
          
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USEUCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USEUCOM CHOICE # 6");
          System.out.println();
          System.out.println("************************************************************************************************" );
         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR USEUCOM:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
            USEUCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
            System.out.println       ("USEUCOM OperatingSystem type  = " + USEUCOM.getOperatingSystemType());
  
              
               System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENIENCE");
              

               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println( "TO CONTINUE WITH NEXT USEUCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USEUCOM CHOICE # 6");
               System.out.println();
               System.out.println("************************************************************************************************" );

         

      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println();

           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR USEUCOM: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
          USEUCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          
          System.out.println ("USEUCOM INTEROPERABILITY-TYPES = " + USEUCOM.getInterOperabilityType());
         
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USEUCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USEUCOM CHOICE # 6");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


      }

else
   
      if (menuSelect == 10)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT USERS-TYPES FOR USEUCOM: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          USEUCOM.setUser       ("Stakeholders Across the Enterprise");
 
         
         System.out.println     ("USEUCOM USERS-TYPES = " + USEUCOM.getUsersType());
         System.out.println();
         
            
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USEUCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USEUCOM CHOICE # 6");
      System.out.println();
      System.out.println("************************************************************************************************" );

          

 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR USEUCOM: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
        USEUCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("USEUCOM BEHAVIOURS-TYPES = " + USEUCOM.getBehavioursType());
         
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USEUCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USEUCOM CHOICE # 6");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


          }
          
          else
            
   
  
  
// ******************Display the Main menu************************************

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");

       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 10) 
  
{
 
 
System.out.println();
System.out.println("THIS IS INVALID COCOM'S CHOICE# "); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();

  } 


break;


//*************************USNORTHCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************


case 7:

 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED USNORTHCOM IOT TAXONOMY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW USNORTHCOM IOT TAXONOMY");
 System.out.println();

InterNetOfThings USNORTHCOM;

//  Following statement creates an object using the InterNetOfThings class as
//its Blueprint. Centcom will reference the object.

USNORTHCOM = new InterNetOfThings();

//*****************DISPLAY THE COCOMS IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USNORTHCOM.");
 System.out.println();
 System.out.println("2.  USNORTHCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USNORTHCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USNORTHCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USNORTHCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USNORTHCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USNORTHCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USNORTHCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USNORTHCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USNORTHCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USNORTHCOM BEHAVIOURS_TYPES.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("THIS IS INVALID SELECTION"); 
 System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USNORTHCOM.");
 System.out.println();
 System.out.println("2.  USNORTHCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USNORTHCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USNORTHCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USNORTHCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USNORTHCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USNORTHCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USNORTHCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USNORTHCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USNORTHCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USNORTHCOM BEHAVIOURS_TYPES.");

 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
  System.out.print("ENTER YOUR CHOICE FROM 1 to 11: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - USNORTHCOM: ");
          System.out.println();
          
          USNORTHCOM.setInformation           ("Classified and Unclassified; Standardized with common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for Decision Support, Visualization Algorithms, Distribution Contexts; lost data from business failure");

          USNORTHCOM.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");

          USNORTHCOM.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");

          USNORTHCOM.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");

          USNORTHCOM.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

          USNORTHCOM.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");


         USNORTHCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         USNORTHCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

         USNORTHCOM.setUser                  ("Stakeholders across the enterprise");
   
         USNORTHCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
       


// Display the Centcom IOT taxonomy values stored in the fields

     
      System.out.println               ("USNORTHCOM INFORMATION-TYPES      = " + USNORTHCOM.getInformationType());
      System.out.println();
      System.out.println               ("USNORTHCOM DEVICE_TYPES           = " + USNORTHCOM.getDeviceType());
      System.out.println();
      System.out.println               ("USNORTHCOM PROCESSOR_TYPES        = " + USNORTHCOM.getProcessorType());
      System.out.println();
      System.out.println               ("USNORTHCOM NETWORK_TYPES          = " + USNORTHCOM.getNetworkType());
      System.out.println();
      System.out.println               ("USNORTHCOM INFRASTRUCTURE_TYPES   = " + USNORTHCOM.getInfrastructureType());
      System.out.println();
      System.out.println               ("USNORTHCOM OPERATING_SYSTEM_TYPES = " + USNORTHCOM.getOperatingSystemType());
      System.out.println();
      System.out.println               ("USNORTHCOM INTEROPERABILITY_TYPES = " + USNORTHCOM.getInterOperabilityType());
      System.out.println();
      System.out.println               ("USNORTHCOM USER_TYPES             = " + USNORTHCOM.getUsersType());
      System.out.println();
      System.out.println               ("USNORTHCOM BEHAVIOUR_TYPES        = " + USNORTHCOM.getBehavioursType());
      System.out.println();      
      System.out.println               ("USNORTHCOM PLATFORM_TYPES         = " + USNORTHCOM.getPlatformType());
     
      System.out.println();
     
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USNORTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USNORTHCOM CHOICE # 7");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR USNORTHCOM: ");
         System.out.println();
  
  // *****************Information Types***************

        USNORTHCOM.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

      
//**************** Display the USAFRICOM IOT INFORMATION TYPES****************

     
      System.out.println    ("USNORTHCOM INFORMATION-TYPES = " + USNORTHCOM.getInformationType());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USNORTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USNORTHCOM CHOICE # 7");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR USNORTHCOM: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         USNORTHCOM.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        
      System.out.println   ("USNORTHCOM DEVICE-TYPES = " + USNORTHCOM.getDeviceType());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USNORTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USNORTHCOM CHOICE # 7");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR USNORTHCOM: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      USNORTHCOM.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

       

      System.out.println("USNORTHCOM PLATFORM-TYPES = " + USNORTHCOM.getPlatformType());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USNORTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USNORTHCOM CHOICE # 7");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR USNORTHCOM:");
 
         System.out.println();
       
       

  // ****************Processor Types*******************
  
  
     USNORTHCOM.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      

      System.out.println("USNORTHCOM PROCESSOR-TYPES = " + USNORTHCOM.getProcessorType());
      System.out.println();
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USNORTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USNORTHCOM CHOICE # 7");
      System.out.println();
      System.out.println("************************************************************************************************" );

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR USNORTHCOM: ");
          System.out.println();
         

  // ***************************NETWORK TYPES*************************
 

       USNORTHCOM.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
      System.out.println("USNORTHCOM NETWORK-TYPES = " + USNORTHCOM.getNetworkType());
      System.out.println();
       
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USNORTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USNORTHCOM CHOICE # 7");
      System.out.println();
      System.out.println("************************************************************************************************" );
        

      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println();
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR USNORTHCOM: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE TYPES*******************
 
  
          USNORTHCOM.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          
          System.out.println ("USNORTHCOM INFRASTRUCTURE-TYPES = " + USNORTHCOM.getInfrastructureType());
          
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USNORTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USNORTHCOM CHOICE # 7");
          System.out.println();
          System.out.println("************************************************************************************************" );
         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR USNORTHCOM:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
              USNORTHCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
              System.out.println            ("USEUCOM OperatingSystem type  = " + USNORTHCOM.getOperatingSystemType());
  
              
               
              

               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println( "TO CONTINUE WITH NEXT USNORTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USNORTHCOM CHOICE # 7");
               System.out.println();
               System.out.println("************************************************************************************************" );

         

      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println();

           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR USNORTHCOM: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
          USNORTHCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          
          System.out.println ("USNORTHCOM INTEROPERABILITY-TYPES = " + USNORTHCOM.getInterOperabilityType());
         
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USNORTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USNORTHCOM CHOICE # 7");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


      }

else
   
      if (menuSelect == 10)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT USERS-TYPES FOR USNORTHCOM: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          USNORTHCOM.setUser       ("Stakeholders Across the Enterprise");
 
         
         System.out.println     ("USNORTHCOM USERS-TYPES = " + USNORTHCOM.getUsersType());
         System.out.println();
         
            
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USNORTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USNORTHCOM CHOICE # 7");
      System.out.println();
      System.out.println("************************************************************************************************" );

          

 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR USNORTHCOM: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
        USNORTHCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("USNORTHCOM BEHAVIOURS-TYPES = " + USNORTHCOM.getBehavioursType());
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USNORTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USNORTHCOM CHOICE # 7");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


          }
          else
            
   
  
  
// ******************Display the Main menu************************************

      System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");


       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 10) 
  
{
 
 
 System.out.println();
 System.out.println("THIS IS INVALID COCOM'S CHOICE# "); 
 System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();
    
 } 



break;


//*************************USPACOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************


case 8:

 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED USPACOM IOT TAXONOMY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW USPACOM IOT TAXONOMY");
 System.out.println();

InterNetOfThings USPACOM;

//  Following statement creates an object using the InterNetOfThings class as
//its Blueprint. Centcom will reference the object.

USPACOM = new InterNetOfThings();

//*****************DISPLAY THE COCOMS IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USPACOM.");
 System.out.println();
 System.out.println("2.  USPACOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USPACOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USPACOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USPACOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USPACOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USPACOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USPACOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USPACOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USPACOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USPACOM BEHAVIOURS_TYPES.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("THIS IS INVALID SELECTION"); 
 System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USPACOM.");
 System.out.println();
 System.out.println("2.  USPACOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USPACOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USPACOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USPACOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USPACOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USPACOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USPACOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USPACOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USPACOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USPACOM BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - USPACOM: ");
          System.out.println();
          
          USPACOM.setInformation           ("Classified and Unclassified; Standardized with common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for Decision Support, Visualization Algorithms, Distribution Contexts; lost data from business failure");

          USPACOM.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");

          USPACOM.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");

          USPACOM.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");

          USPACOM.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

          USPACOM.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");


         USPACOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         USPACOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

         USPACOM.setUser                  ("Stakeholders across the enterprise");
   
         USPACOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
       


// Display the USPACOM IOT taxonomy values stored in the fields

     
      System.out.println               ("USPACOM INFORMATION-TYPES      = " + USPACOM.getInformationType());
      System.out.println();
      System.out.println               ("USPACOM DEVICE_TYPES           = " + USPACOM.getDeviceType());
      System.out.println();
      System.out.println               ("USPACOM PROCESSOR_TYPES        = " + USPACOM.getProcessorType());
      System.out.println();
      System.out.println               ("USPACOM NETWORK_TYPES          = " + USPACOM.getNetworkType());
      System.out.println();
      System.out.println               ("USPACOM INFRASTRUCTURE_TYPES   = " + USPACOM.getInfrastructureType());
      System.out.println();
      System.out.println               ("USPACOM OPERATING_SYSTEM_TYPES = " + USPACOM.getOperatingSystemType());
      System.out.println();
      System.out.println               ("USPACOM INTEROPERABILITY_TYPES = " + USPACOM.getInterOperabilityType());
      System.out.println();
      System.out.println               ("USPACOM USER_TYPES             = " + USPACOM.getUsersType());
      System.out.println();
      System.out.println               ("USNORTHCOM BEHAVIOUR_TYPES     = " + USPACOM.getBehavioursType());
      System.out.println();
      System.out.println               ("USPACOM PLATFORM_TYPES         = " + USPACOM.getPlatformType());
     
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USPACOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USPACOM CHOICE # 8");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR USPACOM: ");
         System.out.println();
  
  // *****************Information Types***************

        USPACOM.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

      
//**************** Display the USAFRICOM IOT INFORMATION TYPES****************

     
      System.out.println    ("USPACOM INFORMATION-TYPES = " + USPACOM.getInformationType());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USPACOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USPACOM CHOICE # 8");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         //System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR USPACOM: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         USPACOM.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        
      System.out.println   ("USPACOM DEVICE-TYPES = " + USPACOM.getDeviceType());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USPACOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USPACOM CHOICE # 8");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR USPACOM: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      USPACOM.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

       

      System.out.println("USPACOM PLATFORM-TYPES = " + USPACOM.getPlatformType());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USPACOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USPACOM CHOICE # 8");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR USPACOM:");
 
         System.out.println();
       
       

  // ****************Processor Types*******************
  
  
     USPACOM.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      

      System.out.println("USPACOM PROCESSOR-TYPES = " + USPACOM.getProcessorType());
      System.out.println();
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USPACOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USPACOM CHOICE # 8");
      System.out.println();
      System.out.println("************************************************************************************************" );

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR USPACOM: ");
          System.out.println();
         

  // ***************************NETWORK TYPES*************************
 

       USPACOM.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("USPACOM NETWORK-TYPES = " + USPACOM.getNetworkType());
        System.out.println();
       
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USPACOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USPACOM CHOICE # 8");
      System.out.println();
      System.out.println("************************************************************************************************" );
        

      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println();
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR USPACOM: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE TYPES*******************
 
  
          USPACOM.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          
          System.out.println ("USPACOM INFRASTRUCTURE-TYPES = " + USPACOM.getInfrastructureType());
          
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USPACOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USPACOM CHOICE # 8");
          System.out.println();
          System.out.println("************************************************************************************************" );
         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR USPACOM:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
              USPACOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
              System.out.println       ("USEUCOM OperatingSystem type  = " + USPACOM.getOperatingSystemType());
  
              
              
              

               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println( "TO CONTINUE WITH NEXT USPACOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USPACOM CHOICE # 8");
               System.out.println();
               System.out.println("************************************************************************************************" );

         

      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println();

           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR USPACOM: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
          USPACOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          
          System.out.println ("USPACOM INTEROPERABILITY-TYPES = " + USPACOM.getInterOperabilityType());
         
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USPACOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USPACOM CHOICE # 8");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


      }

else
   
      if (menuSelect == 10)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT USERS-TYPES FOR USPACOM: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          USPACOM.setUser       ("Stakeholders Across the Enterprise");
 
         
         System.out.println     ("USPACOM USERS-TYPES = " + USPACOM.getUsersType());
         System.out.println();
         
            
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USPACOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USPACOM CHOICE # 8");
      System.out.println();
      System.out.println("************************************************************************************************" );

          

 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR USPACOM: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
        USPACOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("USPACOM BEHAVIOURS-TYPES = " + USPACOM.getBehavioursType());
          System.out.println();
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USPACOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USPACOM CHOICE # 8");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


          }
          else
            
   
  
  
// ******************Display the Main menu************************************

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");

       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 10) 
  
{
 
 
System.out.println();
System.out.println("THIS IS INVALID COCOM'S CHOICE# "); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");

   

  
  menuSelection = keyboard.nextInt();
  
  
   } 


break;

//***********************************SEE BELOW CYBERCOM IOT TAXONOMY & FRAMEWORK**************************************

case 9:

 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED USCYBERCOM IOT TAXONOMY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW USCYBERCOM IOT TAXONOMY");
 System.out.println();

InterNetOfThings USCYBERCOM;

//  Following statement creates an object using the InterNetOfThings class as
//its Blueprint. Centcom will reference the object.

USCYBERCOM = new InterNetOfThings();

//*****************DISPLAY THE COCOMS IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USCYBERCOM.");
 System.out.println();
 System.out.println("2.  USCYBERCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USCYBERCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USCYBERCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USCYBERCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USCYBERCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USCYBERCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USCYBERCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USCYBERCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USPACOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USCYBERCOM BEHAVIOURS_TYPES.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("THIS IS INVALID SELECTION"); 
 System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USCYBERCOM.");
 System.out.println();
 System.out.println("2.  USCYBERCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USCYBERCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USCYBERCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USCYBERCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USCYBERCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USCYBERCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USCYBERCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USCYBERCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USCYBERCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USCYBERCOM BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - USCYBERCOM: ");
          System.out.println();
          
          USCYBERCOM.setInformation           ("Classified and Unclassified; Standardized with common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for Decision Support, Visualization Algorithms, Distribution Contexts; lost data from business failure");

          USCYBERCOM.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");

          USCYBERCOM.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");

          USCYBERCOM.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");

          USCYBERCOM.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

          USCYBERCOM.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");


          USCYBERCOM.setOperatingSystem       ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


          USCYBERCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          USCYBERCOM.setUser                  ("Stakeholders across the enterprise");
   
          USCYBERCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
       


// Display the USCYBERCOM IOT taxonomy values stored in the fields

     
      System.out.println               ("USCYBERCOM INFORMATION-TYPES      = " + USCYBERCOM.getInformationType());
      System.out.println();
      System.out.println               ("USCYBERCOM DEVICE_TYPES           = " + USCYBERCOM.getDeviceType());
      System.out.println();
      System.out.println               ("USCYBERCOM PROCESSOR_TYPES        = " + USCYBERCOM.getProcessorType());
      System.out.println();
      System.out.println               ("USCYBERCOM NETWORK_TYPES          = " + USCYBERCOM.getNetworkType());
      System.out.println();
      System.out.println               ("USCYBERCOM INFRASTRUCTURE_TYPES   = " + USCYBERCOM.getInfrastructureType());
      System.out.println();
      System.out.println               ("USCYBERCOM OPERATING_SYSTEM_TYPES = " + USCYBERCOM.getOperatingSystemType());
      System.out.println();
      System.out.println               ("USCYBERCOM INTEROPERABILITY_TYPES = " + USCYBERCOM.getInterOperabilityType());
      System.out.println();
      System.out.println               ("USCYBERCOM USER_TYPES             = " + USCYBERCOM.getUsersType());
      System.out.println();
      System.out.println               ("USCYBERCOM BEHAVIOUR_TYPES        = " + USCYBERCOM.getBehavioursType());
      System.out.println();
      System.out.println               ("USCYBERCOM PLATFORM_TYPES         = " + USCYBERCOM.getPlatformType());
     
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USPACOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCYBERCOM CHOICE # 9");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR USCYBERCOM: ");
         System.out.println();
  
  // *****************Information Types***************

        USCYBERCOM.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

      
//**************** Display the USAFRICOM IOT INFORMATION TYPES****************

     
      System.out.println    ("USCYBERCOM INFORMATION-TYPES = " + USCYBERCOM.getInformationType());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USCYBERCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USPACOM CHOICE # 8");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR USCYBERCOM: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
      USCYBERCOM.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        
      System.out.println   ("USCYBERCOM DEVICE-TYPES = " + USCYBERCOM.getDeviceType());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USCYBERCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCYBERCOM CHOICE # 9");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR USCYBERCOM: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      USCYBERCOM.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

       

      System.out.println("USCYBERCOM PLATFORM-TYPES = " + USCYBERCOM.getPlatformType());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USCYBERCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCYBERCOM CHOICE # 9");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR USCYBERCOM:");
 
         System.out.println();
       
       

  // ****************Processor Types*******************
  
  
     USCYBERCOM.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      

      System.out.println("USCYBERCOM PROCESSOR-TYPES = " + USCYBERCOM.getProcessorType());
      System.out.println();
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USCYBERCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCYBERCOM CHOICE # 9");
      System.out.println();
      System.out.println("************************************************************************************************" );

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR USCYBERCOM: ");
          System.out.println();
         

  // ***************************NETWORK TYPES*************************
 

       USCYBERCOM.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
      System.out.println("USCYBERCOM NETWORK-TYPES = " + USCYBERCOM.getNetworkType());
      System.out.println();
       
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USCYBERCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCYBERCOM CHOICE # 9");
      System.out.println();
      System.out.println("************************************************************************************************" );
        

      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println();
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR USCYBERCOM: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE TYPES*******************
 
  
          USCYBERCOM.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          
          System.out.println ("USCYBERCOM INFRASTRUCTURE-TYPES = " + USCYBERCOM.getInfrastructureType());
          
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USCYBERCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCYBERCOM CHOICE # 9");
          System.out.println();
          System.out.println("************************************************************************************************" );
         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR USCYBERCOM:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
               USCYBERCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
               System.out.println               ("USCYBERCOM OperatingSystem type  = " + USCYBERCOM.getOperatingSystemType());
  
              
               
              

               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println( "TO CONTINUE WITH NEXT USCYBERCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCYBERCOM CHOICE # 9");
               System.out.println();
               System.out.println("************************************************************************************************" );

         

      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println();

           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR USCYBERCOM: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
          USCYBERCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          
          System.out.println ("USCYBERCOM INTEROPERABILITY-TYPES = " + USCYBERCOM.getInterOperabilityType());
         
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USCYBERCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCYBERCOM CHOICE # 9");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


      }

else
   
      if (menuSelect == 10)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT USERS-TYPES FOR USCYBERCOM: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          USCYBERCOM.setUser       ("Stakeholders Across the Enterprise");
 
         
         System.out.println     ("USCYBERCOM USERS-TYPES = " + USCYBERCOM.getUsersType());
         System.out.println();
         
            
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USCYBERCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCYBERCOM CHOICE # 9");
      System.out.println();
      System.out.println("************************************************************************************************" );

          

 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR USCYBERCOM: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
        USCYBERCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("USCYBERCOM BEHAVIOURS-TYPES = " + USCYBERCOM.getBehavioursType());
          System.out.println();
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USCYBERCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USCYBERCOM CHOICE # 9");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


          }
          else
            
   
  
  
// ******************Display the Main menu************************************

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");

       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 10) 
  
{
 
 
System.out.println();
System.out.println("THIS IS INVALID COCOM'S CHOICE# "); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");

   

  
  menuSelection = keyboard.nextInt();
  
  
   } 


break;



//*************************USSOUTHCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************

case 10:

 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED USSOUTHCOM IOT TAXONOMY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW USSOUTHCOM IOT TAXONOMY");
 System.out.println();

InterNetOfThings USSOUTHCOM;

//  Following statement creates an object using the InterNetOfThings class as
//its Blueprint. Centcom will reference the object.

USSOUTHCOM = new InterNetOfThings();

//*****************DISPLAY THE COCOMS IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USSOUTHCOM.");
 System.out.println();
 System.out.println("2.  USSOUTHCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USSOUTHCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USSOUTHCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USSOUTHCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USSOUTHCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USSOUTHCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USSOUTHCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USSOUTHCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USSOUTHCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USSOUTHCOM BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 11)
  

  
{
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.println("THIS IS INVALID SELECTION"); 
  System.out.println();
 System.out.println("1.  SHOW ENTIRE IOT TAXONOMY FOR USSOUTHCOM.");
 System.out.println();
 System.out.println("2.  USSOUTHCOM INFORMATION_TYPES.");
 System.out.println();
 System.out.println("3.  USSOUTHCOM DEVICE_TYPES.");
 System.out.println();
 System.out.println("4.  USSOUTHCOM PLATFORMS_TYPES.");
 System.out.println();
 System.out.println("5.  USSOUTHCOM PROCESSORS_TYPES.");
 System.out.println();
 System.out.println("6.  USSOUTHCOM NETWORK_TYPES.");
 System.out.println();
 System.out.println("7.  USSOUTHCOM INFRASTRUCTURE_TYPES.");
 System.out.println();
 System.out.println("8.  USSOUTHCOM OPERATING_SYSTEM_TYPES.");
 System.out.println();
 System.out.println("9.  USSOUTHCOM INTEROPERABILITY_TYPES.");
 System.out.println();
 System.out.println("10. USSOUTHCOM USERS_TYPES.");
 System.out.println();
 System.out.println("11. USSOUTHCOM BEHAVIOURS_TYPES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 11: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE-IOT-TAXONOMY FOR - USSOUTHCOM: ");
          System.out.println();
          
          USSOUTHCOM.setInformation           ("Classified and Unclassified; Standardized with common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for Decision Support, Visualization Algorithms, Distribution Contexts; lost data from business failure");

          USSOUTHCOM.setDevice                ("Sensors, Actuators, Circuits, Controllers, Processors, Smart Phones, Computers, Tablets, Wearables, Routers, Drones, Thermostats, Refrigerators, Light Bulbs, Aggregators-Zeta Platforms");

          USSOUTHCOM.setPlatform              ("Raspberry PI, BeagleBone, Arduino, FIWARE, other custom platforms");

          USSOUTHCOM.setProcessor             ("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");

          USSOUTHCOM.setNetwork               ("Software Defined Networks (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

          USSOUTHCOM.setInfrastructure        ("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");


         USSOUTHCOM.setOperatingSystem        ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");


         USSOUTHCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

         USSOUTHCOM.setUser                  ("Stakeholders across the enterprise");
   
         USSOUTHCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
       


// Display the USPACOM IOT taxonomy values stored in the fields

     
      System.out.println               ("USSOUTHCOM INFORMATION-TYPES      = " + USSOUTHCOM.getInformationType().toUpperCase());
      System.out.println();
      System.out.println               ("USSOUTHCOM DEVICE_TYPES           = " + USSOUTHCOM.getDeviceType().toUpperCase());
      System.out.println();
      System.out.println               ("USSOUTHCOM PROCESSOR_TYPES        = " + USSOUTHCOM.getProcessorType().toUpperCase());
      System.out.println();
      System.out.println               ("USSOUTHCOM NETWORK_TYPES          = " + USSOUTHCOM.getNetworkType().toUpperCase());
      System.out.println();
      System.out.println               ("USSOUTHCOM INFRASTRUCTURE_TYPES   = " + USSOUTHCOM.getInfrastructureType().toUpperCase());
      System.out.println();
      System.out.println               ("USSOUTHCOM OPERATING_SYSTEM_TYPES = " + USSOUTHCOM.getOperatingSystemType().toUpperCase());
      System.out.println();
      System.out.println               ("USSOUTHCOM INTEROPERABILITY_TYPES = " + USSOUTHCOM.getInterOperabilityType().toUpperCase());
      System.out.println();
      System.out.println               ("USSOUTHCOM USER_TYPES             = " + USSOUTHCOM.getUsersType().toUpperCase());
      System.out.println();
      System.out.println               ("USSOUTHCOM BEHAVIOUR_TYPES        = " + USSOUTHCOM.getBehavioursType().toUpperCase());
      System.out.println();
      System.out.println               ("USSOUTHCOM PLATFORM_TYPES         = " + USSOUTHCOM.getPlatformType().toUpperCase());
      System.out.println();
      System.out.println();
      
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSOUTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOUTHCOM CHOICE # 10");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE IoT INFORMATION-TYPES FOR USSOUTHCOM: ");
         System.out.println();
  
  // *****************Information Types***************

        USSOUTHCOM.setInformation   ("Classified and Unclassified; Standardized with Common Taxonomies, Ontologies, Metadata; Big Data, Ambient Data, Analytics for decision support, visualization algorithms, distribution contexts; lost data from business failure");

      
//**************** Display the USAFRICOM IOT INFORMATION TYPES****************

     
      System.out.println    ("USSOUTHCOM INFORMATION-TYPES = " + USSOUTHCOM.getInformationType().toUpperCase());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSOUTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOUTHCOM CHOICE # 10");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT DEVICES-TYPES FOR USSOUTHCOM: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         USSOUTHCOM.setDevice        ("SENSORS, ACTUATORS, CIRCUITS, CONTROLLERS, PROCESSORS, smart phones, computers, tablets, wearables, routers, drones, thermostats, refrigerators, light bulbs, Aggregators-Zeta Platforms");
 
        
      System.out.println   ("USSOUTHCOM DEVICE-TYPES = " + USSOUTHCOM.getDeviceType().toUpperCase());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSOUTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOUTHCOM CHOICE # 10");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW IoT PLATFORMS-TYPES FOR USSOUTHCOM: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      USSOUTHCOM.setPlatform("RASPBERRY PI, BEAGLEBONE, Arduino, FIWARE, Other Custom Platforms");

       

      System.out.println("USSOUTHCOM PLATFORM-TYPES = " + USSOUTHCOM.getPlatformType().toUpperCase());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSOUTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOUTHCOM CHOICE # 10");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW IoT PROCESSOR-TYPES FOR USSOUTHCOM:");
 
         System.out.println();
       
       

  // ****************Processor Types*******************
  
  
     USSOUTHCOM.setProcessor("Quark; ARC; ARM Cortex-M; ARM Cortex-A; TI Sitara; MSP430");
 
      

      System.out.println("USSOUTHCOM PROCESSOR-TYPES = " + USSOUTHCOM.getProcessorType().toUpperCase());
      System.out.println();
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSOUTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOUTHCOM CHOICE # 10");
      System.out.println();
      System.out.println("************************************************************************************************" );

      
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT NETWORK-TYPES FOR USSOUTHCOM: ");
          System.out.println();
         

  // ***************************NETWORK TYPES*************************
 

       USSOUTHCOM.setNetwork("SOFTWARE DEFINED NETWORKS (SDN); Mesh networking- Thread, CSRMesh; Area networks (body, home, wide); Delay tolerant; Spectrum analysis; Hypernets 802.15.4 Zigbee, Zwave, Bluetooth, Bluetooth Low-Power, NFC, One M2M,DDS, DSRC, 802.11, WiFi, SATCOM, PKE,XMPP-IoT, 6LowPAN, CoAp, LWM2m, MQTT, Cellular, AMQP, IPv6,PANA, EAP, MAC, HART, HIP, HTTP/HTTPS, PCP");

        
        System.out.println("USSOUTHCOM NETWORK-TYPES = " + USSOUTHCOM.getNetworkType().toUpperCase());
        System.out.println();
       
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSOUTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOUTHCOM CHOICE # 10");
      System.out.println();
      System.out.println("************************************************************************************************" );
        

      }

     else
   
        if ( menuSelect == 7)
      
           {
              
              System.out.println();
              System.out.println("************************************************************************************************" );
              System.out.println();

              System.out.println("PLEASE SEE BELOW IoT INFRASTRUCTURE-TYPES FOR USSOUTHCOM: ");
              System.out.println();

  
 // *************************INFRASTRUCTURE TYPES*******************
 
  
          USSOUTHCOM.setInfrastructure("Cisco Iox (fog); Middleware distributed computing ICORE, COMPOSE, WS02,NSF FIA, MIKE 2.0 , SOAP, REST 4");

          
          System.out.println ("USSOUTHCOM INFRASTRUCTURE-TYPES = " + USSOUTHCOM.getInfrastructureType().toUpperCase());
          
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USSOUTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOUTHCOM CHOICE # 10");
          System.out.println();
          System.out.println("************************************************************************************************" );
         
          }

          else
   
            if (menuSelect == 8)
      
             {
               
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW IoT OPERATING-SYSTEM-TYPES FOR USSOUTHCOM:");
               System.out.println();

  
 // ******************************OPERATING SYSTEM Types********************************
 
 
               USSOUTHCOM.setOperatingSystem    ("Android; Contiki; Embedded Linux, RIOT-OS, Android Auto, uCLinux, Yokto, Snappy Ubuntu, Tiny OS");
               System.out.println           ("USEUCOM OperatingSystem type  = " + USSOUTHCOM.getOperatingSystemType().toUpperCase());
  
              
               System.out.println( "OPERATING-SYSTEM-TYPES - UNDER CONSTRUCTION & SORRY FOR INCOVENIENCE");
              

               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println( "TO CONTINUE WITH NEXT USSOUTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOUTHCOM CHOICE # 10");
               System.out.println();
               System.out.println("************************************************************************************************" );

         

      }

else
   
      if ( menuSelect == 9)
      
       {
           
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println();

           System.out.println("PLEASE SEE BELOW IoT INTEROPERABILITY-TYPES FOR USSOUTHCOM: ");
           System.out.println();

  // ************************INTEROPERABILITY Types***********************
 
  
          USSOUTHCOM.setInterOperability      ("APIs-XIVELY, IOBridge, COSM, Exosite; Integration Frameworks- WeMo, Apple HomeKit, CROWNSet, Temboo, ThingSpeak; Reference Implementations- Inuity");

          
          System.out.println ("USSOUTHCOM INTEROPERABILITY-TYPES = " + USSOUTHCOM.getInterOperabilityType().toUpperCase());
         
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USSOUTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOUTHCOM CHOICE # 10");
          System.out.println();
          System.out.println("************************************************************************************************" );

          


      }

else
   
      if (menuSelect == 10)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT USERS-TYPES FOR USSOUTHCOM: ");
          System.out.println();
 

  // *********************USERS Types*************************
  
  
          USSOUTHCOM.setUser       ("Stakeholders Across the Enterprise");
 
         
      System.out.println     ("USSOUTHCOM USERS-TYPES = " + USSOUTHCOM.getUsersType().toUpperCase());
                
            
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT USSOUTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOUTHCOM CHOICE # 10");
      System.out.println();
      System.out.println("************************************************************************************************" );

          

 
      }

else
   
      if ( menuSelect == 11)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW IoT BEHAVIOURS-TYPES FOR USSOUTHCOM: ");
          System.out.println();
   
 // *********************************BEHAVIOURS Types*********************************
 
 
          USSOUTHCOM.setBehaviours            ("Leadership Opportunity regardless of rank, role, position");
 
          
          System.out.println          ("USSOUTHCOM BEHAVIOURS-TYPES = " + USSOUTHCOM.getBehavioursType().toUpperCase());
          System.out.println();
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println( "TO CONTINUE WITH NEXT USSOUTHCOM TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOUTHCOM CHOICE # 10");
          System.out.println();
          System.out.println("************************************************************************************************" );

           }
         
          else
            
   
  
  
// ******************Display the Main menu************************************

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");

       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 10) 
  
{
 
 
System.out.println();
System.out.println("THIS IS INVALID COCOM'S CHOICE# "); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF ALL COCOM'S: ");
System.out.println();
System.out.println("1.  USSOCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("2.  USTRANSCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("3.  USSTRATCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("4.  USAFRICOM IOT TAXONOMY."); 
System.out.println();
System.out.println("5.  USCENTCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("6.  USEUCOM IOT TAXONOMY.");
System.out.println();
System.out.println("7.  USNORTHCOM IOT TAXONOMY."); 
System.out.println();
System.out.println("8.  USPACOM IOT TAXONOMY."); 
System.out.println();
System.out.println("9.  USCYBERCOM IOT TAXONOMY.");
System.out.println();
System.out.println("10. USSOUTHCOM IOT TAXONOMY.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR COCOM SELECTION # (1 - 10)FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt(); 
  
  } 



break;

  
    }
  }
}

//*************************************END OF IOT TAXONOMY & FRAMEWORK PROGRAM***********************************************