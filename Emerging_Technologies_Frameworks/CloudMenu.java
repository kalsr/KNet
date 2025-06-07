
// CLOUD SERVICE MODELS TAXONOMY & FRAMEWORK dispalys THE TAXONOMY OF INFRASTRUCTURE-AS-SERVICE, PLATFORM-AS-SERVICE & SOFTWARE-AS-SERVICE COMPONENTS OF CLOUD.
// Currently the test data values are USED FOR Each Taxonomy Field. 
// However when the actual values are obtained the Taxonomy fiields will be updated accordingly. 
// This code was written using Object-Oriented programming in Java JGRASP (OCTOBER-15, 2018)
// This code was written by Mr Randy Singh,Computer Scientist,Technology Innovation Team (DISA/BDE5)
// Contact Phone# (301)225-9535  

import java.util.Scanner; 

public class CloudMenu 

{
public static void main(String[] args) 
{
 
// Declare a variable to hold the 
// user's menu selection. 

int menuSelection;

final int MAX_VALUE = 1;
 
// Declare variables  

 String IaaS, PaaS, SaaS;
 
// Create a Scanner object for keyboard input. 

Scanner keyboard = new Scanner(System.in); 

// Display the LIST OF CLOUD Taxonomy Categories 

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("WELCOME TO CLOUD-COMPUTING FRAMEWORK APPLICATION.  ");
System.out.println();
System.out.println   ("BELOW IS THE ONLY AVAILABLE DoD CLOUD FRAMEWORK CATEGORY: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1.  CLOUD-SERVICE-MODELS."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR CHOICE AS #1 FROM ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 1) 
  
{
 
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("THIS IS INVALID CLOUD TAXONOMY SELECTION");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("BELOW IS THE ONLY AVAILABLE ONE DoD CLOUD TAXONOMY CATEGORY: ");
System.out.println();
System.out.println   ("1.  CLOUD-SERVICE-MODELS."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR CHOICE AS #1 FROM ABOVE: ");


  
 menuSelection = keyboard.nextInt();
  
 } 
 
 while (menuSelection > 0 || menuSelection <= 1)
 
  



 switch(menuSelection)
 
{ 

//*************************USSOCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************


 case 1:
 
 int menuSelect;
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED MAIN CATEGORY CLOUD-SERVICE-MODELS FOR DoD-CLOUD TAXONOMY  ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW CLOUD-SERVICE-MODELS SUBCATEGORIES");
 System.out.println();

CloudSetter IPS;

//Following statement creates an object using the CloudSetter Class as
// its Blueprint. 

IPS = new CloudSetter();

//*****************DISPLAY THE COCOMS IOT MENU***************
  
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("1.  SHOW ENTIRE CLOUD-SERVICE-MODELS SUBCATEGORIES OF DoD-CLOUD TAXONOMY.");
 System.out.println();
 System.out.println("2.  INFRASTRUCTURE-AS-SERVICE (IaaS) SUBCATEGORY.");
 System.out.println();
 System.out.println("3.  PLATFORM-AS-SERVICE       (PaaS) SUBCATEGORY.");
 System.out.println();
 System.out.println("4.  SOFTWARE-AS-SERVICE       (SaaS) SUBCATEGORY.");
 System.out.println();
  //System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CLOUD-SERVICE-MODELS SUBCATEGORY CHOICE FROM 1 to 4: ");
   
 
  menuSelect = keyboard.nextInt();

System.out.println("************************************************************************************************" );

 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 4)
  

  
{
  System.out.println("************************************************************************************************" );
  System.out.println();
 
  
 System.out.println("THIS IS INVALID SELECTION");
 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println();

 System.out.print(" ENTER YOUR CLOUD-SERVICE-MODELS SUBCATEGORY CHOICE FROM 1 to 4: "); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("1.  SHOW ENTIRE CLOUD-SERVICE-MODELS SUBCATEGORIES OF DoD-CLOUD TAXONOMY.");
 System.out.println();
 System.out.println("2.  INFRASTRUCTURE-AS-SERVICE (IaaS) SUBCATEGORY.");
 System.out.println();
 System.out.println("3.  PLATFORM-AS-SERVICE       (PaaS) SUBCATEGORY.");
 System.out.println();
 System.out.println("4.  SOFTWARE-AS-SERVICE       (SaaS) SUBCATEGORY.");
 System.out.println();
  //System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CLOUD-SERVICE-MODELS SUBCATEGORY CHOICE FROM 1 to 4: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE TAXONOMY FOR CLOUD-SERVICE-MODELS: ");
          System.out.println();
          
         IPS.setIaaS         ("Infrastructure-as-Service IS DEFINED AS hosted infrastructure components traditionally present in on-premise data centers,including servers, storage and virtualization layer");

         IPS.setPaaS         ("Platform-as-a-Service IS DEFINED AS resilient and optimized environment on which users can install applications and data sets");

         IPS.setSaaS         ("Software-as-a-Service IS DEFINED AS hosted applications made available over the internet");
          
                 
                   
                   
// Display the CLOUD SERVICE MODELS  Taxonomy values stored in the fields

     
      System.out.println               ("IPS INFRASTRUCTRE-AS-SERVICE                = " + IPS.getIaaS());
      System.out.println();          
      System.out.println               ("IPS PLATFORM-AS-SERVICE                     = " + IPS.getPaaS());
      System.out.println();
      System.out.println               ("IPS SOFTWARE-AS-SERVICE                     = " + IPS.getSaaS());
      System.out.println();
      
      System.out.println("************************************************************************************************" );
      System.out.println();
      
      System.out.println( "TO CONTINUE WITH NEXT CLOUD-SERVICE-MODELS TAXONOMY SUBCATEGORY PLEASE SELECT AGAIN CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println();
         System.out.println("PLEASE SEE BELOW SUBCATEGORY INFRASTRUCTURE-AS-SERVICE: ");
         System.out.println();
  
  // *****************Information Types***************

        IPS.setIaaS         ("Infrastructure-as-Service IS DEFINED AS hosted infrastructure components traditionally present in on-premise data centers,including servers, storage and virtualization layer"); 
             
//**************** Display the USSOCOM IOT INFORMATION TYPES****************

     
      System.out.println    ("INFRASTRUCTURE-AS-SERVICE = " + IPS.getIaaS());
      System.out.println();
      
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT CLOUD-SERVICE-MODELS TAXONOMY SUBCATEGORY PLEASE SELECT AGAIN CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW PLATFORM-AS-SERVICE SUBCATEGORY FOR CLOUD-SERVICE-MODELS: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         IPS.setPaaS         ("Platform-as-a-Service IS DEFINED AS resilient and optimized environment on which users can install applications and data sets");
 
        
         System.out.println   (" PLATFORM-AS-SERVICE = " + IPS.getPaaS());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUBCATEGORY OF CLOUD-SERVICE-MODELS SELECT AGAIN CLOUD TAXONOMY CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW SUBCATEGORY SOFTWARE-AS-SERVICE FOR CLOUD CSERVICE MODELS: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      IPS.setSaaS         ("Software-as-a-Service IS DEFINED AS hosted applications made available over the internet");
          


       

      System.out.println(" SOFTWARE-AS-SERVICE = " + IPS.getSaaS());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println("TO CONTINUE WITH NEXT SUBCATEGORY OF CLOUD-SERVICE-MODELS SELECT AGAIN TAXONOMY CHOICE # 1 ");
      System.out.println();
      System.out.println("************************************************************************************************" );

      

      }

  else
   
               
   
  
// ******************Display the Main menu************************************

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("BELOW IS THE ONLY ONE DoD CLOUD TAXONOMY CATEGORY: ");
System.out.println();
System.out.println   ("1.  CLOUD-SERVICE-MODELS."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR CHOICE AS #1 FROM ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 1) 
  
{
 
System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID CLOUD TAXONOMY SELECTION");
System.out.println();
System.out.println   ("BELOW IS THE ONLY ONE DoD CLOUD TAXONOMY CATEGORY: ");
System.out.println();
System.out.println   ("1.  CLOUD-SERVICE-MODELS."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR CHOICE AS #1 FROM ABOVE: ");

   

  
  menuSelection = keyboard.nextInt();


 
 } 

break;


//*************************USTRANSCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************

  
 
 
    }
  }
}

//*************************************END OF IOT TAXONOMY & FRAMEWORK PROGRAM***********************************************