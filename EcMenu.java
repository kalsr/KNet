
// EDGE-COMPUTING FRAMEWORK APPLICATION WAS DEVELOPED BASED ON EDGE-COMPUTING : VISION, CHALLENGES, REQUIREMENTS & USE CASES From IEEE.
// This APPLICATION was written using Object-Oriented TOOL Java JGRASP (APRIL, 2019)
// This APPLICATION was written by Mr Randy Singh,Computer Scientist,Technology Innovation Team (DISA/BDE5)
// Contact Phone# (301)225-9535  

import java.util.Scanner; 

public class EcMenu

{
public static void main(String[] args) 
{
 
// Declare a variable to hold the 
// user's menu selection. 

int menuSelection;

final int MAX_VALUE = 3;
 
// Declare variables to hold the units 
// of measurement.
 
String PushFromCloudServices, PullFromIOT, ChangeFromDataConsumerToProducer, CloudOffloading, VideoAnalytics, SmartHome, SmartCity, CollaborativeEdge, ProgrammabilityChallenge, NamingChallenge,
DataAbstractionChallenge, ServiceManagementChallenge, PrivacyAndSecurityChallenge, OptimizationMetricsChallenge;
 
// Create a Scanner object for keyboard input. 

Scanner keyboard = new Scanner(System.in); 

// Display the LIST OF EDGE-COMPUTING Categories 

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("WELCOME TO INTERNET OF THINGS (IOT) EDGE-COMPUTING FRAMEWORK APPLICATION: ");
System.out.println();
System.out.println   ("INTERNET OF THINGS (IOT) EDGE-COMPUTING FRAMEWORK CATEGORIES: ");
System.out.println();
System.out.println   ("1.  EDGE-COMPUTING FUNCTIONAL CATEGORIES. "); 
System.out.println();
System.out.println   ("2.  EDGE-COMPUTING USE CASES."); 
System.out.println();
System.out.println   ("3.  EDGE-COMPUTING FRAMEWORK CHALLENGES ."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("PLEASE ENTER EDGE-COMPUTING CATEGORY CHOICE (1 - 3)FROM THE LIST ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the EDGE-COMPUTING menu selection. 

 while (menuSelection < 1 || menuSelection > 3) 
  
{
 
System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID CHOICE FOR IOT EDGE-COMPUTING FRAMEWORK CATEGORY SELECTION");
System.out.println();
System.out.println("HERE IS THE VALID LIST OF IOT EDGE-COMPUTING FRAMEWORK CATEGORIES: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
//System.out.println();
System.out.println   ("1.  EDGE-COMPUTING FUNCTIONAL CATEGORIES. "); 
System.out.println();
System.out.println   ("2.  EDGE-COMPUTING USE CASES."); 
System.out.println();
System.out.println   ("3.  EDGE-COMPUTING FRAMEWORK CHALLENGES .");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("PLEASE ENTER IOT EDGE-COMPUTING CATEGORY CHOICE (1 - 3)FROM THE LIST ABOVE: ");


  
 menuSelection = keyboard.nextInt();
  
 } 
 
 while (menuSelection > 0 || menuSelection <= 3)
 
  



 switch(menuSelection)
 
{ 

//*************************EDGE-COMPUTING FRAMEWORK APPLICATION BEGINS HERE******************************************


 case 1:
 
 int menuSelect;
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED FUNCTIONAL-CATEGORIES OF IOT EDGE-COMPUTING FRAMEWORK ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW IOT EDGE-COMPUTING FUNCTIONAL SUBCATEGORIES");
 System.out.println();
System.out.println("************************************************************************************************" );
 System.out.println();

EcSetter ECFR;

//Following statement creates an object using the EcSetter Class as
// its Blueprint. 

ECFR = new EcSetter();

//*****************DISPLAY THE ZERO-TRUST MENU***************
  

 System.out.println("1.  PUSH FROM CLOUD SERVICES.");
 System.out.println();
 System.out.println("2.  PULL FROM IOT.");
 System.out.println();
 System.out.println("3.  CHANGE FROM DATA CONSUMER TO PRODUCER.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR FUNCTIONAL SUBCATEGORY CHOICE FROM 1 to 3: ");
 System.out.println();
 System.out.println("************************************************************************************************" );
 
 
 
  menuSelect = keyboard.nextInt();

//System.out.println("************************************************************************************************" );

 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 3)
  

  
{
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println(); 
 System.out.println("THIS IS INVALID CHOICE");
 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR FUNCTIONAL-SUBCATEGORY CHOICE FROM 1 to 3: "); 
 System.out.println();
 
 System.out.println("1.  PUSH FROM CLOUD SERVICES.");
 System.out.println();
 System.out.println("2.  PUSH FROM PULL FROM IOT.");
 System.out.println();
 System.out.println("3.  CHANGE FROM DATA CONSUMER TO PRODUCER.");
 System.out.println();

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.println("PLEASE SEE BELOW THE FUNCTIONAL-SUBCATEGORY DETAILS ON: PUSH FROM CLOUD SERVICES : ");
  System.out.println();
  System.out.println("************************************************************************************************" );
              
  //System.out.println("*************************************************************************************************");
  //System.out.println("NEED FOR EDGE-COMPUTING DUE TO PUSH FROM CLOUD SERVICES");
  //System.out.println("*************************************************************************************************");
  //System.out.println();
 // System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("1. Putting all the computing tasks on the cloud has been proved to be an efficient way for data processing as the computing power on the cloud outclasses the capability of the things at the edge.".toUpperCase());
  System.out.println();
  System.out.println("2. Compared to the fast developing data processing speed, the bandwidth of the network has come to a standstill.".toUpperCase());
  System.out.println();
  System.out.println("3. Due to growing quantity of data generated at the edge, speed of data transportation is becoming the bottleneck for the cloud-based computing paradigm.".toUpperCase());
  System.out.println();
  System.out.println("4. If all the data needs to be sent to the cloud for processing, the response time would be too long.".toUpperCase());
  System.out.println();
  System.out.println("5. The data needs to be processed at the edge for shorter response time, more efficient processing and smaller network pressure.1".toUpperCase());



                             
// Display the ZERO-TRUST FUNCTIONAL REQUIREMENTS values stored in the fields

     
              
      System.out.println("************************************************************************************************" );
      System.out.println();
      
      System.out.println( "TO CONTINUE WITH NEXT FUNCTIONAL-SUBCATEGORY PLEASE SELECT AGAIN IOT EDGE-COMPUTING MENU CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE FUNCTIONAL-SUBCATEGORY DETAILS ON: PULL FROM IOT: ");
         System.out.println();
         System.out.println("************************************************************************************************" );

  
  // *****************Information Types***************

  //System.out.println();
  System.out.println();
  System.out.println(" 1. Almost all kinds of electrical devices will become part of IoT, and they will play the role of data producers as well as consumers, such as air quality sensors, LED bars, streetlights and even an Internet-connected microwave oven.".toUpperCase()); 
  System.out.println();
  System.out.println(" 2. The number of things at the edge of the network will develop to more than billions in a few years.".toUpperCase());
  System.out.println();
  System.out.println(" 3. Raw  data produced by things will be enormous,making conventional cloud computing not efficient enough to handle all these data.".toUpperCase());
  System.out.println();
  System.out.println(" 4. Most of the data produced by IoT will never be transmitted to the cloud, instead it will be consumed at the edge of the network.".toUpperCase());
  System.out.println();
  System.out.println(" 5. Most of the end nodes in IoT are energy constrained things, and the wireless communication module is usually very energy hungry, so offloading some computing tasks to the edge could be more energy efficient.".toUpperCase());
  System.out.println();


      
//**************** Display the ZERO-TRUST INFORMATION TYPES****************

     
           
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT FUNCTIONAL-SUBCATEGORIES OF IOT EDGE-COMPUTING SELECT AGAIN MENU CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE FUNCTIONAL-SUBCATEGORY DETAILS ON: CHANGE FROM DATA CONSUMER TO PRODUCER: ");
         System.out.println();
         
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" 1. In the cloud computing paradigm, the end devices at the edge usually play as data consumer,for example, watching a YouTube video on your smart phone".toUpperCase()); 
  System.out.println();
  System.out.println(" 2. However, people are also producing data nowadays from their mobile devices. ".toUpperCase());
  System.out.println();
  System.out.println(" 3. The change from data consumer to data producer/consumer requires more function placement at the edge.".toUpperCase());
  System.out.println();
  System.out.println(" 4. The image or video clip could be fairly large and it would occupy a lot of bandwidth for uploading.In this case, the video clip should be demised and adjusted to suitable resolution at the edge before uploading to cloud. Another example would be wearable health devices.".toUpperCase());
  System.out.println();
  System.out.println(" 5. Since the physical data collected by the things at the edge of the network is usually private, processing the data at the edge could protect user privacy better than uploading raw data to cloud. ".toUpperCase());
  System.out.println();

  
     
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT FUNCTIONAL-SUBCATEGORY PLEASE SELECT IOT EDGE-COMPUTING AGAIN CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );
          
   }
   
   else
   
  
System.out.println();
//System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE IOT EDGE-COMPUTING FRAMEWORK CATEGORIES: ");
System.out.println();
System.out.println   ("1.  EDGE-COMPUTING FUNCTIONAL CATEGORIES. "); 
System.out.println();
System.out.println   ("2.  EDGE-COMPUTING USE CASES."); 
System.out.println();
System.out.println   ("3.  EDGE-COMPUTING FRAMEWORK CHALLENGES .");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("PLEASE ENTER EDGE-COMPUTING CATEGORY CHOICE (1 - 3)FROM THE LIST ABOVE: ");

       
       menuSelection = keyboard.nextInt();
 
// Validate the ZERO-TRUST Menu selection. 

 while (menuSelection < 1 || menuSelection > 3) 
  
{
 
 
System.out.println("************************************************************************************************" );
System.out.println(); 
System.out.println("THIS IS INVALID CHOICE FOR IOT EDGE-COMPUTING CATEGORY MENU SELECTION");
System.out.println();
System.out.println("HERE IS THE VALID LIST OF IOT EDGE-COMPUTING CATEGORIES: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1.  EDGE-COMPUTING FUNCTIONAL CATEGORIES. "); 
System.out.println();
System.out.println   ("2.  EDGE-COMPUTING USE CASES."); 
System.out.println();
System.out.println   ("3.  EDGE-COMPUTING FRAMEWORK CHALLENGES .");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("PLEASE ENTER IOT EDGE-COMPUTING CATEGORY CHOICE (1 - 3)FROM THE LIST ABOVE: ");
System.out.println();
System.out.println   ("************************************************************************************************" );



   

  
  menuSelection = keyboard.nextInt();


 
 } 

break;


//*************************ZERO-TRUSTUSE-CASES FRAMEWORK BEGINS HERE******************************************

case 2: 
 
 
 System.out.println();
 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED EDGE-COMPUTING USE CASES CATEGORY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW EDGE-COMPUTING USE-CASES CATEGORIES");
 System.out.println();
 System.out.println("************************************************************************************************" );


 System.out.println();

EcSetter ECUC;

//  Following statement creates an object using the ZTSetter TEMPLATE CLASS as
//  its BLUEPRINT. 

ECUC = new EcSetter();

  

 
 System.out.println("1.  USE-CASE1: CLOUD OFFLOADING.");
 System.out.println();
 System.out.println("2.  USE-CASE2: VIDEO ANALYTICS.");
 System.out.println();
 System.out.println("3.  USE-CASE3: SMART HOME.");
 System.out.println();
 System.out.println("4.  USE-CASE4: SMART CITY.");
 System.out.println();
 System.out.println("5.  USE-CASE5: COLLABORATIVE EDGE.");
 System.out.println();
 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM USE-CASE 1 to 5: ");
 System.out.println();  
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE ZERO-TRUST MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 5)
  

  
{
 System.out.println("************************************************************************************************" );
  System.out.println(); 
 System.out.println("THIS IS INVALID IOT EDGE-COMPUTING USE-CASES CATEGORY");
 System.out.println();
 System.out.println("PLEASE SELECT A VALID USE-CASE FROM THE VALID LIST BELOW"); 
 System.out.println();
 System.out.println("1.  USE-CASE1: CLOUD OFFLOADING.");
 System.out.println();
 System.out.println("2.  USE-CASE2: VIDEO ANALYTICS.");
 System.out.println();
 System.out.println("3.  USE-CASE3:SMART HOME.");
 System.out.println();
 System.out.println("4.  USE-CASE4: SMART CITY.");
 System.out.println();
 System.out.println("5.  USE-CASE5: COLLABORATIVE EDGE.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
  System.out.println();
  System.out.print(" ENTER YOUR CHOICE FROM USE-CASE 1 to 5: ");
   


 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
           System.out.println();
           System.out.println("************************************************************************************************" );
           System.out.println();
           System.out.println("PLEASE SEE BELOW USE-CASE 1: CLOUD-OFFLOADING WALKTHROUGH : ");
           System.out.println();
                   
           System.out.println("1. In the cloud computing paradigm, most of the computations happen in the cloud, which means data and requests are processed in the centralized cloud, such a computing paradigm may suffer longer latency which weakens the user experience. ".toUpperCase());
           System.out.println();
           System.out.println("2. In edge computing, the edge has certain computation resources, and this provides a chance to offload part of the workload from cloud. ".toUpperCase());
           System.out.println();
           System.out.println("3. In the IoT, the data is produced and consumed at the edge. Thus, in the edge computing paradigm, not only data but also operations applied on the data should be cached at the edge. ".toUpperCase());
           System.out.println();
           System.out.println("4. The data at the edge node should be synchronized with the cloud, however, this can be done in the background. ".toUpperCase());
           System.out.println();
           System.out.println("5. Navigation applications can move the navigating or searching services to the edge for a local area,in which case only a few map blocks are involved. ".toUpperCase());
           System.out.println();
           System.out.println("6. Content filtering/aggregating could be done at the edge nodes to reduce the data volume to be transferred. ".toUpperCase());
           System.out.println();
           System.out.println("7. Real-time applications such as vision-aid entertainment games, augmented reality, and connected health, could make fast responses by using edge nodes. ".toUpperCase());
           System.out.println();
           System.out.println("8. By leveraging edge computing, the latency and consequently the user experience for time-sensitive application could be improved significantly . ".toUpperCase());
           System.out.println();

         
                    
          
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH USE-CASE 2 PLEASE SELECT AGAIN EDGE-COMPUTING CATEGORY MENU CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW THE USE-CASE 2:  VIDEO-ANALYTICS WALKTHROUGH : ");
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();

  // *****************VIDEO-ANALYTICS USE CASE***************

                  
         System.out.println("1. The widespread of mobilephones and network cameras make video-analytics an emerging technology. ".toUpperCase());
         System.out.println();
         System.out.println("2. Cloud computing is no longer suitable for applications that requires video analytics due to the long data transmission latency and privacy concerns. ".toUpperCase());
         System.out.println();
         System.out.println("3. The data from the camera will usually not be uploaded to the cloud because of privacy issues or traffic cost, which makes it extremely difficult to leverage the wide area camera data. ".toUpperCase());
         System.out.println();
         System.out.println("4. Even if the data is accessible on the cloud, uploading and searching a huge quantity of data could take a long time");
         System.out.println();
         System.out.println("5. Each thing, for example, a smart phone, can perform the request and search its local camera data and only report the result back to the cloud. ".toUpperCase());
         System.out.println();
         System.out.println("6. In this paradigm, it is possible to leverage the data and computing power on every thing and get the result much faster compared with solitary cloud computing. ".toUpperCase());
         System.out.println();
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH USE-CASE 3 PLEASE SELECT AGAIN IOT EDGE-COMPUTING CATEGORY MENU CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW USE-CASE 3:  SMART-HOME WALKTHROUGH : ");
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
               
         System.out.println("1. IoT would benefit the home environment a lot. Some products have been developed and are available on the market such as smart light, smart TV, and robot vacuum. ".toUpperCase());

         System.out.println();
         System.out.println("2. Just adding a Wi-Fi module to the current electrical device and connecting it to the cloud is not enough for a smart home. In a smart home environment, besides the connected device,cheap wireless sensors and controllers should be deployed to room, pipe, and even floor and wall. ".toUpperCase());

         System.out.println();
         System.out.println("3. These things would report an impressive amount of data and for the consideration of data transportation pressure and privacy protection, this data should be mostly consumed in the home. ".toUpperCase());

         System.out.println();
         System.out.println("4. This feature makes the cloud computing paradigm unsuitable for a smart home therefor edge computing is considered perfect for building a smart home. ".toUpperCase());

         System.out.println();
         System.out.println("5. With an edge gateway running a specialized edge operating system (edgeOS) in the home, the things can be connected and managed easily in the home, the data can be processed locally to release the burdens for Internet bandwidth, and the service can also be deployed on the edgeOS for better management and delivery. ".toUpperCase());

                           
                  
      
//**************** Display SMART-CITY USE CASE REQUIREMENTS****************

     
     
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH USE-CASE 4 PLEASE SELECT AGAIN IOT EDGE-COMPUTING CATEGORY MENU CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );
 
   }
   
   else
   
   if ( menuSelect == 4 )
     
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW USE-CASE 4: SMART-CITY WALKTHROUGH : ");
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();               
         System.out.println("1. The edge computing paradigm can be flexibly expanded from a single home to community, or even city scale. Edge computing claims that computing should happen as close as possible to the data source. ".toUpperCase());
         System.out.println();
         System.out.println("2. With this design, a request could be generated from the top of the computing paradigm and be actually processed at the edge. ".toUpperCase());
         System.out.println();
         System.out.println("3. Edge computing could be an ideal platform for smart city considering the following characteristics: ".toUpperCase());
         System.out.println();
         System.out.println("A. Large-Data-Quantity: A city populated by 1 million people will produce 180 PB data per day by 2019, contributed by public safety, health, utility, and transports, etc. Building centralized cloud data centers to handle all of the data is unrealistic because the traffic workload would be too heavy. In this case, edge computing could be an efficient solution by processing the data at the edge of the network. ".toUpperCase());
         System.out.println();
         System.out.println("B. Low-Latency: For applications that require predictable and low latency such as health emergency or public safety. ".toUpperCase());
         System.out.println();
         System.out.println("C. Location-Awareness: For geographic-based applications such as transportation and utility management, edge computing exceed cloud computing due to the location awareness. In edge computing, data could be collected and processed based on geographic location without being transported to cloud. ".toUpperCase());
         System.out.println();

         
      
//**************** Display COLLABORATIVE-EDGE USE CASE REQUIREMENTS****************

     
           
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH USE-CASE 5 PLEASE SELECT AGAIN IOT EDGE-COMPUTING CATEGORY MENU CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );
 
   }

   else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW USE-CASE 5: COLLABORATIVE EDGE WALKTHROUGH : ");
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();

                         
         System.out.println("1. Cloud has become the de facto computing platform for the big data processing by academia and industry. A key promise behind cloud computing is that the data should be already held or is being transmitted to the cloud and will eventually be processed in the cloud. ".toUpperCase());
         System.out.println();
         System.out.println("2. In many cases, however, the data owned by stakeholders is rarely shared to each other due to privacy concerns and the formidable cost of data transportation. ".toUpperCase()); 
         System.out.println();       
         System.out.println("3. Thus, the chance of collaboration among multiple stake-holders is limited. Edge, as a physical small data center that connects cloud and end user with data processing capability, can also be part of the logical concept. collaborative edge, which connects the edges of multiple stakeholders that are geographically distributed despite their physical location and network structure is proposed. ".toUpperCase());
         System.out.println();
         System.out.println("4. Those ad hoc-like connected edges provide the opportunity for stakeholders to share and cooperate data. ".toUpperCase());
         System.out.println();
         System.out.println("5. One of the promising applications in the near future is connected health. ".toUpperCase());
         System.out.println();
         System.out.println("6. Most of the participants can benefit from collaborative edge in terms of reducing operational cost and improving profitability. However, some of them, like hospitals in our case, could be a pure contributor to the healthcare community since they are the major information collector in this community. ".toUpperCase());
         System.out.println();

      
      
       System.out.println();
       System.out.println("************************************************************************************************" );
       System.out.println();
       System.out.println( "TO CONTINUE WITH USE-CASES PLEASE SELECT AGAIN IOT EDGE-COMPUTING CATEGORY MENU CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );
      }

  else
   
               
 
