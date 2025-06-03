
/* Recent advancements in virtualization and software architecture have led to the new paradigm of serverless computing,
   which allows developers to deploy applications as stateless functions without worrying about the underlying infrastructure.
   Accordingly, a serverless platform handles the lifecycle, execution and scaling of the actual functions; these need to run
   only when invoked or triggered by an event. Thus, the major benefits of serverless computing are low operational concerns
   and efficient resource management and utilization.

   SERVERLESS COMPUTING FRAMEWORK WAS DEVELOPED BASED ON several white papers & USE CASES.
   The Application code was written using programming in Java JGRASP (JUNE, 2020)
   The code was written by Mr Randy Singh, Computer Scientist,Technology Innovation Team (DISA/EM3)
   Contact Phone# (301)225-9535  
*/


import java.util.Scanner; 

public class ScfMenu 

{

public static void main(String[] args) 

{
 

int menuSelection;

final int MAX_VALUE = 7;
 

// Create a Scanner object for keyboard input. 


Scanner keyboard = new Scanner(System.in); 


// Display the LIST OF SERVERLES-COMPUTING FRAMEWORK MAIN MENU Categories 

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   (" WELCOME TO SERVERLESS-COMPUTING FRAMEWORK APPLICATION MAIN MENU.  ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS."); 
System.out.println();
System.out.println ("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER SERVERLESS-COMPUTING MAIN MENU FRAMEWORK CATEGORY CHOICE (1 - 8) FROM THE LIST ABOVE: ");


 menuSelection = keyboard.nextInt();
 
// Validate the SERVER-LESS COMPUTING Menu selection. 

 while (menuSelection < 1 || menuSelection > 8) 
  
{
 
System.out.println("************************************************************************************************" );
System.out.println(); 
System.out.println(" THIS IS INVALID CHOICE FOR SERVERLESS-COMPUTING MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println( "HERE ARE VALID SERVERLESS-COMPUTING MAIN MENU SELECTIONS CHOICE LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println  ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" ENTER SERVERLESS COMPUTING MAIN MENU CATEGORY CHOICE (1 - 8) FROM SELECTIONS ABOVE: ");

  
 menuSelection = keyboard.nextInt();
  
 } 
 
 while (menuSelection > 0 || menuSelection <= 8)
 
 
 switch(menuSelection)
 
{ 


 case 1:
 
 int menuSelect;
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println(" YOU SELECTED FUNCTION-AS-SERVICE (FaaS) CATEGORY OF SERVERLESS-COMPUTING FRAMEWORK ");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println(" PLEASE SEE BELOW SERVERLESS-COMPUTING FUNCTION-AS-SERVICE (FaaS) CAPABILITIES LIST");
 System.out.println();
 System.out.println("************************************************************************************************" );
 
ScfSetter ScFAS;

ScFAS = new ScfSetter();

 System.out.println();   
 System.out.println("1.   SHOW ENTIRE LIST OF FUNCTION-AS-SERVICE (FaaS) CAPABILITIES.");
 System.out.println();
 System.out.println("2.   FUNCTION-EXECUTION-CAPABILTY.");
 System.out.println();
 System.out.println("3.   STORAGE-CAOABILITY");
 System.out.println();
 System.out.println("4.   CONTAINER-INFRASTRUCTURE-CAPABILITY.");
 System.out.println();
 System.out.println("5.   NETWORKING-APABILITY.");
 System.out.println();
 System.out.println("6.   FAULT-TOLERANCE-CAPABILITIES.");
 System.out.println();
 System.out.println("7.   SCALING-OF-THE-FUNCTIONS-CAPABILITY.");
 System.out.println();
 System.out.println("8.   DATA-ANALYTICS-AT-THE NETWORK-EDGE.");
 System.out.println();
 System.out.println("9.   SCIENTIFIC-COMPUTING.");
 System.out.println();
 System.out.println("10.  MOBILE-COMPUTING.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR SERVERLESS-COMPUTING FUNCTION-AS-SERVICE CAPABILTY SELECTION FROM (1 to 10) : ");
   
 
  menuSelect = keyboard.nextInt();
  

 
 while (menuSelect < 1 || menuSelect > 10)
   
{
 System.out.println();
 System.out.println("**************************************************************************************************************" );
 System.out.println(); 
 System.out.println(" THIS IS INVALID SELECTION. ENTER YOUR SERVERLESS-COMPUTING FUNCTION-AS-SERVICE SELECTIONS FROM 1 to 10:");
 System.out.println(); 
 System.out.println("***************************************************************************************************************" );
 System.out.println();
 System.out.println("1.   DISPLAY ENTIRE LIST OF FUNCTION-AS-SERVICE (FaaS) CAPABILITIES.");
 System.out.println();
 System.out.println("2.   FUNCTION-EXECUTION-CAPABILTY.");
 System.out.println();
 System.out.println("3.   STORAGE-CAPABILITY");
 System.out.println();
 System.out.println("4.   CONTAINER-INFRASTRUCTURE-CAPABILITY.");
 System.out.println();
 System.out.println("5.   NETWORKING-CAPABILITY.");
 System.out.println();
 System.out.println("6.   FAULT-TOLERANCE-CAPABILITIES.");
 System.out.println();
 System.out.println("7.   SCALING-OF-THE-FUNCTIONS-CAPABILITY.");
 System.out.println();
 System.out.println("8.   DATA-ANALYTICS-AT-THE-NETWORK-EDGE.");
 System.out.println();
 System.out.println("9.   SCIENTIFIC-COMPUTING.");
 System.out.println();
 System.out.println("10.  MOBILE-COMPUTING.");
 System.out.println();

 
  menuSelect = keyboard.nextInt();

 }

   if ( menuSelect == 1)
      
       {  System.out.println("**************************************************************************************************************" );
          System.out.println();
          System.out.println(" PLEASE SEE BELOW THE ENTIRE DISPLAY OF FUNCTION-AS-SERVICE (FaaS) CAPABILITIES : ");
          System.out.println();
          System.out.println("**************************************************************************************************************" ); 
          
          ScFAS.setFunctionExecutionCapability         (" A server-less platform handles the lifecycle, execution and scaling of the actual functions.These need to run only when invoked or triggered by an event. ");
          
          ScFAS.setStorageCapability                   (" A key challenge in running analytics workloads on serverless platforms is enabling tasks in different execution stages to efficiently communicate data between each other via a shared data store.There are several storage options for data sharing in serverless analytics jobs, each providing different cost, performance and scalability trade-offs. Managed object storage services like S3 offer pay-what-you-use capacity and bandwidth for storage resources managed by the provider. We consider three different categories of storage systems for ephemeral data sharing in serverless analytics:fully managed cloud storage, in-memory keyvalue storage and distributed Flash storage.  ");

          ScFAS.setContainerInfrastructureCapability   (" SCAR, a framework to execute container-based applications using serverless computing, exemplified using Docker as the technology for containers and AWS Lambda as the underlying serverless platform.The following benefits are obtained: First, the ability to run customized execution environments in such platforms opens up new approaches to adopt serverless computing in scientific scenarios that were previously unable to easily exploit the benefits of such computing platforms. Second, new programming languages can be used apart from those natively supported by the serverless platform. Third, a highly-parallel event-driven fileprocessing serverless execution model is defined.");          
         
          ScFAS.setNetworkingCapability                (" Serverless functions like AWS Lambda have been missing a critical ingredient needed to unlock their full potential — peer-to-peer networking. Without peer-to-peer networking, many important use cases are either impossible to achieve or require so much heavy lifting as to place them out of the range of most application developers. Some sample use cases include streaming content to or from a function, sharing files and in-memory objects among two or more functions, harvesting the results of an asynchronously invoked function, and pre-warming capacity. Without these capabilities, many companies struggle to adapt AWS Lambda or forego the benefits of serverless architectures to solve compute-dense distributed algorithms or demanding communication topologies — such as genetic algorithms, video transcoding, Monte Carlo simulations, and more. The launch of Serverless Networking fills this gap by making it easy to connect two Lambda functions to each or to connect a server-based implementation to a Lambda with two lines of code.. "); 
         
          ScFAS.setFaultToleranceCapability            (" Fault tolerance is the property of Server-less computing that enables it to continue operating properly in the event of the failure of (or one or more faults within) some of its components.The ability of maintaining functionality when portions of a system break down is referred to as graceful degradation. with an increasing number of applications being built on Functions-as-a-Service (FaaS) platforms. By default, server-less computing FaaS platforms support retry-based fault tolerance. ");        
          
          ScFAS.setScalingOfTheFunctionsCapability     (" Server-less architecture means that developers and operators do not need to spend time setting up and tuning autoscaling policies or systems, the cloud provider is responsible for scaling the capacity to the demand.Small teams of developers are able to run code themselves without the dependence upon teams of infrastructure and support engineers; more developers are becoming DevOps skilled and distinctions between being a software developer or hardware engineer are blurring. ");
          
          ScFAS.setDataAnalyticsCapability             (" A Serverless Real-Time Data Analytics Platform for Edge Computing. Latency-aware video analytics on edge computing platform. Low-latency video analytics is becoming more and more important for applications in public safety, counter-terrorism, self-driving cars, VR/AR, etc. Server-less edge computing has shown its potential in reducing response time, lowering bandwidth usage, improving energy efficiency and so on. Server-less computing also present an innovative data-driven serverless computing middleware for object storage. It is a lightweight compute solution that allows users to create small, stateless functions that intercept and operate on data flows in a scalable manner without the need to manage a server or a runtime environment.");
          
          ScFAS.setScientificComputingCapability       (" Scientific Workflow in the Cloud using Serverless Functions. A workflow is an orchestrated and repeatable pattern of activity, enabled by the systematic organization of resources into processes that transform materials, provide services, or process information. Doing Science involves the workflow of repeating and documenting experiments and the related data analysis. Consequently, managing workflow is critically important for the scientific endeavor. Serverless computing is a natural fit for workflow management. Serverless allows applications to run on demand without regard to compute resource reservation or management. Serverless computations are triggered by events. Typical among the list of event types are: 1.Messages arriving on Message Queues 2. Changes in Databases 3. Changes in Document Stores 4. Service APIs being invoked 5. Device sensor data sending new updates.These event types are each central to workflow automation.");
          
          ScFAS.setMobileComputingCapability           (" Serverless architecture can be used for building mobile apps, in addition to web applications. Hybrid mobile apps with a serverless backend enable developers to incorporate the benefits of serverless computing while releasing apps that perform like native apps on almost any smartphone or tablet. Serverless mobile apps are able to scale quickly and easily as the user base grows. With hybrid mobile apps, computing takes place in the cloud, not on the device. All cloud-hosted computing processes for the app can be serverless, just like a serverless web application; the only major difference between a serverless web app and a serverless hybrid mobile app is the native wrapper* on the frontend. As with a serverless web application, the app code is hosted by a serverless vendor who handles all backend management. The application is divided up into smaller pieces called functions, and the functions do not live on any specific servers. Each function runs in response to triggering events, and the vendor's infrastructure starts up new instances of functions as needed. For example, if a user taps on a 'Purchase' button within an app with a serverless backend, this can trigger a backend function or series of functions that start up, record the transaction, and initiate delivery of whatever the user purchased. Serverless mobile apps offer the same benefits as building a typical web application with a serverless backend: 1. Scalability: Serverless apps are automatically scalable 2. Less overhead: The vendor manages the entire backend 3. Quick updates: Developers can update functions one at a time instead of updating an entire application at once, and there is no need to wait for users to install updates 4. Pay-as-you-go: Developers only pay for the computing power the application uses, which can reduce ongoing costs 5. Run code anywhere: The code can run on an edge network in order to reduce latency. ");

                  
     
      System.out.println               (" FUNCTIONS EXECUTIONS CAPABILTY          = " + ScFAS.getFunctionExecutionCapability());
      System.out.println();          
      System.out.println               (" STORAGE CAPABILITY                      = " + ScFAS.getStorageCapability());
      System.out.println();
      System.out.println               (" CONTAINER INFRASTRUCTURE CAPABILITY     = " + ScFAS.getContainerInfrastructureCapability());
      System.out.println();
      System.out.println               (" NETWORKING CAPABILITY                   = " + ScFAS.getNetworkingCapability());
      System.out.println();
      System.out.println               (" FAULT TOLERANCE CAPABILITY              = " + ScFAS.getFaultToleranceCapability());
      System.out.println();
      System.out.println               (" SCALING OF THE FUNCTIONS CAPABILITY     = " + ScFAS.getScalingOfTheFunctionsCapability());
      System.out.println();
      System.out.println               (" DATA ANALYTICS CAPABILITY               = " + ScFAS.getDataAnalyticsCapability());
      System.out.println();
      System.out.println               (" SCIENTIFIC COMPUTING CAPABILITY         = " + ScFAS.getScientificComputingCapability());
      System.out.println();
      System.out.println               (" MOBILE COMPUTING CAPABILITY             = " + ScFAS.getMobileComputingCapability());
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT FUNCTION-AS-SERVICE CATEGORY PLEASE SELECT AGAIN SERVERLESS-COMPUTING MAIN MENU CHOICE # 1");
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println(" PLEASE SEE SERVERLESS-COMPUTING FUNCTIONS-EXECUTIONS CAPABILTY : ");
         System.out.println();
  
         ScFAS.setFunctionExecutionCapability         (" A server-less platform handles the lifecycle, execution and scaling of the actual functions.These need to run only when invoked or triggered by an event. ");
   
      
     
       System.out.println(" FUNCTIONS EXECUTIONS CAPABILTY               = " + ScFAS.getFunctionExecutionCapability());
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT FUNCTION-AS-SERVICE CATEGORY PLEASE SELECT AGAIN SERVERLESS-COMPUTING MAIN MENU CHOICE # 1");
       System.out.println();
       System.out.println("****************************************************************************************************************" );   
          
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
        System.out.println();
        System.out.println();
        System.out.println(" PLEASE SEE SERVERLESS-COMPUTING STORAFE CAPACITY: ");
        System.out.println();  

        ScFAS.setStorageCapability  (" A key challenge in running analytics workloads on serverless platforms is enabling tasks in different execution stages to efficiently communicate data between each other via a shared data store.There are several storage options for data sharing in serverless analytics jobs, each providing different cost, performance and scalability trade-offs. Managed object storage services like S3 offer pay-what-you-use capacity and bandwidth for storage resources managed by the provider. We consider three different categories of storage systems for ephemeral data sharing in serverless analytics:fully managed cloud storage, in-memory keyvalue storage and distributed Flash storage.  ");


        
      System.out.println(" SERVERLESS-COMPUTING STORAFE CAPACITY        = " + ScFAS.getStorageCapability());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT FUNCTION-AS-SERVICE CATEGORY PLEASE SELECT AGAIN SERVERLESS-COMPUTING MAIN MENU CHOICE # 1");
      System.out.println();
      System.out.println("****************************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE SERVERLESS-COMPUTING CONTAINER INFRASTRUCTURE CAPABILITY: ");
       System.out.println();
  
      ScFAS.setContainerInfrastructureCapability   (" SCAR, a framework to execute container-based applications using serverless computing, exemplified using Docker as the technology for containers and AWS Lambda as the underlying serverless platform.The following benefits are obtained: First, the ability to run customized execution environments in such platforms opens up new approaches to adopt serverless computing in scientific scenarios that were previously unable to easily exploit the benefits of such computing platforms. Second, new programming languages can be used apart from those natively supported by the serverless platform. Third, a highly-parallel event-driven fileprocessing serverless execution model is defined.");          
      
      System.out.println(" SERVERLESS-COMPUTING CONTAINER INFRASTRUCTURE CAPABILITY     = " + ScFAS.getContainerInfrastructureCapability());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT FUNCTION-AS-SERVICE CATEGORY PLEASE SELECT AGAIN SERVERLESS0-COMPUTING MAIN MENU CHOICE # 1");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
                  
         System.out.println();
         System.out.println(" PLEASE SEE SERVERLESS-COMPUTING NETWOERKING CAPABILITY "); 
         System.out.println();      
         ScFAS.setNetworkingCapability (" Serverless functions like AWS Lambda have been missing a critical ingredient needed to unlock their full potential — peer-to-peer networking. Without peer-to-peer networking, many important use cases are either impossible to achieve or require so much heavy lifting as to place them out of the range of most application developers. Some sample use cases include streaming content to or from a function, sharing files and in-memory objects among two or more functions, harvesting the results of an asynchronously invoked function, and pre-warming capacity. Without these capabilities, many companies struggle to adapt AWS Lambda or forego the benefits of serverless architectures to solve compute-dense distributed algorithms or demanding communication topologies — such as genetic algorithms, video transcoding, Monte Carlo simulations, and more. The launch of Serverless Networking fills this gap by making it easy to connect two Lambda functions to each or to connect a server-based implementation to a Lambda with two lines of code.. "); 
          
         System.out.println(" SERVERLESS-COMPUTING NETWOERKING CAPABILITY            = " + ScFAS.getNetworkingCapability());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT FUNCTION-AS-SERVICE CATEGORY PLEASE SELECT AGAIN SERVERLESS-COMPUTING MAIN MENU CHOICE # 1");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
     
      }

    else
   
        if ( menuSelect == 6)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE SERVERLESS-COMPUTING FAULT TOLERANCE CAPABILITY CAPABILITY ");
         System.out.println();  
         ScFAS.setFaultToleranceCapability (" Fault tolerance is the property of Server-less computing that enables it to continue operating properly in the event of the failure of (or one or more faults within) some of its components.The ability of maintaining functionality when portions of a system break down is referred to as graceful degradation. with an increasing number of applications being built on Functions-as-a-Service (FaaS) platforms. By default, server-less computing FaaS platforms support retry-based fault tolerance. ");        
         
         System.out.println(" SERVERLESS-COMPUTING FAULT TOLERANCE CAPABILITY CAPABILITY = " + ScFAS.getFaultToleranceCapability());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT FUNCTION-AS-SERVICE CATEGORY PLEASE SELECT AGAIN SERVERLESS-COMPUTING MAIN MENU CHOICE # 1");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 7)
       
       {
         
         System.out.println();
         System.out.println(" PLEASE SEE SERVERLESS-COMPUTING SCALING OF THE FUNCTIONS CAPABILITY ");
         System.out.println();
         ScFAS.setScalingOfTheFunctionsCapability (" Server-less architecture means that developers and operators do not need to spend time setting up and tuning autoscaling policies or systems, the cloud provider is responsible for scaling the capacity to the demand.Small teams of developers are able to run code themselves without the dependence upon teams of infrastructure and support engineers; more developers are becoming DevOps skilled and distinctions between being a software developer or hardware engineer are blurring. ");
         
         System.out.println(" SERVERLESS-COMPUTING SCALING OF THE FUNCTIONS CAPABILITY    = " + ScFAS.getScalingOfTheFunctionsCapability());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT FUNCTION-AS-SERVICE CATEGORY PLEASE SELECT AGAIN SERVERLESS-COMPUTING MAIN MENU CHOICE # 1");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 8)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE SERVERLESS-COMPUTING DATA ANALYTICS CAPABILITY ");
          System.out.println();
          
          ScFAS.setDataAnalyticsCapability  (" A Serverless Real-Time Data Analytics Platform for Edge Computing. Latency-aware video analytics on edge computing platform. Low-latency video analytics is becoming more and more important for applications in public safety, counter-terrorism, self-driving cars, VR/AR, etc. Server-less edge computing has shown its potential in reducing response time, lowering bandwidth usage, improving energy efficiency and so on. Server-less computing also present an innovative data-driven serverless computing middleware for object storage. It is a lightweight compute solution that allows users to create small, stateless functions that intercept and operate on data flows in a scalable manner without the need to manage a server or a runtime environment.");
          
         System.out.println(" SERVERLESS-COMPUTING DATA ANALYTICS CAPABILITY   = " + ScFAS.getDataAnalyticsCapability());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT FUNCTION-AS-SERVICE CATEGORY PLEASE SELECT AGAIN SERVERLESS-COMPUTING MAIN MENU CHOICE # 1");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
        

      }

else
          
    if ( menuSelect == 9)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE SERVERLESS-COMPUTING SCIENTIFIC COMPUTING CAPABILITY ");
          System.out.println();
          
         ScFAS.setScientificComputingCapability (" Scientific Workflow in the Cloud using Serverless Functions. A workflow is an orchestrated and repeatable pattern of activity, enabled by the systematic organization of resources into processes that transform materials, provide services, or process information. Doing Science involves the workflow of repeating and documenting experiments and the related data analysis. Consequently, managing workflow is critically important for the scientific endeavor. Serverless computing is a natural fit for workflow management. Serverless allows applications to run on demand without regard to compute resource reservation or management. Serverless computations are triggered by events. Typical among the list of event types are: 1.Messages arriving on Message Queues 2. Changes in Databases 3. Changes in Document Stores 4. Service APIs being invoked 5. Device sensor data sending new updates.These event types are each central to workflow automation.");
         
         System.out.println(" SERVERLESS-COMPUTING SCIENTIFIC COMPUTING CAPABILITY   = " + ScFAS.getScientificComputingCapability());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT FUNCTION-AS-SERVICE CATEGORY PLEASE SELECT AGAIN SERVERLESS-COMPUTING MAIN MENU CHOICE # 1");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
        

      }
else
          
    if ( menuSelect == 10)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE SERVERLESS-COMPUTING MOBILE COMPUTING CAPABILITY");
          System.out.println();
          
         ScFAS.setMobileComputingCapability (" Serverless architecture can be used for building mobile apps, in addition to web applications. Hybrid mobile apps with a serverless backend enable developers to incorporate the benefits of serverless computing while releasing apps that perform like native apps on almost any smartphone or tablet. Serverless mobile apps are able to scale quickly and easily as the user base grows. With hybrid mobile apps, computing takes place in the cloud, not on the device. All cloud-hosted computing processes for the app can be serverless, just like a serverless web application; the only major difference between a serverless web app and a serverless hybrid mobile app is the native wrapper* on the frontend. As with a serverless web application, the app code is hosted by a serverless vendor who handles all backend management. The application is divided up into smaller pieces called functions, and the functions do not live on any specific servers. Each function runs in response to triggering events, and the vendor's infrastructure starts up new instances of functions as needed. For example, if a user taps on a 'Purchase' button within an app with a serverless backend, this can trigger a backend function or series of functions that start up, record the transaction, and initiate delivery of whatever the user purchased. Serverless mobile apps offer the same benefits as building a typical web application with a serverless backend: 1. Scalability: Serverless apps are automatically scalable 2. Less overhead: The vendor manages the entire backend 3. Quick updates: Developers can update functions one at a time instead of updating an entire application at once, and there is no need to wait for users to install updates 4. Pay-as-you-go: Developers only pay for the computing power the application uses, which can reduce ongoing costs 5. Run code anywhere: The code can run on an edge network in order to reduce latency. ");

          
         System.out.println(" SERVERLESS-COMPUTING MOBILE COMPUTING CAPABILITY   = " + ScFAS.getMobileComputingCapability());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT FUNCTION-AS-SERVICE CATEGORY PLEASE SELECT AGAIN SERVERLESS-COMPUTING MAIN MENU CHOICE # 1");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
        

      }

