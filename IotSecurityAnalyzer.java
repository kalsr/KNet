//The IotSecurityAnalyzer program was developed to help Security Analysta, System & Network Administrators addressing IOT Security Vulnerabilities.
//This program addresses Top 10 IOT vulnerabilities identified by Open Web Application Security Project (OWASP). 
//This Application will help to identify what Security Steps can Be Taken TO mitigate these Vulnerabilities,
//What Security Actions Needed & Best Practices to address each of the top 10 vulnerabilities. 
//This Application addresses Security risks identified in GAO IOT Risks Report in DoD dated luly, 2017
//The Application was written by Randy Singh in July, 2017.                  


import java.util.Scanner; 

public class IotSecurityAnalyzer 

{

public static void main(String[] args) 

{ 

// Declare a variable to hold the 
// user's menu selection. 

 int menuSelection;

// Create a Scanner object for keyboard input. 

Scanner keyboard = new Scanner(System.in);
 
// Display the Top 10 IOT Vulnerabilities menu.

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("WELCOME TO IOT SECURITY ANALYZER APPLICATION PLATFORM. ");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");
 
 
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

//while (menuSelection < 1 || menuSelection > 10) 

  
  //System.out.println();

 //menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 10) 

{
   System.out.println("*************************************************************************************************");
   System.out.println("              THAT IS  AN INVALID SELECTION ");
  
 //System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");
 //System.out.println();

 menuSelection = keyboard.nextInt(); 
 
 } 
 
 while (menuSelection > 0 || menuSelection <= 10)
 
// Perform the selected operation. 

 switch(menuSelection) 
{ 
 
 case 1:
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println("CHECKING FOR WEB INTERFACE SECURITY");
  //System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("RECOMMENDED SECURITY STEPS TO CHECK FOR - AN INSECURE WEB INTERFACE:");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" 1. Determining if the default username and password can be changed during initial product setup");
  System.out.println();
  System.out.println(" 2. Determining if a specific user account is locked out after 3 - 5 failed login attempts");
  System.out.println();
  System.out.println(" 3. Determining if valid accounts can be identified using password recovery mechanisms or new user pages");
  System.out.println();
  System.out.println(" 4. Reviewing the interface for issues such as cross-site scripting, cross-site request forgery and sql injection");
  System.out.println();
  System.out.println(" 5. VERIFY SECURITY CHECKLIST FROM DISA RISK MANAGEMENT FRAMEWORK (RMF)" );
  System.out.println();
 // System.out.println("*************************************************************************************************");
  //System.out.println("SECURITY ACTIONS NEEDED TO MAKE WEB INTERFACE SECURE?");
 // System.out.println("*************************************************************************************************");
  //System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BEST PRACTICES TO SECURE A WEB INTERFACE REQUIRES: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" 1. Default passwords and ideally default usernames to be changed during initial setup");
  System.out.println();
  System.out.println(" 2. Ensuring password recovery mechanisms are robust and do not supply an attacker with information indicating a valid account");
  System.out.println();
  System.out.println(" 3. Ensuring web interface is not susceptible to XSS, SQLi or CSRF");
  System.out.println();
  System.out.println(" 4. Ensuring credentials are not exposed in internal or external network traffic");
  System.out.println();
  System.out.println(" 5. Ensuring weak passwords are not allowed");
  System.out.println();
  System.out.println(" 6. Ensuring account lockout after 3 -5 failed login attempts");
  System.out.println();
  System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");

 //System.out.println();

 menuSelection = keyboard.nextInt();
 
//Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 10) 

{
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println("              THAT IS  AN INVALID SELECTION ");
 //System.out.println("*************************************************************************************************");


 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");
 //System.out.println("*************************************************************************************************");
 menuSelection = keyboard.nextInt(); 
 
 } 


break;
 
case 2: 
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println("CHECKING FOR SUFFICIENT AUTHENTICATION/AUTHORIZATION ");
 // System.out.println("*************************************************************************************************");
  System.out.println();
 // Insuuficient Authentication Checks

  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("RECOMMENDED SECURITY STEPS TO CHECK FOR -  INSUFFICIENT AUTHENTICATION INCLUDES: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
 
  System.out.println(" 1. Attempting to use simple passwords such as 1234 is a fast and easy way to determine if the password policy is sufficient across all interfaces");
  System.out.println();
  System.out.println(" 2. Reviewing network traffic to determine if credentials are being transmitted in clear text");
  System.out.println();
  System.out.println(" 3. Reviewing requirements around password controls such as password complexity, password history check, password expiration and forced password reset for new users");
  System.out.println();
  System.out.println(" 4. Reviewing whether re-authentication is required for sensitive features");
  System.out.println();
  System.out.println(" 5. VERIFY SECURITY CHECKLIST FROM DISA RISK MANAGEMENT FRAMEWORK (RMF)" );

  System.out.println();

  // Insuuficient Authorization Checks

  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" RECOMMENDED SECURITY STEPS TO CHECK FOR - INSUFFICIENT AUTHORIZATION INCLUDES: ");
  System.out.println();
  System.out.println("*************************************************************************************************");

  System.out.println();
  System.out.println(" 1. Reviewing the various interfaces to determine whether the interfaces allow for separation of roles. For example, all features will be accessible to administrators, but users will have a more limited set of features available.");
  System.out.println();
  System.out.println(" 2. Reviewing network traffic to determine if credentials are being transmitted in clear text");
  System.out.println();
  System.out.println(" 3. Reviewing access controls and testing for privilege escalation");
  System.out.println();
  System.out.println(" 4. VERIFY SECURITY CHECKLIST FROM DISA RISK MANAGEMENT FRAMEWORK (RMF)" );

  System.out.println();
  //System.out.println("*************************************************************************************************");
  //System.out.println("SECURITY ACTIONS WHICH CAN BE TAKEN TO MAKE AUTHENTICATION/AUTHORIZATION BETTER?");
  //System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BEST PRACTICES FOR AUTHENTICATION/AUTHORIZATION REQUIRES: ");
  System.out.println();
  System.out.println("*************************************************************************************************");

  System.out.println();
  System.out.println(" 1. Ensuring that the strong passwords are required");
  System.out.println();
  System.out.println(" 2. Ensuring granular access control is in place when necessary");
  System.out.println();
  System.out.println(" 3. Ensuring credentials are properly protected");
  System.out.println();
  System.out.println(" 4. Implement two factor authentication where possible");
  System.out.println();
  System.out.println(" 5. Ensuring that password recovery mechanisms are secure");
  System.out.println();
  System.out.println(" 6. Ensuring re-authentication is required for sensitive features");
  System.out.println();
  System.out.println(" 7. Ensuring options are available for configuring password controls");
  System.out.println();
  System.out.println(" 7. Ensuring credential can be revoked");
  System.out.println();
  System.out.println(" 9. The app authentication is required");
  System.out.println();
  System.out.println("10. The device authentication is required");
  System.out.println();
  System.out.println("11. The server authentication is required");
  System.out.println();
  System.out.println("12. Manage authenicated user id(credential info.) and the user's device id, the user's app id mapping table in the authentication server");
  System.out.println();
  System.out.println("13. Ensuring that the authentication token/session key issuing to client is always different");
  System.out.println();
  System.out.println("14. Ensuring that the user id, app id, device id is universally unique");
  System.out.println();
 // System.out.println("*************************************************************************************************");
  System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");

  
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 10) 

{ 
 System.out.println("*************************************************************************************************");
 System.out.println("              THAT IS  AN INVALID SELECTION ");
 //System.out.println("*************************************************************************************************");


 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");
 menuSelection = keyboard.nextInt(); 
 } 
 
break; 

case 3:

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println("CHECKING FOR  NETWORK SERVICES SECURITY");
  //System.out.println("*************************************************************************************************");

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("RECOMMENDED SECURITY STEPS TO CHECK FOR - INSECURE NETWORK SERVICES: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" 1. Determining if insecure network services exist by reviewing your device for open ports using a port scanner");
  System.out.println();
  System.out.println(" 2. Reviewing network ports to ensure they are absolutely necessary and if there are any ports being exposed to the internet using UPnP");
  System.out.println();
  System.out.println(" 3. As open ports are identified, each can be tested using any number of automated tools that look for DoS vulnerabilities, vulnerabilities related to UDP services and vulnerabilities related to buffer overflow and fuzzing attacks");
  System.out.println();
  System.out.println(" 4. VERIFY SECURITY CHECKLIST FROM DISA RISK MANAGEMENT FRAMEWORK (RMF)" );
  //System.out.println();
  //System.out.println("*************************************************************************************************");
  //System.out.println("SECURITY STEPS TO SECURE MY NETWORK SERVICES?");
  //System.out.println("*************************************************************************************************");

  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println("BEST PRACTICES TO SECURE NETWORK SERVICES REQUIRES:  ");
  System.out.println("*************************************************************************************************");

  System.out.println();
  System.out.println(" 1. Ensuring only necessary ports are exposed and available");
  System.out.println();
  System.out.println(" 2. Ensuring services are not vulnerable to buffer overflow and fuzzing attacks.");
  System.out.println();
  System.out.println(" 3. Ensuring services are not vulnerable to DoS attacks which can affect the device itself or other devices and/or users on the local network or other networks.");
  System.out.println();
  System.out.println(" 4. Ensuring network ports or services are not exposed to the internet via UPnP for example");
  System.out.println();
  System.out.println(" 5. The abnormal service request traffic should be detected and blocked on service gateway layer");
  
  System.out.println();
  System.out.println("*************************************************************************************************");

  System.out.println("HERE IS THE LIST OF TOP 10 IOT SECURITY VULNERABILITIES: ");
  System.out.println();
  
  System.out.println("1. INSECURE WEB INTERFACE.."); 
  System.out.println();
  System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
  System.out.println();
  System.out.println("3. INSECURE NETWORK SERVICES."); 
  System.out.println();
  System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
  System.out.println();
  System.out.println("5. PRIVACY CONCERNS."); 
  System.out.println();
  System.out.println("6. INSECURE CLOUD INTERFACE.");
  System.out.println();
  System.out.println("7. INSECURE MOBILE INTERFACE."); 
  System.out.println();
  System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
  System.out.println();
  System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
  System.out.println();
  System.out.println("10.POOR PHYSICAL SECURITY.");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.print("ENTER THE SECURITY VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");
  
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 10) 

{ 
 System.out.println("*************************************************************************************************");
 System.out.println("              THAT IS  AN INVALID SELECTION ");
// System.out.println("*************************************************************************************************");


 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt(); 
 } 

break;

case 4:
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println("CHECKING FOR INSUFFICIENT TRANSPORT ENCRYPTION");
  //System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("RECOMMENDED SECURITY STEPS TO CHECK FOR - LACK OF TRANSPORT ENCRYPTION:");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" 1. Reviewing network traffic of the device, its mobile application and any cloud connections to determine if any information is passed in clear text");
  System.out.println();
  System.out.println(" 2. Reviewing the use of SSL or TLS to ensure it is up to date and properly implemented");
  System.out.println();
  System.out.println(" 3. Reviewing the use of any encryption protocols to ensure they are recommended and accepted");
  System.out.println();
  System.out.println(" 4. VERIFY SECURITY CHECKLIST FROM DISA RISK MANAGEMENT FRAMEWORK (RMF)" );

 // System.out.println();
  //System.out.println("*************************************************************************************************");
  //System.out.println("SECURITY ACTIONS WHICH CAN BE TAKEN TO CORRECT - LACK OF TRANSPORT ENCRYPTION?");
  //System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BEST PRACTICES FOR SUFFICIENT TRANSPORT ENCRYPTION REQUIRES: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" 1. Ensuring data is encrypted using protocols such as SSL and TLS while transiting networks.");
  System.out.println();
  System.out.println(" 2. Ensuring other industry standard encryption techniques are utilized to protect data during transport if SSL or TLS are not available.");
  System.out.println();
  System.out.println(" 3. Ensuring only accepted encryption standards are used and avoid using proprietary encryption protocols");
  System.out.println();
  System.out.println(" 4. Ensuring the message payload encryption");
  System.out.println();
  System.out.println(" 5. Ensuring the secure encryption key handshaking");
  System.out.println();
  System.out.println(" 6. Ensuring received data integrity verification");
  System.out.println();
  System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");

  
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 10) 

{ 
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println("              THAT IS  AN INVALID SELECTION ");
 //System.out.println("*************************************************************************************************");


 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");
 menuSelection = keyboard.nextInt(); 
 } 

break;

case 5:

