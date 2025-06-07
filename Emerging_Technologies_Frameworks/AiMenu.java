
// ARTIFICIAL INTELLIGENCE TAXONOMY & FRAMEWORK Code dispalys AI TAXONOMY For each of the AI CATEGORY
// Currently the test data values are USED FOR Each Taxonomy Field. 
// However when the actual values are obtained the Taxonomy fiields will be updated accordingly. 
// This code was written using Object-Oriented programming in Java JGRASP (OCTOBER-15, 2018)
// This code was written by Mr Randy Singh,Computer Scientist,Technology Innovation Team (DISA/BDE5)
// Contact Phone# (301)225-9535  

import java.util.Scanner; 

public class AiMenu 

{
public static void main(String[] args) 
{
 
// Declare a variable to hold the 
// user's menu selection. 

int menuSelection;

final int MAX_VALUE = 3;
 
// Declare variables to hold the units 
// of measurement.
 
 String ModelingSimulation, DeepLearning, MachineLearning, NaturalLanguageProcessing, DataMining, 
 SuperComputing, NeuroMorphicEngineering, QuantumComputing, VirtualReality, ComputerVision, VirtualAgents;
 
// Create a Scanner object for keyboard input. 

Scanner keyboard = new Scanner(System.in); 

// Display the LIST OF Artificial Intelligence Taxonomy Categories 

System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("WELCOME TO ARTIFICIAL-INTELLIGENCE (AI) FRAMEWORK APPLICATION.  ");
System.out.println();
System.out.println   ("HERE ARE THE DoD - AI TAXONOMY CATEGORIES LIST: ");
System.out.println();
System.out.println   ("1.  LEARNING & INTELLIGENCE CATEGORY. "); 
System.out.println();
System.out.println   ("2.  ADVANCED COMPUTING CATEGORY."); 
System.out.println();
System.out.println   ("3.  AI SYSTEMS CATEGORY."); 
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR DoD - AI TAXONOMY CATEGORY CHOICE 1 - 3)FROM THE LIST ABOVE: ");


 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 3) 
  