     else
  
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   (" HERE ARE SRVERLESS-COMPUTING MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.print(" ENTER SERVERLESS-COMPUTING MAIN MENU SELECTIONS (1 - 8) FROM THE LIST ABOVE: ");
       
 menuSelection = keyboard.nextInt();
 
 while (menuSelection < 1 || menuSelection > 8) 
  
{
 
System.out.println(); 
System.out.println("************************************************************************************************" );
System.out.println();  
System.out.println(" THIS IS INVALID CHOICE FOR SERVERLESS-COMPUTING MAIN MENU SELECTIONS");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println(" HERE IS THE VALID LIST OF SERVERLESS-COMPUTING MAIN MENU SELECTIONS: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS.");  
System.out.println();
System.out.println ("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER SERVERLESS-COMPUTING MAIN MENU SELECTIONS (1 - 8) FROM THE LIST ABOVE: ");   
System.out.println();
System.out.println ("************************************************************************************************" );

  
  menuSelection = keyboard.nextInt();

 
 } 

break;


case 2: 

ScfSetter ScAP;

ScAP = new ScfSetter();

 System.out.println();
 
 System.out.println("YOU SELECTED SERVER-LESS APPLICATION PLATFORMS FROM MAIN MENU ");
 System.out.println();
 System.out.println(" PLEASE SEE BELOW SERVER-LESS APPLICATION PLATFORMS CATEGORIES");
 System.out.println();
 System.out.println("1.   BRIEF DISPLAY OF ALL SERVER-LESS APPLICATION PLATFORMS.");
 System.out.println();
 System.out.println("2.   APACHE OPEN-WHISK.");
 System.out.println();
 System.out.println("3.   FISSION .");
 System.out.println();
 System.out.println("4.   IRON-FUNCTIONS.");
 System.out.println();
 System.out.println("5.   FN-PROJECT.");
 System.out.println();
 System.out.println("6.   OPEN-LAMBDA.");
 System.out.println();
 System.out.println("7.   OPEN-FAAS.");
 System.out.println();
 System.out.println("8.   KUBELESS.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE OF SERVER-LESS PLATFORMS (1 to 8) : ");
   
 
  menuSelect = keyboard.nextInt();

  while (menuSelect < 1 || menuSelect > 8)
  

  
{
 System.out.println("************************************************************************************************" );
  
 System.out.println("THIS IS INVALID SERVER-LESS PLATFORMS CATEGORY SELECTION"); 
 System.out.println();
 System.out.println("PLEASE SELECT A VALID SERVER-LESS PLATFORMS FROM THE LIST BELOW"); 
 System.out.println();
 System.out.println(" PLEASE SEE BELOW SERVER-LESS APPLICATION PLATFORMS CATEGORIES");
 System.out.println();
 System.out.println("1.   BRIEF DISPLAY OF ALL SERVER-LESS APPLICATION PLATFORMS.");
 System.out.println();
 System.out.println("2.   APACHE OPEN-WHISK.");
 System.out.println();
 System.out.println("3.   FISSION .");
 System.out.println();
 System.out.println("4.   IRON-FUNCTIONS.");
 System.out.println();
 System.out.println("5.   FN-PROJECT.");
 System.out.println();
 System.out.println("6.   OPEN-LAMBDA.");
 System.out.println();
 System.out.println("7.   OPEN-FAAS.");
 System.out.println();
 System.out.println("8.   KUBELESS."); 
 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE OF SERVER-LESS PLATFORMS FROM (1 to 8) : ");


 
  menuSelect = keyboard.nextInt();


 }
  
    if ( menuSelect == 1)
      
       {  System.out.println("**************************************************************************************************************" );
          System.out.println();
          System.out.println(" PLEASE SEE BELOW BRIEF DESCRIPTION OF ALL SERVER-LESS APPLICATION PLATFORMS: ");
          System.out.println();
          System.out.println("**************************************************************************************************************" ); 
          
          ScAP.setApacheOpenWhisk (" Apache Open-Whisk is a serverless, open source cloud platform that allows you to execute code in response to events at any scale. It’s written in the Scala language. The framework processes the inputs from triggers like HTTP requests and later fires a snippet of code on either JavaScript or Swift. ");
          
          ScAP.setFission         (" Fission is a serverless computing framework that enables developers to build functions using Kubernetes. It allows coders to write short-lived functions in any programming language and map them with any event triggers, such as HTTP requests.  ");

          ScAP.setIronFunctions   (" Iron-Functions is a serverless computing framework that offers a cohesive microservices platform by integrating its existing services and embracing Docker. Developers write the functions in Go language. ");          
         
          ScAP.setFnProject       (" Fn-Project is an open source container-native serverless platform that you can run anywhere—on any cloud or on-premise. It’s easy to use, supports every programming language, and is extensible and performant. "); 
         
          ScAP.setOpenLambda      (" Open-Lambda is an Apache-licensed serverless computing project, written in Go and based on Linux containers. The primary goal of OpenLambda is to enable exploration of new approaches to serverless computing. ");        
          
          ScAP.setOpenFaas        (" Open-Faas is a framework for building serverless functions with Docker and Kubernetes that offers first-class support for metrics. Any process can be packaged as a function, enabling you to consume a range of web events without repetitive boilerplate coding. ");
          
          ScAP.setKubeless        (" Kubeless is a Kubernetes-native serverless framework that lets you deploy small bits of code without having to worry about the underlying infrastructure. It leverages Kubernetes resources to provide autoscaling, API routing, monitoring, troubleshooting, and more.");
          
                            
     
      System.out.println               (" APACHE OPEN WHISK PLATFORM  = " + ScAP.getApacheOpenWhisk());
      System.out.println();          
      System.out.println               (" FISSION PLATFORM            = " + ScAP.getFission());
      System.out.println();
      System.out.println               (" IRON FUNCTIONS PLATFORM     = " + ScAP.getIronFunctions());
      System.out.println();
      System.out.println               (" FN PROJECT PLATFORM         = " + ScAP.getFnProject());
      System.out.println();
      System.out.println               (" OPEN LAMBDA PLATFORM        = " + ScAP.getOpenLambda());
      System.out.println();
      System.out.println               (" OPEN FAAS PLATFORM          = " + ScAP.getOpenFaas());
      System.out.println();
      System.out.println               (" KUBELESS PLATFORM           = " + ScAP.getKubeless());
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS APPLICATION PLATFORM PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 2");
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW SERVER-LESS APACHE OPEN WHISK PLATFORM: ");
         System.out.println();
  
         ScAP.setApacheOpenWhisk (" Apache OpenWhisk is a serverless, open source cloud platform that allows you to execute code in response to events at any scale. It’s written in the Scala language. The framework processes the inputs from triggers like HTTP requests and later fires a snippet of code on either JavaScript or Swift.");
   
      
     
       System.out.println(" APACHE OPEN WHISK PLATFORM  = " + ScAP.getApacheOpenWhisk());
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS APPLICATION PLATFORM PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 2");
       System.out.println();
       System.out.println();
       System.out.println("****************************************************************************************************************" );   
          
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
        System.out.println();
        System.out.println();
        System.out.println(" PLEASE SEE BELOW SERVER-LESS FISSION PLATFORM: ");
        System.out.println();  

        ScAP.setFission  (" Fission is a serverless computing framework that enables developers to build functions using Kubernetes. It allows coders to write short-lived functions in any programming language and map them with any event triggers, such as HTTP requests. ");


        
      System.out.println(" SERVER-LESS FISSION PLATFORM  = " + ScAP.getFission());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS APPLICATION PLATFORM PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 2");
      System.out.println();
      System.out.println();
      System.out.println("****************************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE BELOW SERVER-LESS IRON FUNCTIONS PLATFORM:: ");
       System.out.println();
  
      ScAP.setIronFunctions (" IronFunctions is a serverless computing framework that offers a cohesive microservices platform by integrating its existing services and embracing Docker. Developers write the functions in Go language.");          
      
      System.out.println(" IRON FUNCTIONS PLATFORM = " + ScAP.getIronFunctions());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS APPLICATION PLATFORM PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 2");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
                  
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS FN PROJECT PLATFORM: "); 
         System.out.println();      
         ScAP.setFnProject (" Fn Project is an open source container-native serverless platform that you can run anywhere—on any cloud or on-premise. It’s easy to use, supports every programming language, and is extensible and performant. "); 
          
         System.out.println(" FN PROJECT PLATFORM = " + ScAP.getFnProject());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS APPLICATION PLATFORM PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 2");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
     
      }

    else
   
        if ( menuSelect == 6)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS OPEN LAMBDA PLATFORM:");
         System.out.println();  
         ScAP.setOpenLambda (" Open-Lambda is an Apache-licensed serverless computing project, written in Go and based on Linux containers. The primary goal of OpenLambda is to enable exploration of new approaches to serverless computing. ");        
         
         System.out.println(" OPEN LAMBDA PLATFORM = " + ScAP.getOpenLambda());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS APPLICATION PLATFORM PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 2");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 7)
       
       {
         
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS OPEN FAAS PLATFORM:");
         System.out.println();
         ScAP.setOpenFaas (" Open-Faas is a framework for building serverless functions with Docker and Kubernetes that offers first-class support for metrics. Any process can be packaged as a function, enabling you to consume a range of web events without repetitive boilerplate coding. ");
         
         System.out.println(" SERVERLESS-COMPUTING SCALING OF THE FUNCTIONS CAPABILITY    = " + ScAP.getOpenFaas());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS APPLICATION PLATFORM PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 2");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 8)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW SERVER-LESS KUBELESS PLATFORM: ");
          System.out.println();
          
          ScAP.setKubeless  (" Kubeless is a Kubernetes-native serverless framework that lets you deploy small bits of code without having to worry about the underlying infrastructure. It leverages Kubernetes resources to provide autoscaling, API routing, monitoring, troubleshooting, and more.");
          
         System.out.println(" SERVERLESS-COMPUTING KUBELESS PLATFORM  = " + ScAP.getKubeless());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS APPLICATION PLATFORM PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 2");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
        

      }