  System.out.println("*************************************************************************************************");
  System.out.println("CHECKING FOR DEVICE PRIVACY CONCERNS ");
  //System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("RECOMMENDED SECURITY STEPS TO CHECK FOR - THE PRIVACY CONCERNS: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println(" 1. Identifying all data types that are being collected by the device, its mobile application and any cloud interfaces");
  System.out.println();
  System.out.println(" 2. The device and it's various components should only collect what is necessary to perform its function");
  System.out.println();
  System.out.println(" 3. Personally identifiable information can be exposed when not properly encrypted while at rest on storage mediums and during transit over networks");
  System.out.println();
  System.out.println(" 4. Reviewing who has access to personal information that is collected ");
  System.out.println();
  System.out.println(" 5. Determining if data collected can be de-identified or anonymized ");
  System.out.println();
  System.out.println(" 6. Determining if data collected is beyond what is needed for proper operation of the device (Does the end-user have a choice for this data collection");
  System.out.println();
  System.out.println(" 7. Determining if a data retention policy is in place");
  System.out.println();
  System.out.println(" 8. Follow Security Technical Implementation Guides (STIGS) for specific DoD-Issued mobile Devices like Apple & Blackbery- GAO Recommended DoD Policy" );
  System.out.println();
  System.out.println(" 9. Follow DoD Component Policies on Wireless and Personal Portable Electronic Devices 2014-2016 " );
  System.out.println();
  System.out.println("10. Follow DODI 8420.01 Commercial Wireless Local-Area Network (WLAN)Devices, Systems & Policies " );


  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();
  System.out.println("BEST PRACTICE IN MINIMIZING PRIVACY CONCERNS: ");
  System.out.println();
  System.out.println("*************************************************************************************************");
  System.out.println();