{
 
System.out.println("************************************************************************************************" );
  
System.out.println("THIS IS INVALID DOD-AI TAXONOMY SELECTION");
System.out.println();
System.out.println("HERE IS THE LIST OF DoD - AI TAXONOMY LIST: ");
System.out.println();
System.out.println("1.  LEARNING & INTELLIGENCE"); 
System.out.println();
System.out.println("2.  ADVANCED COMPUTING."); 
System.out.println();
System.out.println("3.  AI SYSTEMS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR DoD - AI TAXONOMY CATEGORY CHOICE (1 - 3)FROM THE LIST ABOVE: ");



  
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
 System.out.println("YOU SELECTED LEARNING & INTELLIGENCE CATEGORY OF DoD - AI  ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW LEARNING & INTELLIGENCE SUBCATEGORIES");
 System.out.println();

AiSetter LI;

//Following statement creates an object using the AiSetter Class as
// its Blueprint. 

LI = new AiSetter();

//*****************DISPLAY THE COCOMS IOT MENU***************
  

 System.out.println("1.  SHOW ENTIRE LEARNING & INTELLIGENCE SUBCATEGORIES OF DoD - AI.");
 System.out.println();
 System.out.println("2.  LEARNING & INTELLIGENCE - MODELING & SIMULATION SUBCATEGORY.");
 System.out.println();
 System.out.println("3.  LEARNING & INTELLIGENCE - DEEP LEARNING SUBCATEGORY.");
 System.out.println();
 System.out.println("4.  LEARNING & INTELLIGENCE - MACHINE LEARNING SUBCATEGORY.");
 System.out.println();
 System.out.println("5.  LEARNING & INTELLIGENCE - NATURAL LANGUAGE PROCESSING SUBCATEGORY.");
 System.out.println();
 System.out.println("6.  LEARNING & INTELLIGENCE - DATA MINING SUBCATEGORY.");
 System.out.println();
  //System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR LEARNING & INTELLIGENCE (DoD - AI) SUBCATEGORY CHOICE FROM 1 to 6: ");
   
 
  menuSelect = keyboard.nextInt();

System.out.println("************************************************************************************************" );

 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 6)
  

  
{
  System.out.println("************************************************************************************************" );
  
  System.out.println("THIS IS INVALID SELECTION"); 
 
 System.out.print(" ENTER YOUR SUBCATEGORY CHOICE FROM 1 to 6: "); 
 System.out.println();
 
 System.out.println("1.  SHOW ENTIRE LEARNING & INTELLIGENCE SUBCATEGORIES OF DoD - AI.");
 System.out.println();
 System.out.println("2.  LEARNING & INTELLIGENCE - MODELING & SIMULATION SUBCATEGORY.");
 System.out.println();
 System.out.println("3.  LEARNING & INTELLIGENCE - DEEP LEARNING SUBCATEGORY.");
 System.out.println();
 System.out.println("4.  LEARNING & INTELLIGENCE - MACHINE LEARNING SUBCATEGORY.");
 System.out.println();
 System.out.println("5.  LEARNING & INTELLIGENCE - NATURAL LANGUAGE PROCESSING SUBCATEGORY.");
 System.out.println();
 System.out.println("6.  LEARNING & INTELLIGENCE - DATA MINING SUBCATEGORY.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM 1 to 6: ");

 
  menuSelect = keyboard.nextInt();


 }

   // If-else Type ocode starts here****************
  
    if ( menuSelect == 1)
      
       {
          //System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW THE ENTIRE TAXONOMY FOR - LEARNING & INTELLIGENCE : ");
          System.out.println();
          
          LI.setModelingSimulation         ("MODELING & SIMULATION FACILITATE UNDERSTANDING OF SYSTEM BEHAHIOUR WITHOUT TESTING. ");

          LI.setDeepLearning               ("DEEP LEARNING - MIMICKING FUNCTIONS SUCH AS LEARNING OR PROBLEM SOLVING. ");

          LI.setMachineLearning            ("MACHINE LEARNING - THE ABILITY FOR COMPUTERS TO LEARN WITHOUT BEING EXPLICITLY PROGRAMMED. ");
          
          LI.setNaturalLanguageProcessing  ("NATURAL LANGUAGE PROCESSING PROGRAMMING - NATURAL LANGUAGE PROCESSING (NLP). DARPA facilitate it through marquee programs such as Broad Operational Language Translation (BOLT) and Low Resources Languages for Emergency Incidents (LORELEI). ");        
          
          LI.setDataMining                 ("DATA MINING - DICOVERING PAATERNS IN LARGE DATA SETS AND TRANSFORMING THE DATA INTO UNDERSTANDABLE STRUCTURES FOR FURTHER ANALYSIS. ");

                   
// Display the Centcom IOT taxonomy values stored in the fields

     
      System.out.println               ("LI MODELING & SIMULATION       = " + LI.getModelingSimulation());
      System.out.println();          
      System.out.println               ("LI DEEP LEARNING               = " + LI.getDeepLearning());
      System.out.println();
      System.out.println               ("LI MACHINE LEARNING            = " + LI.getMachineLearning());
      System.out.println();
      System.out.println               ("LI NATURAL LANGUAGE PROCESSING = " + LI.getNaturalLanguageProcessing());
      System.out.println();
      System.out.println               ("LI DATA MINING                 = " + LI.getDataMining());
      System.out.println();
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      
      System.out.println( "TO CONTINUE WITH NEXT LI TAXONOMY CATEGORY PLEASE SELECT AGAIN LI CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println();
         System.out.println("PLEASE SEE SUBCATEGORY MODELING & SIMULATION FOR AI-LI: ");
         System.out.println();
  
  // *****************Information Types***************

        LI.setModelingSimulation   ("MODELING & SIMULATION FACILITATE UNDERSTANDING OF SYSTEM BEHAHIOUR WITHOUT TESTING.");


      
//**************** Display the USSOCOM IOT INFORMATION TYPES****************

     
      System.out.println    ("LI - MODELING & SIMULATION = " + LI.getModelingSimulation());
      System.out.println();
      
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT LI TAXONOMY CATEGORY PLEASE SELECT AGAIN LI CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW DEEP LEARNING SUBCATEGORY FOR AI- LI: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         LI.setDeepLearning        ("DEEP LEARNING - MIMICKING FUNCTIONS SUCH AS LEARNING OR PROBLEM SOLVING ");
 
        
         System.out.println   ("LI DEEP LEARNING = " + LI.getDeepLearning());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT SUBCATEGORY OF AI- LI SELECT AGAIN TAXONOMY CHOICE # 1");
      System.out.println();
      System.out.println("************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW SUBCATEGORY MACHINE LEARNING FOR AI-LI: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      LI.setMachineLearning ("MACHINE LEARNING - THE ABILITY FOR COMPUTERS TO LEARN WITHOUT BEING EXPLICITLY PROGRAMMED. ");
          


       

      System.out.println("LI MACHINE LEARNING = " + LI.getMachineLearning());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println("TO CONTINUE WITH NEXT SUBCATEGORY OF AI- LI SELECT AGAIN TAXONOMY CHOICE # 1 ");
      System.out.println();
      System.out.println("************************************************************************************************" );

      

      }

  else
   
      if ( menuSelect == 5)
      
       {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
 
         System.out.println("PLEASE SEE BELOW SUBCATEGORY NATURAL-LANGUAGE-PROCESSING FOR AI-LI:");
 
         System.out.println();
       
       

  // ****************Processor Types*******************
  
  
     LI.setNaturalLanguageProcessing ("NATURAL LANGUAGE PROCESSING PROGRAMMING - NATURAL LANGUAGE PROCESSING (NLP). DARPA Facilitates it through Marquee Programs such as Broad Operational Language Translation (BOLT) and Low Resources Languages for Emergency Incidents (LORELEI. ");
 
      

         System.out.println("LI NATURAL LANGUAGE PROCESSING = " + LI.getNaturalLanguageProcessing());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println( "TO CONTINUE WITH NEXT LI TAXONOMY CATEGORY PLEASE SELECT AGAIN LI CHOICE # 1");
         System.out.println();
         System.out.println("************************************************************************************************" );
     
      }

    else
   
        if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println("************************************************************************************************" );
          System.out.println();
          System.out.println("PLEASE SEE BELOW SUBCATEGORY DATA MINING FOR AI-LI: ");
          System.out.println();
         

  // ***************************NETWORK TYPES*************************
 

        LI.setDataMining("DATA MINING - DISCOVEING PATTERNS IN LARGE DATA SETS & TRANSFORMING THE DATA INTO UNDERSTANDABLE STRUCTURES FOR FURTHER ANALYSIS. ");

         System.out.println("LI DATA MINING = " + LI.getDataMining());
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println( "TO CONTINUE WITH NEXT DoD ARTIFICIAL INTELLIGENCE TAXONOMY CATEGORY PLEASE SELECT AGAIN USSOCOM CHOICE # 1");
         System.out.println();
         System.out.println("************************************************************************************************" );

        

      }

     else
          
   
  
// ******************Display the Main menu************************************

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DOD - AI TAXONOMY LIST: ");
System.out.println();
System.out.println("1.  LEARNING & INTELLIGENCE (LI). "); 
System.out.println();
System.out.println("2.  ADVANCED COMPUTING (AC)."); 
System.out.println();
System.out.println("3.  AI SYSTEMS (AIS)."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR DOD - AI TAXONOMY CHOICE (1 - 3)FROM THE LIST ABOVE: ");
       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 3) 
  
{
 
 
System.out.println();
System.out.println("THIS IS INVALID AI CHOICE# "); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DOD - AI TAXONOMY LIST: : ");
System.out.println();
System.out.println("1.  LEARNING & INTELLIGENCE (LI). "); 
System.out.println();
System.out.println("2.  ADVANCED COMPUTING (AC)."); 
System.out.println();
System.out.println("3.  AI SYSTEMS (AIS)."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR DOD - AI TAXONOMY CHOICE (1 - 3)FROM THE LIST ABOVE:: ");
   

  
  menuSelection = keyboard.nextInt();


 
 } 

break;


//*************************USTRANSCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************

case 2: 
 
 
 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED ADVANCED COMPUTING (AC) TAXONOMY CATEGORY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW ADVANCED COMPUTING (AC) TAXONOMY");
 System.out.println();

AiSetter AC;

//  Following statement creates an object using the AiSetter class as
//its Blueprint. Centcom will reference the object.

AC = new AiSetter();

  

 System.out.println("1.  SHOW ENTIRE TAXONOMY FOR ADVANCED COMPUTING (AC).");
 System.out.println();
 System.out.println("2.  ADVANCED COMPUTING (AC) - SUPER COMPUTING SUBCATEGORY.");
 System.out.println();
 System.out.println("3.  ADVANCED COMPUTING (AC) - NEUROMORPHIC ENGINEERING SUBCATEGORY.");
 System.out.println();
 System.out.println("4.  ADVANCED COMPUTING (AC) - QUANTUM COMPUTING SUBCATEGORY.");
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
 System.out.println("1.  SHOW ENTIRE TAXONOMY FOR ADVANCED COMPUTING (AC).");
 System.out.println();
 System.out.println("2.  ADVANCED COMPUTING (AC) - SUPER COMPUTING SUBCATEGORY.");
 System.out.println();
 System.out.println("3.  ADVANCED COMPUTING (AC) - NEUROMORPHIC ENGINEERING SUBCATEGORY.");
 System.out.println();
 System.out.println("4.  ADVANCED COMPUTING (AC) - QUANTUM COMPUTING SUBCATEGORY.");
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
          System.out.println("PLEASE SEE BELOW THE ENTIRE TAXONOMY FOR ADVANCED COMPUTING (AC): ");
          System.out.println();
          
          AC.setSuperComputing            (" SUPERCOMPUTING - TO Compute Performance Measured in Floating-Point Operations Per Second (FLOPS.");

          AC.setNeuroMorphicEngineering   ("NEUROMORPHIC ENGINEERING -USE of VERY-LARGE-SCALE INTEGRATION (VLSI) systems containing electronic analog circuits to mimic neuro-biological architectures. ");

          AC.setQuantumComputing          ("QUANTUM COMPUTING - USE of QUANTUM BITS (QBITS), Which can be in Superpositions of States Instead of Binary bits, which is always in one or two definite states (0 or 1).");

          

         
// Display the AC taxonomy values stored in the fields

     
      System.out.println               ("AC SUPER COMPUTING                    = " + AC.getSuperComputing());
      System.out.println();
      System.out.println               ("AC NEUROMORPHIC ENGINEERING           = " + AC.getNeuroMorphicEngineering());
      System.out.println();
      System.out.println               ("AC QUANTUM COMPUTING                  = " + AC.getQuantumComputing());
      System.out.println();
           
      System.out.println();
     
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT AC TAXONOMY SUBCATEGORY PLEASE SELECT AGAIN AC CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE SUPER COMPUTING FOR AC: ");
         System.out.println();
  
  // *****************Information Types***************

        AC.setSuperComputing   ("SUPERCOMPUTING - TO compute performance measured in floating-point operations per second (FLOPS).");

      
//**************** Display the USTRANSCOM IOT INFORMATION TYPES****************

     
      System.out.println    ("AC SUPER COMPUTING = " + AC.getSuperComputing());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT AC TAXONOMY CATEGORY PLEASE SELECT AGAIN AC CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW NEUROMORPHIC ENGINEERING SUBCATEGORY FOR AC: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         AC.setNeuroMorphicEngineering        ("NEUROMORPHIC ENGINEERING - USE OF VERY-LARGE-SCALE INTEGRATION (VLSI) SYSTEMS CONTAINING ELECTRONIC ANALOG CIRCUITS TO MIMIC NEURO-BIOLOGICAL ARCHITECTURES.");
 
        
         System.out.println   ("AC NEUROMORPHIC ENGINEERING = " + AC.getNeuroMorphicEngineering());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT AC TAXONOMY SUBCATEGORY PLEASE SELECT AGAIN AC CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW SUBCATEGORY QUANTUM COMPUTING FOR AC: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      AC.setQuantumComputing ("QUANTUM COMPUTING - USE OF QUANTUM BITS (QBITS), WHICH CAN BE IN SUPERPOSITIONS OF STATES INSTEAD OF BINARY BITS,WHICH IS ALWAYS IN ONE or TWO DEFINITE STATES (0 or 1).");

       

      System.out.println("AC QUANTUM COMPUTING = " + AC.getQuantumComputing());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT AC TAXONOMY SUBCATEGORY PLEASE SELECT AGAIN AC CHOICE # 2");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

  else
   
                  
   
  
  

// ******************Display the Main menu************************************

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DOD ARTIFICIAL INTELLIGENCE (DoD -AI)TAXONOMY CATEGORIES LIST: ");
System.out.println();
System.out.println("1.  LEARNING & INTELLIGENCE (LI). "); 
System.out.println();
System.out.println("2.  ADVANCED COMPUTING (AC)."); 
System.out.println();
System.out.println("3.  AI SYSTEMS (AIS)."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR TAXONOMY CHOICE # (1 - 3)FROM THE LIST ABOVE: ");
       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 3) 
  
{
 
 
System.out.println();
System.out.println("THIS IS INVALID AI CHOICE# "); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DOD ARTIFICIAL INTELLIGENCE(DoD -AI)TAXONOMY CATEGORIES LIST:: ");
System.out.println();
System.out.println("1.  LEARNING & INTELLIGENCE (LI). "); 
System.out.println();
System.out.println("2.  ADVANCED COMPUTING (AC)."); 
System.out.println();
System.out.println("3.  AI SYSTEMS (AIS)."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR DOD ARTIFICIAL INTELLIGENCE TAXONOMY CHOICE(1 - 3)FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();

  
 } 


break; 

//*************************USSTRATCOM IOT TAXONOMY AND FRAMEWORK BEGINS HERE******************************************

case 3:

 System.out.println();
 System.out.println("************************************************************************************************" );

 System.out.println("YOU SELECTED AI-SYSTEMS (AIS) TAXONOMY");
 System.out.println();
 System.out.println("PLEASE SEE BELOW AI-SYSTEMS (AIS) TAXONOMY SUBCATEGORIES");
 System.out.println();

AiSetter AIS;

//  Following statement creates an object using the AiSetter class as
//its Blueprint. Centcom will reference the object.

AIS = new AiSetter();

  

 System.out.println("1.  SHOW ENTIRE TAXONOMY FOR AI-SYSTEMS (AIS).");
 System.out.println();
 System.out.println("2.  AI-SYSTEMS (AIS) - VIRTUAL REALTY SUBCATEGORY.");
 System.out.println();
 System.out.println("3.  AI-SYSTEMS (AIS) - COMPUTER VISION SUBCATEGORY.");
 System.out.println();
 System.out.println("4.  AI-SYSTEMS (AIS) - VIRTUAL AGENTS SUBCATEGORY.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR AIS SUBCATEGORY CHOICE FROM 1 to 4: ");
   
 
  menuSelect = keyboard.nextInt();


 
// ***********************VALIDATE THE MENU SELECTION*********************************. 


 while (menuSelect < 1 || menuSelect > 4)
  

  
{
  System.out.println("************************************************************************************************" );
  
 System.out.println    ("THIS IS INVALID SELECTION"); 
 System.out.println();
 System.out.println    ("ENTER YOUR AI-SYSTEMS(AIS) SUBCATEGORY SELECTION FROM 1 to 4: ");
 System.out.println();
 System.out.println("1.  SHOW ENTIRE TAXONOMY FOR AI-SYSTEMS (AIS).");
 System.out.println();
 System.out.println("2.  AI-SYSTEMS (AIS) - VIRTUAL REALTY SUBCATEGORY.");
 System.out.println();
 System.out.println("3.  AI-SYSTEMS (AIS) - COMPUTER VISION SUBCATEGORY.");
 System.out.println();
 System.out.println("4.  AI-SYSTEMS (AIS) - VIRTUAL AGENTS SUBCATEGORY.");
 System.out.println();
 
  System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR AIS SUBCATEGORY CHOICE FROM 1 to 4: ");


 
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
          
          AIS.setVirtualReality          ("VIRTUAL REALITY (VR)- ENVIRONMENTS WHICH PROVIDE A VIRTUAL PRESENCE AND ARTIFICIAL AFFECTS.");

          AIS.setComputerVision          ("COMPUTER VISION - SYSTEMS THAT AUTOMATE HUMANS VISION TASKS, INCLUDING ACQUIRING, PROCESSING AND ANALYZING DIGITAL IMAGES AND HIGH - DIMENSIONAL DATA.");

          AIS.setVirtualAgents              ("VIRTUAL AGENTS - ABSTRACT FUNCTIONAL SYSTEMS THAT OPENED TO A WIDE ARRAY OF QUESTIONS. ");

          

         
// Display the AC taxonomy values stored in the fields

     
      System.out.println               ("AI-SYSTEMS (AIS) - VIRTUAL REALTY             = " + AIS.getVirtualReality());
      System.out.println();
      System.out.println               (" AI-SYSTEMS (AIS)- COMPUTER VISION           = " + AIS.getComputerVision());
      System.out.println();
      System.out.println               ("AI-SYSTEMS (AIS) - VIRTUAL AGENTS             = " + AIS.getVirtualAgents());
      System.out.println();
           
      System.out.println();
     
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT AIS TAXONOMY SUBCATEGORY PLEASE SELECT AGAIN AIS TAXONOMY CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );


      }
      else
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE VIRTUAL REALTY FOR AIS: ");
         System.out.println();
  
  // *****************Information Types***************

        AIS.setVirtualReality   ("VIRTUAL REALITY (VR)- ENVIRONMENTS WHICH PROVIDE A VIRTUAL PRESENCE AND ARTIFICIAL AFFECTS.");

      
//**************** Display the USTRANSCOM IOT INFORMATION TYPES****************

     
      System.out.println    ("AIS VIRTUAL REALTY = " + AIS.getVirtualReality());
      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT AI-AIS TAXONOMY CATEGORY PLEASE SELECT AGAIN AIS CHOICE # 3 ");
      System.out.println();
      System.out.println("************************************************************************************************" );
      
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW COMPUTER VISION CATEGORY FOR AI-AIS: ");
         System.out.println();
         

  
 // *****************Device Types*****************
 
 
         AIS.setComputerVision        ("COMPUTER VISION - SYSTEMS THAT AUTOMATE HUMANS VISION TASKS, INCLUDING ACQUIRING, PROCESSING AND ANALYZING DIGITAL IMAGES AND HIGH - DIMENSIONAL DATA.");
 
        
         System.out.println   ("AIS COMPUTER VISION = " + AIS.getComputerVision());
    

         
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT AIS-AC TAXONOMY SUBCATEGORY PLEASE SELECT AGAIN VIRTUAL AGENTS (AIS) CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

 
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
         System.out.println();
         System.out.println("***********************************************************************************" );
         System.out.println();
         System.out.println("PLEASE SEE BELOW SUBCATEGORY VIRTUAL AGENTS FOR AIS: ");
         System.out.println();
         


  // ********************Platform Types*********************
  
 
      AIS.setVirtualAgents ("VIRTUAL AGENTS - ABSTRACT FUNCTIONAL SYSTEMS THAT OPENED TO A WIDE ARRAY OF QUESTIONS.");

       

      System.out.println("AC VIRTUAL AGENTS = " + AIS.getVirtualAgents());
      

      
      System.out.println();
      System.out.println("************************************************************************************************" );
      System.out.println();
      System.out.println( "TO CONTINUE WITH NEXT AIS TAXONOMY SUBCATEGORY PLEASE SELECT AGAIN AIS CHOICE # 3");
      System.out.println();
      System.out.println("************************************************************************************************" );

      }

  else
   
                  
   
  
  

// ******************Display the Main menu************************************

System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DOD ARTIFICIAL INTELLIGENCE DoD - AI TAXONOMY CATEGORIES LIST: ");
System.out.println();
System.out.println("1.  LEARNING & INTELLIGENCE (LI). "); 
System.out.println();
System.out.println("2.  ADVANCED COMPUTING (AC)."); 
System.out.println();
System.out.println("3.  AI SYSTEMS (AIS)."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR TAXONOMY CHOICE # (1 - 3)FROM THE LIST ABOVE: ");
       
       menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

 while (menuSelection < 1 || menuSelection > 3) 
  
{
 
 
System.out.println();
System.out.println("THIS IS INVALID AI CHOICE# "); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE IS THE LIST OF DOD ARTIFICIAL INTELLIGENCE DoD - AI TAXONOMY LIST: ");
System.out.println();
System.out.println("1.  LEARNING & INTELLIGENCE (LI). "); 
System.out.println();
System.out.println("2.  ADVANCED COMPUTING (AC)."); 
System.out.println();
System.out.println("3.  AI SYSTEMS (AIS)."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();

System.out.print("ENTER YOUR DOD ARTIFICIAL INTELLIGENCE DoD - AI TAXONOMY CHOICE(1 - 3)FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();

  
 } 


break;

 
    }
  }
}

//*************************************END OF IOT TAXONOMY & FRAMEWORK PROGRAM***********************************************