  else        
 
System.out.println();
System.out.println   ("HERE ARE SRVERLESS-COMPUTING MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.print("ENTER SERVER-LESS MAIN MENU CATEGORY CHOICE ( 1 - 8) FROM THE LIST ABOVE: ");
       
   menuSelection = keyboard.nextInt();
 

 while (menuSelection < 1 || menuSelection > 8) 
  
{
System.out.println(); 
System.out.println("THIS IS INVALID CHOICE FOR SERVERLESS-COMPUTING MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE ARE VALID SERVERLESS-COMPUTING MAIN MENU SELECTIONS CHOICE LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.print     ("PLEASE ENTER SERVER-LESS MAIN MENU CATEGORY CHOICE (1 - 8) FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();

  
 } 


break; 

case 3:

ScfSetter ScAI;

ScAI = new ScfSetter();

 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println("YOU SELECTED AI & DEEP-LEARNING CATEGORY FROM SERVER-LESS MAIN MENU");
 System.out.println();
 System.out.println("PLEASE SEE BELOW AI & DEEP-LEARNING SUBCATEGORIES FOR SERVER-LESS");
 System.out.println();
 System.out.println("1.  DESCRIPTION OF ALL AI & DEEP-LEARNING PLATFORMS FOR SERVER-LESS COMPUTING. ");
 System.out.println();
 System.out.println("2.  SERVER-LESS DEEP LEARNING.");
 System.out.println();
 System.out.println("3.  SERVER-LESS DEEP LEARNING FRAMEWORK TENSORFLOW.");
 System.out.println();
 System.out.println("4.  SERVER-LESS DEEP LEARNING FRAMEWORK MXNET.");
 System.out.println();
 System.out.println("5.  SERVER-LESS DEEP LEARNING FRAMEWORK CAFFE.");
 System.out.println();
 System.out.println("6.  SERVER-LESS DEEP LEARNING ON AWS LAMBDA PLATFORM");
 System.out.println();
 System.out.println("7.  SERVER-LESS DEEP LEARNING ON APACHE OPEN-WHISK PLATFORM.");
 System.out.println();
 System.out.println("8.  SERVER-LESS DEEP LEARNING WITH NEURAL NETWORK MODELS.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR AI & DEEP-LEARNING SUBCATEGORY CHOICE FROM (1 to 8): ");
   
 
  menuSelect = keyboard.nextInt();


 while (menuSelect < 1 || menuSelect > 8)
  
  
{
 System.out.println();
 System.out.println("************************************************************************************************" );  
 System.out.println (" THIS IS INVALID SELECTION OF AI & DEEP-LEARNING SUBCATEGORY CHOICE"); 
 System.out.println();
 System.out.println(" PLEASE SEE BELOW VALID AI & DEEP-LEARNING SUBCATEGORY CHOICE ");
 System.out.println();
 System.out.println("1.  DESCRIPTION OF ALL AI & DEEP-LEARNING PLATFORMS FOR SERVER-LESS COMPUTING. ");
 System.out.println();
 System.out.println("2.  SERVER-LESS DEEP LEARNING.");
 System.out.println();
 System.out.println("3.  SERVER-LESS DEEP LEARNING FRAMEWORK TENSORFLOW.");
 System.out.println();
 System.out.println("4.  SERVER-LESS DEEP LEARNING FRAMEWORK MXNET.");
 System.out.println();
 System.out.println("5.  SERVER-LESS DEEP LEARNING FRAMEWORK CAFFE.");
 System.out.println();
 System.out.println("6.  SERVER-LESS DEEP LEARNING ON AWS LAMBDA PLATFORM");
 System.out.println();
 System.out.println("7.  SERVER-LESS DEEP LEARNING ON APACHE OPEN-WHISK PLATFORM.");
 System.out.println();
 System.out.println("8.  SERVER-LESS DEEP LEARNING WITH NEURAL NETWORK MODELS.");
 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR AI & DEEP-LEARNING SUBCATEGORY CHOICE (1 to 8): ");


 
  menuSelect = keyboard.nextInt();


 }


   
   if ( menuSelect == 1)
      
       {  System.out.println("**************************************************************************************************************" );
          System.out.println();
          System.out.println(" PLEASE SEE BELOW BRIEF DESCRIPTION OF ALL AI & DEEP-LEARNING PLATFORMS FOR SERVER-LESS COMPUTING: ");
          System.out.println();
          System.out.println("**************************************************************************************************************" ); 
          
          ScAI.setDeepLearning (" Deep learning is a Technique for implementing Machine Learning. It uses neural networks to learn, sometimes, using decision trees may also be referred to as deep learning, but for the most part deep learning involves the use of neural networks. Deep learning, driven by large neural network models, is overtaking traditional machine learning methods for understanding unstructured and perceptual data domains such as speech, text, and vision. AI has been fueled by three recent trends: the explosion in the amount of training data, the use of accelerators such as graphics processing units (GPUs), and advancements in the design of models used for training. Using any of the deep learning frameworks (e.g., Caffe, Tensorflow, MXNet), users can develop and train their models.  ");
          
          ScAI.setDlTesorflow  (" Tensorflow is the most popular and apparently best Deep Learning Framework out there. TensorFlow is created by the Google Brain team, is an open source library for numerical computation and large-scale machine learning. TensorFlow bundles together a slew of machine learning and deep learning (aka neural networking) models and algorithms and makes them useful by way of a common metaphor. TensorFlow is a Python library for fast numerical computing created and released by Google. It is a foundation library that can be used to create Deep Learning models directly or by using wrapper libraries that simplify the process built on top of TensorFlow. ");

          ScAI.setDlMxnet      (" MXNet provides a comprehensive and flexible Python API to serve a broad community of developers with different levels of experience and wide ranging requirements. Apache MXNet is an open-source deep learning software framework, used to train, and deploy deep neural networks. It is scalable, allowing for fast model training, and supports a flexible programming model and multiple programming languages (including C++, Python, Java, Julia, Matlab, JavaScript, Go, R, Scala, Perl, and Wolfram Language). The MXNet library is portable and can scale to multiple GPUs and multiple machines. MXNet is supported by public cloud providers including Amazon Web Services (AWS) and Microsoft Azure. Amazon has chosen MXNet as its deep learning framework of choice at AWS. Apache MXNet is a lean, flexible, and ultra-scalable deep learning framework that supports state of the art in deep learning models, including convolutional neural networks (CNNs) and long short-term memory networks (LSTMs). ");          
         
          ScAI.setDlCaffe      (" Caffe is a deep learning framework made with expression, speed, and modularity in mind. It is developed by Berkeley AI Research (BAIR) and by community contributors. Yangqing Jia created the project during his PhD at UC Berkeley. Caffe is released under the BSD 2-Clause license. Expressive architecture encourages application and innovation. Extensible code fosters active development. Speed makes Caffe perfect for research experiments and industry deployment. Caffe can process over 60M images per day with a single NVIDIA K40 GPU. Community: Caffe already powers academic research projects, startup prototypes, and even large-scale industrial applications in vision, speech, and multimedia. Join our community of brewers on the caffe-users group and Github. "); 
         
          ScAI.setDlLambda     (" AWS Lambda is a serverless compute service that runs the code in response to events and automatically manages the underlying compute resources. AWS Lambda can be used to extend other AWS services with custom logic, or create your own back-end services that operate at AWS scale, performance, and security. You do not have to scale your Lambda functions – AWS Lambda scales them automatically on your behalf. Every time an event notification is received for your function, AWS Lambda quickly locates free capacity within its compute fleet and runs your code. AWS Lambda can use Java, Node.jS, Python, GO, Net.Core & Ruby. ");        
          
          ScAI.setDlOpenWhisk  (" Apache OpenWhisk is an open source distributed Serverless platform that executes functions (fx) in response to events at any scale. OpenWhisk manages the infrastructure, servers & scaling using Dockers containers so you can focus on building amazing and efficient applications. OpenWhisk platform supports a programming model in which developers write functional logic (called Actions), in any supported programming language that can be dynamically scheduled and run in response to associated events (via Triggers)from external sources (Feeds) or from HTTP requests. the project includes a REST API based command line interface (CLI) along with other tools to support packaging, catalog services and many popular container deployment options. ");
          
          ScAI.setDlNeural     (" A neural network, is a collection of layers that transform the input in some way to produce an output. Neural network models range in size from small (5MB) to very large (500MB). Training neural networks can take a significant amount of time, and the goal is to find suitable weights for the different variables in the neural network. Once the model training is complete, it can be used for inferencing , serving applying the trained model on new data in domains such a natural language processing, speech recognition, or image classification. ");
          
                            
     
      System.out.println               (" SERVER-LESS DEEP LEARNING                               = " + ScAI.getDeepLearning());
      System.out.println();          
      System.out.println               (" SERVER-LESS DEEP LEARNING FRAMEWORK TENSORFLOW          = " + ScAI.getDlTesorflow ());
      System.out.println();
      System.out.println               (" SERVER-LESS DEEP LEARNING FRAMEWORK MXNET               = " + ScAI.getDlMxnet());
      System.out.println();
      System.out.println               (" SERVER-LESS DEEP LEARNING FRAMEWORK CAFFE               = " + ScAI.getDlCaffe  ());
      System.out.println();
      System.out.println               (" SERVER-LESS DEEP LEARNING FRAMEWORK LAMBDA              = " + ScAI.getDlLambda ());
      System.out.println();
      System.out.println               (" SERVER-LESS DEEP LEARNING APACHE OPEN WHISK PLATFORM    = " + ScAI.getDlOpenWhisk());
      System.out.println();
      System.out.println               (" SERVER-LESS DEEP LEARNING NEURAL NETWORKS               = " + ScAI.getDlNeural());
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT AI & DEEP-LEARNING CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 3");
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW SERVER-LESS DEEP LEARNING PLATFORM: ");
         System.out.println();
  
         ScAI.setDeepLearning (" Deep learning is a Technique for implementing Machine Learning. It uses neural networks to learn, sometimes, using decision trees may also be referred to as deep learning, but for the most part deep learning involves the use of neural networks. Deep learning, driven by large neural network models, is overtaking traditional machine learning methods for understanding unstructured and perceptual data domains such as speech, text, and vision. AI has been fueled by three recent trends: the explosion in the amount of training data, the use of accelerators such as graphics processing units (GPUs), and advancements in the design of models used for training. Using any of the deep learning frameworks (e.g., Caffe, Tensorflow, MXNet), users can develop and train their models.  ");
   
      
     
       System.out.println (" SERVER-LESS DEEP LEARNING = " + ScAI.getDeepLearning());
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT AI & DEEP-LEARNING CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 3");
       System.out.println();
       System.out.println();
       System.out.println("****************************************************************************************************************" );   
          
       }
     
     else
     
     if ( menuSelect == 3 )
     
        {
        System.out.println();
        System.out.println();
        System.out.println(" PLEASE SEE BELOW SERVER-LESS DEEP LEARNING FRAMEWORK TENSORFLOW: ");
        System.out.println();  

        ScAI.setDlTesorflow (" Tensorflow is the most popular and apparently best Deep Learning Framework out there. TensorFlow is created by the Google Brain team, is an open source library for numerical computation and large-scale machine learning. TensorFlow bundles together a slew of machine learning and deep learning (aka neural networking) models and algorithms and makes them useful by way of a common metaphor. TensorFlow is a Python library for fast numerical computing created and released by Google. It is a foundation library that can be used to create Deep Learning models directly or by using wrapper libraries that simplify the process built on top of TensorFlow. ");


        
      System.out.println (" SERVER-LESS DEEP LEARNING FRAMEWORK TENSORFLOW = " + ScAI.getDlTesorflow ());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT AI & DEEP-LEARNING CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 3");
      System.out.println();
      System.out.println();
      System.out.println("****************************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE BELOW SERVER-LESS DEEP LEARNING FRAMEWORK MXNET: ");
       System.out.println();
  
      ScAI.setDlMxnet      (" MXNet provides a comprehensive and flexible Python API to serve a broad community of developers with different levels of experience and wide ranging requirements. Apache MXNet is an open-source deep learning software framework, used to train, and deploy deep neural networks. It is scalable, allowing for fast model training, and supports a flexible programming model and multiple programming languages (including C++, Python, Java, Julia, Matlab, JavaScript, Go, R, Scala, Perl, and Wolfram Language). The MXNet library is portable and can scale to multiple GPUs and multiple machines. MXNet is supported by public cloud providers including Amazon Web Services (AWS) and Microsoft Azure. Amazon has chosen MXNet as its deep learning framework of choice at AWS. Apache MXNet is a lean, flexible, and ultra-scalable deep learning framework that supports state of the art in deep learning models, including convolutional neural networks (CNNs) and long short-term memory networks (LSTMs). ");          
      
      System.out.println   (" SERVER-LESS DEEP LEARNING FRAMEWORK MXNET = " + ScAI.getDlMxnet());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT AI & DEEP-LEARNING CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 3");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
                  
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS DEEP LEARNING FRAMEWORK CAFFE: "); 
         System.out.println();      
         ScAI.setDlCaffe      (" Caffe is a deep learning framework made with expression, speed, and modularity in mind. It is developed by Berkeley AI Research (BAIR) and by community contributors. Yangqing Jia created the project during his PhD at UC Berkeley. Caffe is released under the BSD 2-Clause license. Expressive architecture encourages application and innovation. Extensible code fosters active development. Speed makes Caffe perfect for research experiments and industry deployment. Caffe can process over 60M images per day with a single NVIDIA K40 GPU. Community: Caffe already powers academic research projects, startup prototypes, and even large-scale industrial applications in vision, speech, and multimedia. Join our community of brewers on the caffe-users group and Github. "); 
         
         System.out.println   (" SERVER-LESS DEEP LEARNING FRAMEWORK CAFFE = " + ScAI.getDlCaffe  ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT AI & DEEP-LEARNING CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 3");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
     
      }

    else
   
        if ( menuSelect == 6)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS DEEP LEARNING FRAMEWORK LAMBDA:");
         System.out.println();  
         ScAI.setDlLambda     (" AWS Lambda is a serverless compute service that runs the code in response to events and automatically manages the underlying compute resources. AWS Lambda can be used to extend other AWS services with custom logic, or create your own back-end services that operate at AWS scale, performance, and security. You do not have to scale your Lambda functions – AWS Lambda scales them automatically on your behalf. Every time an event notification is received for your function, AWS Lambda quickly locates free capacity within its compute fleet and runs your code. AWS Lambda can use Java, Node.jS, Python, GO, Net.Core & Ruby. ");        
          
          System.out.println  (" SERVER-LESS DEEP LEARNING FRAMEWORK LAMBDA = " + ScAI.getDlLambda ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT AI & DEEP-LEARNING CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 3");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 7)
       
       {
         
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS DEEP LEARNING APACHE OPEN WHISK PLATFORM:");
         System.out.println();
         ScAI.setDlOpenWhisk  (" Apache OpenWhisk is an open source distributed Serverless platform that executes functions (fx) in response to events at any scale. OpenWhisk manages the infrastructure, servers & scaling using Dockers containers so you can focus on building amazing and efficient applications. OpenWhisk platform supports a programming model in which developers write functional logic (called Actions), in any supported programming language that can be dynamically scheduled and run in response to associated events (via Triggers)from external sources (Feeds) or from HTTP requests. the project includes a REST API based command line interface (CLI) along with other tools to support packaging, catalog services and many popular container deployment options. ");
          
         System.out.println   (" SERVER-LESS DEEP LEARNING APACHE OPEN WHISK PLATFORM = " + ScAI.getDlOpenWhisk());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT AI & DEEP-LEARNING CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 3");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 8)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW SERVER-LESS DEEP LEARNING NEURAL NETWORKS PLATFORM: ");
          System.out.println();
          
          ScAI.setDlNeural     (" A neural network, is a collection of layers that transform the input in some way to produce an output. Neural network models range in size from small (5MB) to very large (500MB). Training neural networks can take a significant amount of time, and the goal is to find suitable weights for the different variables in the neural network. Once the model training is complete, it can be used for inferencing , serving applying the trained model on new data in domains such a natural language processing, speech recognition, or image classification. ");
          
         System.out.println    (" SERVER-LESS DEEP LEARNING NEURAL NETWORKS = " + ScAI.getDlNeural());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT AI & DEEP-LEARNING CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 3");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
        

      }


  else 
  
System.out.println();
System.out.println   ("HERE ARE SRVERLESS-COMPUTING MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.print("ENTER SERVER-LESS MAIN MENU CATEGORY CHOICE ( 1 - 8) FROM THE LIST ABOVE: ");
       
   menuSelection = keyboard.nextInt();
 

 while (menuSelection < 1 || menuSelection > 8) 
  
{
System.out.println(); 
System.out.println("THIS IS INVALID CHOICE FOR SERVERLESS-COMPUTING MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE ARE VALID SERVERLESS-COMPUTING MAIN MENU SELECTIONS CHOICE LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS.");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.print     ("PLEASE ENTER SERVER-LESS MAIN MENU CATEGORY CHOICE (1 - 8) FROM THE LIST ABOVE: ");

    
  menuSelection = keyboard.nextInt();
  
 } 

break;

case 4:
 
ScfSetter ScUC;

ScUC = new ScfSetter();
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println(" YOU SELECTED USE-CASES CATEGORY FROM SERVER-LESS MAIN MENU.");
 System.out.println();
 System.out.println(" PLEASE SEE BELOW TOP 10 USE CASES OF SERVER-LESS COMPUTING: ");
 System.out.println(); 
 System.out.println("1.    BRIEF DESCRIPTION OF ALL USE-CASES FOR SERVER-LESS COMPUTING");
 System.out.println();
 System.out.println("2.    MULTIMEDIA PROCESSING");
 System.out.println();
 System.out.println("3.    DATABASE CHANGES OR CHANGE DATA CAPTURE.");
 System.out.println();
 System.out.println("4.    IoT SENSOR INPUT MESSAGES.");
 System.out.println();
 System.out.println("5.    STREAM PROCESSING OF SCALE.");
 System.out.println();
 System.out.println("6.    CHATBOTS.");
 System.out.println();
 System.out.println("7.    BATCH JOBS SCHEDULED TASKS.");
 System.out.println();
 System.out.println("8.    HTTP REST APIs AND WEB APPS.");
 System.out.println();
 System.out.println("9.    MOBILE BACK ENDS.");
 System.out.println();
 System.out.println("10.   BUSINESS LOGIC.");
 System.out.println();
 System.out.println("11.   CONTINUOUS INTEGRATION PIPELINE.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM SERVERLESS USE-CASES ( 1 to 11): ");
   
 
  menuSelect = keyboard.nextInt();

 while (menuSelect < 1 || menuSelect > 11)
  
{ 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println(); 
 System.out.println(" THIS IS INVALID CHOICE FOR SERVER-LESS USE-CASES SELECTION"); 
 System.out.println();
 System.out.println(" PLEASE SEE BELOW VALID USE-CASES SELECTIONS OF SERVER-LESS COMPUTING. ");
 System.out.println();
 System.out.println("1.    BRIEF DESCRIPTION OF ALL USE-CASES FOR SERVER-LESS COMPUTING");
 System.out.println();
 System.out.println("2.    MULTIMEDIA PROCESSING");
 System.out.println();
 System.out.println("3.    DATABASE CHANGES OR CHANGE DATA CAPTURE.");
 System.out.println();
 System.out.println("4.    IoT SENSOR INPUT MESSAGES.");
 System.out.println();
 System.out.println("5.    STREAM PROCESSING OF SCALE.");
 System.out.println();
 System.out.println("6.    CHATBOTS.");
 System.out.println();
 System.out.println("7.    BATCH JOBS SCHEDULED TASKS.");
 System.out.println();
 System.out.println("8.    HTTP REST APIs AND WEB APPS.");
 System.out.println();
 System.out.println("9.    MOBILE BACK ENDS.");
 System.out.println();
 System.out.println("10.   BUSINESS LOGIC.");
 System.out.println();
 System.out.println("11.   CONTINUOUS INTEGRATION PIPELINE."); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR USE-CASES CATEGORY CHOICE FROM (1 to 11):  ");

  menuSelect = keyboard.nextInt();

 }
     if ( menuSelect == 1)
      
       {  System.out.println("**************************************************************************************************************" );
          System.out.println();
          System.out.println(" PLEASE SEE BELOW BRIEF DESCRIPTION OF ALL USE-CASES FOR SERVER-LESS COMPUTING: ");
          System.out.println();
          System.out.println("**************************************************************************************************************" ); 
          
          ScUC.setMultimediaProcessing   (" The implementation of functions that execute a transformational process in response to a file upload.  ");
          
          ScUC.setDatabaseChanges        (" Auditing or ensuring changes meet quality standards. ");

          ScUC.setIotSensor              (" The ability to respond to messages and scale in response. ");          
         
          ScUC.setStreamProcessing       ("  Processing data within a potentially infinite stream of messages."); 
         
          ScUC.setChatBots               (" Scaling automatically for peak demands. ");        
           
          ScUC.setBatchJobsScheduledtasks (" The ability to remove the need for pre-provisioned hosts. ");

          ScUC.setHttpRestApi            (" Jobs that require intense parallel computation, IO or network access. ");
          
          ScUC.setMobileBackEnds          (" Traditional request and response workloads. ");
          
          ScUC.setBusinessLogic          (" Ability to build on the REST API backend workload above the BaaS APIs.  ");
          
          ScUC.setContinuousIntegration  (" The orchestration of microservice workloads that execute a series of steps. ");
          
          

                      
     
      System.out.println               (" MULTIMEDIA PROCESSING:                   = " + ScUC.getMultimediaProcessing());
      System.out.println();          
      System.out.println               (" DATABASE CHANGES OR CHANGE DATA CAPTURE: = " + ScUC.getDatabaseChanges ());
      System.out.println();
      System.out.println               (" IoT SENSOR INPUT MESSGES:                = " + ScUC.getIotSensor ());
      System.out.println();
      System.out.println               (" STREAM PROCESSING AT SCALE:              = " + ScUC.getStreamProcessing ());
      System.out.println();
      System.out.println               (" CHATBOTS:                                = " + ScUC.getChatBots ());
      System.out.println();
      System.out.println               (" BATCH JOBS SCHEDULED TASKS:              = " + ScUC.getBatchJobsScheduledtasks());
      System.out.println();
      System.out.println               (" HTTPS REST APIs & WEB APPS:              = " + ScUC.getHttpRestApi ());
      System.out.println();
      System.out.println               (" MOBILE BACK-ENDS:                        = " + ScUC.getMobileBackEnds ());
      System.out.println();
      System.out.println               (" BUSINESS LOGIC:                          = " + ScUC.getBusinessLogic ());
      System.out.println();
      System.out.println               (" CONTINUOUS INTEGRATION PIPELINE:         = " + ScUC.getContinuousIntegration());
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT USE-CASES CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 4");
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW SERVER-LESS MULTIMEDIA PROCESSING USE-CASE: ");
         System.out.println();
  
         ScUC.setMultimediaProcessing   (" The implementation of functions that execute a transformational process in response to a file upload.  ");
   
      
     
       System.out.println               (" IoT SENSOR INPUT MESSGES:                = " + ScUC.getMultimediaProcessing ());
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT USE-CASES CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 4");
       System.out.println();
       System.out.println();
       System.out.println("****************************************************************************************************************" );   
          
       }
     
     else
     
     if ( menuSelect == 3 )
     
        {
        System.out.println();
        System.out.println();
        System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE DATA BASE CHANGES: ");
        System.out.println();  

        ScUC.setDatabaseChanges        (" Auditing or ensuring changes meet quality standards. ");


        
      System.out.println               (" DATABASE CHANGES OR CHANGE DATA CAPTURE: = " + ScUC.getDatabaseChanges ());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT USE-CASES CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 4");
      System.out.println();
      System.out.println();
      System.out.println("****************************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE IoT SENSOR: ");
       System.out.println();
  
      ScUC.setIotSensor              (" The ability to respond to messages and scale in response. ");   
       
      System.out.println               (" IoT SENSOR INPUT MESSGES:= " + ScUC.getIotSensor ());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT USE-CASES CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 4");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
                  
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE: "); 
         System.out.println();
               
         ScUC.setStreamProcessing       ("  Processing data within a potentially infinite stream of messages.");
                
         System.out.println               (" STREAM PROCESSING AT SCALE: = " + ScUC.getStreamProcessing ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT USE-CASES CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 4");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
     
      }

    else
   
        if ( menuSelect == 6)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
         ScUC.setChatBots               (" Scaling automatically for peak demands. "); 
                 
         System.out.println               (" CHATBOTS: = " + ScUC.getChatBots ());         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT USE-CASES CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 4");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 7)
       
       {
         
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println();
         
         ScUC.setBatchJobsScheduledtasks (" The ability to remove the need for pre-provisioned hosts. "); 
                 
         System.out.println               (" BATCH JOBS SCHEDULED TASKS: = " + ScUC.getBatchJobsScheduledtasks());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT USE-CASES CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 4");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 8)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE: ");
          System.out.println();
          
         ScUC.setHttpRestApi            (" Jobs that require intense parallel computation, IO or network access. ");
                   
         System.out.println               (" HTTPS REST APIs & WEB APPS: = " + ScUC.getHttpRestApi ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT USE-CASES CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 4");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
     
     else
   
        if ( menuSelect == 9)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
         ScUC.setMobileBackEnds          (" Traditional request and response workloads. ");
 
                 
         System.out.println               (" MOBILE BACK-ENDS: = " + ScUC.getMobileBackEnds ());

         
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT USE-CASES CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 4");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 10)
       
       {
         
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println();
         
         ScUC.setBusinessLogic          (" Ability to build on the REST API backend workload above the BaaS APIs.  "); 
                  
         System.out.println             (" BUSINESS LOGIC: = " + ScUC.getBusinessLogic ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT USE-CASES CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 4");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      } 
        
      else
   
        if ( menuSelect == 11)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
         ScUC.setContinuousIntegration  (" The orchestration of microservice workloads that execute a series of steps. "); 
                 
         System.out.println               (" CONTINUOUS INTEGRATION PIPELINE: = " + ScUC.getContinuousIntegration());
         
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT USE-CASES CATEGORIES PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 4");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

           
      else
      
System.out.println();
System.out.println   (" HERE ARE SRVERLESS-COMPUTING MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS.");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.print("ENTER SERVER-LESS MAIN MENU CATEGORY CHOICE ( 1 - 8) FROM THE LIST ABOVE: ");   
    
  menuSelection = keyboard.nextInt();
 
 while (menuSelection < 1 || menuSelection > 8) 
  
{
System.out.println(); 
System.out.println(" THIS IS INVALID CHOICE FOR SERVERLESS-COMPUTING MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println(" HERE ARE VALID SERVERLESS-COMPUTING MAIN MENU SELECTIONS CHOICE LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.print     ("PLEASE ENTER SERVER-LESS MAIN MENU CATEGORY CHOICE (1 - 8) FROM THE LIST ABOVE: ");

    
  menuSelection = keyboard.nextInt();
  
 } 
        
break;

case 5:
 
ScfSetter ScCHR;

ScCHR = new ScfSetter();
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println(" YOU SELECTED SEVER-LESS CHARACTERISTICS CATEGORY");
 System.out.println();
 System.out.println(" PLEASE SEE BELOW SEVER-LESS CHARACTERISTICS: ");
 System.out.println(); 
 System.out.println("1.  BRIEF DESCRIPTION OF ALL SERVER-LESS CHARACTERISTICS. ");
 System.out.println();
 System.out.println("2.  COST. ");
 System.out.println();
 System.out.println("3.  PERFORMANCE & LIMITS.");
 System.out.println();
 System.out.println("4.  PROGRAMMING LANGUAGES.");
 System.out.println();
 System.out.println("5.  PROGRAMMING MODEL.");
 System.out.println();
 System.out.println("6.  COMPOSABILITY.");
 System.out.println();
 System.out.println("7.  DEPLOYMENT.");
 System.out.println();
 System.out.println("8.  SECURITY & ACCOUNTING.");
 System.out.println();
 System.out.println("9.  MONITORING & DEBUGGING.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM SEVER-LESS CHARACTERISTICS (1 to 9): ");
   
 
  menuSelect = keyboard.nextInt();

 while (menuSelect < 1 || menuSelect > 9)
  
{
 System.out.println("************************************************************************************************" );  
 System.out.println("THIS IS INVALID CHOICE FOR SERVER-LESS CHARACTERISTICS"); 
 System.out.println();
 System.out.println("PLEASE SEE BELOW THE LIST OF VALID SERVER-LESS CHARACTERISTICS: "); 
 System.out.println();
 System.out.println("1.  BRIEF DESCRIPTION OF ALL SERVER-LESS CHARACTERISTICS. ");
 System.out.println();
 System.out.println("2.  COST. ");
 System.out.println();
 System.out.println("3.  PERFORMANCE & LIMITS.");
 System.out.println();
 System.out.println("4.  PROGRAMMING LANGUAGES.");
 System.out.println();
 System.out.println("5.  PROGRAMMING MODEL.");
 System.out.println();
 System.out.println("6.  COMPOSABILITY.");
 System.out.println();
 System.out.println("7.  DEPLOYMENT.");
 System.out.println();
 System.out.println("8.  SECURITY & ACCOUNTING.");
 System.out.println();
 System.out.println("9.  MONITORING & DEBUGGING.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR SEVER-LESS CHARACTERISTICS CHOICE FROM (1 to 9): ");

 
  menuSelect = keyboard.nextInt();

 }
    if ( menuSelect == 1)
      
       {  System.out.println("**************************************************************************************************************" );
          System.out.println();
          System.out.println(" PLEASE SEE BELOW BRIEF DESCRIPTION OF ALL SEVER-LESS CHARACTERISTICS: ");
          System.out.println();
          System.out.println("**************************************************************************************************************" ); 
          
          ScCHR.setCost                    (" SERVER-LESS USAGE is metered and users pay only for the time and resources used when serverless functions are running. This ability to scale to zero instances is one of the key differentiators of a serverless platform. The resources that are metered, such as memory or CPU, and the pricing model, such as off-peak discounts, vary among providers. ");
          
          ScCHR.setPerformanceLimits        (" There are a variety of limits set on the runtime resource requirements of serverless code, including the number of concurrent requests, and the maximum memory and CPU resources available to a function invocation. Some limits may be increased when users’ need grow, such as the concurrent request threshold, while others are inherent to the platforms, such as the maximum memory size. ");

          ScCHR.setProgrammingLanguages     (" Serverless services support a wide variety of programming languages including Javascript, Java, Python, Go, C#, and Swift. Most platforms support more than one programming language. Some of the platforms also support extensibility mechanisms for code written in any language as long as it is packaged in a Docker image that supports a well-defined API. ");          
         
          ScCHR.setProgrammingModel         (" Currently, serverless platforms typically execute a single main function that takes a dictionary (such as a JSON object) as input and produces a dictionary as output. "); 
          
          ScCHR.setComposability            (" The platforms generally offer some way to invoke one serverless function from another, but some platforms provide higher level mechanisms for composing these functions and may make it easier to construct more complex serverless apps.");
         
          ScCHR.setDeployment               (" Platforms strive to make deployment as simple as possible. Typically, developers just need to provide a file with the function source code. Beyond that there are many options where code can be packaged as an archive with multiple files inside or as a Docker image with binary code. As well, facilities to version or group functions are useful but rare. ");        
           
          ScCHR.setSecurityAccounting       (" Serverless platforms are multi-tenant and must isolate the execution of functions between users and provide detailed accounting so users understand how much they need to pay. ");

          ScCHR.setMonitoringDebugging      (" Every platform supports basic debugging by using print statements that are recorded in the execution logs. Additional capabilities may be provided to help developers find bottlenecks, trace errors, and better understand the cicumstances of function execution. ");     

                      
     
      System.out.println               (" COST:                    = " + ScCHR.getCost());
      System.out.println();          
      System.out.println               (" PERFORMANCE AND LIMITS:  = " + ScCHR.getPerformanceLimits ());
      System.out.println();
      System.out.println               (" PROGRAMMING LANGUAGES    = " + ScCHR.getProgrammingLanguages ());
      System.out.println();
      System.out.println               (" PROGRAMMING MODEL:       = " + ScCHR.getProgrammingModel ());
      System.out.println();
      System.out.println               (" COMPOSABILITY:           = " + ScCHR.getComposability ());
      System.out.println();
      System.out.println               (" DEPLOYMENT:              = " + ScCHR.getDeployment ());
      System.out.println();
      System.out.println               (" SECURITY AND ACCOUNTING: = " + ScCHR.getSecurityAccounting());
      System.out.println();
      System.out.println               (" MONITORING AND DEBUGGING = " + ScCHR.getMonitoringDebugging ());
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SEVER-LESS CHARACTERISTIC CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 5");
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println      (" PLEASE SEE BELOW SERVER-LESS MULTIMEDIA PROCESSING USE-CASE: ");
         System.out.println();
  
         ScCHR.setCost           (" SERVER-LESS USAGE is metered and users pay only for the time and resources used when serverless functions are running. This ability to scale to zero instances is one of the key differentiators of a serverless platform. The resources that are metered, such as memory or CPU, and the pricing model, such as off-peak discounts, vary among providers. ");
  
      
     
       System.out.println               (" COST: = " + ScCHR.getCost ());
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT SEVER-LESS CHARACTERISTIC CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 5");
       System.out.println();
       System.out.println();
       System.out.println("****************************************************************************************************************" );   
          
       }
     
     else
     
     if ( menuSelect == 3 )
     
        {
        System.out.println();
        System.out.println();
        System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE DATA BASE CHANGES: ");
        System.out.println();  

        ScCHR.setPerformanceLimits     (" There are a variety of limits set on the runtime resource requirements of serverless code, including the number of concurrent requests, and the maximum memory and CPU resources available to a function invocation. Some limits may be increased when users’ need grow, such as the concurrent request threshold, while others are inherent to the platforms, such as the maximum memory size. ");


        
      System.out.println               (" PERFORMANCE AND LIMITS: = " + ScCHR.getPerformanceLimits ());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SEVER-LESS CHARACTERISTIC CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 5");
      System.out.println();
      System.out.println();
      System.out.println("****************************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE IoT SENSOR: ");
       System.out.println();
  
      ScCHR.setProgrammingLanguages     (" Serverless services support a wide variety of programming languages including Javascript, Java, Python, Go, C#, and Swift. Most platforms support more than one programming language. Some of the platforms also support extensibility mechanisms for code written in any language as long as it is packaged in a Docker image that supports a well-defined API. ");          
       
      System.out.println               (" PROGRAMMING LANGUAGES:= " + ScCHR.getProgrammingLanguages ());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SEVER-LESS CHARACTERISTIC CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 5");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
                  
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE: "); 
         System.out.println();
               
         ScCHR.setProgrammingModel        (" Currently, serverless platforms typically execute a single main function that takes a dictionary (such as a JSON object) as input and produces a dictionary as output. "); 
                
         System.out.println               (" PROGRAMMING MODEL: = " + ScCHR.getProgrammingModel());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SEVER-LESS CHARACTERISTIC CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 5");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
     
      }

    else
   
        if ( menuSelect == 6)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
          ScCHR.setComposability          (" The platforms generally offer some way to invoke one serverless function from another, but some platforms provide higher level mechanisms for composing these functions and may make it easier to construct more complex serverless apps.");
                 
         System.out.println               (" COMPOSABILITY: = " + ScCHR.getComposability ());         
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SEVER-LESS CHARACTERISTIC CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 5");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 7)
       
       {
         
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println();
         
         ScCHR.setDeployment              (" Platforms strive to make deployment as simple as possible. Typically, developers just need to provide a file with the function source code. Beyond that there are many options where code can be packaged as an archive with multiple files inside or as a Docker image with binary code. As well, facilities to version or group functions are useful but rare. ");        
                
         System.out.println               (" DEPLOYMENT: = " + ScCHR.getDeployment());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SEVER-LESS CHARACTERISTIC CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 5");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 8)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE: ");
          System.out.println();
          
         ScCHR.setSecurityAccounting     (" Serverless platforms are multi-tenant and must isolate the execution of functions between users and provide detailed accounting so users understand how much they need to pay. ");

             
         System.out.println               (" SECURITY AND ACCOUNTING: = " + ScCHR.getSecurityAccounting ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SEVER-LESS CHARACTERISTIC CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 5");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
     
     else
   
        if ( menuSelect == 9)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
        ScCHR.setMonitoringDebugging      (" Every platform supports basic debugging by using print statements that are recorded in the execution logs. Additional capabilities may be provided to help developers find bottlenecks, trace errors, and better understand the cicumstances of function execution. ");     


 
                 
         System.out.println               (" MONITORING AND DEBUGGING: = " + ScCHR.getMonitoringDebugging());

         
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SEVER-LESS CHARACTERISTIC CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 5");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }
      
      else
      
System.out.println();
System.out.println   (" HERE ARE SRVERLESS-COMPUTING MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS.");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER 5G CATEGORY MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");
       
  menuSelection = keyboard.nextInt();
 
 while (menuSelection < 1 || menuSelection > 8) 
  
{
  
System.out.println(" THIS IS INVALID CHOICE FOR SERVERLESS-COMPUTING MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println(" HERE ARE VALID SERVERLESS-COMPUTING MAIN MENU SELECTIONS CHOICE LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.print     ("PLEASE ENTER SERVER-LESS MAIN MENU CATEGORY CHOICE (1 - 8) FROM THE LIST ABOVE: "); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.print("PLEASE ENTER 5G MAIN MENU CATEGORY CHOICE (1 - 8) FROM THE LIST ABOVE: ");

    
  menuSelection = keyboard.nextInt();
  
  
 } 
       
break;

case 6:
 
ScfSetter ScCHL;

ScCHL = new ScfSetter();
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println("YOU SELECTED SERVER-LESS CHALLENGES FROM SERVER-LESS MAIN MENU ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW SERVER-LESS SYSTEM LEVEL & PROGRAMMING MODELS & DEVOPS CHALLENGES: ");
 System.out.println(); 
 System.out.println("1.   BRIEF DESCRIPTION OF ALL SYSTEM-LEVEL, PROGRAMMING-MODELS & DEVOPS CHALLANGES:.");
 System.out.println();
 System.out.println("2    COST.");
 System.out.println();
 System.out.println("3.   COLD START.");
 System.out.println();
 System.out.println("4.   RESOURCE LIMITS.");
 System.out.println();
 System.out.println("5.   SECURITY.");
 System.out.println();
 System.out.println("6.   SCALING.");
 System.out.println();
 System.out.println("7.   HYBRID CLOUD.");
 System.out.println();
 System.out.println("8.   LEGACY SYSTEMS.");
 System.out.println();
 System.out.println("9.   TOOLS.");
 System.out.println();
 System.out.println("10.  DEPLOYMENT.");
 System.out.println();
 System.out.println("11.  MONITORING & DEBUGGING.");
 System.out.println();
 System.out.println("12.  IDEs.");
 System.out.println();
 System.out.println("13.  COMPOSABILITY.");
 System.out.println();
 System.out.println("14.  LONG RUNNING.");
 System.out.println();
 System.out.println("15.  STATE.");
 System.out.println();
 System.out.println("16.  CONCURRENCY.");
 System.out.println();
 System.out.println("17.  RECOVERY SEMANTICS.");
 System.out.println();
 System.out.println("18.  CODE GRANULARITY.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE OF SERVER_LESS CHALLENGES FROM (1 to 18): ");
   
 
  menuSelect = keyboard.nextInt();

 while (menuSelect < 1 || menuSelect > 18)
  
{

 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println(" THIS IS INVALID CHOICE FOR SERVER_LESS CHALLENGE SELECTIONS "); 
 System.out.println();
 System.out.println(" PLEASE SEE BELOW VALID SERVER-LESS SYSTEM LEVEL & PROGRAMMING MODELS & DEVOPS CHALLENGES: ");
 System.out.println(); 
 System.out.println("1.   BRIEF DESCRIPTION OF ALL SYSTEM-LEVEL, PROGRAMMING-MODELS & DEVOPS CHALLANGES:.");
 System.out.println();
 System.out.println("2    COST.");
 System.out.println();
 System.out.println("3.   COLD START.");
 System.out.println();
 System.out.println("4.   RESOURCE LIMITS.");
 System.out.println();
 System.out.println("5.   SECURITY.");
 System.out.println();
 System.out.println("6.   SCALING.");
 System.out.println();
 System.out.println("7.   HYBRID CLOUD.");
 System.out.println();
 System.out.println("8.   LEGACY SYSTEMS.");
 System.out.println();
 System.out.println("9.   TOOLS.");
 System.out.println();
 System.out.println("10.  DEPLOYMENT.");
 System.out.println();
 System.out.println("11.  MONITORING & DEBUGGING.");
 System.out.println();
 System.out.println("12.  IDEs.");
 System.out.println();
 System.out.println("13.  COMPOSABILITY.");
 System.out.println();
 System.out.println("14.  LONG RUNNING.");
 System.out.println();
 System.out.println("15.  STATE.");
 System.out.println();
 System.out.println("16.  CONCURRENCY.");
 System.out.println();
 System.out.println("17.  RECOVERY SEMANTICS.");
 System.out.println();
 System.out.println("18.  CODE GRANULARITY."); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR SERVER-LESS CHALLENGES CHOICE FROM (1 to 18) : ");


 
  menuSelect = keyboard.nextInt();

 }
 
         if ( menuSelect == 1)
      
       {  System.out.println("**************************************************************************************************************" );
          System.out.println();
          System.out.println(" BRIEF DESCRIPTION OF ALL SYSTEM, PROGRAMMING-MODELS & DEVOPS LEVELS CHALLANGES: ");
          System.out.println();
          System.out.println("**************************************************************************************************************" ); 
          System.out.println();
          ScCHL.setCostch                   (" Cost is a fundamental challenge. This includes minimizing the resource usage of a serverless function, both when it is executing and when idle. Another aspect is the pricing model, including how it compares to other cloud computing approaches. For example, serverless functions are currently most economical for CPU-bound computations, whereas I/O bound functions may be cheaper on dedicated VMs or containers. ");
          
          ScCHL.setColdStart                (" A key differentiator of serverless is the ability to scale to zero, or not charging customers for idle time. Scaling to zero, however, leads to the problem of cold starts, and paying the penalty of getting serverless code ready to run. Techniques to minimize the cold start problem while still scaling to zero are critical. ");

          ScCHL.setResourceLimits           (" Resource limits are needed to ensure that the platform can handle load spikes, and manage attacks. Enforceable resource limits on a serverless function include memory, execution time, bandwidth, and CPU usage. In additional, there are aggregate resource limits that can be applied across a number of functions or across the entire platform.");          
         
          ScCHL.setSecurity                 (" Strong isolation of functions is critical since functions from many users are running on a shared platform."); 
         
          ScCHL.setScaling                  (" The platform must ensure the scalability and elasticity of users’ functions. This includes proactively provisioning resources in response to load, and in anticipation of future load. This is a more challenging problem in serverless because these predictions and provisioning decisions must be made with little or no application-level knowledge. For example, the system can use request queue lengths as an indication of the load, but is blind to the nature of these requests. ");        
           
          ScCHL.setHybridCloud              (" As serverless is gaining popularity there may be more than one serverless platform and multiple serverless services that need to work together. It is unlikely one platform will have all functionality and work for all use cases. ");       
       
          ScCHL.setLegacySystems            (" It should be easy to access older cloud and non-cloud systems from serverless code running in serverless platforms. ");
          
          ScCHL.setTools                    (" Traditional tools that assumed access to servers to be able to monitor and debug applications aren’t applicable in serverless architectures, and new approaches are needed. ");
          
          ScCHL.setDeploymentch             (" Developers should be able to use declarative approaches to control what is deployed and tools to support it.  ");
          
          ScCHL.setMonitoringDebuggingch    (" As developers no longer have servers that they can access, serverless services and tools need to focus on developer productivity. As serverless functions are running for shorter amounts of time there will be many orders of magnitude more of them running making it harder to identify problems and bottlenecks. When the functions finish the only trace of their execution is what serverless platforms monitoring recorded. ");
          
          ScCHL.setIdes                     (" Higher level developer capabilities, such as refactoring functions (e.g.,splitting and merging functions), reverting to an older version, etc. will be needed and should be fully integrated with serverless platforms."); 
         
          ScCHL.setComposabilitych          (" This includes being able to call one function from another, creating functions that call and coordinate a number of other functions, and higher level constructs such as parallel executions and graphs. Tools will be needed to facilitate creation of compositions and their maintenance.");        
           
          ScCHL.setLongRunning              (" Currently serverless functions are often limited in their execution time. There are scenarios that require long running (if intermittent) logic. Programming models and tools may decompose long running tasks into smaller units and provide necessary context to track them as one long running unit of work.  ");

          ScCHL.setState                    (" Real applications often require state, and it’s not clear how to manage state in stateless serverless functions - programing models, tools, libraries etc. will need to provide necessary levels of abstraction.");
          
          ScCHL.setConcurrency              ("  Express concurrency semantics, such as atomicity (function executions need to be serialized), etc.");
          
          ScCHL.setRecoverySemantics        ("  Includes exactly once, at most once, and at least once semantics.  ");
          
          ScCHL.setCodeGranularity          ("  Currently, serverless platforms encapsulate code at the granularity of functions. It’s an open question whether coarser or finer grained modules would be useful. ");        

                     
     
      System.out.println               (" COST:                    = " + ScCHL.getCostch());
      System.out.println();          
      System.out.println               (" COLD START:              = " + ScCHL.getColdStart ());
      System.out.println();
      System.out.println               (" RESOURCE LIMITS:          = " + ScCHL.getResourceLimits ());
      System.out.println();
      System.out.println               (" SECURITY:                 = " + ScCHL.getSecurity ());
      System.out.println();
      System.out.println               (" SCALING:                  = " + ScCHL.getScaling ());
      System.out.println();
      System.out.println               (" HYBRID CLOUD:             = " + ScCHL.getHybridCloud());
      System.out.println();
      System.out.println               (" LEGACY SYSTEMS:           = " + ScCHL.getLegacySystems ());
      System.out.println();
      System.out.println               (" Tools:                    = " + ScCHL.getTools ());
      System.out.println();
      System.out.println               (" DEPLOYMENT:               = " + ScCHL.getDeploymentch ());
      System.out.println();
      System.out.println               (" MONITORING AND DEBUGGING: = " + ScCHL.getMonitoringDebuggingch());
      System.out.println();
      System.out.println               (" IDE'S:                    = " + ScCHL.getIdes());
      System.out.println();          
      System.out.println               (" COMPOSABILITY:            = " + ScCHL.getComposabilitych());
      System.out.println();
      System.out.println               (" LONG RUNNING:             = " + ScCHL.getLongRunning ());
      System.out.println();
      System.out.println               (" STATE:                    = " + ScCHL.getState ());
      System.out.println();
      System.out.println               (" CONCURRENCY:              = " + ScCHL.getConcurrency ());
      System.out.println();
      System.out.println               (" RECOVERY SEMANTICS:       = " + ScCHL.getRecoverySemantics());
      System.out.println();
      System.out.println               (" CODE GRANULARITY:         = " + ScCHL.getCodeGranularity ());
      System.out.println();       
      System.out.println("******************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      System.out.println();
      }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW SERVER-LESS MULTIMEDIA PROCESSING USE-CASE: ");
         System.out.println();
  
         ScCHL.setCostch                (" Cost is a fundamental challenge. This includes minimizing the resource usage of a serverless function, both when it is executing and when idle. Another aspect is the pricing model, including how it compares to other cloud computing approaches. For example, serverless functions are currently most economical for CPU-bound computations, whereas I/O bound functions may be cheaper on dedicated VMs or containers. ");
   
      
     
       System.out.println               (" COST: = " + ScCHL.getCostch ());
       
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
       System.out.println();
       System.out.println();
       System.out.println("****************************************************************************************************************" );   
       System.out.println();   
       }
     
     else
     
     if ( menuSelect == 3 )
     
        {
      System.out.println();
      System.out.println();
      System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE DATA BASE CHANGES: ");
      System.out.println();  

      ScCHL.setColdStart                (" A key differentiator of serverless is the ability to scale to zero, or not charging customers for idle time. Scaling to zero, however, leads to the problem of cold starts, and paying the penalty of getting serverless code ready to run. Techniques to minimize the cold start problem while still scaling to zero are critical. ");


        
      System.out.println               (" COLD START: = " + ScCHL.getColdStart());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();     
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE IoT SENSOR: ");
       System.out.println();
  
      ScCHL.setResourceLimits           (" Resource limits are needed to ensure that the platform can handle load spikes, and manage attacks. Enforceable resource limits on a serverless function include memory, execution time, bandwidth, and CPU usage. In additional, there are aggregate resource limits that can be applied across a number of functions or across the entire platform.");          
       
      System.out.println                (" RESOURCE LIMITS:= " + ScCHL.getResourceLimits ());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );
      System.out.println();
      }

  else
   
      if ( menuSelect == 5)
      
       {
                  
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE: "); 
         System.out.println();
               
         ScCHL.setSecurity                 (" Strong isolation of functions is critical since functions from many users are running on a shared platform."); 
               
         System.out.println                (" SECURITY: = " + ScCHL.getSecurity());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
      }

    else
   
        if ( menuSelect == 6)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
          ScCHL.setScaling                  (" The platform must ensure the scalability and elasticity of users’ functions. This includes proactively provisioning resources in response to load, and in anticipation of future load. This is a more challenging problem in serverless because these predictions and provisioning decisions must be made with little or no application-level knowledge. For example, the system can use request queue lengths as an indication of the load, but is blind to the nature of these requests. ");        
  
                 
         System.out.println                 (" SCALING: = " + ScCHL.getScaling ());        
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 7)
       
       {
         
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println();
         
         ScCHL.setHybridCloud             (" As serverless is gaining popularity there may be more than one serverless platform and multiple serverless services that need to work together. It is unlikely one platform will have all functionality and work for all use cases. ");       
                  
         System.out.println               (" HYBRID CLOUD: = " + ScCHL.getHybridCloud());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 8)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE: ");
          System.out.println();
          
         ScCHL.setLegacySystems           (" It should be easy to access older cloud and non-cloud systems from serverless code running in serverless platforms. ");
                    
         System.out.println               (" LEGACY SYSTEMS: = " + ScCHL.getLegacySystems ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
     else
          
    if ( menuSelect == 9)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE: ");
          System.out.println();
          
          ScCHL.setTools                  (" Traditional tools that assumed access to servers to be able to monitor and debug applications aren’t applicable in serverless architectures, and new approaches are needed. ");

                   
         System.out.println               (" TOOLS: = " + ScCHL.getTools ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
       }
       
     else
   
        if ( menuSelect == 10)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
         ScCHL.setDeploymentch              (" Developers should be able to use declarative approaches to control what is deployed and tools to support it.  ");
 
 
                 
         System.out.println                 (" DEPLOYMENTR: = " + ScCHL.getDeploymentch ());

         System.out.println();

         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();         
         System.out.println("****************************************************************************************************************" );        

      }
      
       else
   
        if ( menuSelect == 11)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
         ScCHL.setMonitoringDebuggingch      (" As developers no longer have servers that they can access, serverless services and tools need to focus on developer productivity. As serverless functions are running for shorter amounts of time there will be many orders of magnitude more of them running making it harder to identify problems and bottlenecks. When the functions finish the only trace of their execution is what serverless platforms monitoring recorded. ");

 
                 
         System.out.println                  (" MONITORING AND DEBUGGING: = " + ScCHL.getMonitoringDebuggingch ());

         System.out.println();

         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }
      
    else
   
        if ( menuSelect == 12)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
         ScCHL.setIdes                    (" Higher level developer capabilities, such as refactoring functions (e.g.,splitting and merging functions), reverting to an older version, etc. will be needed and should be fully integrated with serverless platforms."); 
 
 
                 
         System.out.println               (" IDE'S: = " + ScCHL.getIdes());

         System.out.println();

         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }
 else
   
        if ( menuSelect == 13)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
         ScCHL.setComposabilitych            (" This includes being able to call one function from another, creating functions that call and coordinate a number of other functions, and higher level constructs such as parallel executions and graphs. Tools will be needed to facilitate creation of compositions and their maintenance.");        
 
 
                 
         System.out.println                (" COMPOSABILITY = " + ScCHL.getComposabilitych ());

         System.out.println();

         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }
      
      else
   
        if ( menuSelect == 14)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
         ScCHL.setLongRunning              (" Currently serverless functions are often limited in their execution time. There are scenarios that require long running (if intermittent) logic. Programming models and tools may decompose long running tasks into smaller units and provide necessary context to track them as one long running unit of work.  ");


 
                 
         System.out.println               (" LONG RUNNING: = " + ScCHL.getLongRunning());

         System.out.println();

         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }
      
    else
   
        if ( menuSelect == 15)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
         ScCHL.setState                    (" Real applications often require state, and it’s not clear how to manage state in stateless serverless functions - programing models, tools, libraries etc. will need to provide necessary levels of abstraction.");

 
                 
         System.out.println                (" STATE = " + ScCHL.getState ());

         System.out.println();

         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }
      
 else
   
        if ( menuSelect == 16)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
         ScCHL.setConcurrency              ("  Express concurrency semantics, such as atomicity (function executions need to be serialized), etc.");
 
 
                 
         System.out.println                (" CONCURRENCY: = " + ScCHL.getConcurrency ());

         System.out.println();

         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

 else
   
        if ( menuSelect == 17)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
         ScCHL.setRecoverySemantics        ("  Includes exactly once, at most once, and at least once semantics.  ");

 
                 
         System.out.println               (" RECOVERY SEMANTICS = " + ScCHL.getRecoverySemantics ());
         System.out.println();

         
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }
 else
   
        if ( menuSelect == 18)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println(); 
          
         ScCHL.setCodeGranularity          ("  Currently, serverless platforms encapsulate code at the granularity of functions. It’s an open question whether coarser or finer grained modules would be useful. ");        

 
                 
         System.out.println                (" CODE GRANULArity: = " + ScCHL.getCodeGranularity ());

         System.out.println();

         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS CHALLENGES CHOICE PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }
 

            
  else
  
System.out.println();
System.out.println   (" HERE ARE SRVERLESS-COMPUTING MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS.");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER 5G CATEGORY MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");
       
       menuSelection = keyboard.nextInt();

 while (menuSelection < 1 || menuSelection >8) 
  
{
  
System.out.println(); 
System.out.println(" THIS IS INVALID CHOICE FOR SERVERLESS-COMPUTING MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println(" HERE ARE VALID SERVERLESS-COMPUTING MAIN MENU SELECTIONS CHOICE LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.print     ("PLEASE ENTER SERVER-LESS MAIN MENU CATEGORY CHOICE (1 - 8) FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();

  
 } 
 
break;

case 7:
 
ScfSetter ScEC;

ScEC = new ScfSetter();
 
 System.out.println();
 
 System.out.println("************************************************************************************************" );
 System.out.println("YOU SELECTED EVALUATION CRITERIA OF SERVER-LESS COMPUTING FRAMEWORK");
 System.out.println();
 System.out.println("PLEASE SEE BELOW SERVER-LESS EVALUATION CRITERIA. ");
 System.out.println();
 System.out.println("1.  OPEN SOURCE LICENSE.");
 System.out.println();
 System.out.println("2.  STRONG DEVELOPER COMMUNITY.");
 System.out.println();
 System.out.println("3.  PROGRAMMING LANGUAGE SUPPORT.");
 System.out.println();
 System.out.println("4.  AUTO SCALING.");
 System.out.println();
 System.out.println("5.  SUPPORT FOR MULTIPLE ORCHESTRATORS.");
 System.out.println();
 System.out.println("6.  FUNCTION TRIGGERS.");
 System.out.println();
 System.out.println("7.  AVAILABILITY OF MONITORING TOOLS.");
 System.out.println();
 System.out.println("8.  CLI INTERFACE.");
 System.out.println();
 System.out.println("9.  EASE OF DEPLOYMENT.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR SERVER-LESS EVALUATION CRITERIA SELECTION FROM (1 to 9) : ");
   
 
  menuSelect = keyboard.nextInt();

 while (menuSelect < 1 || menuSelect >9)
  
{

 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println("THIS IS INVALID CHOICE FOR SERVER-LESS EVALUATION CRITERIA SELECTION. "); 
 System.out.println();
 System.out.println("PLEASE SEE BELOW VALID SERVER-LESS EVALUATION CRITERIA SELECTIONS: ");
 System.out.println();
 System.out.println("1.  OPEN SOURCE LICENSE.");
 System.out.println();
 System.out.println("2.  STRONG DEVELOPER COMMUNITY.");
 System.out.println();
 System.out.println("3.  PROGRAMMING LANGUAGE SUPPORT.");
 System.out.println();
 System.out.println("4.  AUTO SCALING.");
 System.out.println();
 System.out.println("5.  SUPPORT FOR MULTIPLE ORCHESTRATORS.");
 System.out.println();
 System.out.println("6.  FUNCTION TRIGGERS.");
 System.out.println();
 System.out.println("7.  AVAILABILITY OF MONITORING TOOLS.");
 System.out.println();
 System.out.println("8.  CLI INTERFACE.");
 System.out.println();
 System.out.println("9.  EASE OF DEPLOYMENT.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR SERVER-LESS EVALUATION CRITERIA SELECTION FROM (1 to 9) : ");

  menuSelect = keyboard.nextInt();

 }
         
      if ( menuSelect == 1)
    
        {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW SERVER-LESS EVALUATION CRITERIA AS OPEN SOURCE LICENSE: ");
         System.out.println();
  
         ScEC.setLicense (" The selected framework should be an open source implementation so that developers can customize features. Specifically, the license should allow to freely access, use, modify and distribute (both in modified and unmodified form) code to others.  ");
   
      
     
       System.out.println (" OPEN SOURCE LICENSE: = " + ScEC.getLicense ());
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS EVALUATION CRITERIA SELECTION PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 7");
       System.out.println();
       System.out.println();
       System.out.println("****************************************************************************************************************" );   
       System.out.println();   
       }
     
     else
     
     if ( menuSelect == 2 )
     
        {
      System.out.println();
      System.out.println();
      System.out.println(" PLEASE SEE BELOW SERVER-LESS EVALUATION CRITERIA AS STRONG DEVELOPER COMMUNITY: ");
      System.out.println();  

      ScEC.setDeveloperCommunity (" The selected framework should have a strong and thriving developer community. This is evaluated by analyzing the code commit frequency, pull requests/merge requests frequency, reputation, availability of support platforms (such as web-based forums, mailing lists, Slack channel) and commercial support. ");


        
      System.out.println         (" STRONG DEVELOPER COMMUNITY: = " + ScEC.getDeveloperCommunity());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS EVALUATION CRITERIA SELECTION PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 7");
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();     
   }
   
   else
   
      if ( menuSelect == 3)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE AS PROGRAMMING LANGUAGE SUPPORT: ");
       System.out.println();
  
      ScEC.setLanguageSupport (" The selected solution should have support for multiple languages. There should be out of the box support for popular languages, such as Go, Python and Node.js [30]. Additionally, it should be possible to add support for more languages. This would enable developers to also upgrade the version of a language if required.");          
       
      System.out.println     (" PROGRAMMING LANGUAGE SUPPORT:= " + ScEC.getLanguageSupport());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS EVALUATION CRITERIA SELECTION PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 7");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );
      System.out.println();
      }

  else
   
      if ( menuSelect == 4)
      
       {
                  
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS EVALUATION CRITERIA AS AUTO SCALING: "); 
         System.out.println();
               
         ScEC.setAutoScaling ("  Serverless functions are expected to serve infrequent and sporadic demands. Thus, the framework must support scaling in order to efficiently utilize the underlying hardware even with varying incoming traffic. We also consider whether the framework supports multiple or configurable scaling criteria, such as requests per second/- queries per second (QPS), CPU and message queue size. "); 
               
         System.out.println  (" AUTO SCALING: = " + ScEC.getAutoScaling());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS EVALUATION CRITERIA SELECTION PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 7");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
      }

    else
   
        if ( menuSelect == 5)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS EVALUATION CRITERIA AS SUPPORT FOR MULTIPLE ORCHESTRATORS:");
         System.out.println(); 
          
          ScEC.setOrchestrators (" Support for container orchestrators apart from Kubernetes (such as Docker Swarm, Nomad, etc.) provides more flexibility for both the development and operations team. ");        
  
                 
         System.out.println     (" SUPPORT FOR MULTIPLE ORCHESTRATORS: = " + ScEC.getOrchestrators());        
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS EVALUATION CRITERIA SELECTION PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 7");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 6)
       
       {
         
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS EVALUATION CRITERIA AS FUNCTION TRIGGERS:");
         System.out.println();
         
         ScEC.setFunctionTriggers (" The selected solution should support both HTTP (synchronous) and event-based (asynchronous triggers).");       
                  
         System.out.println       (" FUNCTION TRIGGERS: = " + ScEC.getFunctionTriggers());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS EVALUATION CRITERIA SELECTION PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 7");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 7)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW SERVER-LESS EVALUATION CRITERIA AS AVAILABILITY OF MONITORING TOOLS: ");
          System.out.println();
          
         ScEC.setMonitoringTools (" It is important that the framework has an integrated monitoring tool which can help the operations team to monitor the performance metrics of a deployed function, such as the number of invocations and execution time. ");
                    
         System.out.println      (" AVAILABILITY OF MONITORING TOOLS: = " + ScEC.getMonitoringTools());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS EVALUATION CRITERIA SELECTION PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 7");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
     else
          
    if ( menuSelect == 8)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW SERVER-LESS EVALUATION CRITERIA AS CLI INTERFACE: ");
          System.out.println();
          
          ScEC.setCliInterface ("  Availability of a command line interface will greatly ease the management of functions. This will also allow for better integration with third party tools for actions, such as event-driven triggers.");

                   
         System.out.println    (" CLI INTERFACE: = " + ScEC.getCliInterface());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS EVALUATION CRITERIA SELECTION PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 7");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
       }
       
     else
   
        if ( menuSelect == 9)
       
       {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW SERVER-LESS EVALUATION CRITERIA AS EASE OF DEPLOYMENT:");
         System.out.println(); 
          
         ScEC.setDeploymentEase (" It should be easy to deploy the selected framework with minimal configuration changes. The steps and complexity of deployment helps evaluate how quickly a new Kubernetes cluster with the framework can be set up. This can be evaluated by following the “Getting Started” guide of each framework. ");
 
 
                 
         System.out.println     (" EASE OF DEPLOYMENT: = " + ScEC.getDeploymentEase());

         System.out.println();

         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS EVALUATION CRITERIA SELECTION PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 7");
         System.out.println();         
         System.out.println("****************************************************************************************************************" );        

      }
      
               
   else 
             
System.out.println();
System.out.println   (" HERE ARE SRVERLESS-COMPUTING MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS.");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER 5G CATEGORY MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");  
     
       menuSelection = keyboard.nextInt();

 while (menuSelection < 1 || menuSelection > 8) 
  
{
System.out.println(); 
System.out.println(" THIS IS INVALID CHOICE FOR SERVERLESS-COMPUTING MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println(" HERE ARE VALID SERVERLESS-COMPUTING MAIN MENU SELECTIONS CHOICE LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.print     ("PLEASE ENTER SERVER-LESS MAIN MENU CATEGORY CHOICE (1 - 8) FROM THE LIST ABOVE: ");   

  
  menuSelection = keyboard.nextInt();
  
 } 
 
break;

case 8:
 
ScfSetter ScGPL;

ScGPL = new ScfSetter();
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED SERVER-LESS COMPUTING CATEGORY GAPS AND LIMITATIONS ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW SERVER-LESS COMPUTING GAPS AND LIMITATIONS: ");
 System.out.println(); 
 System.out.println("1.   STATE.");
 System.out.println();
 System.out.println("2.   LATENCY.");
 System.out.println();
 System.out.println("3.   LOCAL TESTING.");
 System.out.println(); 
 System.out.println("4.   LOSS OF CONTROL : CONFIGURATION.");
 System.out.println();
 System.out.println("5.   LOSS OF CONTROL : PERFORMANCE.");
 System.out.println();
 System.out.println("6.   LOSS OF CONTROL : ISSUE RESOLUTION.");
 System.out.println();
 System.out.println("7.   LOSS OF CONTROL : SECURITY. ");
 System.out.println();
 System.out.println("8.   COLD START. ");
 System.out.println();
 System.out.println("9.   TOOLING LIMITATION : DEPLOYMENT TOOLS.");
 System.out.println();
 System.out.println("10.  TOOLING LIMITATION : EXECUTION ENVIRONMENTS.");
 System.out.println();
 System.out.println("11.  TOOLING LIMITATION : MONITORING AND LOGGING.");
 System.out.println();
 System.out.println("12.  TOOLING LIMITATION : REMOTE TESTING. ");
 System.out.println();
 System.out.println("13.  TOOLING LIMITATION : DEBUGGING. ");
 System.out.println();
 System.out.println("14.  VENDOR LOCK-IN. ");
 System.out.println();
 System.out.println("15.  IMMATURITY OF SERVICES. ");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM SERVER-LESS COMPUTING CATEGORY GAPS AND LIMITATIONS (1 to 15): ");
   
 
  menuSelect = keyboard.nextInt();

 while (menuSelect < 1 || menuSelect > 15)
  
{
 System.out.println();
 System.out.println("************************************************************************************************" );  
 System.out.println("THIS IS INVALID CHOICE FOR SERVER-LESS COMPUTING CATEGORY GAPS AND LIMITATIONS SELECTIONS. "); 
 System.out.println();
 System.out.println("PLEASE SEE BELOW VALID SERVER-LESS COMPUTING CATEGORY GAPS AND LIMITATIONS SELECTIONS: "); 
 System.out.println();
 System.out.println("1.   STATE.");
 System.out.println();
 System.out.println("2.   LATENCY.");
 System.out.println();
 System.out.println("3.   LOCAL TESTING.");
 System.out.println(); 
 System.out.println("4.   LOSS OF CONTROL : CONFIGURATION.");
 System.out.println();
 System.out.println("5.   LOSS OF CONTROL : PERFORMANCE.");
 System.out.println();
 System.out.println("6.   LOSS OF CONTROL : ISSUE RESOLUTION.");
 System.out.println();
 System.out.println("7.   LOSS OF CONTROL : SECURITY. ");
 System.out.println();
 System.out.println("8.   COLD START. ");
 System.out.println();
 System.out.println("9.   TOOLING LIMITATION : DEPLOYMENT TOOLS.");
 System.out.println();
 System.out.println("10.  TOOLING LIMITATION : EXECUTION ENVIRONMENTS.");
 System.out.println();
 System.out.println("11.  TOOLING LIMITATION  MONITORING AND LOGGING.");
 System.out.println();
 System.out.println("12.  TOOLING LIMITATION : REMOTE TESTING. ");
 System.out.println();
 System.out.println("13.  TOOLING LIMITATION : DEBUGGING. ");
 System.out.println();
 System.out.println("14.  VENDOR LOCK-IN. ");
 System.out.println();
 System.out.println("15.  IMMATURITY OF SERVICES. ");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM SERVER-LESS COMPUTING GAPS AND LIMITATIONS (1 to 15): ");


 
  menuSelect = keyboard.nextInt();

 }
     if ( menuSelect == 1)
    
        {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW SERVER-LESS COMPUTING GAPS AND LIMITATION: ");
         System.out.println();
  
         ScGPL.setStateGpl (" Stateless components must, by definition, interact with other, stateful components to persist any information beyond their immediate lifespan. Interaction with other components inevitably introduces latency, as well as some complexity. Stateful Serverless components may have very different ways of managing information between vendors. For example, a BaaS product like Firebase, from Google, has different data expiry mechanisms and policies than a similar product like DynamoDB, from AWS. Also, while statelessness is the fundamental rule in many cases, oftentimes specific implementations, especially FaaS platforms, do preserve some state between function invocations. This is purely an optimization and cannot be relied upon as it depends heavily on the underlying implementation of the platform. Unfortunately, it can also confuse developers and muddy the operational picture of a system. One knock-on effect of this opportunistic state optimization is that of inconsistent performance.");
   
      
     
       System.out.println (" State : = " + ScGPL.getStateGpl ());
       System.out.println();
       System.out.println("******************************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS COMPUTING GAPS AND LIMITATION CATEGORY - PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 8. ");
       System.out.println();
       System.out.println();
       System.out.println("*******************************************************************************************************************************" );   
       System.out.println();   
       }
     
     else
     
     if ( menuSelect == 2 )
     
        {
      System.out.println();
      System.out.println();
      System.out.println     (" PLEASE SEE BELOW SERVER-LESS COMPUTING GAPS AND LIMITATION: ");
      System.out.println();  

      ScGPL.setLatencyGpl (" In a non-Serverless application, if latency between application components is a concern, those components can generally be reliably co-located (within the same rack, or on the same host instance), or can even be brought together in the same process. Also, communication channels between components can be optimized to reduce latency, using specialized network protocols and data formats. While Serverless platform providers are always improving the performance of their underlying infrastructure, the highly-distributed, loosely coupled nature of Serverless applications means that latency will always be a concern. For some classes of problems, a Serverless approach may not be viable based on this limitation alone. ");


        
      System.out.println         (" LATENCY : = " + ScGPL.getLatencyGpl());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS COMPUTING GAPS AND LIMITATION CATEGORY - PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 8. ");
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();     
   }
   
   else
   
      if ( menuSelect == 3)
      
       {
       System.out.println();
       System.out.println     (" PLEASE SEE BELOW SERVER-LESS SERVER-LESS COMPUTING GAPS AND LIMITATION: ");
       System.out.println();
  
      ScGPL.setLocalTesting (" The difficulty of local testing is one of the most jarring limitations of Serverless application architectures. In a non-Serverless world, developers often have local analogs of application components (like databases, or message queues) which can be integrated for testing in much the same way the application might be deployed in production. Serverless applications can, of course, rely on unit tests, but more realistic integration or end-to-end testing is significantly more difficult. The difficulties in local testing of Serverless applications can be classified in two ways. Firstly, because much of the infrastructure is abstracted away inside the platform, it can be difficult to connect the application components in a realistic way, incorporating production-like error handling, logging, performance, and scaling characteristics. Secondly, Serverless applications are inherently distributed, and consist of many separate pieces, so simply managing the myriad functions and BaaS components is challenging, even locally. Instead of trying to perform integration testing locally,it is recommended doing so remotely. This makes use of the Serverless platform directly, although that too has limitations, as we’ll describe in the next section.");          
       
      System.out.println    (" LOCAL TESTING := " + ScGPL.getLocalTesting());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS COMPUTING GAPS AND LIMITATION CATEGORY - PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 8. ");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );
      System.out.println();
      }

  else
   
      if ( menuSelect == 4)
      
       {
                  
         System.out.println();
         System.out.println        (" PLEASE SEE BELOW SERVER-LESS SERVER-LESS COMPUTING GAPS AND LIMITATION: "); 
         System.out.println();
               
         ScGPL.setConfigurationGpl ("  An obvious limitation of Serverless is a loss of absolute control over configuration. For example, in the AWS Lambda FaaS platform, there are a very limited number of configuration parameters available, and no control whatsoever over JVM or operating system runtime parameters.  "); 
               
         System.out.println  (" LOSS OF CONTROL : CONFIGURATION : = " + ScGPL.getConfigurationGpl());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS COMPUTING GAPS AND LIMITATION CATEGORY - PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
      }

    else
   
        if ( menuSelect == 5)
       
       {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW SERVER-LESS SERVER-LESS COMPUTING GAPS AND LIMITATION: ");
         System.out.println(); 
          
          ScGPL.setPerformanceGpl (" Coupled closely with loss of control over configuration is a similar loss of control over the performance of Serverless components. The performance issue can be further broken down into two major categories: performance of application code and performance of the underlying Serverless platform. Serverless platforms hide the details of program execution, in part due to the multiple layers of virtualization and abstraction that allow the platform operators to efficiently utilize their physical hardware. If you have access to the physical hardware, core operating system, and runtime, it is straightforward to optimize your application code for peak performance on that hardware and software foundation. If your code is running in a container, which is itself running on a virtual server (like an EC2 instance), it becomes much more difficult to predict or optimize how your code might perform.  ");        
  
                 
         System.out.println     (" LOSS OF CONTROL : PERFORMANCE : = " + ScGPL.getPerformanceGpl());        
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS COMPUTING GAPS AND LIMITATION CATEGORY - PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 6)
       
       {
         
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW SERVER-LESS SERVER-LESS COMPUTING GAPS AND LIMITATION: ");
         System.out.println();
         
         ScGPL.setIsueResolution (" Once that support ticket is opened, however, who has the capability to resolve it? Issue resolution is another area in which we cede control to a vendor. In a fully controlled system, if a hardware component has a fault, or the operating system requires a security patch, the owner of the system can take action to resolve issues. This extends into any infrastructure that the owner of the system also controls. In the case of noncritical issues, the system owner might choose to delay downtime or a maintenance window to a convenient time, perhaps when there is less load on the system or when a backup system might be available. In a Serverless world, the only issues we can resolve are those within our application code, or issues due to the configuration of Serverless components and services. All other classes of issues must be resolved by the platform owner—we may not even know when or if an issue has occurred. AWS is well known for a lack of visibility into most issues with their underlying platforms, even serious ones.");       
                  
         System.out.println       (" LOSS OF CONTROL : ISSUE RESOLUTION : = " + ScGPL.getIsueResolution());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS COMPUTING GAPS AND LIMITATION CATEGORY - PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 7)
       
       {
          System.out.println();
          System.out.println   (" PLEASE SEE BELOW SERVER-LESS SERVER-LESS COMPUTING GAPS AND LIMITATION: ");
          System.out.println();
          
         ScGPL.setSecurityGpl (" Platform security controls may not meet the security requirements of your application. For example, all AWS API Gateways can be reached from anywhere on the public internet; access is controlled solely via API keys rather than any transport-based access controls. However, many internal applications are locked down via network controls. If an application should only be accessible from certain IP addresses, then API Gateway cannot be used. ");
                    
         System.out.println   (" LOSS OF CONTROL : SECURITY : = " + ScGPL.getSecurityGpl());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS EVALUATION CRITERIA SELECTION PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 7");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
     else
          
    if ( menuSelect == 8)
       
       {
          System.out.println();
          System.out.println     (" PLEASE SEE BELOW SERVER-LESS SERVER-LESS COMPUTING GAPS AND LIMITATION: ");
          System.out.println();
          
          ScGPL.setColdStart ("   Serverless platforms can have inconsistent and poorly documented performance characteristics. One of the most common performance issues is referred to as a cold start. On the AWS Lambda platform, this refers to the instantiation of the container in which our code is run, as well as some initialization of our code. These slower cold starts occur when a Lambda function is invoked for the first time or after having its configuration altered, when a Lambda function scales out (to more instances running concurrently), or when the function simply hasn’t been invoked in a while. Once a container is instantiated, it can handle events without undergoing that same instantiation and initialization process. These “warm” invocations of the Lambda function are much faster. On the AWS Lambda platform, regularly used containers stay warm for hours, so in many applications cold starts are infrequent. For an AWS Lambda function processing at least one event per second, more than 99.99% of events should be processed by a warm container. The difference between the “cold” and “warm” performance of FaaS functions makes it difficult to consistently predict performance, but as platforms mature, These limitations will be minimized or addressed.");

                   
         System.out.println    (" IMPLEMENTATION LIMITATION : COLD START : = " + ScGPL.getColdStart());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS COMPUTING GAPS AND LIMITATION CATEGORY - PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
       }
       
     else
   
        if ( menuSelect == 9)
       
       {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW SERVER-LESS SERVER-LESS COMPUTING GAPS AND LIMITATION: ");
         System.out.println(); 
          
         ScGPL.setDeploymentTools (" Serverless deployment tools interact with the underlying platform, usually via an API. Since Serverless applications are composed of many individual components, deploying an entire application atomically is generally not feasible. Because of that fundamental architectural difference, it can be challenging to orchestrate deployments of large-scale Serverless applications. ");
 
 
                 
         System.out.println     (" TOOLING LIMITATIONS : DEPLOYMENT TOOLS : = " + ScGPL.getDeploymentTools());

         System.out.println();

         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS COMPUTING GAPS AND LIMITATION CATEGORY - PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 8. ");
         System.out.println();         
         System.out.println("****************************************************************************************************************" );        

      }
      
      else
     
     if ( menuSelect == 10 )
     
        {
      System.out.println();
      System.out.println();
      System.out.println     (" PLEASE SEE BELOW SERVER-LESS SERVER-LESS COMPUTING GAPS AND LIMITATION: ");
      System.out.println();  

      ScGPL.setExecutionEnvironments (" One of the most well publicized limitations of Serverless is the constrained execution environment of FaaS platforms. FaaS functions execute with limited CPU, memory, disk, and I/O resources, and unlike legacy server processes, cannot run indefinitely. For example, AWS Lambda functions can execute for a maximum of five minutes before being terminated by the platform, and are limited to a maximum of 1.5 GB of memory. As the FaaS platform’s underlying hardware gets more powerful, we can expect these resource limits to increase (as they already have in some cases). Further, designing a system to work comfortably within these limits often leads to a more scalable architecture. ");


        
      System.out.println         (" TOOLING LIMITATIONS : EXECUTION ENVIRONMENTS : = " + ScGPL.getExecutionEnvironments());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS COMPUTING GAPS AND LIMITATION CATEGORY - PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 8. ");
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();     
   }
   
   else
   
      if ( menuSelect == 11)
      
       {
       System.out.println();
       System.out.println     (" PLEASE SEE BELOW SERVER-LESS SERVER-LESS COMPUTING GAPS AND LIMITATION: ");
       System.out.println();
  
      ScGPL.setMonitoringLogging (" One of the benefits of Serverless is that you’re no longer responsible for many host- or process-level aspects of an application, and so monitoring metrics like disk space, CPU, and network I/O is not necessary (or, in fact, supported in many situations). However metrics more closely associated with actual business functionality still need to be monitored. The extent to which monitoring is well supported in a Serverless environment is currently a mixed bag. As an example, AWS Lambda has a number of ways monitoring can be performed, but some of them are poorly documented, or at least poorly understood by most users. AWS also gives a default logging platform in CloudWatch Logs. CloudWatch Logs is somewhat limited as a log analysis platform (for example, searching over a number of different sources); however, it is fairly easy to export logs from CloudWatch to another system. An area that is significantly lacking in support at present is distributed monitoring—that is the ability to understand what is happening for a business request as it is processed by a number of components. This kind of monitoring is under active development generally since it’s also a concern for users of Microservices architectures, however Serverless systems will be much more easily operated once this kind of functionality is common place.");          
       
      System.out.println     (" TOOLING LIMITATIONS : MONITORING AND LOGGING := " + ScGPL.getMonitoringLogging());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS COMPUTING GAPS AND LIMITATION CATEGORY - PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 8. ");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );
      System.out.println();
      }

  else
   
      if ( menuSelect == 12)
      
       {
                  
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW SERVER-LESS SERVER-LESS COMPUTING GAPS AND LIMITATION: "); 
         System.out.println();
               
         ScGPL.setRemoteTesting ("  In stark contrast to the inherent limitations of testing Serverless applications locally, the difficulty of remote testing is merely an implementation limitation. Some Serverless platform providers do make some remote testing possible, but typically only at the component level (for example, an individual function), not at the Serverless application level. It can be difficult to exhaustively test a complex Serverless application without setting up an entirely separate account with the platform provider, to ensure that testing does not impact production resources, and to ensure that account-wide platform limits are not exceeded by testing. "); 
               
         System.out.println  (" TOOLING LIMITATIONS : REMOTE TESTING : = " + ScGPL.getRemoteTesting());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS COMPUTING GAPS AND LIMITATION CATEGORY - PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
      }

    else
   
        if ( menuSelect == 13)
       
       {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW SERVER-LESS SERVER-LESS COMPUTING GAPS AND LIMITATION: ");
         System.out.println(); 
          
          ScGPL.setDebuggingTl (" Debugging Serverless applications is still quite difficult, although due to their often stateless nature, there is less to be gained in introspection and runtime debugging. However, for thorny problems, there is no replacement for a runtime debugger that allows introspection and line-by-line stepping. In addition to the limitations of debugging Serverless compute components, debugging Serverless applications as a whole is difficult, as it is with any distributed application.  ");        
  
                 
         System.out.println     (" TOOLING LIMITATIONS : DEBUGGING : = " + ScGPL.getDebuggingTl());        
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS COMPUTING GAPS AND LIMITATION CATEGORY - PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 14)
       
       {
         
         System.out.println();
         System.out.println    (" PLEASE SEE BELOW SERVER-LESS SERVER-LESS COMPUTING GAPS AND LIMITATION: ");
         System.out.println();
         
         ScGPL.setVendorLockin (" Vendor lock-in seems like an obviously inherent limitation of Serverless applications. However, different Serverless platform vendors enforce different levels of lock-in, through their choice of integration patterns, APIs, and documentation. Application developers can also limit their use of vendor-specific features, admittedly with varying degrees of success depending on the platform. ");       
                  
         System.out.println    (" VENDOR LOCK-IN := " + ScGPL.getVendorLockin());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS EVALUATION CRITERIA SELECTION PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 7");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 15)
       
       {
          System.out.println();
          System.out.println     (" PLEASE SEE BELOW SERVER-LESS SERVER-LESS COMPUTING GAPS AND LIMITATION: ");
          System.out.println();
          
         ScGPL.setImmaturityOfServices (" Some types of Serverless services, especially FaaS, work better with a good ecosystem around them. Some of these services are new and still need to have a few more revisions before they cover a lot of what we might want to throw at them. API Gateway, for example, has improved substantially in its first 18 months but still doesn’t support certain features we might expect from a universal web server (e.g., web sockets), and some features it does have are difficult to work with. ");
                    
         System.out.println      (" IMMATURITY OF SERVICES: = " + ScGPL.getImmaturityOfServices());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT SERVER-LESS EVALUATION CRITERIA SELECTION PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 7");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
     
      
      else
      
System.out.println();
System.out.println   (" HERE ARE SRVERLESS-COMPUTING MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS.");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER SERVER-LESS COMPUTING MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");
       
  menuSelection = keyboard.nextInt();
 
 while (menuSelection < 1 || menuSelection > 8) 
  
{
  
System.out.println(); 
System.out.println(" THIS IS INVALID CHOICE FOR SERVERLESS-COMPUTING MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println(" HERE ARE VALID SERVERLESS-COMPUTING MAIN MENU SELECTIONS CHOICE LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. FUNCTION-AS_SERVICE (FaaS). "); 
System.out.println();
System.out.println   ("2. SERVER-LESS APPLICATIONS PLATFORMS."); 
System.out.println();
System.out.println   ("3. AI & DEEP-LEARNING."); 
System.out.println();
System.out.println   ("4. SEVER-LESS USE CASES."); 
System.out.println();
System.out.println   ("5. SEVER-LESS CHARACTERISTICS."); 
System.out.println();
System.out.println   ("6. SERVER-LESS CHALLENGES."); 
System.out.println();
System.out.println   ("7. SERVER-LESS EVALUATION CRITERIA."); 
System.out.println();
System.out.println   ("8. SERVERLESS-GAPS-LIMITATIONS."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.print     ("PLEASE ENTER SERVER-LESS COMPUTING MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");

    
  menuSelection = keyboard.nextInt();
  
  
 }
 
break; 
 
    }
  }
}

//*************************************END OF IOT TAXONOMY & FRAMEWORK PROGRAM***********************************************