  System.out.println(" 1. Ensuring only data critical to the functionality of the device is collected");
  System.out.println();
  System.out.println(" 2. Ensuring that any data collected is of a less sensitive nature (i.e., try not to collect sensitive data)");
  System.out.println();
  System.out.println(" 3. Ensuring that any data collected is de-identified or anonymized");
  System.out.println();
  System.out.println(" 4. Ensuring any data collected is properly protected with encryption");
  System.out.println();
  System.out.println(" 5. Ensuring the device and all of its components properly protect personal information");
  System.out.println();
  System.out.println(" 6. Ensuring only authorized individuals have access to collected personal information");
  System.out.println();
  System.out.println(" 7. Ensuring that retention limits are set for collected data");
  System.out.println();
  System.out.println(" 8. Ensuring that end-users are provided with NOTICE AND CHOICE if data collected is more than what would be expected from the product");
  System.out.println();
  System.out.println(" 9. Ensuring the role based access control/authorization to the collected data/analyzed data is applied");
  System.out.println();
  System.out.println("10. Ensuring that the analyzed data is de-identified");
  System.out.println();
  System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");
  
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 10) 

{ 
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println("              THAT IS  AN INVALID SELECTION ");
 //System.out.println("*************************************************************************************************");


 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");
 menuSelection = keyboard.nextInt(); 
 } 