System.out.println();
System.out.println   ("HERE ARE IOT EDGE-COMPUTING FRAMEWORK CATEGORIES: ");
System.out.println();
System.out.println   ("1.  EDGE-COMPUTING FUNCTIONAL CATEGORIES. "); 
System.out.println();
System.out.println   ("2.  EDGE-COMPUTING USE CASES."); 
System.out.println();
System.out.println   ("3.  EDGE-COMPUTING FUNCTIONAL CHALLENGES ."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("PLEASE ENTER IOT EDGE-COMPUTING CATEGORY CHOICE (1 - 3)FROM THE LIST ABOVE: "); 
      
       menuSelection = keyboard.nextInt();
 
// Validate the IOT EDGE-COMPUTING Menu selection. 

 while (menuSelection < 1 || menuSelection > 3) 
  
{
 
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println("THIS IS INVALID CHOICE FOR IOT EDGE-COMPUTING CATEGORY SELECTION");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE VALID LIST OF EDGE-COMPUTING CATEGORIES: ");
System.out.println();
System.out.println   ("1.  EDGE-COMPUTING FUNCTIONAL CATEGORIES. "); 
System.out.println();
System.out.println   ("2.  EDGE-COMPUTING USE CASES."); 
System.out.println();
System.out.println   ("3.  EDGE-COMPUTING FUNCTIONAL CHALLENGES ."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("PLEASE ENTER IOT EDGE-COMPUTING CATEGORY CHOICE (1 - 3)FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();

  
 } 


break; 

//***********************IOT EDGE-COMPUTING FRAMEWORK CATEGORY-3 - ARCHITECTURAL REQUIREMENTS******************************************

case 3:

 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED IOT EDGE-COMPUTING CHALLENGES CATEGORY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW IOT EDGE-COMPUTING CHALLENGES CATEGORIES");
 System.out.println();
 System.out.println   ("************************************************************************************************" );
System.out.println();

EcSetter ECFC;


ECFC = new EcSetter();

  

 System.out.println("1.  PROGRAMMABILITY CHALLENGE.");
 System.out.println();
 System.out.println("2.  NAMING CHALLENGE.");
 System.out.println();
 System.out.println("3.  DATA ABSTRACTION CHALLENGE.");
 System.out.println();
 System.out.println("4.  SERVICE MANAGEMENT CHALLENGE.");
 System.out.println();
 System.out.println("5.  PRIVACY AND SECURITY CHALLENGE.");
 System.out.println();
 System.out.println("6.  OPTIMIZATION METRICS CHALLENGE.");
 System.out.println();
  
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR IOT EDGE-COMPUTING CHALLENGE CHOICE FROM 1 to 6: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE ZERO-TRUST MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 6)
  

  
{
  System.out.println("************************************************************************************************" );
  
 System.out.println    ("THIS IS INVALID IOT EDGE-COMPUTING CHALLENGES SELECTION"); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println    ("ENTER YOUR EDGE-COMPUTING CHALLENGES SELECTION FROM 1 to 6: ");
 System.out.println();
 System.out.println("1.  PROGRAMMABILITY CHALLENGE.");
 System.out.println();
 System.out.println("2.  NAMING CHALLENGE.");
 System.out.println();
 System.out.println("3.  DATA ABSTRACTION CHALLENGE.");
 System.out.println();
 System.out.println("4.  SERVICE MANAGEMENT CHALLENGE.");
 System.out.println();
 System.out.println("5.  PRIVACY AND SECURITY CHALLENGE.");
 System.out.println();
 System.out.println("6.  OPTIMIZATION METRICS CHALLENGE.");
 System.out.println();
  
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR IOT EDGE-COMPUTING CHALLENGES CHOICE FROM 1 to 6: ");



 
  menuSelect = keyboard.nextInt();


 }

     
    if ( menuSelect == 1)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("IOT EDGE-COMPUTING: PROGRAMMABILITY CHALLENGES : ");
          System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();                    
System.out.println("1. In cloud computing, users program their code and deploy them on the cloud. The cloud provider is in charge to decide where the computing is conducted in a cloud. ".toUpperCase());
System.out.println();
System.out.println("2. Users have zero or partial knowledge of how the application runs. This is one of the benefits of cloud computing that the infrastructure is transparent to the user. ".toUpperCase());
System.out.println();
System.out.println("3. Usually, the program is written in one programing language and compiled for a certain target platform, since the program only runs in the cloud. However, in the edge computing, computation is offloaded from the cloud,and the edge nodes are most likely heterogeneous platforms. In this case, the runtime of these nodes differ from each other, and the programmer faces huge difficulties to write an application that may be deployed in the edge computing paradigm.".toUpperCase());
System.out.println();
System.out.println("4. To address the programmability of edge computing, we propose the concept of computing stream that is defined as a serial of functions/computing applied on the data along the data propagation path.".toUpperCase());
System.out.println();
System.out.println("5. The functions/computing could be entire or partial functionalities of an application, and the computing can occur anywhere on the path as long as the application defines where the computing should be conducted. " .toUpperCase());
System.out.println();
System.out.println("6. The computing stream is software defined computing flow such that data can be processed in distributed and efficient fashion on data generating devices, edge nodes, and the cloud environment. ".toUpperCase());
System.out.println();
System.out.println("7. As defined in edge computing, a lot of computing can be done at the edge instead of the centric cloud. In this case, the computing stream can help the user to determine what functions/computing should be done and how the data is propagated after the computing happened at the edge. ".toUpperCase());
System.out.println();
System.out.println("8. The function/computing distribution metric could be latency-driven, energy cost, TCO, and hardware/software specified limitations. ".toUpperCase());
System.out.println();
System.out.println("9. By deploying a computing stream, we expect that data is computed as close as possible to the data source, and the data transmission cost can be reduced.In a computing stream, the function can be reallocated, and the data and state along with the function should also be reallocated. Moreover, the collaboration issues (e.g., synchronization, data/state migration, etc.) have to be addressed across multiple layers in the edge computing paradigm. The system shall support certificate-based authentication. ".toUpperCase());
System.out.println();
                                               
               
      System.out.println();
     
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT CHALLENGE PLEASE SELECT AGAIN IOT EDGE-COMPUTING CATEGORY MENU CHOICE # 3"); 
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         
        System.out.println("***********************************************************************************" );
        System.out.println();
        System.out.println("IOT EDGE-COMPUTING: NAMING CHALLENGES ");
        System.out.println();
        System.out.println("***********************************************************************************" );
 System.out.println();
System.out.println("1  In edge computing, one important assumption is that the number of things is tremendously large. At the top of the edge nodes, there are a lot of applications running, and each application has its own structure about how the service is provided. ".toUpperCase()); 
System.out.println();
System.out.println("2. Similar to all computer systems, the naming scheme in edge computing is very important for programing, addressing,things identification, and data communication. However, an efficient naming mechanism for the edge computing paradigm has not been built and standardized yet.".toUpperCase());
System.out.println(); 
System.out.println("3. Edge practitioners usually needs to learn various communication and network protocols in order to communicate with the heterogeneous things in their system. The naming scheme for edge computing needs to handle the mobility of things, highly dynamic network topology, privacy and security protection, as well as the scalability targeting the tremendously large amount of unreliable things.".toUpperCase());
System.out.println();
System.out.println("4. Traditional naming mechanisms such as DNS and uniform resource identifier satisfy most of the current networks very well. However, they are not flexible enough to serve the dynamic edge network since sometimes most of the things at edge could be highly mobile and resource constrained. Moreover, for some resource constrained things at the edge of the network, IP based naming scheme could be too heavy to support considering its complexity and overhead. ".toUpperCase());
System.out.println(); 
System.out.println("5. New naming mechanisms such as named data networking(NDN)and MobilityFirst could also be applied to edge computing. NDN provide a hierarchically structured name for content/data centric network, and it is human friendly for service management and provides good scalability for edge. However, it would need extra proxy in order to fit into other communication protocols such as BlueTooth or ZigBee,and so on. ".toUpperCase());
System.out.println(); 
System.out.println("6. Another issue associated with NDN is security, since it is very hard to isolate things hardware information with service providers. MobileFirst can separate name from network address in order to provide better mobility support,and it would be very efficient if applied to edge services where things are of highly mobility. ".toUpperCase());
System.out.println(); 
System.out.println("7. A global unique identification (GUID) needs to be used for naming is MobileFirst, and this is not required in related fixed information aggregation service at the edge of the network such as home environment. Another disadvantage of MobileFirst for edge is the difficulty in service management since GUID is not human friendly. ".toUpperCase());
System.out.println(); 
System.out.println("8. For a relative small and fixed edge such as home environment, let the edgeOS assign network address to each thing could be a solution. With in one system, each thing could have a unique human friendly name which describes the following information: location (where), role (who), and data description (what), for example, “kitchen.oven2.temperature3.” Then the edgeOS will assign identifier and network address to this thing, as shown in Fig. 5. The human friendly name is unique for each thing and it will be used for service management, things diagnosis, and component replacement. ".toUpperCase());
System.out.println();
System.out.println("9. This naming mechanism provides better programmability to service providers and in the meanwhile, it blocks service providers from getting hardware information, which will protect data privacy and security better. Unique identifier and network address could be mapped from human friendly name. Identifier will be used for things management in edgeOS. Network address such as IP address or MAC address will be used to support various communication protocols such as BlueTooth, ZigBee or WiFi,and so on. ".toUpperCase());

    
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT CHALLENGE PLEASE SELECT AGAIN IOT EDGE-COMPUTING CATEGORY MENU CHOICE # 3"); 
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("IOT EDGE-COMPUTING: DATA-ABSTRACTION CHALLENGES ");
         System.out.println();
          System.out.println("************************************************************************************************" );
         System.out.println();


  
 // *****************Authorization Requirements*****************
 
 
       //  ZTAR.setAuthorizationRequirements ("1 The system shall control authorization of user and machines 1.1 The system shall be able to assign role based access controls to groups and users 2 The system shall support time limited authorization for administrators 2.1 The system shall provide a portal to request privileged access to systems 3 The system shall associate identity to authorization policy through integration of Zero Trust Architecture tools 3.1 The system shall align network security policy to authorization of users and machines 4 The system shall support dynamic/real-time access decisions 5 The system shall support querying to determine authorization level of user or device ");        
         
System.out.println("1  Data abstraction has been well discussed and researched in the wireless sensor network and cloud computing paradigm. However,in edge computing, this issue becomes more challenging. With IoT, there would be a huge number of data generators in the network, and here we take a smart home environment as an example. ".toUpperCase());
System.out.println();
System.out.println("2. In a smart home, almost all of the things will report data to the edgeOS, not to mention the large number of things deployed all around the home. However, most of the things at the edge of the network, only periodically report sensed data to the gateway. For example, the thermometer could report the temperature every minute, but this data will most likely only be consumed by the real user several times a day. Another example could be a security camera in the home which might keep recording and sending the video to the gateway, but the data will just be stored in the database for a certain time with nobody actually consuming it, and then be flushed by the latest video. ".toUpperCase()); 
System.out.println();
System.out.println("3. Based on this observation, we envision that human involvement in edge computing should be minimized and the edge node should consume/process all the data and interact with users in a proactive fashion. In this case, data should be preprocessed at the gateway level, such as noise/low-quality removal,event detection, and privacy protection, and so on. Processed data will be sent to the upper layer for future service providing.There will be several challenges in this process. ".toUpperCase());
System.out.println(); 
System.out.println("4. For the concern of privacy and security, applications running on the gateway should be blinded from raw data. Moreover, they should extract the knowledge they are interested in from an integrated data table. We can easily define the table with id, time, name, data (e.g.,{0000, 12:34:56PM 01/01/2016,kitchen.oven2.temperature3, 78}) such that any edge thing’s data can be fitted in. However, the details of sensed data have been hidden, which may affect the usability of data. ".toUpperCase()); 
System.out.println();
System.out.println("5. It is sometimes difficult to decide the degree of data abstraction. If too much raw data is filtered out, some applications or services could not learn enough knowledge.However, if we want to keep a large quantity of raw data, there would be a challenge for data storage. Lastly, data reported by things at edge could be not reliable sometime, due to the low precision sensor, hazard environment, and unreliable wireless connection. In this case, how to abstract useful information from unreliable data source is still a challenge for IoT application and system developers. ".toUpperCase());
System.out.println();
System.out.println("6. One more issue with data abstraction is the applicable operations on the things. Collecting data is to serve the application and the application should be allowed to control (e.g., read from and write to) the things in order to complete certain services the user desires. Combining the data representation and operations, the data abstraction layer will serve as an public interface for all things connected to edgeOS. Furthermore, due the heterogeneity of the things, both data representation and allowed operations could diverse a lot, which also increases the barrier of universal data abstraction. ".toUpperCase()); 
System.out.println();
//System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");
       
        
       
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT CHALLENGE PLEASE SELECT AGAIN IOT EDGE-COMPUTING CATEGORY MENU CHOICE # 3"); 
 
      System.out.println();
      System.out.println("************************************************************************************************" );


 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("IOT EDGE-COMPUTING: SERVICE-MANAGEMENT CHALLENGES ");
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();



    
 
         
System.out.println("1  In terms of service management at the edge of the network, we argue that the following four fundamental features should be supported to guarantee a reliable system, including differentiation, extensibility, isolation, and reliability. ".toUpperCase());
System.out.println();
System.out.println("2. Differentiation: With the fast growth of IoT deployment, we expected multiple services will be deployed at the edge of the network, such as Smart Home. These services will have different priorities. For example, critical services such as things diagnosis and failure alarm should be processed earlier than ordinary service. Health related service, for example, fall detection or heart failure detection should also have a higher priority compared with other service such as entertainment. ".toUpperCase());
System.out.println();
System.out.println("3. Extensibility: Extensibility could be a huge challenge at the edge of the network, unlike a mobile system, the things in the IoT could be very dynamic. When the owner purchases a new thing, can it be easily added to the current service without any problem? Or when one thing is replaced due to wearing out,can the previous service adopt a new node easily? These problems should be solved with a flexible and extensible design of service management layer in the edgeOS. ".toUpperCase()); 
System.out.println();
System.out.println("4. Isolation: Isolation would be another issue at the edge of the network. In mobile OS, if an application fails or crashes, the whole system will usually crash and reboot. Or in a distributed system the shared resource could be managed with different synchronization mechanisms such as a lock or token ring. However, in a smart edgeOS, this issue might be more complicated. There could be several applications that share the same data resource, for example, the control of light. If one application failed or was not responding, a user should still be able to control their lights, without crashing the whole edgeOS. Or when a user removes the only application that controls lights from the system, the lights should still be alive rather than experiencing a lost connection to the edgeOS.This challenge could be potentially solved by introducing a deployment/undeployment framework. If the conflict could be detected by the OS before an application is installed, then a user can be warned and avoid the potential access issue. Another side of the isolation challenge is how to isolate a user’s private data from third party applications. For example, your activity tracking application should not be able to access your electricity usage data. To solve this challenge, a well-designed control access mechanism should be added to the service management layer in the edgeOS. ".toUpperCase());
System.out.println();
System.out.println("5. Reliability: Last but not least, reliability is also a key challenge at the edge of the network. We identify the challenges in reliability from the different views of service, system, and data here.".toUpperCase());
System.out.println(); 
System.out.println("A. From the service-point-of-view, it is sometimes very hard to identify the reason for a service failure accurately at field. For example, if an air conditioner is not working, a potential reason could be that a power cord is cut, compressor failure, or even a temperature controller has run out of battery. A sensor node could have lost connection very easily to the system due to battery outage, bad connection condition, component wear out, etc. At the edge of the network, it is not enough to just maintain a current service when some nodes lose connection, but to provide the action after node failure makes more sense to the user. For example, it would be very nice if the edgeOS could inform the user which component in the service is not responding, or even alert the user ahead if some parts in the system have a high risk of failure.Potential solutions for this challenge could be adapted from a wireless sensor network, or industrial network such as PROFINET. ".toUpperCase());
System.out.println();                                               
System.out.println("B. From the system-point-of-view, it is very important for the edgeOS to maintain the network topology of the whole system, and each component in the system is able to send status/diagnosis information to the edgeOS. With this feature, services such as failure detection, thing replacement, and data quality detection could be easily deployed at the system level. ".toUpperCase());
System.out.println();
System.out.println("C. From the data-point-of-view, reliability challenge rise mostly from the data sensing and communication part. As previously researched and discussed, things at the edge of the network could fail due to various reasons and they could also report low fidelity data under unreliable new communication protocols for IoT data collection are also proposed. These protocols serves well for the support of huge number of sensor nodes and the highly dynamic network condition [31]. However, the connection reliability is not as good as BlueTooth or WiFi. If both sensing data and communication are not reliable, how the system can still provide reliable service by leveraging multiple reference data source and historical data record is still an open challenge. ".toUpperCase()); 
System.out.println();                                              
   
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT CHALLENGE PLEASE SELECT AGAIN IOT EDGE-COMPUTING CATEGORY MENU CHOICE # 3"); 
 
      System.out.println();
      System.out.println("************************************************************************************************" );
      
      }
      else
      
 if ( menuSelect == 5 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("IOT EDGE-COMPUTING: PRIVACY-AND-SECURITY CHALLENGES ");
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();


  
 
System.out.println("1. At the edge of the network, usage privacy and data security protection are the most important services that should be provided. If a home is deployed with IoT, a lot of privacy information can be learned from the sensed usage data. For example, with the reading of the electricity or water usage, one can easily speculate if the house is vacant or not. In this case, how to support service without harming privacy is a challenge. Some of the private information could be removed from data before processing such as masking all the faces in the video. We think that keeping the computing at the edge of data resource, which means in the home, could be a decent method to protect privacy and data security. To protect the data security and usage privacy at the edge of the network, several challenges remain open.  ".toUpperCase());
System.out.println();
System.out.println("2. First is the awareness of privacy and security to the community. We take WiFi networks security as an example. Among the 439 million households who use wireless connections,49% of WiFi networks are unsecured, and 80% of households still have their routers set on default passwords. For public WiFi hotspots, 89% of them are unsecured [32]. All the stake holders including service provider, system and application developer and end user need to aware that the users’privacy would be harmed without notice at the edge of the network. For example, ip camera, health monitor, or even some WiFi enabled toys could easily be connected by others if not protected properly. ".toUpperCase());
System.out.println();
System.out.println("3. Second is the ownership of the data collected from things at edge. Just as what happened with mobile applications, the data of end user collected by things will be stored and analyzed at the service provider side. However, leave the data at the edge where it is collected and let the user fully own the data will be a better solution for privacy protection. Similar to the health record data, end user data collected at the edge of the network should be stored at the edge and the user should be able to control if the data should be used by service providers. During the process of authorization, highly private data could also be removed by the things to further protect user privacy.  ".toUpperCase());
System.out.println();
System.out.println("4. Third is the missing of efficient tools to protect data privacy and security at the edge of the network. Some of the things are highly resource constrained so the current methods for security protection might not be able to be deployed on thing because they are resource hungry. Moreover, the highly dynamic environment at the edge of the network also makes the network become vulnerable or unprotected. For privacy protection, some platform such as Open mHealth is proposed to standardize and store health data [33], but more tools are still missing to handle diverse data attributes for edge computing. ".toUpperCase());
System.out.println();

//System.out.println("PLEASE NOTE: *******************ACTUAL PROOF OF CONCEPT BASED ON THESE REQUIREMENTS IS UNDER-CONSTRUCTION*************************");
 
        
            

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT CHALLENGE PLEASE SELECT AGAIN IOT EDGE-COMPUTING CATEGORY MENU CHOICE # 3"); 
      System.out.println();
      System.out.println("************************************************************************************************" );


 
   }
   
   else
   
      if ( menuSelect == 6)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("IOT EDGE-COMPUTING: OPTIMIZATION-METRICS CHALLENGES ");
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();



System.out.println("1  In edge computing, we have multiple layers with different computation capability. Workload allocation becomes a big issue. We need to decide which layer to handle the workload or how many tasks to assign at each part. There are multiple allocation strategies to complete a workload, for instances, evenly distribute the workload on each layer or complete as much as possible on each layer. The extreme cases are fully operated on endpoint or fully operated on cloud. To choose an optimal allocation strategy, we discuss several optimization metrics in this section, including latency, bandwidth, energy and cost. ".toUpperCase());
System.out.println();       
System.out.println("A. LATENCY: Latency is one of the most important metrics to evaluate the performance, especially in interaction applications/services. Servers in cloud computing provide high computation capability. They can handle complex workloads in a relatively short time, such as image processing, voice recognition and so on. However, latency is not only determined by computation time. Long WAN delays can dramatically influence the real-time/interaction intensive applications’ behavior. To reduce the latency, the workload should better be finished in the nearest layer which has enough computation capability to the things at the edge of the network.For example, in the smart city case, we can leverage phones to process their local photos first then send a potential missing child’s info back to the cloud instead of uploading all photos. Due to the large amount of photos and their size, it will be much faster to preprocess at the edge. However, the nearest physical layer may not always be a good option. We need to consider the resource usage information to avoid unnecessary waiting time so that a logical optimal layer can be found. If a user is playing games, since the phone’s computation resource is already occupied, it will be better to upload a photo to the nearest gateway or micro-center. ".toUpperCase());
System.out.println();
System.out.println("B. BANDWIDTH: From latency’s point of view, high bandwidth can reduce transmission time, especially for large data (e.g.,video, etc.). For short distance transmission, we can establish high bandwidth wireless access to send data to the edge. On one hand, if the workload can be handled at the edge, the latency can be greatly improved compared to work  on the cloud. The bandwidth between the edge and the cloud is also saved. For example, in the smart home case, almost all the data can be handled in the home gateway through Wi-Fi or other high speed transmission methods. In addition, the transmission reliability is also enhanced as the transmission path is short. On the other hand, although the transmission distance cannot be reduced since the edge cannot satisfy the computation demand, at least the data is preprocessed at the edge and the upload data size will be significantly reduced. In the smart city case, it is better to preprocess photos before upload, so the data size can be greatly reduced. It saves the users’ bandwidth, especially if they are using a carriers’ data plan. From a global perspective, the bandwidth is saved in both situations, and it can be used by other edges to upload/download data. Hence, we need to evaluate if a high bandwidth connection is needed and which speed is suitable for an edge. Besides, to correctly determine the workload allocation in each layer, we need to consider the computation capability and bandwidth usage information in layers to avoid competition and delay. ".toUpperCase()); 
System.out.println();
System.out.println("C. ENERGY: Battery is the most precious resource for things at the edge of the network. For the endpoint layer, offloading workload to the edge can be treated as an energy free method [22], [39]. So for a given workload, is it energy efficient to offload the whole workload (or part of it) to the edge rather than compute locally? The key is the tradeoff between the computation energy consumption and transmission energy consumption. Generally speaking, we first need to consider the power characteristics of the workload. Is it computation intensive? How much resource will it use to run locally? Besides the network signal strength [40], the data size and available bandwidth will also influence the transmission energy overhead. We prefer to use edge computing only if the transmission overhead is smaller than computing locally. However, if we care about the whole edge computing process rather than only focus on endpoints, total energy consumption should be the accumulation of each used layer’s energy cost. Similar to the endpoint layer, each layer’s energy consumption can be estimated as local computation cost plus transmission cost. In this case, the optimal workload allocation strategy may change. For example, the local data center layer is busy, so the workload is continuously uploaded to the upper layer. Comparing with computing on endpoints, the multihop transmission may dramatically increase the overhead which causes more energy consumption.  ".toUpperCase());
System.out.println();
System.out.println("D. COST: From the service providers’ perspective, e.g.,YouTube, Amazon, etc., edge computing provides them less latency and energy consumption, potential increased throughput and improved user experience. As a result, they can earn more money for handling the same unit of workload. For example, based on most residents’ interest, we can put a popular video on the building layer edge. The city layer edge can free from this task and handle more complex work. The total throughput can be increased. The investment of the service providers is the cost to build and maintain the things in each layer. To fully utilize the local data in each layer, providers can charge users based on the data location. New cost models need to be developed to guarantee the profit of the service provider as well as acceptability of users. ".toUpperCase()); 
System.out.println();
System.out.println("E. Workload allocation is not an easy task. The metrics are closely related to each other. For example, due to the energy constraints, a workload needs to be complete on the city data center layer. Comparing with the building server layer, the energy limitation inevitably affects the latency. Metrics should be given priority (or weight) for different workloads so that a reasonable allocation strategy can be selected. Besides, the cost analysis needs to be done in runtime. The interference and resource usage of concurrent workloads should be considered as well.  ".toUpperCase());
System.out.println();

                  
           
      //System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH CHALLENGE PLEASE SELECT AGAIN IOT EDGE-COMPUTING CATEGORY CHOICE # 3"); 
      System.out.println();
      System.out.println("************************************************************************************************" );
      }

   else
  



