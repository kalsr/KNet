
/* A cross-domain solution (CDS) is a means of information assurance that provides the ability to manually 
   or automatically access or transfer information between two or more differing security domains.
   They are integrated systems of hardware and software that enable transfer of information among incompatible security domains
   or levels of classification. Modern military, intelligence, and law enforcement operations critically depend on timely sharing
   of information.CDS is distinct from the more rigorous approaches, because it supports transfer that would otherwise be precluded 
   by established models of computer, network, and data security.
   
   CDS development, assessment, and deployment are based on risk management. The goal of a CDS is to allow an isolated critical network
   to exchange information with others, without introducing the security threat that normally comes from network connectivity. 
   The CDS FRAMEWORK Application was written using programming in Java JGRASP (JULY, 2020)
   The code was written by Kalsnet Technologies (KNet).
   Contact Phone# (301)225-9535  
*/


import java.util.Scanner; 

public class CDSMenu 

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
System.out.println   (" WELCOME TO CROSS DOMAIN SOLUTIONS MAIN MENU.  ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println ("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");


 menuSelection = keyboard.nextInt();
 
// Validate the SERVER-LESS COMPUTING Menu selection. 

 while (menuSelection < 1 || menuSelection > 8) 
  
{
System.out.println(); 
System.out.println("************************************************************************************************" );
System.out.println(); 
System.out.println(" THIS IS INVALID CHOICE FOR CROSS DOMAIN MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println( "HERE ARE VALID CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");


  
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
 System.out.println(" YOU SELECTED ELEMENTS OF CROSS DOMAIN SOLUTION CATEGORY. ");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println(" PLEASE SEE BELOW ELEMENTS OF CROSS DOMAIN SOLUTION LIST");
 System.out.println();
 System.out.println("************************************************************************************************" );
 
CDSSetter CDSelm;

CDSelm = new CDSSetter();

 System.out.println();   
 System.out.println("1.   DISPLAY ALL CROSS DOMAIN ELEMENTS.");
 System.out.println();
 System.out.println("2.   DATA CONFIDENTIALITY.");
 System.out.println();
 System.out.println("3.   DATA INTEGRITY.");
 System.out.println();
 System.out.println("4.   DATA AVAILABILITY.");
 System.out.println();
 System.out.println("5.   CDS USEFULNESS.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER CROSS DOMAIN ELEMENTS SELECTION CHOICE (1 to 5) : ");
   
 
  menuSelect = keyboard.nextInt();
  

 
 while (menuSelect < 1 || menuSelect > 5)
   
{
 System.out.println();
 System.out.println("**************************************************************************************************************" );
 System.out.println(); 
 System.out.println(" THIS IS INVALID CROSS DOMAIN ELEMENTS SELECTION - ENTER YOUR VALID ELEMENT SELECTION FROM 1 to 4:");
 System.out.println(); 
 System.out.println("***************************************************************************************************************" );
 System.out.println();
 System.out.println("1.   DISPLAY ALL CROSS DOMAIN ELEMENTS.");
 System.out.println();
 System.out.println("2.   DATA CONFIDENTIALITY.");
 System.out.println();
 System.out.println("3.   DATA INTEGRITY.");
 System.out.println();
 System.out.println("4.   DATA AVAILABILITY.");
 System.out.println();
 System.out.println("5.   CDS USEFULNESS.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER CROSS DOMAIN ELEMENTS SELECTION CHOICE (1 to 5) : "); 
 System.out.println();

 
  menuSelect = keyboard.nextInt();

 }

   if ( menuSelect == 1)
      
       {  System.out.println("**************************************************************************************************************" );
          System.out.println();
          System.out.println(" PLEASE SEE BELOW ALL CROSS DOMAIN SOLUTION  ELEMENTS DISPALYED: ");
          System.out.println();
          System.out.println("**************************************************************************************************************" ); 
          
          CDSelm.setDataConfidentiality        ("1. DATA CONFIDENTIALITY - most often imposed by hardware-enforced one-way data transfer. ");
          
          CDSelm.setDataIntegrity              ("2. DATA INTEGRITY - content management using filtering for viruses and malware; content examination utilities; in high-to-low security transfer audited human review. ");

          CDSelm.setDataAvailability           ("3. DATA AVAILABILITY - security-hardened operating systems, role-based administration access, redundant hardware, etc.");          
         
          CDSelm.setUsefulness                 ("4. CDS USEFULNESS - Cross Domain Solution capacitates a user operating from any network to locate and interact with any relevant user who is in possession of information/skillfulness conducive to successful completion of a project. Sharing of information is ad-hoc, resilient and rapid; wherein a number of linguistically diverse, concurrent users on multiple networks will be served. The information is accompanied with images and files. ");
 
                           
     
      System.out.println                       (" DATA CONFIDENTIALITY = " + CDSelm.getDataConfidentiality());
      System.out.println();          
      System.out.println                       (" DATA INTEGRITY       = " + CDSelm.getDataIntegrity());
      System.out.println();
      System.out.println                       (" DATA AVAILABILITY    = " + CDSelm.getDataAvailability());
      System.out.println();
      System.out.println                       (" CDS USEFULNESS       = " + CDSelm.getUsefulness());
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT NEXT CROSS DOMAIN ELEMENT PLEASE SELECT AGAIN CROSS DOMAIN SOLUTION MAIN MENU CHOICE # 1");
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW CROSS DOMAIN SOLUTION'S DATA CONFIDENTIALITY ELEMENT: ");
         System.out.println();
  
         CDSelm.setDataConfidentiality (" DATA CONFIDENTIALITY - most often imposed by hardware-enforced one-way data transfer. ");
    
      
     
       System.out.println(" DATA CONFIDENTIALITY = " + CDSelm.getDataConfidentiality());
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
        System.out.println( " TO CONTINUE WITH NEXT NEXT CROSS DOMAIN ELEMENT PLEASE SELECT AGAIN CROSS DOMAIN SOLUTION MAIN MENU CHOICE # 1");       
        System.out.println();
       System.out.println("****************************************************************************************************************" );   
          
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
        System.out.println();
        System.out.println();
        System.out.println(" PLEASE SEE BELOW CROSS DOMAIN SOLUTION ELEMENT DATA INTEGRITY: ");
        System.out.println();  

        CDSelm.setDataIntegrity (" DATA INTEGRITY - content management using filtering for viruses and malware; content examination utilities; in high-to-low security transfer audited human review. ");


        
      System.out.println          (" DATA INTEGRITY = " + CDSelm.getDataIntegrity());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT NEXT CROSS DOMAIN ELEMENT PLEASE SELECT AGAIN CROSS DOMAIN SOLUTION MAIN MENU CHOICE # 1");
      System.out.println();
      System.out.println("****************************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE BELOW CROSS DOMAIN SOLUTION'S ELEMENT DATA AVAILABILITY: ");
       System.out.println();
  
      CDSelm.setDataAvailability   (" DATA AVAILABILITY - security-hardened operating systems, role-based administration access, redundant hardware, etc.");          
       
      System.out.println           (" DATA AVAILABILTY = " + CDSelm.getDataAvailability());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT NEXT CROSS DOMAIN ELEMENT PLEASE SELECT AGAIN CROSS DOMAIN SOLUTION MAIN MENU CHOICE # 1");
      System.out.println();

      System.out.println("*****************************************************************************************************************" );

      }
        
        else
      
      if ( menuSelect == 5)
    
        {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW CROSS DOMAIN SOLUTION'S USEFULNESS: ");
         System.out.println();
  
         CDSelm.setUsefulness (" CDS USEFULNESS - Cross Domain Solution capacitates a user operating from any network to locate and interact with any relevant user who is in possession of information/skillfulness conducive to successful completion of a project. Sharing of information is ad-hoc, resilient and rapid; wherein a number of linguistically diverse, concurrent users on multiple networks will be served. The information is accompanied with images and files. ");
    
      
     
       System.out.println(" CDS USEFULNESS = " + CDSelm.getUsefulness());
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
        System.out.println( " TO CONTINUE WITH NEXT NEXT CROSS DOMAIN ELEMENT PLEASE SELECT AGAIN CROSS DOMAIN SOLUTION MAIN MENU CHOICE # 1");       
        System.out.println();
       System.out.println("****************************************************************************************************************" );   
          
       }

       else
  
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   (" WELCOME TO CROSS DOMAIN SOLUTIONS MAIN MENU.  ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println ("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");


 menuSelection = keyboard.nextInt();
 
// Validate the CDS  Menu selection. 

 while (menuSelection < 1 || menuSelection > 8) 
  
{
 
System.out.println("************************************************************************************************" );
System.out.println(); 
System.out.println(" THIS IS INVALID CHOICE FOR CROSS DOMAIN MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println( "HERE ARE VALID CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");


  
  menuSelection = keyboard.nextInt();

 
 } 

break;


case 2: 

CDSSetter CDSType;

CDSType = new CDSSetter();

 System.out.println();
 
 System.out.println("YOU SELECTED TYPES OF CROSS DOMAIN SOLUTIONS FROM MAIN MENU ");
 System.out.println();
 System.out.println(" PLEASE SEE BELOW TYPES OF CROSS DOMAIN SOLUTIONS. ");
 System.out.println();
 System.out.println("1.   BRIEF DISPLAY OF ALL CROSS DOMAIN SOLUTIONS.");
 System.out.println();
 System.out.println("2.   ACCESS SOLUTIONS.");
 System.out.println();
 System.out.println("3.   TRANSFER SOLUTIONS ."); 
 System.out.println();
 System.out.println("4.   MULTI-LEVEL SOLUTIONS.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE OF CROSS DOMAIN SOLUTION (1 to 4) : ");
   
 
  menuSelect = keyboard.nextInt();

  while (menuSelect < 1 || menuSelect > 4)
  

  
{
System.out.println("************************************************************************************************" );
System.out.println("THIS IS INVALID CROSS DOMAIN SOLUTIONS CATEGORY"); 
System.out.println();
System.out.println("PLEASE SELECT A VALID CROSS DOMAIN SOLUTIONS CATEGORY FROM THE LIST BELOW"); 
System.out.println();
System.out.println(" PLEASE SEE BELOW TYPES OF CROSS DOMAIN SOLUTIONS. ");
System.out.println();
System.out.println("1.   BRIEF DISPLAY OF ALL CROSS DOMAIN SOLUTIONS.");
System.out.println();
System.out.println("2.   ACCESS SOLUTIONS.");
System.out.println();
System.out.println("3.   TRANSFER SOLUTIONS .");
System.out.println();
System.out.println("4.   MULTI-LEVEL SOLUTIONS.");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS CHOICE (1 - 4) FROM THE LIST ABOVE: ");



 
  menuSelect = keyboard.nextInt();


 }
  
    if ( menuSelect == 1)
      
       {  System.out.println("**************************************************************************************************************" );
          System.out.println();
          System.out.println(" PLEASE SEE BELOW BRIEF DESCRIPTION OF ALL CROSS DOMAIN SOLUTIONS: ");
          System.out.println();
          System.out.println("**************************************************************************************************************" ); 
          
          CDSType.setAccessSolution     (" An access solution describes a users ability to view and manipulate information from domains of differing security levels and caveats. In theory, the ideal solution respects separation requirements between domains by preventing overlaps of data between domains, which ensures data of differing classifications cannot leak (i.e. data spill) between networks at any host layer of the OSI/TCP model. In practice, however, data spills are an ever-present concern that system designers attempt to mitigate within acceptable risk levels. For this reason, data transfer is addressed as a separate CDS.");
          
          CDSType.setTransferSolution   (" A transfer CDS simply offers the ability to move information between security domains that are of different classification level or different caveat of the same classification level. Transfer solutions must be evaluated to ensure the guard is capable of respecting all constrictions of the various domains that require protection.");

          CDSType.setMultiLevelSolution (" Access and transfer solutions rely on multiple single level (MSL) systems that maintain the separation of domains; this architecture is considered multiple individual levels of security (MILS). A multi-level solution (MLS) differs from MILS architecture by storing all data in a single domain. The solution uses trusted labeling and integrated Mandatory Access Control (MAC) schema to parse data according to user credentials and clearance in order to authenticate read and right privileges. In this manner, an MLS is considered an all-in-one CDS, encompassing both access and data transfer capabilities. ");       
                            
     
      System.out.println               (" ACCESS SOLUTIONS      = " + CDSType.getAccessSolution());
      System.out.println();          
      System.out.println               (" TRANSFER SOLUTIONS    = " + CDSType.getTransferSolution());
      System.out.println();
      System.out.println               (" MULTI-LEVEL SOLUTIONS = " + CDSType.getMultiLevelSolution());
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CROSS DOAMAIN SOLUTION PLEASE SELECT AGAIN SERVER-LESS MAIN MENU CHOICE # 2");
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW ACCESS CROSS DOMAIN SOLUTION: ");
         System.out.println();
  
         CDSType.setAccessSolution (" An access solution describes a users ability to view and manipulate information from domains of differing security levels and caveats. In theory, the ideal solution respects separation requirements between domains by preventing overlaps of data between domains, which ensures data of differing classifications cannot leak (i.e. data spill) between networks at any host layer of the OSI/TCP model. In practice, however, data spills are an ever-present concern that system designers attempt to mitigate within acceptable risk levels. For this reason, data transfer is addressed as a separate CDS.");
   
      
     
       System.out.println          (" ACCESS SOLUTIONS  = " + CDSType.getAccessSolution());
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN SOLUTION PLEASE SELECT AGAIN CROSS DOMAIN MAIN MENU CHOICE # 2");
       System.out.println();
       System.out.println();
       System.out.println("****************************************************************************************************************" );   
          
       }
       
     else
     
     if ( menuSelect == 3 )
     
        {
        System.out.println();
        System.out.println();
        System.out.println(" PLEASE SEE BELOW TRANSFER CROSS DOMAIN SOLUTION: ");
        System.out.println();  

        CDSType.setTransferSolution (" A transfer CDS simply offers the ability to move information between security domains that are of different classification level or different caveat of the same classification level. Transfer solutions must be evaluated to ensure the guard is capable of respecting all constrictions of the various domains that require protection.");

        
      System.out.println            (" TRANSFER SOLUTIONS = " + CDSType.getTransferSolution());
      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN SOLUTION PLEASE SELECT AGAIN CROSS DOMAIN MAIN MENU CHOICE # 2");
      System.out.println();
      System.out.println();
      System.out.println("****************************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE BELOW MULTI-LEVEL CROSS DOMAIN SOLUTION: ");
       System.out.println();
  
      CDSType.setMultiLevelSolution   (" Access and transfer solutions rely on multiple single level (MSL) systems that maintain the separation of domains; this architecture is considered multiple individual levels of security (MILS). A multi-level solution (MLS) differs from MILS architecture by storing all data in a single domain. The solution uses trusted labeling and integrated Mandatory Access Control (MAC) schema to parse data according to user credentials and clearance in order to authenticate read and right privileges. In this manner, an MLS is considered an all-in-one CDS, encompassing both access and data transfer capabilities. ");       
     
      System.out.println       (" MULTI-LEVEL SOLUTIONS = " + CDSType.getMultiLevelSolution());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN SOLUTION PLEASE SELECT AGAIN CROSS DOMAIN MAIN MENU CHOICE # 2");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );

      }

  
  else        
 
System.out.println();
System.out.println   ("HERE ARE CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");
       
   menuSelection = keyboard.nextInt();
 

 while (menuSelection < 1 || menuSelection > 8) 
  
{
System.out.println(); 
System.out.println("THIS IS INVALID CHOICE FOR CROSS DOMAIN MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE ARE VALID CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();

  
 } 


break; 

case 3:

CDSSetter CDSSc;

CDSSc = new CDSSetter();

 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println(" YOU SELECTED CROSS DOMAIN SECURITY CONTROLS FROM MAIN MENU");
 System.out.println();
 System.out.println("1.   DISPLAY ALL SECURITY CONTROLS. ");
 System.out.println();
 System.out.println("2.   SECURE CONNECTIONS. ");
 System.out.println();
 System.out.println("3.   CENTRALIZED SECURITY MANAGEMENT.");
 System.out.println();
 System.out.println("4.   USE OF ADAPTIVE SECURITY TECHNIQUES.");
 System.out.println();
 System.out.println("5.   TRUE MULTILEVEL ACCESS.");
 System.out.println();
 System.out.println("6.   INTEGRATION OF MULTILEVEL SECURITY.");
 System.out.println();
 System.out.println("7.   SECURE SINGLE SIGN-ON. ");
 System.out.println();
 System.out.println("8.   SERVER REPLICATION TO SUPPORT SCALABILITY.");
 System.out.println();
 System.out.println("9.   IPV6 IN A MULTILEVEL CONTEXT.");
 System.out.println();
 System.out.println("10.  INTEROPERABILITY.");
 System.out.println();
 System.out.println("11.  HIGH ASSURRANCE TRUSTED PATH.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR SECURITY CONTROL CHOICE FROM (1 to 11): ");
   
 
  menuSelect = keyboard.nextInt();


 while (menuSelect < 1 || menuSelect > 11)
  
  
{
 System.out.println();
 System.out.println("************************************************************************************************" );  
 System.out.println (" THIS IS INVALID SELECTION OF SECURITY CONTROLS CHOICE"); 
 System.out.println();
 System.out.println(" PLEASE SEE BELOW VALID SECURITY CONTROLS CHOICE ");
 System.out.println();
 System.out.println("1.  DISPLAY ALL SECURITY CONTROLS. ");
 System.out.println();
 System.out.println("2.   SECURE CONNECTIONS. ");
 System.out.println();
 System.out.println("3.   CENTRALIZED SECURITY MANAGEMENT.");
 System.out.println();
 System.out.println("4.   USE OF ADAPTIVE SECURITY TECHNIQUES.");
 System.out.println();
 System.out.println("5.   TRUE MULTILEVEL ACCESS.");
 System.out.println();
 System.out.println("6.   INTEGRATION OF MULTILEVEL SECURITY.");
 System.out.println();
 System.out.println("7.   SECURE SINGLE SIGN-ON. ");
 System.out.println();
 System.out.println("8.   SERVER REPLICATION TO SUPPORT SCALABILITY.");
 System.out.println();
 System.out.println("9.   IPV6 IN A MULTILEVEL CONTEXT.");
 System.out.println();
 System.out.println("10.  INTEROPERABILITY.");
 System.out.println();
 System.out.println("11.  HIGH ASSURRANCE TRUSTED PATH.");
 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR SECURITY CONTROL CHOICE FROM (1 to 11): ");

 
  menuSelect = keyboard.nextInt();


 }


   
   if ( menuSelect == 1)
      
       {  System.out.println("**************************************************************************************************************" );
          System.out.println();
          System.out.println(" PLEASE SEE BELOW BRIEF DESCRIPTION OF ALL AI & DEEP-LEARNING PLATFORMS FOR SERVER-LESS COMPUTING: ");
          System.out.println();
          System.out.println("**************************************************************************************************************" ); 
          
          CDSSc.setSecureConnections   (" Secure connections to classified networks.  ");
          
          CDSSc.setSecMgmt  (" Centralized security management. ");

          CDSSc.setAdaptiveSecurity    (" Use of adaptive security techniques to provide dynamic security services. ");          
         
          CDSSc.setMultiAccess         (" True multilevel access to data at multiple levels of security using a single commodity workstation. "); 
         
          CDSSc.setMultiSecurity       (" Integration of multilevel security with existing sensitive networks using high assurance trusted communication channels. ");        
          
          CDSSc.setSingleSignOn        (" Secure single sign-on across multiple MLS servers. ");
          
          CDSSc.setScalability         (" Server replication to support scalability. ");          
          
          CDSSc.setIpv6                (" IPv6 in a multilevel context. ");        
          
          CDSSc.setInterOperability    (" Interoperability with the DoD PKI infrastructure. ");
          
          CDSSc.setTrustedPath         (" High assurance trusted path and trusted channel techniques for managing access to the MLS cloud. ");
                            
     
      System.out.println               (" SECURE CONNECTIONS                        = " + CDSSc.getSecureConnections());
      System.out.println();          
      System.out.println               (" CENTRALIZED SECURITY MANAGEMENT           = " + CDSSc.getSecMgmt());
      System.out.println();
      System.out.println               (" USE OF ADAPTIVE SECURITY TECHNIQUES       = " + CDSSc.getAdaptiveSecurity());
      System.out.println();
      System.out.println               (" TRUE MULTI LEVEL ACCESS                   = " + CDSSc.getMultiAccess());
      System.out.println();
      System.out.println               (" INTEGRATION OF MULTILEVEL SECURITY        = " + CDSSc.getMultiSecurity());
      System.out.println();
      System.out.println               (" SECURE SINGLE SIGN-ON                     = " + CDSSc.getSingleSignOn());
      System.out.println();
      System.out.println               (" SERVER REPLICATION TO SUPPORT SCALABILITY = " + CDSSc.getScalability());
      System.out.println();
      System.out.println               (" IPV6 IN MULTILEVELVCONTEXT                = " + CDSSc.getIpv6 ());
      System.out.println();
      System.out.println               (" INTEROPERABILITY                          = " + CDSSc.getInterOperability());
      System.out.println();
      System.out.println               (" HIGH ASSURRANCE TRUSTED PATH               = " + CDSSc.getTrustedPath());
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
         System.out.println     (" PLEASE SEE BELOW CDS SECURE CONNECTIONS: ");
         System.out.println();
  
         CDSSc.setSecureConnections (" Deep learning is a Technique for implementing Machine Learning. It uses neural networks to learn, sometimes, using decision trees may also be referred to as deep learning, but for the most part deep learning involves the use of neural networks. Deep learning, driven by large neural network models, is overtaking traditional machine learning methods for understanding unstructured and perceptual data domains such as speech, text, and vision. AI has been fueled by three recent trends: the explosion in the amount of training data, the use of accelerators such as graphics processing units (GPUs), and advancements in the design of models used for training. Using any of the deep learning frameworks (e.g., Caffe, Tensorflow, MXNet), users can develop and train their models.  ");
   
      
     
       System.out.println (" CDS SECURE CONNECTIONS = " + CDSSc.getSecureConnections());
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT CDS SECURITY CONTROL CATEGORY PLEASE SELECT MAIN MENU CHOICE # 3");
       System.out.println();
       System.out.println();
       System.out.println("****************************************************************************************************************" );   
          
       }
     
     else
     
     if ( menuSelect == 3 )
     
        {
        System.out.println();
        System.out.println();
        System.out.println(" PLEASE SEE BELOW CDS SECURITY MANAGEMENT: ");
        System.out.println();  

        CDSSc.setSecMgmt (" Tensorflow is the most popular and apparently best Deep Learning Framework out there. TensorFlow is created by the Google Brain team, is an open source library for numerical computation and large-scale machine learning. TensorFlow bundles together a slew of machine learning and deep learning (aka neural networking) models and algorithms and makes them useful by way of a common metaphor. TensorFlow is a Python library for fast numerical computing created and released by Google. It is a foundation library that can be used to create Deep Learning models directly or by using wrapper libraries that simplify the process built on top of TensorFlow. ");


        
      System.out.println            (" CDS SECURITY MANAGEMENT = " + CDSSc.getSecMgmt());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CDS SECURITY CONTROL CATEGORY PLEASE SELECT MAIN MENU CHOICE # 3");
      System.out.println();
      System.out.println();
      System.out.println("****************************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE BELOW CDS ADAPTIVE SECURITY: ");
       System.out.println();
  
      CDSSc.setAdaptiveSecurity      (" MXNet provides a comprehensive and flexible Python API to serve a broad community of developers with different levels of experience and wide ranging requirements. Apache MXNet is an open-source deep learning software framework, used to train, and deploy deep neural networks. It is scalable, allowing for fast model training, and supports a flexible programming model and multiple programming languages (including C++, Python, Java, Julia, Matlab, JavaScript, Go, R, Scala, Perl, and Wolfram Language). The MXNet library is portable and can scale to multiple GPUs and multiple machines. MXNet is supported by public cloud providers including Amazon Web Services (AWS) and Microsoft Azure. Amazon has chosen MXNet as its deep learning framework of choice at AWS. Apache MXNet is a lean, flexible, and ultra-scalable deep learning framework that supports state of the art in deep learning models, including convolutional neural networks (CNNs) and long short-term memory networks (LSTMs). ");          
      
      System.out.println              (" CDS ADAPTIVE SECURITY = " + CDSSc.getAdaptiveSecurity());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CDS SECURITY CONTROL CATEGORY PLEASE SELECT MAIN MENU CHOICE # 3");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
                  
         System.out.println();
         System.out.println(" PLEASE SEE BELOW CDS MULTI-LEVEL ACCESS: "); 
         System.out.println();      
         CDSSc.setMultiAccess      (" Caffe is a deep learning framework made with expression, speed, and modularity in mind. It is developed by Berkeley AI Research (BAIR) and by community contributors. Yangqing Jia created the project during his PhD at UC Berkeley. Caffe is released under the BSD 2-Clause license. Expressive architecture encourages application and innovation. Extensible code fosters active development. Speed makes Caffe perfect for research experiments and industry deployment. Caffe can process over 60M images per day with a single NVIDIA K40 GPU. Community: Caffe already powers academic research projects, startup prototypes, and even large-scale industrial applications in vision, speech, and multimedia. Join our community of brewers on the caffe-users group and Github. "); 
         
         System.out.println        (" CDS MULTI-LEVEL ACCESS = " + CDSSc.getMultiAccess  ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CDS SECURITY CONTROL CATEGORY PLEASE SELECT MAIN MENU CHOICE # 3");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
     
      }

    else
   
        if ( menuSelect == 6)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW CDS MULTI-LEVEL SECURITY:");
         System.out.println();  
         CDSSc.setMultiSecurity   (" AWS Lambda is a serverless compute service that runs the code in response to events and automatically manages the underlying compute resources. AWS Lambda can be used to extend other AWS services with custom logic, or create your own back-end services that operate at AWS scale, performance, and security. You do not have to scale your Lambda functions  AWS Lambda scales them automatically on your behalf. Every time an event notification is received for your function, AWS Lambda quickly locates free capacity within its compute fleet and runs your code. AWS Lambda can use Java, Node.jS, Python, GO, Net.Core & Ruby. ");        
          
         System.out.println       (" CDS MULTI-LEVEL SECURITY = " + CDSSc.getMultiSecurity ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CDS SECURITY CONTROL CATEGORY PLEASE SELECT MAIN MENU CHOICE # 3");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 7)
       
       {
         
         System.out.println();
         System.out.println(" PLEASE SEE BELOW CDS SECURE SINGLE SIGN-ON:");
         System.out.println();
         CDSSc.setSingleSignOn  (" Apache OpenWhisk is an open source distributed Serverless platform that executes functions (fx) in response to events at any scale. OpenWhisk manages the infrastructure, servers & scaling using Dockers containers so you can focus on building amazing and efficient applications. OpenWhisk platform supports a programming model in which developers write functional logic (called Actions), in any supported programming language that can be dynamically scheduled and run in response to associated events (via Triggers)from external sources (Feeds) or from HTTP requests. the project includes a REST API based command line interface (CLI) along with other tools to support packaging, catalog services and many popular container deployment options. ");
           
         System.out.println     (" CDS SECURE SINGLE SIGN-ON = " + CDSSc.getSingleSignOn());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CDS SECURITY CONTROL CATEGORY PLEASE SELECT MAIN MENU CHOICE # 3");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 8)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW CDS SUPPORT FOR SCALABILITY: ");
          System.out.println();
          
          CDSSc.setScalability     (" A neural network, is a collection of layers that transform the input in some way to produce an output. Neural network models range in size from small (5MB) to very large (500MB). Training neural networks can take a significant amount of time, and the goal is to find suitable weights for the different variables in the neural network. Once the model training is complete, it can be used for inferencing , serving applying the trained model on new data in domains such a natural language processing, speech recognition, or image classification. ");
          
         System.out.println    (" SERVER-LESS DEEP LEARNING NEURAL NETWORKS = " + CDSSc.getScalability());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CDS SECURITY CONTROL CATEGORY PLEASE SELECT MAIN MENU CHOICE # 3");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
        

      }
      
      if ( menuSelect == 9)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW CDS IPV6 MULTILEVEL CONTEXT: ");
          System.out.println();
          
          CDSSc.setIpv6        (" A neural network, is a collection of layers that transform the input in some way to produce an output. Neural network models range in size from small (5MB) to very large (500MB). Training neural networks can take a significant amount of time, and the goal is to find suitable weights for the different variables in the neural network. Once the model training is complete, it can be used for inferencing , serving applying the trained model on new data in domains such a natural language processing, speech recognition, or image classification. ");
          
         System.out.println    (" CDS IPV6 MULTILEVEL CONTEXT = " + CDSSc.getIpv6());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CDS SECURITY CONTROL CATEGORY PLEASE SELECT MAIN MENU CHOICE # 3");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
        

      }

if ( menuSelect == 10)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW CDS INTEROPERABILITY: ");
          System.out.println();
          
          CDSSc.setInterOperability     (" A neural network, is a collection of layers that transform the input in some way to produce an output. Neural network models range in size from small (5MB) to very large (500MB). Training neural networks can take a significant amount of time, and the goal is to find suitable weights for the different variables in the neural network. Once the model training is complete, it can be used for inferencing , serving applying the trained model on new data in domains such a natural language processing, speech recognition, or image classification. ");
          
         System.out.println    (" CDS INTEROPERABILITY = " + CDSSc.getInterOperability());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CDS SECURITY CONTROL CATEGORY PLEASE SELECT MAIN MENU CHOICE # 3");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
        

      }

if ( menuSelect == 11)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW CDS TRUSTED PATH: ");
          System.out.println();
          
          CDSSc.setTrustedPath     (" A neural network, is a collection of layers that transform the input in some way to produce an output. Neural network models range in size from small (5MB) to very large (500MB). Training neural networks can take a significant amount of time, and the goal is to find suitable weights for the different variables in the neural network. Once the model training is complete, it can be used for inferencing , serving applying the trained model on new data in domains such a natural language processing, speech recognition, or image classification. ");
          
         System.out.println        (" CDS TRUSTED PATH = " + CDSSc.getTrustedPath());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CDS SECURITY CONTROL CATEGORY PLEASE SELECT MAIN MENU CHOICE # 3");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
        

      }


  else 
  
System.out.println();
System.out.println   ("HERE ARE CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");
       
   menuSelection = keyboard.nextInt();
 

 while (menuSelection < 1 || menuSelection > 8) 
  
{
System.out.println(); 
System.out.println("THIS IS INVALID CHOICE FOR CROSS DOMAIN MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE ARE VALID CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");

    
  menuSelection = keyboard.nextInt();
  
 } 

break;

case 4:
 
CDSSetter CDSArch;

CDSArch = new CDSSetter();
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println(" YOU SELECTED CROSS DOMAIN ENTERPRISE SERVICES (CDES) & CDS ARCHITECTURE FROM CROSS DOMAIN MAIN MENU.");
 System.out.println();
 System.out.println(" PLEASE SEE BELOW CDES & CDS ARCHITECTURE CATEGORIES: ");
 System.out.println(); 
 System.out.println("1. DISPLAY ALL CDES & CDS ARCHITECTURE CATEGORIES. ");
 System.out.println();
 System.out.println("2  CROSS DOMAIN ENTERPRISE SERVICE (CDES). ");
 System.out.println();
 System.out.println("3. CDES ORG ELEMENTS. ");
 System.out.println();
 System.out.println("4. CDES TECHNICAL REVIEW BOARD (TRB) PROCESS.");
 System.out.println();
 System.out.println("5. CROSS DOMAIN XML GUARD. ");
 System.out.println();
 System.out.println("6. COLLABORATION GATEWWAY (CG). ");
 System.out.println();
 System.out.println("7. COLLABORATION GATEWAY (CG) FUNCTIONS.");
 System.out.println();
 System.out.println("8. COLLABORATION CLIENT."); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FOR CDES & CDS ARCHITECTURE CATEGORIES ( 1 to 8): ");
   
 
  menuSelect = keyboard.nextInt();

 while (menuSelect < 1 || menuSelect > 8)
  
{ 
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println(); 
 System.out.println(" THIS IS INVALID CHOICE FOR CDES & CDS ARCHITECTURE SELECTIONS"); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println(" PLEASE SEE BELOW VALID CDES & CDS ARCHITECTURE CHOICES. ");
 System.out.println();
 System.out.println("1. DISPLAY ALL CDES & CDS ARCHITECTURE CATEGORIES. ");
 System.out.println();
 System.out.println("2  CROSS DOMAIN ENTERPRISE SERVICE (CDES). ");
 System.out.println();
 System.out.println("3. CDES ORG ELEMENTS. ");
 System.out.println();
 System.out.println("4. CDES TECHNICAL REVIEW BOARD (TRB) PROCESS.");
 System.out.println();
 System.out.println("5. CROSS DOMAIN XML GUARD. ");
 System.out.println();
 System.out.println("6. COLLABORATION GATEWWAY (CG). ");
 System.out.println();
 System.out.println("7. COLLABORATION GATEWAY (CG) FUNCTIONS.");
 System.out.println();
 System.out.println("8. COLLABORATION CLIENT."); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FOR CDES & CDS ARCHITECTURE CATEGORIES ( 1 to 8): ");
 
  menuSelect = keyboard.nextInt();

 }
     if ( menuSelect == 1)
      
       {  System.out.println("************TT**************************************************************************************************" );
          System.out.println();
          System.out.println(" PLEASE SEE BELOW BRIEF DESCRIPTION OF ALL CDES & CDS ARCHITECTURE CATEGORIES: ");
          System.out.println();
          System.out.println("************TTTTTTTTT*************************************************************************************************" ); 
           
          CDSArch.setCdes   (" (U) DISA'S CROSS DOMAIN ENTERPRISE SERVICE (CDES) DEPLOYS, OPERATES & MAINTAINS CROSS DOMAIN TECHNOLOGIES TO FACILITATE THE TRANSFER OF DATA BETWEEN DIFFERING SECURITY DOMAINS FOE A VARIETY OF FILE TYPES & TRANSFER PROTOCOLS. (U)CDES PROVIDES ENTERPRISE, ENTERPRISE-HOSTED, & MISSION SPECIFIC CROSS DOMAIN SERVICES FOR DoD & OTHER GOVERNMENT AGENCIES IN A SECURE, CONSOLIDATED, ENTERPRISE ENVIRONMENT. (U) CDES FACILITATES POINT TO POINT (P2P) CROSS DOMAIN SOLUTIONS. CDES SUPPORTS CUSTOMERS THROUGHOUT THE cd LIFECYCLE TO INCLUDE REQUIREMENTS DEFINATION,DEVELOPMENT & INTEGRATION, DEPLOYMENT & TESTING, CERTIFICATION & ACCREDETATION (C&A) AND OPERATIONS & MAINTENANCE (O&M). (U) CDES SUPPORTS CND & CYBER SECURITY COMPLIANCE FOR THE CDS DEVICES WITHIN THE ENTERPRISE INFRASTRUCTURE. ");
          
          CDSArch.setOrgElements         (" CDES ORG ELEMENTS ARE: #1. PROJECT MANAGEMENT & PLANNING #2. ENGINEERING #3. ACCREDETATION & AUTHORIZATION #4. TESTING #5. OPERATIONS #6. BUDGET & FINANCE. ");

          CDSArch.setTrb                 (" CDES TRB PROCESS : #1. CUSTOMER COMPLETES QUESTIONNAIRE #2. CROSS DOMAIN SYSTEMS ENGINEER (CDSE) CONCURS ON & SUBMITS QUESTIONNARE TO CDES #3. ID3 INQUIRY MANAGER (IM) REVIEWS QUESTIONNAIRE #4. ID32 TRB ENGINEER PERFORMS QA REVIEWS WITH THE CUSTOMER #5. WITHIN 2 WEEKS TRB IDENTIFIES QUESTIONS/INFORMATION NEEDED #6. IM COMMUNICATES QUESTIONS TO CUSTOMER #7. CUSTOMER UPDATES & RESUBMITS QUESTIONNAIRE #8. TRB NOTES CDES COMPATABILITIES/INCOMPATABILITIES IN TRB MINUTES #9. IM DRAFTS CDES COMPATIBILITY ASSESSMENT MEMO #10 CHIEF REVIEWS TRB EVALUATION, SIGNS MEMO #11. IM PROVIDES SIGNED MEMO TO CUSTOMER & CDSE.");          
         
          CDSArch.setXmlGuard            (" CROSS DOMAIN XML GUARD: Collaboration Gateway sits at the heart of CDCIE. It supplies mechanisms conducive for triggering collaboration via any Cross Domain Solutions guard capable of XML traffic transfer."); 
         
          CDSArch.setCollaborationGateway(" COLLABORATION GATEWWAY (CG): Collaboration Gateway which is an XMPP-enabled collaboration server. ");        
           
          CDSArch.setCgFunctions         (" COLLABORATION GATEWAY FUNCTIONS: #1. Implementing user security policy #2. Authenticating and authorizing users #3. Determining users authority to initiate cross-domain chats #4.Controlling users access to different chat rooms #5. Impose Message security policy #6. Forward or block messages by checking messages classification labels #7. Checking messages integrity #8. Verifying digital signature to prevent message repudiation #9.	Identifying message transformation #10. Scanning messages for potential viruses #11. Providing services pertaining to logging, archiving, searching and retrieving information #12. Logging and archiving the entire array of cross-domain messages to local database #13. Logging every administrative action to controlled log files #14. Creating new log files every day #15. Preventing access to log files by collaboration users. ");

          CDSArch.setCollaborationClient (" COLLABORATION CLIENT:Collaboration client which can be users machine run software application or CG provided web-based client. ");
          
          
                                      
     
      System.out.println               (" CROSS DOMAIN ENTERPRISE SERVICE (CDES): = " + CDSArch.getCdes());
      System.out.println();          
      System.out.println               (" CDES ORG ELEMENTS:                      = " + CDSArch.getOrgElements ());
      System.out.println();
      System.out.println               (" CDES TRB PROCESS:                       = " + CDSArch.getTrb ());
      System.out.println();
      System.out.println               (" CROSS DOMAIN XML GUARD:                 = " + CDSArch.getXmlGuard ());
      System.out.println();
      System.out.println               (" COLLABORATION GATEWAY (CG):             = " + CDSArch.getCollaborationGateway ());
      System.out.println();
      System.out.println               (" COLLABORATION GATEWAY FUNCTIONS:        = " + CDSArch.getCgFunctions());
      System.out.println();
      System.out.println               (" COLLABORATION CLIENT:                   = " + CDSArch.getCollaborationClient ());
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CDS ARCHITECTURE CATEGORY AGAIN SELECT CROSS DOMAIN MENU CHOICE # 4");
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW CROSS DOMAIN ENTERPRISE SERVICES: ");
         System.out.println();
  
         CDSArch.setCdes       (" (U) DISA'S CROSS DOMAIN ENTERPRISE SERVICE (CDES) DEPLOYS, OPERATES & MAINTAINS CROSS DOMAIN TECHNOLOGIES TO FACILITATE THE TRANSFER OF DATA BETWEEN DIFFERING SECURITY DOMAINS FOE A VARIETY OF FILE TYPES & TRANSFER PROTOCOLS. (U)CDES PROVIDES ENTERPRISE, ENTERPRISE-HOSTED, & MISSION SPECIFIC CROSS DOMAIN SERVICES FOR DoD & OTHER GOVERNMENT AGENCIES IN A SECURE, CONSOLIDATED, ENTERPRISE ENVIRONMENT. (U) CDES FACILITATES POINT TO POINT (P2P) CROSS DOMAIN SOLUTIONS. CDES SUPPORTS CUSTOMERS THROUGHOUT THE cd LIFECYCLE TO INCLUDE REQUIREMENTS DEFINATION,DEVELOPMENT & INTEGRATION, DEPLOYMENT & TESTING, CERTIFICATION & ACCREDETATION (C&A) AND OPERATIONS & MAINTENANCE (O&M). (U) CDES SUPPORTS CND & CYBER SECURITY COMPLIANCE FOR THE CDS DEVICES WITHIN THE ENTERPRISE INFRASTRUCTURE. ");
    
      
     
       System.out.println                  (" CROSS DOMAIN ENTERPRISE SERVICES = " + CDSArch.getCdes ());
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT CDS ARCHITECTURE CATEGORY AGAIN SELECT CROSS DOMAIN MENU CHOICE # 4");
       System.out.println();
       System.out.println();
       System.out.println("****************************************************************************************************************" );   
          
       }
     
     else
     
     if ( menuSelect == 3 )
     
        {
        System.out.println();
        System.out.println();
        System.out.println(" PLEASE SEE BELOW CDES ORG ELEMENTS: ");
        System.out.println();  

        CDSArch.setOrgElements        (" #1. PROJECT MANAGEMENT & PLANNING #2. ENGINEERING #3. ACCREDETATION & AUTHORIZATION #4. TESTING #5. OPERATIONS #6. BUDGET & FINANCE. ");


        
      System.out.println              (" CDES ORG ELEMENTS = " + CDSArch.getOrgElements ());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CDS ARCHITECTURE CATEGORY AGAIN SELECT CROSS DOMAIN MENU CHOICE # 4");
      System.out.println();
      System.out.println();
      System.out.println("****************************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE BELOW CDES TRB PROCESS: ");
       System.out.println();
  
      CDSArch.setTrb               (" #1. CUSTOMER COMPLETES QUESTIONNAIRE #2. CROSS DOMAIN SYSTEMS ENGINEER (CDSE) CONCURS ON & SUBMITS QUESTIONNARE TO CDES #3. ID3 INQUIRY MANAGER (IM) REVIEWS QUESTIONNAIRE #4. ID32 TRB ENGINEER PERFORMS QA REVIEWS WITH THE CUSTOMER #5. WITHIN 2 WEEKS TRB IDENTIFIES QUESTIONS/INFORMATION NEEDED #6. IM COMMUNICATES QUESTIONS TO CUSTOMER #7. CUSTOMER UPDATES & RESUBMITS QUESTIONNAIRE #8. TRB NOTES CDES COMPATABILITIES/INCOMPATABILITIES IN TRB MINUTES #9. IM DRAFTS CDES COMPATIBILITY ASSESSMENT MEMO #10 CHIEF REVIEWS TRB EVALUATION, SIGNS MEMO #11. IM PROVIDES SIGNED MEMO TO CUSTOMER & CDSE.");          
       
      System.out.println           (" CDES TRB PROCESS = " + CDSArch.getTrb ());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CDS ARCHITECTURE CATEGORY AGAIN SELECT CROSS DOMAIN MENU CHOICE # 4");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
                  
         System.out.println();
         System.out.println(" PLEASE SEE BELOW CROSS DOMAIN XML GUARD: "); 
         System.out.println();
               
         CDSArch.setXmlGuard        (" Collaboration Gateway sits at the heart of CDCIE. It supplies mechanisms conducive for triggering collaboration via any Cross Domain Solutions guard capable of XML traffic transfer."); 
                
         System.out.println          (" CROSS DOMAIN XML GUARD = " + CDSArch.getXmlGuard ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CDS ARCHITECTURE CATEGORY AGAIN SELECT CROSS DOMAIN MENU CHOICE # 4");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
     
      }

    else
   
        if ( menuSelect == 6)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW COLLABORATION GATEWAY (CG):");
         System.out.println(); 
          
          CDSArch.setCollaborationGateway  (" Collaboration Gateway which is an XMPP-enabled collaboration server. ");        
                  
         System.out.println                (" COLLABORATION GATEWAY (CG) = " + CDSArch.getCollaborationGateway ());         
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CDS ARCHITECTURE CATEGORY AGAIN SELECT CROSS DOMAIN MENU CHOICE # 4");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 7)
       
       {
         
         System.out.println();
         System.out.println(" PLEASE SEE BELOW COLLABORATION GATEWAY FUNCTIONS:");
         System.out.println();
         
         CDSArch.setCgFunctions (" #1. Implementing user security policy #2. Authenticating and authorizing users #3. Determining users authority to initiate cross-domain chats #4.Controlling users access to different chat rooms #5. Impose Message security policy #6. Forward or block messages by checking messages classification labels #7. Checking messages integrity #8. Verifying digital signature to prevent message repudiation #9.	Identifying message transformation #10. Scanning messages for potential viruses #11. Providing services pertaining to logging, archiving, searching and retrieving information #12. Logging and archiving the entire array of cross-domain messages to local database #13. Logging every administrative action to controlled log files #14. Creating new log files every day #15. Preventing access to log files by collaboration users. ");

                 
         System.out.println     (" COLLABORATION GATEWAY FUNCTIONS = " + CDSArch.getCgFunctions());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CDS ARCHITECTURE CATEGORY AGAIN SELECT CROSS DOMAIN MENU CHOICE # 4");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 8)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW CDS COLLABORATION CLIENT: ");
          System.out.println();
          
         CDSArch.setCollaborationClient   (" Collaboration client which can be users machine run software application or CG provided web-based client. ");
                   
         System.out.println               ("COLLABORATION CLIENT = " + CDSArch.getCollaborationClient ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CDS ARCHITECTURE CATEGORY AGAIN SELECT CROSS DOMAIN MENU CHOICE # 4");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
    
     
     else         
      
System.out.println();
System.out.println   ("HERE ARE CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");
       
   menuSelection = keyboard.nextInt();
 

 while (menuSelection < 1 || menuSelection > 8) 
  
{
System.out.println(); 
System.out.println("THIS IS INVALID CHOICE FOR CROSS DOMAIN MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE ARE VALID CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");

    
  menuSelection = keyboard.nextInt();
  
 } 
        
break;

case 5:
 
CDSSetter CDSAa;

CDSAa = new CDSSetter();
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println(" YOU SELECTED CROSS DOMAIN ACCREDITATION & AUTHORIZATION PROCESSES ");
 System.out.println();
 System.out.println(" PLEASE SEE BELOW ACCREDITATION & AUTHORIZATION PROCESSES CATEGORIES: ");
 System.out.println(); 
 System.out.println("1.  BRIEF DESCRIPTION OF ALL ACCREDITATION & AUTHORIZATION PROCESSES. ");
 System.out.println();
 System.out.println("2.  SABI & TSABI PROCESS. ");
 System.out.println();
 System.out.println("3.  COMPLETING CONNECTION APPROVAL DOCUMENTATION.");
 System.out.println();
 System.out.println("4.  CYBERSECURITY & RISK ASSESSMENT.");
 System.out.println();
 System.out.println("5.  CDES WORKING GROUP SUPPORT.");
 System.out.println();
 System.out.println("6.  DEVELOP FILTERS.");
 System.out.println();
 System.out.println("7.  PERFORM TECHNICAL ASSESSMENTS.");
 System.out.println();
 System.out.println("8.  VALIDATE PATCHESS.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM SEVER-LESS CHARACTERISTICS (1 to 9): ");
   
 
  menuSelect = keyboard.nextInt();

 while (menuSelect < 1 || menuSelect > 6)
  
{
 System.out.println("************************************************************************************************" );  
 System.out.println("THIS IS INVALID CHOICE FOR CROSS DOMAIN ACCREDITATION & AUTHORIZATION PROCESSES. "); 
 System.out.println();
 System.out.println("PLEASE SEE BELOW THE LIST OF VALID CROSS DOMAIN ACCREDITATION & AUTHORIZATION PROCESSES: "); 
 System.out.println();
 System.out.println("1.  BRIEF DESCRIPTION OF ALL ACCREDITATION & AUTHORIZATION PROCESSES. ");
 System.out.println();
 System.out.println("2.  SABI & TSABI PROCESS. ");
 System.out.println();
 System.out.println("3.  COMPLETING CONNECTION APPROVAL DOCUMENTATION.");
 System.out.println();
 System.out.println("4.  CYBERSECURITY & RISK ASSESSMENT.");
 System.out.println();
 System.out.println("5.  CDES WORKING GROUP SUPPORT.");
 System.out.println();
 System.out.println("6.  DEVELOP FILTERS.");
 System.out.println();
 System.out.println("7.  PERFORM TECHNICAL ASSESSMENTS.");
 System.out.println();
 System.out.println("8.  VALIDATE PATCHESS.");
 System.out.println();
 System.out.println("9.  MAINTAIN IAVM & STIGS.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR SEVER-LESS CHARACTERISTICS CHOICE FROM (1 to 9): ");

 
  menuSelect = keyboard.nextInt();

 }
    if ( menuSelect == 1)
      
       {  System.out.println("**************************************************************************************************************" );
          System.out.println();
          System.out.println(" PLEASE SEE BELOW BRIEF DESCRIPTION OF ALL ACCREDITATION & AUTHORIZATION PROCESSES. ");
          System.out.println();
          System.out.println("**************************************************************************************************************" ); 
          
          CDSAa.setSabiTsabi                 (" Currently, two processes govern accreditation. The first is Secret and Below Interoperability (SABI), which falls under Defense Information Systems Agency oversight. SABI is integrated with the Defense Information System Network Security and Accreditation Working Group, the body that accredits multilevel security programs, and follows the Department of Defense Information Technology Security Certification and Accreditation Process. The second process involves Top Secret and Below Interoperability (TSABI), which the DIA oversees. The SABI and TSABI processes are similar except that the latter occurs through the Defense Intelligence Community Accreditation Support Team. The technical requirements for these certifications differ and pose some additional technical issues when used to try to satisfy both worlds .");
          
          CDSAa.setConnectionApproval        (" The DISN CPG is a step-by-step guide that outlines procedures DISN customers (DoD Components and Mission Partners) must follow to obtain and retain enclave connections to the DISN. The guide consolidates the connection processes for DISN networks and services into one document, helps customers understand connection requirements and timelines, and provides contacts for assistance throughout the process. The Risk Adjudication and Connection Division is not the process owner for all the elements that comprise DoDs and DISAs requirements for establishing a DISN connection. Functions such as: Request Fulfillment (RF), Acquisition, Provisioning, Design and Testing, Assessment and Authorization (A&A) under the new RMF or Certification and Accreditation (C&A) under DIACAP are performed by other offices. The DISN CPG focus is on the DISN Connection Approval Process (CAP) and where appropriate point customers to appropriate information services, websites, or offices wherever possible to help guide customers through other related processes. For example, request fulfillment is provided by DISA Global Operations Command; Assessment and authorization of enclaves is accomplished by the customer; DISA Infrastructure Engineering (IE) in collaboration with the customer determines the appropriate DISN service; Department of Defense Chief Information Officer (DoD CIO) validates the mission requirement for Mission Partner connections to DISN, and the customer accomplished the A&A for the customer network enclave being connected to DISN . ");

          CDSAa.setRiskAssesments            (" A number of factors complicate the risk management of a CDS. By definition, a CDS connects discrete security domains which may be operating under separate administrative or organisational authorities. Additionally, technical risks will exist in any CDS. Outside of technical mitigation strategies, a significant number of security policy and procedural measures will likely be required to ensure access to, and use of, any CDS are adequately controlled. Involvement of security authorities throughout the development of CDS capabilities is crucial to ensuring that decisions are well understood in the context of an organisations risk management framework and expected business outcomes. The implementation of a CDS should solve security problems by design rather than blindly apply security controls to an existing system. ");          
         
          CDSAa.setWorkingGroup              (" ID32 - SupportS CDES interests in CDRM working groupS. "); 
          
          CDSAa.setDevelopFilters            (" ID32 - ENGINEERING SUPPORT GROUP DEVELOPS THE FILTER & GATEWAYS.");
         
          CDSAa.setTechAssesments            (" ID32 - ENGINEERING SUPPORT GROUP PERFORM TECHNICAL ASSESSMENTS. ");        
           
          CDSAa.setValidatePatches           (" ID32 - TESTING GROUP VALIDATES CDS SECURITY PATCHES");

          CDSAa.setStigs                     (" ID32 - OPERATIONS GROUP MAINTAINS IAVM & STIGS.  ");     

                      
     
      System.out.println               (" SABI & TSABI PROCESS                           = " + CDSAa.getSabiTsabi());
      System.out.println();          
      System.out.println               (" COMPLETING CONNECTION APPROVAL DOCUMENTATION   = " + CDSAa.getConnectionApproval ());
      System.out.println();
      System.out.println               (" CYBERSECURITY & RISK ASSESSMENTS               = " + CDSAa.getRiskAssesments ());
      System.out.println();
      System.out.println               (" CDES WORKING GROUP SUPPORT                     = " + CDSAa.getWorkingGroup ());
      System.out.println();
      System.out.println               (" DEVELOP FILTERS                                = " + CDSAa.getDevelopFilters ());
      System.out.println();
      System.out.println               (" PERFORM TECHNICAL ASSESSMENTS                  = " + CDSAa.getTechAssesments ());
      System.out.println();
      System.out.println               (" VALIDATE PATCHES                               = " + CDSAa.getValidatePatches());
      System.out.println();
      System.out.println               (" MAINTAIN IAVM & STIGS                          = " + CDSAa.getStigs ());
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT ACCREDITATION & AUTHORIZATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 5");
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println      (" PLEASE SEE BELOW SABI & TSABI PROCESS: ");
         System.out.println();
  
          CDSAa.setSabiTsabi          (" Currently, two processes govern accreditation. The first is Secret and Below Interoperability (SABI), which falls under Defense Information Systems Agency oversight. SABI is integrated with the Defense Information System Network Security and Accreditation Working Group, the body that accredits multilevel security programs, and follows the Department of Defense Information Technology Security Certification and Accreditation Process. The second process involves Top Secret and Below Interoperability (TSABI), which the DIA oversees. The SABI and TSABI processes are similar except that the latter occurs through the Defense Intelligence Community Accreditation Support Team. The technical requirements for these certifications differ and pose some additional technical issues when used to try to satisfy both worlds .");
  
      
     
       System.out.println              (" SABI & TSABI PROCESS = " + CDSAa.getSabiTsabi());

       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT ACCREDITATION & AUTHORIZATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 5");
       System.out.println();
       System.out.println();
       System.out.println("****************************************************************************************************************" );   
          
       }
     
     else
     
     if ( menuSelect == 3 )
     
        {
        System.out.println();
        System.out.println();
        System.out.println(" PLEASE SEE BELOW COMPLETING CONNECTION APPROVAL DOCUMENTATION: ");
        System.out.println();  

        CDSAa.setConnectionApproval    (" The DISN CPG is a step-by-step guide that outlines procedures DISN customers (DoD Components and Mission Partners) must follow to obtain and retain enclave connections to the DISN. The guide consolidates the connection processes for DISN networks and services into one document, helps customers understand connection requirements and timelines, and provides contacts for assistance throughout the process. The Risk Adjudication and Connection Division is not the process owner for all the elements that comprise DoDs and DISAs requirements for establishing a DISN connection. Functions such as: Request Fulfillment (RF), Acquisition, Provisioning, Design and Testing, Assessment and Authorization (A&A) under the new RMF or Certification and Accreditation (C&A) under DIACAP are performed by other offices. The DISN CPG focus is on the DISN Connection Approval Process (CAP) and where appropriate point customers to appropriate information services, websites, or offices wherever possible to help guide customers through other related processes. For example, request fulfillment is provided by DISA Global Operations Command; Assessment and authorization of enclaves is accomplished by the customer; DISA Infrastructure Engineering (IE) in collaboration with the customer determines the appropriate DISN service; Department of Defense Chief Information Officer (DoD CIO) validates the mission requirement for Mission Partner connections to DISN, and the customer accomplished the A&A for the customer network enclave being connected to DISN . ");


        
      System.out.println               (" COMPLETING CONNECTION APPROVAL DOCUMENTATION = " + CDSAa.getConnectionApproval ());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT ACCREDITATION & AUTHORIZATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 5");
      System.out.println();
      System.out.println();
      System.out.println("****************************************************************************************************************" );
          
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE BELOW CYBERSECURITY & RISK ASSESSMENTS: ");
       System.out.println();
  
      CDSAa.setRiskAssesments     (" A number of factors complicate the risk management of a CDS. By definition, a CDS connects discrete security domains which may be operating under separate administrative or organisational authorities. Additionally, technical risks will exist in any CDS. Outside of technical mitigation strategies, a significant number of security policy and procedural measures will likely be required to ensure access to, and use of, any CDS are adequately controlled. Involvement of security authorities throughout the development of CDS capabilities is crucial to ensuring that decisions are well understood in the context of an organisations risk management framework and expected business outcomes. The implementation of a CDS should solve security problems by design rather than blindly apply security controls to an existing system. ");          
      
      System.out.println          (" CYBERSECURITY & RISK ASSESSMENTS = " + CDSAa.getRiskAssesments ());
      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT ACCREDITATION & AUTHORIZATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 5");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );

      }

  else
   
      if ( menuSelect == 5)
      
       {
                  
         System.out.println();
         System.out.println(" PLEASE SEE BELOW CDES WORKING GROUP SUPPORT: "); 
         System.out.println();
               
         CDSAa.setWorkingGroup        (" ID32 - SupportS CDES interests in CDRM working groupS. ");               
         System.out.println           (" CDES WORKING GROUP SUPPORT = " + CDSAa.getWorkingGroup ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT ACCREDITATION & AUTHORIZATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 5");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
     
      }

    else
   
        if ( menuSelect == 6)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW DEVELOP FILTERS:");
         System.out.println(); 
          
         CDSAa.setDevelopFilters            (" ID32 - ENGINEERING SUPPORT GROUP DEVELOPS THE FILTER & GATEWAYS.");                
         System.out.println                 (" DEVELOP FILTERS = " + CDSAa.getDevelopFilters ());         
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT ACCREDITATION & AUTHORIZATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 5");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 7)
       
       {
         
         System.out.println();
         System.out.println(" PLEASE SEE BELOW SERVER-LESS USE-CASE:");
         System.out.println();
         
         CDSAa.setTechAssesments           (" ID32 - ENGINEERING SUPPORT GROUP PERFORM TECHNICAL ASSESSMENTS. ");               
         System.out.println                (" PERFORM TECHNICAL ASSESSMENTS = " + CDSAa.getTechAssesments ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT ACCREDITATION & AUTHORIZATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 5");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 8)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW VALIDATE PATCHES: ");
          System.out.println();
          
         CDSAa.setValidatePatches      (" ID32 - TESTING GROUP VALIDATES CDS SECURITY PATCHES");             
         System.out.println            (" VALIDATE PATCHES = " + CDSAa.getValidatePatches());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT ACCREDITATION & AUTHORIZATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 5");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
     
     else
   
        if ( menuSelect == 9)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW MAINTAIN IAVM & STIGS:");
         System.out.println(); 
          
         CDSAa.setStigs     (" ID32 - OPERATIONS GROUP MAINTAINS IAVM & STIGS.  "); 
                 
         System.out.println (" MAINTAIN IAVM & STIGS = " + CDSAa.getStigs ());

         
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT ACCREDITATION & AUTHORIZATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 5");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }
      
      else
      
System.out.println();
System.out.println   ("HERE ARE CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDITATION & AUTHORIZATION." );  
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");
       
   menuSelection = keyboard.nextInt();
 

 while (menuSelection < 1 || menuSelection > 8) 
  
{
System.out.println(); 
System.out.println("THIS IS INVALID CHOICE FOR CROSS DOMAIN MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE ARE VALID CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDITATION & AUTHORIZATION." );  
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");

    
  menuSelection = keyboard.nextInt();
  
  
 } 
       
break;

case 6:
 
CDSSetter CDSFunctions;

CDSFunctions = new CDSSetter();
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println("YOU SELECTED CROSS DOMAIN FUNCTIONS FROM CDS MAIN MENU ");
 System.out.println();
 System.out.println("PLEASE SEE BELOW CROSS DOMAIN FUNCTIONS CATEGORIES: ");
 System.out.println(); 
 System.out.println("1.   BRIEF DESCRIPTION OF ALL CROSS DOMAIN FUNCTIONAL CATEGORIES:");
 System.out.println();
 System.out.println("2    Providing an interface between the CDS core and each of the connected security domains.");
 System.out.println();
 System.out.println("3.   Enforcing a security policy for data flowing between security domains.");
 System.out.println();
 System.out.println("4.   Protecting the operation of the CDS.");
 System.out.println();
 System.out.println("5.   Maintaining a forensic audit trail.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE OF CROSS DOMAIN FUNCTIONS FROM (1 to 5): ");
   
 
  menuSelect = keyboard.nextInt();

 while (menuSelect < 1 || menuSelect > 5)
  
{

 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println(" THIS IS INVALID CHOICE FOR SERVER_LESS CHALLENGE SELECTIONS "); 
 System.out.println();
 System.out.println(" PLEASE SEE BELOW VALID SERVER-LESS SYSTEM LEVEL & PROGRAMMING MODELS & DEVOPS CHALLENGES: ");
 System.out.println(); 
 System.out.println("1.   BRIEF DESCRIPTION OF ALL CROSS DOMAIN FUNCTIONAL CATEGORIES:");
 System.out.println();
 System.out.println("2    Providing an interface between the CDS core and each of the connected security domains.");
 System.out.println();
 System.out.println("3.   Enforcing a security policy for data flowing between security domains.");
 System.out.println();
 System.out.println("4.   Protecting the operation of the CDS.");
 System.out.println();
 System.out.println("5.   Maintaining a forensic audit trail."); 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE OF CROSS DOMAIN FUNCTIONS FROM (1 to 5): ");


 
  menuSelect = keyboard.nextInt();

 }
 
         if ( menuSelect == 1)
      
       {  System.out.println("**************************************************************************************************************" );
          System.out.println();
          System.out.println(" BRIEF DESCRIPTION OF ALL CROSS DOMAIN FUNCTIONS: ");
          System.out.println();
          System.out.println("**************************************************************************************************************" ); 
          System.out.println();
          
          CDSFunctions.setInterface        (" Providing an interface between the CDS core and each of the connected security domains, as well as any relevant management network planes, by: accepting data from authenticated and authorised users and/or source systems for inspection and treatment, presenting filtered data in a usable form to approved destination systems and/or users, maintaining logical separation between connected security domains, reducing the attack surface of the CDS core and the high side security domain. ");
          
          CDSFunctions.setSecurityPolicy   (" Enforcing a security policy for data flowing between security domains, including: blocking all traffic between security domains by default and enforcing the paths that data can transit via the CDS, which typically includes the use of one-way security controls, performing filtering, data normalisation, transformation and/or sanitisation on traffic to eliminate malicious content and prevent loss of sensitive or classified data. permitting selected data to pass based on pre-determined security policy rulesets and release approval processes,	operating as a proxy between networks, rather than routing original network traffic. ");

          CDSFunctions.setOperations       (" Protecting the operation of the CDS, including: providing secure functionality for configuration and management, maintaining a secure, verifiable and patched state, allowing system monitoring and alerting,catching and handling operational errors, and ensuring data channels fail secure by default in the event of any error or failure in a subsystem. ");          
         
          CDSFunctions.setForensic        (" Maintaining a forensic audit trail, including: maintaining a security audit of the access control mechanisms for all system elements, maintaining a security audit of the data channels and security-enforcement decisions, maintaining a security audit of the system state and any changes to configuration ."); 
                 
           
                                    
     
      System.out.println               (" Providing an interface              = " + CDSFunctions.getInterface());
      System.out.println();          
      System.out.println               (" Enforcing a security policy         = " + CDSFunctions.getSecurityPolicy ());
      System.out.println();
      System.out.println               (" Protecting the operation of the CDS = " + CDSFunctions.getOperations ());
      System.out.println();
      System.out.println               (" Maintaining a forensic audit trail  = " + CDSFunctions.getForensic ());
      System.out.println();
               
      System.out.println("******************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN FUNCTION CHOICE PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 6");
      System.out.println();
      System.out.println("******************************************************************************************************************" );
      System.out.println();
      }
      
      else
      
      if ( menuSelect == 2)
    
        {
         System.out.println();
         System.out.println              (" PLEASE SEE BELOW Providing an interface between the CDS core and each of the connected security domains: ");
         System.out.println();
  
         CDSFunctions.setInterface       (" Providing an interface between the CDS core and each of the connected security domains, as well as any relevant management network planes, by: accepting data from authenticated and authorised users and/or source systems for inspection and treatment, presenting filtered data in a usable form to approved destination systems and/or users, maintaining logical separation between connected security domains, reducing the attack surface of the CDS core and the high side security domain. ");
  
      
     
       System.out.println                (" Providing an interface = " + CDSFunctions.getInterface());
       
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN FUNCTION CHOICE PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 6");
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
      System.out.println(" PLEASE SEE BELOW Enforcing a security policy: ");
      System.out.println();  

     CDSFunctions.setSecurityPolicy    (" Enforcing a security policy for data flowing between security domains, including: blocking all traffic between security domains by default and enforcing the paths that data can transit via the CDS, which typically includes the use of one-way security controls, performing filtering, data normalisation, transformation and/or sanitisation on traffic to eliminate malicious content and prevent loss of sensitive or classified data. permitting selected data to pass based on pre-determined security policy rulesets and release approval processes,	operating as a proxy between networks, rather than routing original network traffic. ");


        
      System.out.println               (" Enforcing a security policy  = " + CDSFunctions.getSecurityPolicy  ());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN FUNCTION CHOICE PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 6");
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();     
   }
   
   else
   
      if ( menuSelect == 4)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE BELOW ecting the operation of the CDS: ");
       System.out.println();
  
       CDSFunctions.setOperations         (" Protecting the operation of the CDS, including: providing secure functionality for configuration and management, maintaining a secure, verifiable and patched state, allowing system monitoring and alerting,catching and handling operational errors, and ensuring data channels fail secure by default in the event of any error or failure in a subsystem. ");          
       
      System.out.println                  (" Protecting the operation of the CDS = " + CDSFunctions.getOperations ());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN FUNCTION CHOICE PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 6");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );
      System.out.println();
      }

  else
   
      if ( menuSelect == 5)
      
       {
                  
         System.out.println();
         System.out.println(" PLEASE SEE BELOW Maintaining a forensic audit trail: "); 
         System.out.println();
               
         CDSFunctions.setForensic         (" Maintaining a forensic audit trail, including: maintaining a security audit of the access control mechanisms for all system elements, maintaining a security audit of the data channels and security-enforcement decisions, maintaining a security audit of the system state and any changes to configuration ."); 
              
         System.out.println               (" Maintaining a forensic audit trail  = " + CDSFunctions.getForensic ());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN FUNCTION CHOICE PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 6");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
      }            

                 
   else
  
System.out.println();
System.out.println   ("HERE ARE CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");
       
   menuSelection = keyboard.nextInt();
 

 while (menuSelection < 1 || menuSelection > 8) 
  
{
System.out.println(); 
System.out.println("THIS IS INVALID CHOICE FOR CROSS DOMAIN MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE ARE VALID CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS.");
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");
   

  
  menuSelection = keyboard.nextInt();

  
 } 
 
break;

case 7:
 
CDSSetter CDSUc;

CDSUc = new CDSSetter();
 
 System.out.println();
 
 System.out.println("************************************************************************************************" );
 System.out.println("YOU SELECTED CROSS DOMAIN USE CASES FROM CDS FRAMEWORK");
 System.out.println();
 System.out.println("PLEASE SEE BELOW CROSS DOMAIN USE CASE CATEGORIES: ");
 System.out.println();
 System.out.println("1.  CYBER SECURITY.");
 System.out.println();
 System.out.println("2.  DIASASTER-RESPONSE.");
 System.out.println();
 System.out.println("3.  SUPPLY CHAIN SECURITY.");
 System.out.println();
 System.out.println("4.  DEFENSE INTELLIGENSE SERVICES.");
 System.out.println();
 System.out.println("5.  CLOUD ASSURANCE.");
 System.out.println();
 System.out.println("6.  TRANSFERRING FIXED FORMAT MESSAGES.");
 System.out.println();
 System.out.println("7.  TRANSFERRING BUSINESS FILES.");
 System.out.println();
 System.out.println("8.  INGESTING BULK OPERATIONAL DATA.");
 System.out.println();
 System.out.println("9.  AGGREGATING INFORMATION FROM MULTIPLE DIFFERENT-CLASSIFIED ENVIRONMENTS.");
 System.out.println();
 System.out.println("10. ACCESSING MULTIPLE WORKSPACES WITH DIFFERENT SENSITIVITIES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CROSS DOMAIN USE CASE SELECTION FROM (1 to 10) : ");
   
 
  menuSelect = keyboard.nextInt();

 while (menuSelect < 1 || menuSelect >10)
  
{

 System.out.println(); 
 System.out.println("************************************************************************************************" );
 System.out.println("THIS IS INVALID CHOICE FOR CROSS DOMAIN USE CASE SELECTION SELECTION. "); 
 System.out.println();
 System.out.println("PLEASE SEE BELOW CROSS DOMAIN USE CASE CATEGORIES: ");
 System.out.println();
 System.out.println("1.  CYBER SECURITY.");
 System.out.println();
 System.out.println("2.  DIASASTER-RESPONSE.");
 System.out.println();
 System.out.println("3.  SUPPLY CHAIN SECURITY.");
 System.out.println();
 System.out.println("4.  DEFENSE INTELLIGENSE SERVICES.");
 System.out.println();
 System.out.println("5.  CLOUD ASSURANCE.");
 System.out.println();
 System.out.println("6.  TRANSFERRING FIXED FORMAT MESSAGES.");
 System.out.println();
 System.out.println("7.  TRANSFERRING BUSINESS FILES.");
 System.out.println();
 System.out.println("8.  INGESTING BULK OPERATIONAL DATA.");
 System.out.println();
 System.out.println("9.  AGGREGATING INFORMATION FROM MULTIPLE DIFFERENT-CLASSIFIED ENVIRONMENTS.");
 System.out.println();
 System.out.println("10. ACCESSING MULTIPLE WORKSPACES WITH DIFFERENT SENSITIVITIES.");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CROSS DOMAIN USE CASE SELECTION FROM (1 to 10) : ");


  menuSelect = keyboard.nextInt();

 }
         
      if ( menuSelect == 1)
    
        {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW USE-CASE CYBER SEURITY: ");
         System.out.println();
  
         CDSUc.setCS (" The situational analysis mandates incorporation of large volume of high speed data from internal and external sources. Cross Domain Solutions messaging tools enable real time access to events, logs, sensors, and intelligence data across multiple networks without logically connecting them.  ");
       
     
       System.out.println ("  CYBER SECURITY = " + CDSUc.getCS ());
       System.out.println();
       System.out.println("****************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN USE CASE SELECTION PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 7");
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
      System.out.println(" PLEASE SEE BELOW USE-CASE DIASASTER-RESPONSE: ");
      System.out.println();  

      CDSUc.setDR                (" Cross Domain Solutions permit Federal agencies to easily establish quick communication lines with non-government agencies during a natural disaster for coordinating response and support services. Cross Domain Solutions facilitate open access to geo-spatial services, intelligence feeds and other communication for police, volunteers etc.  ");


        
      System.out.println         (" DIASASTER-RESPONSE = " + CDSUc.getDR());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN USE CASE SELECTION PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 7");
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();     
   }
   
   else
   
      if ( menuSelect == 3)
      
       {
       System.out.println();
       System.out.println(" PLEASE SEE BELOW USE-CASE SUPPLY CHAIN SECURITY : ");
       System.out.println();
  
      CDSUc.setSC            (" Mission critical information is required to be strategically delivered to external partners with whom a company has entered into collaboration to ensure steady supply flow. Cross Domain Solution offers immunity to sensitive information from inside threats and corporate espionage. ");          
       
      System.out.println     (" SUPPLY CHAIN SECURITY = " + CDSUc.getSC());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN USE CASE SELECTION PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 7");     
      System.out.println();
      System.out.println("*****************************************************************************************************************" );
      System.out.println();
      }

  else
   
      if ( menuSelect == 4)
      
       {
                  
         System.out.println();
         System.out.println(" PLEASE SEE BELOW USE-CASE DEFENSE INTELLIGENCE SERVICE: "); 
         System.out.println();
               
         CDSUc.setDIS        (" Cross Domain Solution enables timely and highly secure communication between multiple coalition partners, military or government agencies to store, process and save data critical to security. The flexibility, speed and security provided are unprecedented. Federal agencies are no longer required to squeeze the entire computing paraphernalia in a fighter or military jet.  "); 
               
         System.out.println  (" DEFENSE INTELLIGENCE SERVICES = " + CDSUc.getDIS());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN USE CASE SELECTION PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 7");        
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
      }

    else
   
        if ( menuSelect == 5)
       
       {
         System.out.println();
         System.out.println(" PLEASE SEE BELOW  USE-CASE CLOUD ASSURANCE:");
         System.out.println(); 
          
          CDSUc.setCA (" Cloud has exploited Cross Domain Solutions to introduce an information sharing environment with numerous user communities each having their own set of unique security policies and checks. Cross Domain Solutions facilitate real time processing and information storage. Information is protected from malicious attacks as it passes along the cloud without the organization directly controlling it through physical or logical checks.  ");        
  
                 
         System.out.println     (" CLOUD ASSURANCE = " + CDSUc.getCA());        
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN USE CASE SELECTION PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 7");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 6)
       
       {
         
         System.out.println();
         System.out.println(" PLEASE SEE BELOW  USE-CASE TRANSFERRING FIXED FORMAT MESSAGES:");
         System.out.println();
         
         CDSUc.setFFM             (" Transferring fixed-format messages between government and military systems. ");       
                  
         System.out.println       (" TRANSFERRING FIXED FORMAT MESSAGES = " + CDSUc.getFFM());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN USE CASE SELECTION PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 7");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 7)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW  USE-CASE TRANSFERRING BUSINESS FILES: ");
          System.out.println();
          
         CDSUc.setTBF            (" Transferring business files into or out of isolated systems");
                    
         System.out.println      (" TRANSFERRING BUSINESS FILES = " + CDSUc.getTBF());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN USE CASE SELECTION PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 7");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
     else
          
    if ( menuSelect == 8)
       
       {
          System.out.println();
          System.out.println(" PLEASE SEE BELOW  USE-CASE INGESTING OPERATIONAL DATA: ");
          System.out.println();
          
          CDSUc.setIOD (" Ingesting bulk operational data from a sensitive network into a classified network. ");

                   
         System.out.println    (" INGESTING OPERATIONAL DATA = " + CDSUc.getIOD());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN USE CASE SELECTION PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 7");  
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
       }
       
     else
   
        if ( menuSelect == 9)
       
       {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW USE-CASE AGGREGATING INFORMATION FROM MULTIPLE DIFFERENT-CLASSIFIED ENVIRONMENTS:");
         System.out.println(); 
          
         CDSUc.setAIME          (" Aggregating input from multiple differently-classified environments in a central audit or monitoring system");
 
 
                 
         System.out.println     (" AGGREGATING INFORMATION FROM MULTIPLE DIFFERENT-CLASSIFIED ENVIRONMENTS = " + CDSUc.getAIME());

         System.out.println();

         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN USE CASE SELECTION PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 7");
         System.out.println();         
         System.out.println("****************************************************************************************************************" );        

      }
      else
   
        if ( menuSelect == 10)
       
       {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW  USE-CASE ACCESSING MULTIPLE WORKSPACES WITH DIFFERENT SENSITIVITIES:");
         System.out.println(); 
          
         CDSUc.setAMS (" Accessing multiple workspaces, with different sensitivities, from a single client device on the most trusted network. ");
 
 
                 
         System.out.println     (" ACCESSING MULTIPLE WORKSPACES WITH DIFFERENT SENSITIVITIES = " + CDSUc.getAMS());

         System.out.println();

         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN USE CASE SELECTION PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 7");
         System.out.println();         
         System.out.println("****************************************************************************************************************" );        

      }
      
               
   else 
             
System.out.println();
System.out.println   ("HERE ARE CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");
       
   menuSelection = keyboard.nextInt();
 

 while (menuSelection < 1 || menuSelection > 8) 
  
{
System.out.println(); 
System.out.println("THIS IS INVALID CHOICE FOR CROSS DOMAIN MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE ARE VALID CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");   

  
  menuSelection = keyboard.nextInt();
  
 } 
 
break;

case 8:
 
CDSSetter CDSImp;

CDSImp = new CDSSetter();
 
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.println(" YOU SELECTED CROSS DOMAIN IMPLEMENTATIONS. ");
 System.out.println();
 System.out.println(" PLEASE SEE BELOW VALID CROSS DOMAIN IMPLEMENTATION CATEGORIES: ");
 System.out.println(); 
 System.out.println("1.   IMPLEMENTING CROSS DOMAIN");
 System.out.println();
 System.out.println("2.   IDENTIFYING THE TYPE & NUMBER OF DOMAINS TO BE SUPPORTED.");
 System.out.println();
 System.out.println("3.   IDENTIFYING EXISTING CROSS DOMAIN SOLUTION REQUIREMENTS AND INFRASTRUCTURE.");
 System.out.println(); 
 System.out.println("4.   INSTALLATION, INTEGRATION & TRAINING.");
 System.out.println();
 System.out.println("5.   RISK MANAGEMENT APPROACH TO IMPLEMENT CDS.");
 System.out.println();
 System.out.println("6.   COMMON CDS RISKS.");
 System.out.println();
 System.out.println("7.   AVOIDING THE NEED FOR CDS.");
 System.out.println();
 System.out.println("8.   DOMAIN BOUNDARY. ");
 System.out.println();
 System.out.println("9.   AIR GAP. ");
 System.out.println();
 System.out.println("10.  SECURITY ZONE, TRUST ZONE & DEMILITRIZED ZONE.");
 System.out.println();
 System.out.println("11.  SECURITY POLICY ENFORCEMENT");
 System.out.println();
 System.out.println("12.  MALWARE PREVENTION.");
 System.out.println();
 System.out.println("13.  DATA LOSS PROTECTION. ");
 System.out.println();
 System.out.println("14.  ACCESS AUTHORIZATION. ");
 System.out.println();
 System.out.println("15.  DATA PROVENANCE. ");
 System.out.println();
 System.out.println("16.  TRANSFORMATION & NORMALIZATION. ");
 System.out.println();
 System.out.println("17.  PROTOCOL BREAK. ");
 System.out.println();
 System.out.println("18.  FLOW CONTROL. ");
 System.out.println();
 System.out.println("19.  CDS THREATS. ");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM CROSS DOMAIN IMPLEMENTATIONS (1 to 19): ");
   
 
  menuSelect = keyboard.nextInt();

 while (menuSelect < 1 || menuSelect > 19)
  
{
 System.out.println();
 System.out.println("************************************************************************************************" );  
 System.out.println("THIS IS INVALID CHOICE FOR CROSS DOMAIN IMPLEMENTATION CATEGORY. "); 
 System.out.println();
 System.out.println(" PLEASE SEE BELOW VALID CROSS DOMAIN IMPLEMENTATION CATEGORIES: ");
 System.out.println(); 
 System.out.println("1.   IMPLEMENTING CROSS DOMAIN");
 System.out.println();
 System.out.println("2.   IDENTIFYING THE TYPE & NUMBER OF DOMAINS TO BE SUPPORTED.");
 System.out.println();
 System.out.println("3.   IDENTIFYING EXISTING CROSS DOMAIN SOLUTION REQUIREMENTS AND INFRASTRUCTURE.");
 System.out.println(); 
 System.out.println("4.   INSTALLATION, INTEGRATION & TRAINING.");
 System.out.println();
 System.out.println("5.   RISK MANAGEMENT APPROACH TO IMPLEMENT CDS.");
 System.out.println();
 System.out.println("6.   COMMON CDS RISKS.");
 System.out.println();
 System.out.println("7.   AVOIDING THE NEED FOR CDS.");
 System.out.println();
 System.out.println("8.   DOMAIN BOUNDARY. ");
 System.out.println();
 System.out.println("9.   AIR GAP. ");
 System.out.println();
 System.out.println("10.  SECURITY ZONE, TRUST ZONE & DEMILITRIZED ZONE.");
 System.out.println();
 System.out.println("11.  SECURITY POLICY ENFORCEMENT. ");
 System.out.println();
 System.out.println("12.  MALWARE PREVENTION.");
 System.out.println();
 System.out.println("13.  DATA LOSS PROTECTION. ");
 System.out.println();
 System.out.println("14.  ACCESS AUTHORIZATION. ");
 System.out.println();
 System.out.println("15.  DATA PROVENANCE. ");
 System.out.println();
 System.out.println("16.  TRANSFORMATION & NORMALIZATION. ");
 System.out.println();
 System.out.println("17.  PROTOCOL BREAK. ");
 System.out.println();
 System.out.println("18.  FLOW CONTROL. ");
 System.out.println();
 System.out.println("19.  CDS THREATS. ");
 System.out.println();
 System.out.println("************************************************************************************************" );
 System.out.println();
 System.out.print(" ENTER YOUR CHOICE FROM CROSS DOMAIN IMPLEMENTATIONS (1 to 19): ");


 
  menuSelect = keyboard.nextInt();

 }
     if ( menuSelect == 1)
    
        {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW IMPLEMENTING CROSS DOMAIN: ");
         System.out.println();
  
         CDSImp.setImp          (" Cross Domain Solutions implementation starts with identification of people who require collaborating. Their needs are mapped. Various situations are explored like the need for synchronous collaboration capability combining text chat and whiteboarding, general purpose use, or whether a real-time operational support requirement for enhanced availability is justified. The need for language translation is taken into consideration. Would the users like to continue with existing tools like chat clients? If users opt for asynchronous collaboration, would they require the ability for erecting multiple simultaneous domains? ");
   
      
     
       System.out.println       (" IMPLEMENTING CROSS DOMAIN = " + CDSImp.getImp ());
       System.out.println();
       System.out.println("******************************************************************************************************************************" );
       System.out.println();
       System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
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
      System.out.println         (" PLEASE SEE BELOW IDENTIFYING THE TYPE & NUMBER OF DOMAINS TO BE SUPPORTED.: ");
      System.out.println();  

      CDSImp.setTN               (" Correct level of information assurance can be provided by cross-connecting the right domains. CG paves way for concurrent cross-connection of multiple domains. Several national domains can be connected through demilitarized zone via CG, allowing each domain to lay down its peculiar security policy. Higher-level classifications can be protected through a different accreditation method. ");


        
      System.out.println         (" IDENTIFYING THE TYPE & NUMBER OF DOMAINS TO BE SUPPORTED. = " + CDSImp.getTN());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
       System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();     
   }
   
   else
   
      if ( menuSelect == 3)
      
       {
       System.out.println();
       System.out.println     (" PLEASE SEE BELOW IDENTIFYING EXISTING CROSS DOMAIN SOLUTION REQUIREMENTS AND INFRASTRUCTURE: ");
       System.out.println();
  
      CDSImp.setECD           (" The pre-existence of cross-domain transfer solution makes addition of simple Cross Domain Solution. If no infrastructure exists, evaluation of requirements is to be carried out to obtain benefits contingent upon the specific message types to be transmitted.");          
       
      System.out.println      (" IDENTIFYING EXISTING CROSS DOMAIN SOLUTION REQUIREMENTS AND INFRASTRUCTURE = " + CDSImp.getECD());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );
      System.out.println();
      }

      else
   
        if ( menuSelect == 4)
       
       {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW INSTALLATION, INTEGRATION & TRAINING: ");
         System.out.println(); 
          
          CDSImp.setIIT         (" The specifics of installation are to be assessed based on criteria like need for perfectly new installation, or extension of cross-domain transfer solution already in place. All relevant users and administrators should be imparted adequate training to ensure streamlined transition to new system. The nature and complexity of Cross Domain Solutions will have a bearing on implementation timeline which can stretch to several months. Significant time is consumed in obtaining required administrative approvals. Once the permission to hook on to live networks is obtained, adequate assistance is extended to onsite personnel for plan execution. Cross Domain Solutions that are starkly new would require close coordination with solution providers. ");        
  
                 
         System.out.println     (" INSTALLATION, INTEGRATION & TRAINING = " + CDSImp.getIIT());        
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 5)
       
       {
         
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW  RISK MANAGEMENT APPROACH TO IMPLEMENT CDS: ");
         System.out.println();
         
         CDSImp.setRM             (" A number of factors complicate the risk management of a CDS. By definition, a CDS connects discrete security domains which may be operating under separate administrative or organisational authorities. Additionally, technical risks will exist in any CDS. Outside of technical mitigation strategies, a significant number of security policy and procedural measures will likely be required to ensure access to, and use of, any CDS are adequately controlled. Involvement of security authorities throughout the development of CDS capabilities is crucial to ensuring that decisions are well understood in the context of an organisations risk management framework and expected business outcomes. The implementation of a CDS should solve security problems by design rather than blindly apply security controls to an existing system. Projects involving a CDS should engage with their organisations security teams and CDS advisory bodies early and often to ensure that security problems and risks are comprehensively understood and managed. An informed risk acceptance decision is only achievable as a result of  ");       
                  
         System.out.println       ("  RISK MANAGEMENT APPROACH TO IMPLEMENT CDS = " + CDSImp.getRM());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 6)
       
       {
          System.out.println();
          System.out.println   (" PLEASE SEE BELOW COMMON CDS RISKS: ");
          System.out.println();
          
         CDSImp.setCR         (" When security controls for a CDS are inadequately enforced, connections between different security domains may allow threat actors to: gain unauthorised access to steal, copy or interfere with information, establish covert channels (i.e. data paths not intended in the original design of the system or product) into, or out of, systems, bypass security-enforcing mechanisms, interrupt the availability of critical systems or services, propagate by pivoting through less-protected networks to access more sensitive systems. NOTE: that this list of risks is not complete, and risks specific to each CDS will need to be considered. Tailored threat and risk assessment activities will assist in identifying such risks, along with potential mitigation strategies and security controls to address them.");
                    
         System.out.println   (" COMMON CDS RISKS = " + CDSImp.getCR());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
     else
          
    if ( menuSelect == 7)
       
       {
          System.out.println();
          System.out.println     (" PLEASE SEE BELOW AVOIDING THE NEED FOR CDS: ");
          System.out.println();
          
          CDSImp.setANCD       ("  In many business cases that propose introducing an additional CDS, the optimal solution for addressing business requirements may be to leverage a pre-existing CDS or even to avoid using a CDS altogether. Alternative approaches to implementing an additional CDS can include: using existing enterprise CDS (eCDS) capabilities where available, using an existing CDS where available and appropriate, noting that a non-enterprise CDS is highly tailored to both the environment and data requirements, changing business practices, noting the potential for increased business risk (i.e. working within existing security domains and reducing data transfer requirements), using existing data transfer procedures, noting a potential for increased risk compared to a CDS if insufficient security enforcement, such as content filtering, is applied to data transfers. For use cases involving SECRET or TOP SECRET networks, connecting these security domains without use of an assured CDS is in violation of the guidance within the ISM and an organisation would be doing so at their own risk. ");

                   
         System.out.println    (" AVOIDING THE NEED FOR CDS = " + CDSImp.getANCD());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
       }
       
     else
   
        if ( menuSelect == 8)
       
       {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW CDS DOMAIN BOUNDARY ");
         System.out.println(); 
          
         CDSImp.setDB          (" A domain boundary is a logical delineation around a security domain wherever systems that are contained within that security domain can interface externally, such as with other security domains. If there is no permanent interface to any external systems, the domain boundary will exist as an air gap since the necessary logical separation is also supported by physical separation. In a typical cross domain environment, the domain boundary (also considered as a trust boundary) will be located within a CDS. More specifically, the actual domain boundary within the architecture of a CDS will likely be located wherever a network bridge, protocol break and/or one-way data flow control (e.g. data diode) occurs. Some system architectures may otherwise define a staged boundary by introducing an intermediary zone or security domain separated from other security domains between a pair of data diodes or similar controls. This is known as a diode sandwich design pattern.  ");
 
 
                 
         System.out.println     (" DOMAIN BOUNDARY = " + CDSImp.getDB());

         System.out.println();

         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();         
         System.out.println("****************************************************************************************************************" );        

      }
      
      else
     
     if ( menuSelect == 9 )
     
        {
      System.out.println();
      System.out.println();
      System.out.println     (" PLEASE SEE BELOW CDS AIR GAP: ");
      System.out.println();  

      CDSImp.setAG              (" A high side security domain that is separated or segregated from lesser security domains through physical separation is considered to be protected by an air gap. Notably, a stand-alone network or system will maintain a high level of security, possibly at the expense of utility. Data can only enter or leave air-gapped environments via removable media or a secure CDS capability. There is a risk of compromising an air-gapped network when performing routine system maintenance and patching. Users may also attempt to transfer data across the air gap in an uncontrolled fashion. Note that as soon as you pass removable media between systems, you have effectively removed or bridged the air gap. There are public examples of threat actors and malicious insiders successfully compromising an air gap via removable media. Physical isolation via an air gap is likely to be maintained, or at least very carefully controlled, wherever extraordinary security is essential. Examples include military and intelligence networks, industrial control systems, financial services, and life-critical systems such as medical equipment and avionics.  ");


        
      System.out.println         (" AIR GAP = " + CDSImp.getAG());

      System.out.println();
      System.out.println("***************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();     
   }
   
   else
   
      if ( menuSelect == 10)
      
       {
       System.out.println();
       System.out.println        (" PLEASE SEE BELOW  CDS SECURITY ZONE, TRUST ZONE & DEMILITRIZED ZONE: ");
       System.out.println();
  
      CDSImp.setSCTZ             (" In networking, a security zone is a logical area in a network with a defined level of security. This security is typically defined relative to the security of another security zone such as the internet (where there is zero trust). Security zones layered in this way are also known as trust zones, which are used as a mechanism for establishing defence-in-depth in a network design. Unlike a proper security domain, a security zone or trust zone may not have its own defined or enforced security policy. Rather, security enforcement will typically be limited to logical network separation and access control rules. A demilitarised zone (DMZ) is a specialised form of security zone with one or more servers that are kept separate from the core network, either on the outside of the core network firewall or as a separate network protected by the firewall. DMZs are used to prevent direct access to information and services on internal networks. DMZs usually provide a selection of information and services to less trusted networks, such as the internet. A DMZ does not necessarily provide additional security functionality, it simply provides a level of network separation for servers that must be made available externally. Therefore, a DMZ may be seen as both a type of security domain and type of trust zone. If the DMZ and internal network are protected by a single firewall, also known as a three-legged firewall, this is likely to present a single point of failure between public and internal zones. For example, a public web server located within a DMZ will allow access to that server from both the internet (low side) and the internal network (high side) whilst denying untrusted users any access to the internal network. ");          
       
      System.out.println         (" CDS SECURITY ZONE, TRUST ZONE & DEMILITRIZED ZONE = " + CDSImp.getSCTZ());      
      System.out.println();
      System.out.println("****************************************************************************************************************" );
      System.out.println();
      System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
      System.out.println();
      System.out.println("*****************************************************************************************************************" );
      System.out.println();
      }

  else
   
      if ( menuSelect == 11)
      
       {
                  
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW CDS SECURITY POLICY ENFORCEMENT: "); 
         System.out.println();
               
         CDSImp.setSPE          (" A CDS will enforce a security policy, developed to meet an organisations information sharing requirements, whilst upholding the security and risk acceptance assumptions of the high side security domain. The security policy must consider the information being shared (i.e. the semantic content) and the data format used to convey that information (i.e. the syntax or syntactic structure). A CDS should validate all file content, and any other data, against a schema of known and expected traffic. Furthermore, a CDS will ensure all information, including data type, content, source and originator, is approved for release via conformance to the security policy or a securely-implemented manual intervention process that reveals any hidden content to a knowledgeable reviewer.  "); 
               
         System.out.println     (" SECURITY POLICY ENFORCEMENT = " + CDSImp.getSPE());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
      }

    else
   
        if ( menuSelect == 12)
       
       {
         System.out.println();
         System.out.println     (" PLEASE SEE BELOW CDS MALWARE PREVENTION: ");
         System.out.println(); 
          
          CDSImp.setMP          (" A CDS will filter data and information moving from low side to high side, to protect the integrity of the high side security domain from malicious content. This will include employing traditional signature-based antivirus techniques to identify known bad content, as well as behavioural analysis and advanced content filtering where appropriate. Where possible, passive neutralisation of malicious content is more effective than traditional malware detection and prevention techniques. This can be achieved through lossy transformation of original data formats into alternative formats that ensure business information remains present (i.e. the data is semantically equivalent) but the binary content and metadata has been modified (i.e. the data is syntactically different).  ");        
  
                 
         System.out.println     (" MALWARE PREVENTION = " + CDSImp.getMP());        
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("****************************************************************************************************************" );        

      }

     else
          
    if ( menuSelect == 13)
       
       {
         
         System.out.println();
         System.out.println    (" PLEASE SEE BELOW CDS DATA LOSS PROTECTION: ");
         System.out.println();
         
         CDSImp.setLP          ("A CDS will filter data and information to mitigate its inadvertent or deliberate transfer onto a system not approved to handle it. For fixed-format messages, a data field should be dedicated to the sensitivity or security classification of messages. A CDS will then check that field to ensure the destination security domain can handle it. For systems that employ a Reliable Human Review process, system developers should note that humans are unreliable at identifying hidden content without technical assistance, this can decrease further when data is more verbose or more frequent. Release approvers must be knowledgeable about the information for which they are attesting, including its sensitivity and appropriateness for release.  ");       
                  
         System.out.println    (" DATA LOSS PROTECTION = " + CDSImp.getLP());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 14)
       
       {
          System.out.println();
          System.out.println     (" PLEASE SEE BELOW CDS ACCESS AUTHORIZATION: ");
          System.out.println();
          
         CDSImp.setAA            (" A CDS will ensure all users, including non-human system user accounts, are authenticated and authorised to access the CDS and related security functions. If it is necessary to receive information from unauthenticated sources (e.g. web or email servers), a CDS should implement cyber security best practice to confirm the authenticity of each data source, such as through verification of Transport Layer Security certificates. This measure would also support provenance checking. ");
                    
         System.out.println      ("  ACCESS AUTHORIZATION = " + CDSImp.getAA());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
      else
          
    if ( menuSelect == 15)
       
       {
         
         System.out.println();
         System.out.println    (" PLEASE SEE BELOW CDS DATA PROVENANCE: ");
         System.out.println();
         
         CDSImp.setDP          (" A CDS will check where data has originated to ensure it aligns with expectations and that provenance is maintained through any links between source and destination systems. A chain of provenance may be based on the physical design of CDS systems, cryptographic techniques or other approved means. A CDS will also ensure data is not accessed or modified, other than by trusted and approved users or processes. A CDS should support best practice data-in-transit protection for all connections (e.g. point-to-point encryption). ");       
                  
         System.out.println    (" DATA PROVENANCE = " + CDSImp.getDP());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );        

      }
else
          
    if ( menuSelect == 16)
       
       {
          System.out.println();
          System.out.println           (" PLEASE SEE BELOW CDS TRANSFORMATION & NORMALIZATION: ");
          System.out.println();
          
         CDSImp.setTN1                  (" A CDS, where possible, will convert file types into a standard and normalised format. Content transformation processes have the potential to remove malicious or hidden content within files or to make malicious content inert. For this reason, transformation is a critical  ");
                    
         System.out.println            (" TRANSFORMATION & NORMALIZATION = " + CDSImp.getTN1());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
else
          
    if ( menuSelect == 17)
       
       {
          System.out.println();
          System.out.println           (" PLEASE SEE BELOW CDS PROTOCOL BREAK.: ");
          System.out.println();
          
         CDSImp.setPB                  (" A CDS will act as a network proxy and terminate transport protocols at multiple layers of the OSI model for all network traffic. This protocol break helps a CDS protect the high side from malicious network traffic and application layer protocols. For example, at the transport layer (OSI model Layer 4), Transmission Control Protocol connections may be broken and retransmitted using the User Datagram Protocol. ");                 
         System.out.println            (" PROTOCOL BREAK = " + CDSImp.getPB());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
       else
          
    if ( menuSelect == 18)
       
       {
          System.out.println();
          System.out.println           (" PLEASE SEE BELOW CDS FLOW CONTROL: ");
          System.out.println();
          
         CDSImp.setFC                  (" A CDS will monitor the size, volume, quantity and types of traffic and take action when this traffic exceeds defined thresholds. Unexpected traffic, such as that arriving from an unknown source, on an unused network port or at an unusual time, should trigger a security action (e.g. alert or block) as this may indicate a misconfiguration or compromise of upstream services. ");
                    
         System.out.println            (" FLOW CONTROL = " + CDSImp.getFC());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }
      else
          
    if ( menuSelect == 19)
       
       {
          System.out.println();
          System.out.println           (" PLEASE SEE BELOW CDS THREATS: ");
          System.out.println();
          
         CDSImp.setCDT                 (" First-order threats to security domains needing protection by a CDS may include: threat actors with low side access deliberately or accidentally attempting to enable malicious content to pass to the high side, thereby threatening high side integrity or availability via a low side to high side data connection, threat actors with high side access deliberately or accidentally attempting to enable data to spill or leak onto the low side, thereby threatening high side confidentiality via a high side to low side data connection, threat actors with low side access attempting to pass malicious software to the high side in order to enable the leak of data to the low side, thereby threatening high side confidentiality via the high side to low side return path. Second-order threats to a CDS and their security-enforcing mechanisms may include: threat actors with low side access attempting to disrupt or degrade security functionality, or cause an insecure failure condition, and then enabling any of the first-order threats, thereby threatening the ability of a CDS to protect high side confidentiality, integrity and availability, threat actors attempting to disrupt the operation of a CDS, thereby threatening availability of the CDS and impacting cross domain business operations, threat actors interfering with security functionality of a CDS within the cyber supply chain, thereby threatening the assurance in the CDS to perform their function and high side confidentiality, integrity and availability. Third-order threats impacting support systems used by a CDS may include: threat actors attempting to disrupt or compromise peripheral systems such as audit, monitoring, timekeeping or identity and access management to indirectly disrupt or compromise secure operation of a CDS, thereby enabling any of the second-order threats. Note though, the threats and corresponding mitigations for a CDS may be better captured through threat modelling.");
                    
         System.out.println            (" CDS THREATS = " + CDSImp.getCDT());
         System.out.println();
         System.out.println("****************************************************************************************************************" );
         System.out.println();
         System.out.println( " TO CONTINUE WITH NEXT CROSS DOMAIN IMPLEMENTATION CATEGORY PLEASE SELECT AGAIN CDS MAIN MENU CHOICE # 8. ");
         System.out.println();
         System.out.println("*****************************************************************************************************************" );
     }

      
      else
      
System.out.println();
System.out.println   ("HERE ARE CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println   ("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");
       
   menuSelection = keyboard.nextInt();
 

 while (menuSelection < 1 || menuSelection > 8) 
  
{
System.out.println(); 
System.out.println("THIS IS INVALID CHOICE FOR CROSS DOMAIN MAIN MENU SELECTION");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println("HERE ARE VALID CROSS DOMAIN MAIN MENU SELECTIONS LIST: ");
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.println   ("1. ELEMENTS OF CROSS DOMAIN SOLUTION. "); 
System.out.println();
System.out.println   ("2. CROSS DOMAIN TYPES."); 
System.out.println();
System.out.println   ("3. CROSS DOMAIN SECURITY CONTROLS."); 
System.out.println();
System.out.println   ("4. CROSS DOMAIN ARCHITECTURE."); 
System.out.println();
System.out.println   ("5. CROSS DOMAIN ACCREDETATION & AUTHORIZATION."); 
System.out.println();
System.out.println   ("6. CROSS DOMAIN FUNCTIONS."); 
System.out.println();
System.out.println   ("7. CROSS DOMAIN USE CASES."); 
System.out.println();
System.out.println   ("8. CROSS DOMAIN IMPLEMENTATIONS."); 
System.out.println();
System.out.println("************************************************************************************************" );
System.out.println();
System.out.print(" PLEASE ENTER CROSS DOMAIN SOLUTIONS MAIN MENU CHOICE (1 - 8) FROM THE LIST ABOVE: ");

    
  menuSelection = keyboard.nextInt();
  
  
 }
 
break; 
 
    }
  }
}

//*************************************END OF IOT TAXONOMY & FRAMEWORK PROGRAM***********************************************