break;

case 6:

System.out.println();

System.out.println("*************************************************************************************************");
System.out.println("CHECKING FOR CLOUD INTERFACE SECURITY");
//System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("RECOMMENDED ECURITY STEPS TO CHECK FOR - INSECURE CLOUD INTERFACE: "); 
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("1•	Determining if the default username and password can be changed during initial product setup. ");
System.out.println();
System.out.println("2•	Determining if a specific user account is locked out after 3 - 5 failed login attempts. ");
System.out.println();
System.out.println("3•	Determining if valid accounts can be identified using password recovery mechanisms or new user pages. ");
System.out.println();
System.out.println("4•	Reviewing the interface for issues such as cross-site scripting, cross-site request forgery and sql injection. ");
System.out.println();
System.out.println("5•	Reviewing all cloud interfaces for vulnerabilities (API interfaces and cloud-based web interfaces. ");
System.out.println();
System.out.println("6. VERIFY SECURITY CHECKLIST FROM DISA RISK MANAGEMENT FRAMEWORK (RMF)" );
//System.out.println();
//System.out.println("*************************************************************************************************");
//System.out.println("RECOMMENDED SECURITY ACTIONS TO SECURE CLOUD INTERFACE?. ");
//System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println("BEST PRACTICES TO SECURE CLOUD INTERFACE REQUIRES: ");
System.out.println("*************************************************************************************************");
System.out.println(); 
System.out.println("1.	Default passwords and ideally default usernames to be changed during initial setup. ");
System.out.println();
System.out.println("2.	Ensuring user accounts can not be enumerated using functionality such as password reset mechanisms. ");
System.out.println();
System.out.println("3.	Ensuring account lockout after 3- 5 failed login attempts. ");
System.out.println();
System.out.println("4.	Ensuring the cloud-based web interface is not susceptible to XSS, SQLi or CSRF. ");
System.out.println();
System.out.println("5.	Ensuring credentials are not exposed over the internet. ");
System.out.println();
System.out.println("6.	Implement two factor authentication if possible. ");
System.out.println();
System.out.println("7.	Detect or block the abnormal reqests/attempts. ");

