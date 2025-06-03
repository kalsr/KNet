
// BIG DATA TAXONOMY & FRAMEWORK Code dispalys BIG DATA TAXONOMY For each of the BIG-DATA CATEGORY
// Currently the test data values are USED FOR Each Taxonomy Field. 
// However when the actual values are obtained the Taxonomy fiields will be updated accordingly. 
// This code was written using Object-Oriented programming in Java JGRASP (OCTOBER-16, 2018)
// The Cpde was written by Mr Randy Singh,Computer Scientist,Technology Innovation Team (DISA/BDE5)
// Contact Phone# (301)225-9535  

import java.util.Scanner; 

public class BigDataMenu 

{
public static void main(String[] args) 
{
 
// Declare a variable to hold the 
// user's menu selection. 

int menuSelection;

final int MAX_VALUE = 3;
 
// Declare variables to hold the units 
// of measurement.
 
 String EtlDataProcessing, DataCollection, DataHygiene, DataHygieneSoftware, DataWarehouse, DistributedProcessingSoftware, DataArchitectureModeling, BusinessAnalytics, IntelligenceExploitation, DataAnalytics, DataVisualizationSoftware;

 
// Create a Scanner object for keyboard input. 

Scanner keyboard = new Scanner(System.in); 

// Display the LIST OF BIG DATA Taxonomy Categories 

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("WELCOME TO BIG-DATA FRAMEWORK APPLICATION.  ");
System.out.println();
System.out.println   ("HERE ARE THE BIG DATA FRAMEWORK CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  DATA COLLECTION & PROCESSING CATEGORY (DCP). "); 
System.out.println();
System.out.println   ("2.  BIG DATA TECHNOLOGIES CATEGORY (BDT). "); 
System.out.println();
System.out.println   ("3.  ANALYTICS CATEGORY (AS)."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR BIG DATA TAXONOMY CATEGORY CHOICE 1 - 3FROM THE LIST ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 3) 
  
{
 
System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID BIG DATA TAXONOMY SELECTION");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE IS THE BIG DATA TAXONOMY CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  DATA COLLECTION & PROCESSING CATEGORY (DCP). "); 
System.out.println();
System.out.println   ("2.  BIG DATA TECHNOLOGIES CATEGORY (BDT)."); 
System.out.println();
System.out.println   ("3.  ANALYTICS CATEGORY (AS)."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR BIG DATA TAXONOMY CATEGORY CHOICE 1 - 3 FROM THE LIST ABOVE: ");


  
 menuSelection = keyboard.nextInt();
  
 } 
 
 while (menuSelection > 0 || menuSelection <= 3)
 
  



 switch(menuSelection)
 
{ 

//*************************USSOCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************


 case 1:
 
 int menuSelect;
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println("YOU SELECTED DATA COLLECTION & PROCESSING CATEGORY OF BIG DATA  ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW SUBCATEGORIES OF DATA COLLECTION & PROCESSING ");
 System.out.println();

BigDataSetter DCP;

//Following statement creates an object using the AiSetter Class as
// its Blueprint. 

DCP = new BigDataSetter();

//*****************DISPLAY THE COCOMS IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE LIST OF DATA COLLECTION & PROCESSING SUBCATEGORIES.");
 System.out.println();
 System.out.println("2.  DATA COLLECTION & PROCESSING - ETL & DATA PROCESSING SUBCATEGORY.");
 System.out.println();
 System.out.println("3.  DATA COLLECTION & PROCESSING - DATA COLLECTION SUBCATEGORY.");
 System.out.println();
 System.out.println("4.  DATA COLLECTION & PROCESSING - DATA HYGIENE SUBCATEGORY.");
 System.out.println();
 System.out.println("5.  DATA COLLECTION & PROCESSING - DATA HYGEINE SOFTWARE SUBCATEGORY.");
 System.out.println();
   //System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR DATA COLLECTION & PROCESSING (DoD - BIG DATA) SUBCATEGORY CHOICE FROM 1 to 5: ");
   
 
  menuSelect = keyboard.nextInt();

System.out.println("************************************************************************************************" );

 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 5)
  

  
{
  System.out.println("************************************************************************************************" );
  
  System.out.println("THIS IS INVALID SELECTION"); 
 
 System.out.print(" ENTER YOUR DATA COLLECTION & PROCESSING SUBCATEGORY CHOICE FROM 1 to 5: "); 
 System.out.println();
 
 System.out.println("1.  SHOW ENTIRE LIST OF DATA COLLECTION & PROCESSING SUBCATEGORIES.");
 System.out.println();
 System.out.println("2.  DATA COLLECTION & PROCESSING - ETL & DATA PROCESSING SUBCATEGORY.");
 System.out.println();
 System.out.println("3.  DATA COLLECTION & PROCESSING - DATA COLLECTION SUBCATEGORY.");
 System.out.println();
 System.out.println("4.  DATA COLLECTION & PROCESSING - DATA HYGIENE SUBCATEGORY.");
 System.out.println();
 System.out.println("5.  DATA COLLECTION & PROCESSING - DATA HYGEINE SOFTWARE SUBCATEGORY.");
 System.out.println();

 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 5: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          //System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE TAXONOMY FOR - DATA COLLECTION & PROCESSING CATEGORY: ");
          System.out.println();
          
          DCP.setEtlDataProcessing    ("EXTRACTION TRANSFORMATION & LOADING (ETL) & DATA PROCESSING HAVE THREE FUNCTIONS USED TO PULL DATA OUT OF STAGING DATABASES AND PLACE THEM INTO PRODUCTION DATABASES. ");

          DCP.setDataCollection       ("DATA COLLECTION IS THE PROCESS OF GATHERING INFORMATION IN A SYSTEMATIC FASHION.");

          DCP.setDataHygiene          ("DATA HYGEINE IS THE PROCESS TO ENSURE THAT DATA IS FREE FROM ERROR AND IS IN A USABLE FORMAT. ");
          
          DCP.setDataHygieneSoftware  ("DATA HYGEINE SOFTWARE DETECTS AND CORRECTS CORRUPT OR INACCURATE RECORDS. ");        
          
      

                   
// Display the Centcom IOT taxonomy values stored in the fields

     
      System.out.println               (" ETL-DATA-PROCESSING         = " + DCP.getEtlDataProcessing());
      System.out.println();          
      System.out.println               (" DATA-COLLECTION             = " + DCP.getDataCollection());
      System.out.println();
      System.out.println               (" DATA-HYGEINE                = " + DCP.getDataHygiene());
      System.out.println();
      System.out.println               (" DATA-HYGEINE-SOFTWARE       = " + DCP.getDataHygieneSoftware());
      System.out.println();
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      
      System.out.println( "TO CONTINUE WITH NEXT DATA COLLECTION & PROCESSING (DCP) SUBCATEGORY PLEASE SELECT AGAIN BIG DATA CATEGORY CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println();
         System.out.println("PLEASE SEE SUBCATEGORY ETL & DATA PROCESSING FOR(DCP): ");
         System.out.println();
  
  // *****************Information Types***************

       DCP.setEtlDataProcessing    ("EXTRACTION TRANSFORMATION & LOADING (ETL) & DATA PROCESSING HAVE THREE FUNCTIONS USED TO PULL DATA OUT OF STAGING DATABASES AND PLACE THEM INTO PRODUCTION DATABASES. ");

      
//**************** Display the USSOCOM IOT INFORMATION TYPES****************

     
      System.out.println    ("ETL & DATA PROCESSING = " + DCP.getEtlDataProcessing());
      System.out.println();
      
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT DATA COLLECTION & PROCESSING (DCP) SUBCATEGORY PLEASE SELECT AGAIN BIG DATA CHOICE # 1");

      System.out.println();
      System.out.println("************************************************************************************************" );      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW DATA-COLLECTION SUBCATEGORY OF DCP: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
        DCP.setDataCollection       ("DATA COLLECTION IS THE PROCESS OF GATHERING INFORMATION IN A SYSTEMATIC FASHION.");
 
        
         System.out.println   ("DATA COLLECTIONG = " + DCP.getDataCollection());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUBCATEGORY OF DCP SELECT AGAIN TAXONOMY CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW SUBCATEGORY DATA-HYGEINE FOR DCP: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      DCP.setDataHygiene          ("DATA HYGEINE IS THE PROCESS TO ENSURE THAT DATA IS FREE FROM ERROR AND IS IN A USABLE FORMAT. ");
          


       

      System.out.println("DATA HYGEINE = " + DCP.getDataHygiene());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println("TO CONTINUE WITH NEXT SUBCATEGORY OF DCP SELECT AGAIN BIG DATA TAXONOMY CATEGORY CHOICE # 1 ");
      System.out.println();
      System.out.println("************************************************************************************************" );

      

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW SUBCATEGORY DATA-HYGIENE-SOFTWARE FOR DCP:");
 
         System.out.println();
       
       

  // ****************Processor Types*******************
  
  
     DCP.setDataHygieneSoftware           ("DATA HYGEINE SOFTWARE DETECTS AND CORRECTS CORRUPT OR INACCURATE RECORDS. ");  
      

         System.out.println               (" DATA-HYGEINE-SOFTWARE       = " + DCP.getDataHygieneSoftware());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println( "TO CONTINUE WITH NEXT DCP SUBCATEGORY PLEASE SELECT AGAIN BIG DATA TAXONOMY CATEGORY CHOICE # 1");
         System.out.println();
         System.out.println("************************************************************************************************" );
     
      }

   
     else
          
   
  
// ******************Display the Main menu************************************

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE THE BIG DATA TAXONOMY CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  DATA COLLECTION & PROCESSING CATEGORY (DCP). "); 
System.out.println();
System.out.println   ("2.  BIG DATA TECHNOLOGIES CATEGORY (BDT). "); 
System.out.println();
System.out.println   ("3.  ANALYTICS CATEGORY (AS)."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR BIG DATA TAXONOMY CATEGORY CHOICE 1 - 3 FROM THE LIST ABOVE: ");
       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 3) 
  
{
 
 
System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID BIG DATA TAXONOMY SELECTION");
System.out.println();
System.out.println   ("HERE ARE THE BIG DATA TAXONOMY CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  DATA COLLECTION & PROCESSING CATEGORY (DCP). "); 
System.out.println();
System.out.println   ("2.  BIG DATA TECHNOLOGIES CATEGORY (BDT). "); 
System.out.println();
System.out.println   ("3.  ANALYTICS CATEGORY (AS)."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR BIG DATA TAXONOMY CATEGORY CHOICE 1 - 3 FROM THE LIST ABOVE: ");
       

   

  
  menuSelection = keyboard.nextInt();


 
 } 

break;


//*************************USTRANSCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************

case 2: 
 
 
 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED BIG-DATA-TECHNOLOGIES (BDT) CATEGORY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW BIG DATA TECHNOLOGIES (BDT) SUBCATEGORIES");
 System.out.println();

BigDataSetter BDT;

//  Following statement creates an object using the AiSetter class as
//its Blueprint. Centcom will reference the object.

BDT = new BigDataSetter();

  

 System.out.println("1.  SHOW ENTIRE LIST OF BIG DATA TECHNOLOGIES (BDT) SUBCATEGORIES.");
 System.out.println();
 System.out.println("2.  BIG DATA TECHNOLOGIES (BDT) - DATA WAREHOUSE.");
 System.out.println();
 System.out.println("3.  BIG DATA TECHNOLOGIES (BDT) - DISTRIBUTED PROCESSIN SOFTWARE.");
 System.out.println();
 System.out.println("4.  BIG DATA TECHNOLOGIES (BDT) - DATA ARCHITECTURE & MODELING.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 4: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 4)
  

  
{
   System.out.println("************************************************************************************************" );
  
 System.out.println("THIS IS INVALID SELECTION"); 
 System.out.println();
 System.out.println("1.  SHOW ENTIRE LIST OF BIG DATA TECHNOLOGIES (BDT) SUBCATEGORIES.");
 System.out.println();
 System.out.println("2.  BIG DATA TECHNOLOGIES (BDT) - DATA WAREHOUSE.");
 System.out.println();
 System.out.println("3.  BIG DATA TECHNOLOGIES (BDT) - DISTRIBUTED PROCESSIN SOFTWARE.");
 System.out.println();
 System.out.println("4.  BIG DATA TECHNOLOGIES (BDT) - DATA ARCHITECTURE & MODELING.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 4: ");


 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW ENTIRE LIST OF BIG-DATA-TECHNOLOGIES (BDT) SUBCATEGORIES: ");
          System.out.println();
          
          BDT.setDataWarehouse                   ("DATA WAREHOUSE IS A REPOSITORY OF INTEGRATED DATA FROM ONE OR MORE DISEPARATE SOURCES, WHICH ARE ROUTINELY MANIPULATED & PROCESSED. ");

          BDT.setDistributedProcessingSoftware   ("DISTRIBUTED PROCESSING SOFTWARE IS SOFTWARE USED TO MANAGE SHARED RESOURCES IN DATA PROCESSING, STANDARDIZATIONAND NORMALIZATION. ");

          BDT.setDataArchitectureModeling        ("DATA ARCHITECTURE & MODELLING IS COLLECTION OF POLICIES, MODELS, RULES AND STANDARDS THAT GOVERN WHICH DATA IS COLLECTED AND HOW IT IS STORED, ARRANGED, INTEGRATED AND PUT INTO DATA ARCHITECTURE AND SYSTEMS. ");

          

         
// Display the AC taxonomy values stored in the fields

     
      System.out.println               ("DATA WAREHOUSE                    = " + BDT.getDataWarehouse());
      System.out.println();
      System.out.println               ("DISTRIBUTED PROCESSIN SOFTWARE    = " + BDT.getDistributedProcessingSoftware());
      System.out.println();
      System.out.println               ("DATA ARCHITECTURE & MODELING      = " + BDT.getDataArchitectureModeling());
      System.out.println();
           
      System.out.println();
     
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT BDT SUBCATEGORY PLEASE SELECT AGAIN BDT CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE DATA WAREHOUSE SUBCATEGORY FOR BDT : ");
         System.out.println();
  
  // *****************Information Types***************

         BDT.setDataWarehouse           ("DATA WAREHOUSE IS A REPOSITORY OF INTEGRATED DATA FROM ONE OR MORE DISEPARATE SOURCES, WHICH ARE ROUTINELY MANIPULATED & PROCESSED. ");


      
//**************** Display the USTRANSCOM IOT INFORMATION TYPES****************

     
      System.out.println               ("DATA WAREHOUSE                    = " + BDT.getDataWarehouse());

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT BDT SUBCATEGORY PLEASE SELECT AGAIN BDT CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW SUBCATEGORY DISTRIBUTED PROCESSING SOFTWARE  FOR BDT: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
          BDT.setDistributedProcessingSoftware   ("DISTRIBUTED PROCESSING SOFTWARE IS SOFTWARE USED TO MANAGE SHARED RESOURCES IN DATA PROCESSING, STANDARDIZATIONAND NORMALIZATION. ");
 
        
         System.out.println               ("DISTRIBUTED PROCESSIN SOFTWARE    = " + BDT.getDistributedProcessingSoftware());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT BDT TAXONOMY SUBCATEGORY PLEASE SELECT AGAIN BDT CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW SUBCATEGORY DATA ARCHITECTURE & MODELING  FOR BDT: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      BDT.setDataArchitectureModeling        ("DATA ARCHITECTURE & MODELLING IS COLLECTION OF POLICIES, MODELS, RULES AND STANDARDS THAT GOVERN WHICH DATA IS COLLECTED AND HOW IT IS STORED, ARRANGED, INTEGRATED AND PUT INTO DATA ARCHITECTURE AND SYSTEMS. ");

       

      System.out.println("DATA ARCHITECTURE & MODELLING = " + BDT.getDataArchitectureModeling());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT BDT TAXONOMY SUBCATEGORY PLEASE SELECT AGAIN BDT CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

  else
   
                  
   
  
  

// ******************Display the Main menu************************************

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE THE BIG DATA TAXONOMY CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  DATA COLLECTION & PROCESSING CATEGORY (DCP). "); 
System.out.println();
System.out.println   ("2.  BIG DATA TECHNOLOGIES CATEGORY (BDT). "); 
System.out.println();
System.out.println   ("3.  ANALYTICS CATEGORY (AS)."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR BIG DATA TAXONOMY CATEGORY CHOICE 1 - 3 FROM THE LIST ABOVE: ");
       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 3) 
  
{
 
 
System.out.println();
System.out.println("THIS IS INVALID CHOICE# "); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE THE BIG DATA TAXONOMY CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  DATA COLLECTION & PROCESSING CATEGORY (DCP). "); 
System.out.println();
System.out.println   ("2.  BIG DATA TECHNOLOGIES CATEGORY (BDT). "); 
System.out.println();
System.out.println   ("3.  ANALYTICS CATEGORY (AS)."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR BIG DATA TAXONOMY CATEGORY CHOICE 1 - 3 FROM THE LIST ABOVE: ");

  
  menuSelection = keyboard.nextInt();

  
 } 


break; 

//*************************USSTRATCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************

case 3:

 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED ANALYTICS (AS)CATEGORY OF BIG DATA TAXONOMY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW BIG DATA ANALYTICS (AS) SUBCATEGORIES");
 System.out.println();

BigDataSetter AS;

//  Following statement creates an object using the AiSetter class as
//its Blueprint. Centcom will reference the object.

AS = new BigDataSetter();

  

 System.out.println("1.  SHOW ENTIRE LIST OF ANALYTICS (AS) SUBCATEGORIES).");
 System.out.println();
 System.out.println("2.  BIG DATA -ANALYTICS (AS) - BUSINESS ANALYTICS SUBCATEGORY.");
 System.out.println();
 System.out.println("3.  BIG DATA -ANALYTICS (AS) - INTELLIGENCE EXPLOITATION SUBCATEGORY.");
 System.out.println();
 System.out.println("4.  BIG DATA -ANALYTICS (AS) - DATA ANALYTICS SUBCATEGORY.");
 System.out.println();
 System.out.println("5.  BIG DATA -ANALYTICS (AS) - DATA VIRTULIZATION SOFTWARE SUBCATEGORY.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR ANALYTICS (AS) SUBCATEGORY CHOICE FROM 1 to 5: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect >5)
  

  
{
  System.out.println("************************************************************************************************" );
  
 System.out.println    ("THIS IS INVALID SELECTION"); 
 System.out.println();
 System.out.println    ("ENTER YOUR ANALYTICS (AS) SUBCATEGORY SELECTION FROM 1 to 5: ");
 System.out.println();
 System.out.println("1.  SHOW ENTIRE LIST OF ANALYTICS (AS) SUBCATEGORIES).");
 System.out.println();
 System.out.println("2.  BIG DATA -ANALYTICS (AS) - BUSINESS ANALYTICS SUBCATEGORY.");
 System.out.println();
 System.out.println("3.  BIG DATA -ANALYTICS (AS) - INTELLIGENCE EXPLOITATION SUBCATEGORY.");
 System.out.println();
 System.out.println("4.  BIG DATA -ANALYTICS (AS) - DATA ANALYTICS SUBCATEGORY.");
 System.out.println();
 System.out.println("5.  BIG DATA -ANALYTICS (AS) - DATA VIRTULIZATION SOFTWARE SUBCATEGORY.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR ANALYTICS (AS) SUBCATEGORY CHOICE FROM 1 to 5: ");
   


 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE TAXONOMY FOR AI-SYSTEMS : ");
          System.out.println();
          
          AS.setBusinessAnalytics               ("BUSINESS ANALYTICS  ARE DATA SKILLS, technologies and practices used to gain insight.");

          AS.setIntelligenceExploitation        ("INTELIGENCE EXPLOITATION HAS DATA METHODS such as translating, evaluating and transforming raw intelligence data and information into useful forms .");

          AS.setDataAnalytics                   ("DATA ANALYTICS IS THE PROCESS OF EXAMINING lARGE DATA SETS IN ORDER TO DRAW CONCLUSIONS, increasingly with the aid of specialized systems and software. ");
         
          AS.setDataVisualizationSoftware       ("DATA VISUALIZATION SOFTWARE IS THE SOFTWARE that abstracts data in schematic form and organizes for visual representation. ");


          

         
// Display the AC taxonomy values stored in the fields

     
      System.out.println               ("BIG DATA -ANALYTICS (AS) - BUSINESS ANALYTICS SUBCATEGORY                 = " + AS.getBusinessAnalytics());
      System.out.println();
      System.out.println               (" BIG DATA -ANALYTICS (AS) - INTELLIGENCE EXPLOITATION SUBCATEGORY         = " + AS.getIntelligenceExploitation());
      System.out.println();
      System.out.println               ("BIG DATA -ANALYTICS (AS) - DATA ANALYTICS SUBCATEGORY                     = " + AS.getDataAnalytics());
      
      System.out.println               ("BIG DATA -ANALYTICS (AS) - DATA VIRTULIZATION SOFTWARE SUBCATEGORY        = " + AS.getDataVisualizationSoftware());
      System.out.println();
           
      System.out.println();
     
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT AS  SUBCATEGORY PLEASE SELECT AGAIN ANALYTICS (AS) TAXONOMY CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BUSINESS ANALYTICS SUBCATEGORY FOR ANALYTICS (AS): ");
         System.out.println();
  
  // *****************Information Types***************

         AS.setBusinessAnalytics                ("BUSINESS ANALYTICS  ARE DATA SKILLS, technologies and practices used to gain insight.");

      
//**************** Display the USTRANSCOM IOT INFORMATION TYPES****************

     
      System.out.println    (" AS - BUSINESS ANALYTICS = " + AS.getBusinessAnalytics());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ANALYTICS (AS) TAXONOMY SUBCATEGORY PLEASE SELECT AGAIN ANALYTICS CHOICE # 3 ");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW INTELLIGENCE-EXPLOITATION SUBCATEGORY FOR ANALYTICS (AS): ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         AS.setIntelligenceExploitation        ("INTELIGENCE EXPLOITATION HAS DATA METHODS such as translating, evaluating and transforming raw intelligence data and information into useful forms .");
        
         System.out.println                    ("ANALYTICS -  INTELIGENCE EXPLOITATION = " + AS.getIntelligenceExploitation());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ANALYTICS (AS) SUBCATEGORY PLEASE SELECT AGAIN ANALYTICS CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW SUBCATEGORY DATA-ANALYTICS FOR ANALYTICS (AS): ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      AS.setDataAnalytics                   ("DATA-ANALYTICS IS THE PROCESS OF EXAMINING lARGE DATA SETS IN ORDER TO DRAW CONCLUSIONS, increasingly with the aid of specialized systems and software. ");

       

      System.out.println("AS DATA-ANALYTICS = " + AS.getDataAnalytics());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ANALYTICS (AS) SUBCATEGORY PLEASE SELECT AGAIN ANALYTICS CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

  else
   
     if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW SUBCATEGORY DATA-VIRTUALIZATION-SOFTWARE FOR ANALYTICS (AS): ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      AS.setDataVisualizationSoftware      ("DATA VISUALIZATION SOFTWARE IS THE SOFTWARE that abstracts data in schematic form and organizes for visual representation. ");

       

      System.out.println("AS DATA-VIRTUALIZATION-SOFTWARE = " + AS.getDataVisualizationSoftware());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT ANALYTICS (AS) SUBCATEGORY PLEASE SELECT AGAIN ANALYTICS CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
              
  else
  
  

// ******************Display the Main menu************************************

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE THE BIG DATA TAXONOMY CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  DATA COLLECTION & PROCESSING CATEGORY (DCP). "); 
System.out.println();
System.out.println   ("2.  BIG DATA TECHNOLOGIES CATEGORY (BDT). "); 
System.out.println();
System.out.println   ("3.  ANALYTICS CATEGORY (AS)."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR BIG DATA TAXONOMY CATEGORY CHOICE 1 - 3 FROM THE LIST ABOVE: ");

       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 3) 
  
{
 
 
System.out.println();
System.out.println("THIS IS INVALID CHOICE# "); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("HERE ARE THE BIG DATA TAXONOMY CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  DATA COLLECTION & PROCESSING CATEGORY (DCP). "); 
System.out.println();
System.out.println   ("2.  BIG DATA TECHNOLOGIES CATEGORY (BDT). "); 
System.out.println();
System.out.println   ("3.  ANALYTICS CATEGORY (AS)."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR BIG DATA TAXONOMY CATEGORY CHOICE 1 - 3 FROM THE LIST ABOVE: ");

  
  menuSelection = keyboard.nextInt();

  
 } 


break;

 
    }
  }
}

//*************************************END OF IOT TAXONOMY & FRAMEWORK PROGRAM***********************************************