System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE IOT EDGE-COMPUTING FRAMEWORK CATEGORIES: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1.  EDGE-COMPUTING FUNCTIONAL CATEGORIES. "); 
System.out.println();
System.out.println   ("2.  EDGE-COMPUTING USE CASES."); 
System.out.println();
System.out.println   ("3.  EDGE-COMPUTING FUNCTIONAL CHALLENGES ."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("PLEASE ENTER IOT EDGE-COMPUTING CATEGORY CHOICE (1 - 3)FROM THE LIST ABOVE: "); 
       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 3) 
  
{
System.out.println(); 
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println("THIS IS INVALID CHOICE FOR IOT EDGE-COMPUTING CATEGORY SELECTION");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE VALID LIST OF IOT EDGE-COMPUTING CATEGORIES: ");
System.out.println();
System.out.println   ("1.  EDGE-COMPUTING FUNCTIONAL CATEGORIES. "); 
System.out.println();
System.out.println   ("2.  EDGE-COMPUTING USE CASES."); 
System.out.println();
System.out.println   ("3.  EDGE-COMPUTING FUNCTIONAL CHALLENGES ."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("PLEASE ENTER IOT EDGE-COMPUTING CATEGORY CHOICE (1 - 3)FROM THE LIST ABOVE: ");

   

  
  menuSelection = keyboard.nextInt();

  
 } 


break; 
 
    }
  }
}


//*************************************END OF IOT EDGE-COMPUTING FRAMEWORK APPLICATION***********************************************