System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");
  
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 10) 

{
 System.out.println(); 
 System.out.println("*************************************************************************************************");
 System.out.println("              THAT IS  AN INVALID SELECTION ");
 //System.out.println("*************************************************************************************************");


 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt(); 
 } 

break;

case 7:
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println("CHECKING FOR MOBILE INTERFACE SECURITY");
//System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("RECOMMENDED SECURITY STEPS TO CHECK FOR - AN INSECURE MOBILE INTERFACE INCLUDES: ");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println(); 
System.out.println("1.	Determining if the default username and password can be changed during initial product setup.");
System.out.println();
System.out.println("2.	Determining if a specific user account is locked out after 3 - 5 failed login attempts.");
System.out.println();
System.out.println("3.	Determining if valid accounts can be identified using password recovery mechanisms or new user pages.");
System.out.println();
System.out.println("4.	Reviewing whether credentials are exposed while connected to wireless networks.");
System.out.println();
System.out.println("5.	Reviewing whether two factor authentication options are available.");
System.out.println();
System.out.println("8.  Follow Security Technical Implementation Guides (STIGS) for specific DoD-Issued mobile Devices like Apple & Blackbery- GAO Recommended DoD Policy" );
System.out.println();
System.out.println("9.  Follow DoD Component Policies on Wireless and Personal Portable Electronic Devices 2014-2016 " );

System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("BEST PRACTICES TO SECURE MOBILE INTERFACE REQUIRES: ");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println(); 
System.out.println("1.	Default passwords and ideally default usernames to be changed during initial setup.");
System.out.println();
System.out.println("2.	Ensuring user accounts can not be enumerated using functionality such as password reset mechanisms.");
System.out.println();
System.out.println("3.	Ensuring account lockout after an 3 - 5 failed login attempts.");
System.out.println();
System.out.println("4.	Ensuring credentials are not exposed while connected to wireless networks.");
System.out.println();
System.out.println("5.	Implementing two factor authentication if possible.");
System.out.println();
System.out.println("6.	Apply mobile app obfuscation techinque.");
System.out.println();
System.out.println("7.	Implement mbile app anti-tempering mechanism.");
System.out.println();
System.out.println("8.	Ensuring the mobile app's memory hacking is possible.");
System.out.println();
System.out.println("9.	Restric the mobile app's execution on tempered OS environment.");
System.out.println();
 System.out.println("10. Follow DODI 8420.01 Commercial Wireless Local-Area Network (WLAN)Devices, Systems & Policies " );
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");
  
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 10) 

{
 System.out.println(); 
 System.out.println("*************************************************************************************************");
 System.out.println("              THAT IS  AN INVALID SELECTION ");
 //System.out.println("*************************************************************************************************");


 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");
 menuSelection = keyboard.nextInt(); 
 } 

break;

case 8:
System.out.println();
System.out.println("*************************************************************************************************");

System.out.println("CHECKING FOR  SECURITY CONFIGURABILITY");
//System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("RECOMMENDED SECURITY STEPS TO CHECK FOR - INSUFFICIENT SECURITY CONFIGURABILITY INCLUDES:");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
 
System.out.println("1.	Reviewing the administrative interface of the device for options to strengthen security such as forcing the creation of strong passwords");
System.out.println();
System.out.println("2.	Reviewing the administrative interface for the ability to separate admin users from normal users");
System.out.println();
System.out.println("3.	Reviewing the administrative interface for encryption options");
System.out.println();
System.out.println("4.	Reviewing the administrative interface for options to enable secure logging of various security events");
System.out.println();
System.out.println("5.	Reviewing the administrative interface for options to enable alerts and notifications to the end user for security events");
System.out.println();
System.out.println("6. VERIFY SECURITY CHECKLIST FROM DISA RISK MANAGEMENT FRAMEWORK (RMF)" );

//System.out.println();
//System.out.println("*************************************************************************************************");
//System.out.println("SECURITY STEPS WHICH CAN BE TAKEN TO IMPROVE MY SECURITY CONFIGURABILITY?");
//System.out.println("*************************************************************************************************");

System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("BEST PRACTICES FOR IMPROVING SECURITY CONFIGURABILITY:");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
 
System.out.println("1.	Ensuring the ability to separate normal users from administrative users");
System.out.println();
System.out.println("2.	Ensuring the ability to encrypt data at rest or in transit");
System.out.println();
System.out.println("3.	Ensuring the ability to force strong password policies");
System.out.println();
System.out.println("4.	Ensuring the ability to enable logging of security events");
System.out.println();
System.out.println("5.	Ensuring the ability to notify end users of security events");

System.out.println();
System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 10) 

{ 
 System.out.println();
 //System.out.println("**********THAT IS  AN INVALID SELECTION*********.");
// System.out.println();

 System.out.println("*************************************************************************************************");
 System.out.println("              THAT IS  AN INVALID SELECTION ");
 //System.out.println("*************************************************************************************************");

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");

 menuSelection = keyboard.nextInt(); 
 } 

break;

case 9:

System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("CHECKING FOR SOFTWARE/FIRMWARE SECURITY");
//System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("NOTE: - IT IS VERY IMPORTANT THAT DEVICES FIRST AND FOREMOST HAVE THE ABILITY TO UPDATE AND PERFORM UPDATES REGULARLY.");
//System.out.println();
//System.out.println("*************************************************************************************************");
System.out.println();
//System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("RECOMMENDED SECURITY STEPS TO CHECK FOR - INSECURE SOFTWARE/FIRMAWARE UPDATES INCLUDE:");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println(); 
System.out.println("1.	Reviewing the update file itself for exposure of sensitive information in human readable format by someone using a hex edit tool");
System.out.println();
System.out.println("2.	Reviewing the production file update for proper encryption using accepted algorithms");
System.out.println();
System.out.println("3.	Reviewing the production file update to ensure it is properly signed");
System.out.println();
System.out.println("4.	Reviewing the communication method used to transmit the update");
System.out.println();
System.out.println("5.	Reviewing the cloud update server to ensure transport encryption methods are up to date and properly configured and that the server itself is not vulnerable");
System.out.println();
System.out.println("6.	Reviewing the device for proper validation of signed update files");
System.out.println();
System.out.println("7. VERIFY SECURITY CHECKLIST FROM DISA RISK MANAGEMENT FRAMEWORK (RMF)" );
//System.out.println();
//System.out.println("*************************************************************************************************");
//System.out.println("SECURITY STEPS WHICH CAN BE TAKEN TO SECURE MY SOFTWARE/FIRMWARE?");
//System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("BEST PRACTICES IN SECURING SOFTWARE/FIRMWARE REQUIRES:");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println(); 
System.out.println("1.	Ensuring the device has the ability to update (very important, need secure update mechanism)");
System.out.println();
System.out.println("2.	Ensuring the update file is encrypted using accepted encryption methods");
System.out.println();
System.out.println("3.	Ensuring the update file is transmitted via an encrypted connection");
System.out.println();
System.out.println("4.	Ensuring the update file does not expose sensitive data");
System.out.println();
System.out.println("5.	Ensuring the update is signed and verified before allowing the update to be uploaded and applied");
System.out.println();
System.out.println("6.	Ensuring the update server is secure");
System.out.println();
System.out.println("7.	Implement the secure boot if possible (chain of trust)");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");

  
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 10) 

{ 
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println("              THAT IS  AN INVALID SELECTION ");
 //System.out.println("*************************************************************************************************");


 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");


 menuSelection = keyboard.nextInt(); 
 } 

break;

case 10:

System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("CHECKING FOR PHYSICAL SECURITY");
//System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("RECOMMENDED SECURITY STEPS TO CHECK FOR - POOR PHYSICAL SECURITY INCLUDES:"); 
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("1.	Reviewing how easily a device can be disassembled and data storage mediums accessed or removed");
System.out.println();
System.out.println("2.	Reviewing the use of external ports such as USB to determine if data can be accessed on the device without disassembling the device.");
System.out.println();
System.out.println("3.	Reviewing the number of physical external ports to determine if all are required for proper device function");
System.out.println();
System.out.println("4.	Reviewing the administrative interface to determine if external ports such as USB can be deactivated");
System.out.println();
System.out.println("5.	Reviewing the administrative interface to determine if administrative capabilities can be limited to local access only");
System.out.println();
System.out.println("6. VERIFY SECURITY CHECKLIST FROM DISA RISK MANAGEMENT FRAMEWORK (RMF)" );
//System.out.println();
//System.out.println("*************************************************************************************************");
//System.out.println("SECURITY STEPS WHICH CAN BE TAKEN TO PHYSICALLY SECURE MY DEVICE?");
//System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println();
System.out.println("BEST PRACTICES FOR ADEQUATE PHYSICAL SECURITY REQUIRES:");
System.out.println();
System.out.println("*************************************************************************************************");
System.out.println(); 
System.out.println("1.	Ensuring data storage medium can not be easily removed.");
System.out.println();
System.out.println("2.	Ensuring stored data is encrypted at rest.");
System.out.println();
System.out.println("3.	Ensuring USB ports or other external ports can not be used to maliciously access the device.");
System.out.println();
System.out.println("4.	Ensuring device can not be easily disassembled.");
System.out.println();
System.out.println("5.	Ensuring only required external ports such as USB are required for the product to funtion");
System.out.println();
System.out.println("6.	Ensuring the product has the ability to limit administrative capabilities");
System.out.println();
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");

  
 menuSelection = keyboard.nextInt();
 
// Validate the menu selection. 

while (menuSelection < 1 || menuSelection > 10) 

{
 System.out.println(); 
 System.out.println("*************************************************************************************************");
 System.out.println("              THAT IS  AN INVALID SELECTION ");
 //System.out.println("*************************************************************************************************");


 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("HERE IS THE LIST OF TOP 10 IOT VULNERABILITIES: ");
 System.out.println();
 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.println("1. INSECURE WEB INTERFACE.."); 
 System.out.println();
 System.out.println("2. INSUFFICIENT AUTHENTICATION/AUTH."); 
 System.out.println();
 System.out.println("3. INSECURE NETWORK SERVICES."); 
 System.out.println();
 System.out.println("4. LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION."); 
 System.out.println();
 System.out.println("5. PRIVACY CONCERNS."); 
 System.out.println();
 System.out.println("6. INSECURE CLOUD INTERFACE.");
 System.out.println();
 System.out.println("7. INSECURE MOBILE INTERFACE."); 
 System.out.println();
 System.out.println("8. INSUFFICIENT SECURITY CONFIGURABILITY."); 
 System.out.println();
 System.out.println("9. INSECURE SOFTWARE/FIRMWARE.");
 System.out.println();
 System.out.println("10.POOR PHYSICAL SECURITY.");
 System.out.println();

// Prompt the user for a Security Selection Selection 

 System.out.println("*************************************************************************************************");
 System.out.println();
 System.out.print ("ENTER THE VULNERABILITY NUMBER YOU NEED TO KNOW THE DETAILS: ");
  
 menuSelection = keyboard.nextInt(); 
 } 

break;

    }
  }

 }